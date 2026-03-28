def f(step):
    if step < 0:
        return 0
    elif step == 1 or step == 0:
        return 1
    return sum([f(step - i) for i in range(1, 3)])


n = int(input())
print(f(n))
