code = input()
nums = [int(x) for x in code[: 12]]
s = sum(nums[1:: 2]) * 3 + sum(nums[:: 2])
m = (10 - s % 10) % 10
if m == int(code[12]):
    print("校验码正确")
else:
    print("校验码错误")
