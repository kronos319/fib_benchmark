import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fib_iterations(iterations, n):
    sum = 0
    for i in range(iterations):
        start_time = time.perf_counter()
        result = fibonacci(n)
        end_time = time.perf_counter()
        #print(f"Fibonacci({n}) = {result}")
        print(f"{i}) Time taken: {end_time - start_time:.6f} seconds")
        sum += end_time - start_time
    print(f"Average time taken ({iterations} iterations): {sum / iterations:.6f} seconds")

#Input nth Fibonacci to find
n = int(input("Enter desired nth Fibonacci to find: "))
#Input number of iterations
iterations = int(input("Enter number of iterations: " ))

fib_iterations(iterations,n)