c = [100, 98, 98, 98, 95, 95, 94, 93, 90, 90, 89, 88, 80, 76]
score = int(input())
rating = 1
for i in c:
    if score < i:
        rating += 1
    else:
        break
print(rating)
