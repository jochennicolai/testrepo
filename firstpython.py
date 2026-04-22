python# Simple Python Example

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# List operations
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]

# Main
if __name__ == "__main__":
    print(greet("World"))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"Squares: {squares}")
