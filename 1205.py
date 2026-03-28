week = ["Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]
a, b = map(int, input().split())
print(week[int(a ** b) % 7])
