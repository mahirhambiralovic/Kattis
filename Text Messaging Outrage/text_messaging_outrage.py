import sys

first = True
cases = 0
array = []

for line in sys.stdin:
    if first:
        cases = int(line.split()[0])
        first = False
    else:
        array.append(list(map(int, line.split())))

i = 0
case = 1
while(case <= cases):
    number_of_keys = array[i][1]
    alphabet_length = array[i][2]

    sum = 0
    array[i+1].sort(reverse=True)
    j = 0
    letter_depth_on_key = 1
    while(j < alphabet_length):
        if(j % number_of_keys == 0 and j != 0):
            # print("Going one key deeper")
            letter_depth_on_key += 1
        sum += array[i+1][j] * letter_depth_on_key
        #print("j: {}, val: {}, depth: {}, tot: {}".format(j,array[i+1][j], letter_depth_on_key, array[i+1][j] * letter_depth_on_key))
        j+=1
    print("Case #%d: %d" % (case, sum))
    # Go down two lines for next case
    i+=2
    case += 1
