from fastapi import FastAPI, Request, HTTPException
from PIL import Image
import io
import boto3
import uvicorn
import json 

app = FastAPI()

# Initialize S3 client
s3 = boto3.client("s3")

# Dummy image processing function
def process_image(image):
    return image.convert("L")  # Convert image to grayscale (dummy processing)

@app.get("/ping")
async def ping():
    return {"message": "Healthy"}

@app.get("/ping/{msg}")
async def ping(msg: str):
    return {"message": f"Healthy{msg}"}

@app.post("/invocations")
async def invocations(request: Request):
    try:
        print("Step-1: Invocations API called")
        print("Step-2: Headers", request.headers)
        print("Step-3: Headers", request)
        
        # Read from S3 since Async Inference sends an S3 path as raw bytes
        custom_attributes = request.headers.get("X-Amzn-SageMaker-Custom-Attributes", "")
        print("Step-4: Custom Attributes", custom_attributes)

        s3_input_path = (await request.body()).decode("utf-8").strip()
        print("Step-5.0: Body", s3_input_path)

        if s3_input_path is dict:
            print("Step-5.1: S3 Input Path is Dict")
        elif s3_input_path is str:
            print("Step-5.1: S3 Input Path is String")
        else:
            print(f"Step-5.1: type: {type(s3_input_path)}")

        s3_input_path_loads = json.loads(s3_input_path)
        print(f"Step-5.2 After Json Loads: {s3_input_path_loads}")

        input_bucket = "flask-demo-bucket-99989"
        input_key = s3_input_path_loads.get("input_image")
        output_key = s3_input_path_loads.get("output_image")

        # Download image from S3
        image_bytes = io.BytesIO()
        s3.download_fileobj(input_bucket, input_key, image_bytes)
        image_bytes.seek(0)
        print("Step-6: Image downloaded from S3")

        # Open image with PIL
        image = Image.open(image_bytes)
        processed_image = process_image(image)

        # Save processed image to BytesIO
        output_bytes = io.BytesIO()
        processed_image.save(output_bytes, format="PNG")
        output_bytes.seek(0)
        print("Step-7: Image processed")

        # Upload processed image back to S3
        s3.upload_fileobj(output_bytes, input_bucket, output_key, ExtraArgs={'ContentType': 'image/png'})

        print("Step-8: Image uploaded to S3")
        return {"message": "Processing complete", "s3_output": output_key}

    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

def parse_s3_path(s3_path):
    """Extract bucket and key from S3 path"""
    if s3_path.startswith("s3://"):
        s3_path = s3_path[5:]
    bucket, key = s3_path.split("/", 1)
    return bucket, key

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)