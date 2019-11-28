import sys

def get_av_val(line):
    a1 = int(line[0])
    b1 = int(line[1])
    a2 = int(line[2])
    b2 = int(line[3])
    return ((a1 + (b1 - a1)/2) + (a2 + (b2 - a2 + 2)/2))

i = 0
for line in sys.stdin:
    input = line.rsplit()
    if i == 0:
        gunnar_av_val = get_av_val([input[0], input[1], input[2],input[3]])
    else:
        emma_av_val = get_av_val([input[0], input[1], input[2],input[3]])
    i += 1

if gunnar_av_val > emma_av_val:
    print("Gunnar")
elif gunnar_av_val < emma_av_val:
    print("Emma")
else:
    print("Tie")
