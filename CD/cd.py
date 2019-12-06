import io
import sys

file = [int(x) for x in sys.stdin.read().split()]
n = int(file[0])
m = int(file[1])
sum = 0
i = 2
while True:
    jackcds = set()
    for cd in range(n):
        jackcds.add(file[i])
        i +=1
    for cd in range(m):
        if cd in jackcds:
            sum +=1
        i +=1
    sys.stdout.write(str(sum) + "\n")
    n = file[i]
    m = file[i+1]
    if n == 0 and m == 0:
        break
    jackcds.clear()
