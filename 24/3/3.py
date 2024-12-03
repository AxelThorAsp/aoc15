import re
import sys
ll = sys.stdin.read()

# p1
p = r"mul\((\d{1,3},\d{1,3})\)"
m = re.findall(p,ll)
s = 0
for P in m:
    a, b = map(int, P.split(','))
    s+=a*b
print(s)

# p2
p = r"(do\(\))|(don't\(\))|mul\((\d{1,3},\d{1,3})\)"
m = re.finditer(p, ll)
ok = True
s = 0
for match in m:
    do = match.group(1)
    dont = match.group(2)
    nums = match.group(3)
    if do:
        ok = True
        continue
    if dont:
        ok = False
        continue
    if nums and ok:
        a, b = map(int, nums.split(','))
        s += a*b
print(s)
