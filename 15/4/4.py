import hashlib

data = input()

for i in range(0, 50_000_000):
    temp = f"{data}{i}"
    md5_hash = hashlib.md5()
    md5_hash.update(temp.encode('utf-8'))
    first_six = md5_hash.hexdigest()[:6]
    if (first_six == "000000"):
        print(i)
        exit(0)
