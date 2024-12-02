import sys
d = {}
ll = []
rr = []
for line in sys.stdin:
    l,r = line.split()
    ll.append(int(l))
    rr.append(int(r))

for i in ll:
    d[i] = rr.count(i)
s = 0
for k in d:
    s += k*d[k]
print(s)
