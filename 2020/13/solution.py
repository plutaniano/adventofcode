arrival, ids, _ = open('input.txt').read().split('\n')
arrival = int(arrival)
ids = ids.split(',')

best = (9999999999, None)
for i in ids:
    if i == 'x':
        continue

    delay = int(i) - (arrival % int(i))
    if delay < best[0]:
        best = (delay, int(i))

solution1 = best[0] * best[1]

ids = [(n, i) for i, n in enumerate(ids) if n != 'x']
