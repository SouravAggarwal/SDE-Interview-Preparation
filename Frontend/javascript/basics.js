
// 1. async functions always return a promise
async function fetchData(isError = false) {
    if (isError) {
        throw new Error("An error occurred while fetching data");
    }

    return "Data fetched";
}


// Using the async function
const fetchDataPromise = fetchData(false);
fetchDataPromise
    .then(data => console.log(data))
    .catch(error => console.error("Error2:", error));

// 2. promise implementation
const promise = new Promise((resolve, reject) => {
    resolve("Data fetched from promise");
    reject(new Error("An error occurred while fetching data from promise"));
});
   
// Using the async function
promise
    .then(data => console.log(data))
    .catch(error => console.error("Error3:", error));


// // Using async/await syntax
// async function fetchDataAsync() {
//     try {
//         const data = await fetchData();
//         console.log(data);
//     } catch (error) {
//         console.error("Error:", error);
//     }
// }
// fetchDataAsync();
// Example of an async function with error handling