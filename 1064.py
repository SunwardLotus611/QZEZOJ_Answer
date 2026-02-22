data = [float(i) for i in input().split(',') if i.strip()]
points = [(0, 0)] + [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
tot_len = sum(((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) **
              0.5 for p1, p2 in zip(points[: len(points) - 1], points[1:]))
print(round(tot_len, 2))
