n, s, m = map(int, input().split())

v = list(map(int, input().split()))

results = []
def volume_manager(volume, i):
    if volume + v[i] <= m:
        new_volume = volume + v[i]
        if i + 1 < len(v):
            volume_manager(new_volume, i + 1)
        else:
            results.append(new_volume)
    if volume - v[i] >= 0:
        new_volume = volume - v[i]
        if i + 1 < len(v):
            volume_manager(new_volume, i + 1)
        else:
            results.append(new_volume)

volume_manager(s, 0)
if results:
    results = sorted(results, reverse=True)
    print(results[0])
else:
    print(-1)

