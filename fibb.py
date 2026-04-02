

def main():
    print("Fibonacci Series Program")
    n = 15 
    if n <= 0:
        print("Please enter a positive number")
        return
    a = 0
    b = 1
    print("Fibonacci series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
if __name__ == "__main__":
    main()