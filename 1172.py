a = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    operation = [int(i) if i.isdigit() or i[1].isdigit()
                 else i for i in input().split()]
    if operation[0] == 'add':
        for i in range(operation[1], operation[2] + 1):
            a[i] += operation[3]
    elif operation[0] == 'query':
        print(sum(a[operation[1]: operation[2] + 1]))
