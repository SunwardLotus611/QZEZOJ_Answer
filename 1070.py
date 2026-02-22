this_year = int(input())
flag = False
for age in range(100):
    birth_year = this_year - age
    digit_sum = sum(int(i) for i in str(birth_year))
    if digit_sum == age:
        print(age)
        flag = True
        break
if not flag:
    print("无解")
