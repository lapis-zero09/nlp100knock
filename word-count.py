import sys

f = open(sys.argv[1], "r")
ans = {}

for line in f:
    line = line.strip().split()
    for ch in line:
        ch = ch.strip()
        # print(ch)
        if ch in ans:
            ans[ch] += 1
        else:
            ans[ch] = 1

for key, value in sorted(ans.items()):
    print("%s\t%d" %(key, value))
# for key, value in sorted(ans.items(), key=lambda x:x[1]):
#     print("%s\t%d" %(key, value))
