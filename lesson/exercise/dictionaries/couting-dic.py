count = dict()

names = ['abc', 'dff', 'axx', 'abc', 'dff']
for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] = count[name] + 1

    print(count)