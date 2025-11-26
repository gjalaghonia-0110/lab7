# original code - fibonacci

def fibonacci(n):
    # returns nth fib number
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    previous = 0
    current = 1
    
    for i in range(2, n + 1):
        next_value = previous + current
        previous = current
        current = next_value
    
    return current


def factorial(n):
    # n!
    if n <= 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result = result * i
    
    return result


if __name__ == "__main__":
    print("Fibonacci sequence (first 10):")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")
    
    print("\nFactorials:")
    for i in range(1, 8):
        print(f"{i}! = {factorial(i)}")

