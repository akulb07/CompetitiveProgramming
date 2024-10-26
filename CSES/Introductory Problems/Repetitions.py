n = input("")
count = 1
max_l = 1

for i in range(1,len(n)):
    if n[i] == n[i-1]:
        count += 1
        max_l = max(count,max_l)
    else:
        count = 1
print(max_l)