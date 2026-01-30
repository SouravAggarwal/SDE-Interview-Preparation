#include <cstdio>
#include <chrono>

#if defined(__clang__)
#pragma clang fp reassociate(off)
#pragma clang fp contract(off)
#endif

static inline double calculate(int iterations, int param1, int param2) {
    double result = 1.0;
    const double step = static_cast<double>(param1);
    const double p2 = static_cast<double>(param2);
    double x = step; // x = i * param1

    int i = 1;
    // Unroll by 4 to reduce loop overhead while preserving exact operation order
    for (; i + 3 <= iterations; i += 4) {
        // i
        result -= 1.0 / (x - p2);
        result += 1.0 / (x + p2);
        x += step;
        // i+1
        result -= 1.0 / (x - p2);
        result += 1.0 / (x + p2);
        x += step;
        // i+2
        result -= 1.0 / (x - p2);
        result += 1.0 / (x + p2);
        x += step;
        // i+3
        result -= 1.0 / (x - p2);
        result += 1.0 / (x + p2);
        x += step;
    }
    for (; i <= iterations; ++i) {
        result -= 1.0 / (x - p2);
        result += 1.0 / (x + p2);
        x += step;
    }
    return result;
}

int main() {
    using clock = std::chrono::system_clock;
    const auto start_time = clock::now();

    double result = calculate(200000000, 4, 1) * 4.0;

    const auto end_time = clock::now();
    const double elapsed = std::chrono::duration<double>(end_time - start_time).count();

    std::printf("Result: %.12f\n", result);
    std::printf("Execution Time: %.6f seconds\n", elapsed);
    return 0;
}