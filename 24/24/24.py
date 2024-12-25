import sys
S = sys.stdin.read().strip()

s1, s2 = S.strip().split("\n\n")
known = {}
rules = []
for r in s2.replace("->", "").split("\n"):
    op1, operation, op2, res = r.split()
    rules.append((op1,operation,op2,res))

for i in s1.splitlines():
    val, k = i.split(":")
    known[val] = int(k)

def do(op1, operation, op2):
    if operation == "AND":
        return op1 & op2
    elif operation == "OR":
        return op1 | op2
    elif operation == "XOR":
        return op1 ^ op2
    else:
        assert False

while rules:
    op1, operation, op2, res = rules.pop(0)
    if op1 in known and op2 in known:
        result = do(known[op1],operation, known[op2])
        known[res] = result
    else:
        rules.append((op1, operation, op2, res))


careabout = [k for k in known if k.startswith("z")]
r = int("".join(str(known[k]) for k in sorted(careabout, key = lambda x: int(x[1:]), reverse=True)),2)
print(r)
