import sys

l = [list(map(int, line.split())) for line in sys.stdin]
def safe2(a,b):
    return abs(a-b) < 4 and abs(a-b) > 0
def safe(line):
    desc = [line[i] < line[i+1] and safe2(line[i],line[i+1]) for i in range(len(line)-1)]
    asc =  [line[i] > line[i+1] and safe2(line[i],line[i+1]) for i in range(len(line)-1)]
    return all(desc) or all(asc)
# p1
#print([safe(line) for line in l].count(True))    

# p2 
def checkall(line):
    if safe(line):
        return True
    org = line
    for i in range(len(line)):
        copy = org.copy()
        copy.pop(i)
        if safe(copy):
            return True
    return False
t = 0
for line in l:
    if checkall(line):
        t+=1
print(t)
