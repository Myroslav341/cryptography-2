f = open('log.txt', 'r')

MAX = 0
log = f.read().split()
for x in log:
    x = int(x)
    if x > MAX:
        MAX = x

log_norm = []
for x in log:
    log_norm.append(int(x) / MAX)

intervals = 100
val = [0 for _ in range(intervals)]
L = 1 / intervals
for x in log_norm:
    for i in range(intervals):
        if L * i < x <= L * (i + 1):
            val[i] += 1
print(val)

print([(x - sum(val) / intervals) / x for x in val])
