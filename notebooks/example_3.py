# how to create a bidirectional array in python?
a = []

for i in range(2):
    a.append([])
    for j in range(2):
        a[i].append(i+j)

print(a)
