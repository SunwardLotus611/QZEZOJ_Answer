def Fibonacci(num1, num2, time):
    if time != 0:
        return Fibonacci(num2, num1 + num2, time - 1)
    else:
        return num1


n = int(input())
print(Fibonacci(0, 1, n))
