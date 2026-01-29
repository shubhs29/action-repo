"""
Sample Application
This is a simple Python application to demonstrate GitHub webhook events.
"""

def greet(name):
    """Return a greeting message"""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers"""
    return a + b

def main():
    """Main function"""
    print(greet("World"))
    print(f"2 + 2 = {add(2, 2)}")

if __name__ == "__main__":
    main()
