import sys
import math


cloud_count = 0
while True:
    start_line = sys.stdin.readline().split()
    if start_line == ["0","0"]:
        break
    W = int(start_line[0])
    N = int(start_line[1])
    word_dict = {}
    cloud_count+=1
    max_count = 0
    for i in range(N):
        new_line = str(sys.stdin.readline()).split()
        word_dict[new_line[0]] = int(new_line[1])

        if max_count < int(new_line[1]):
            max_count = int(new_line[1])
    total_height = 0
    current_tot_W = 0
    max_height_on_row = 0
    i = 1
    for word in word_dict:
        height = math.ceil(8+(40*(word_dict[word]-4))/(max_count-4))
        width = math.ceil((9/16)*len(word)*height)
        # new row
        if current_tot_W + width > W:
            total_height += max_height_on_row
            max_height_on_row = height
            current_tot_W = width + 10
        else:
            current_tot_W += width + 10

        if max_height_on_row < height:
            max_height_on_row = height
        # last row
        if i == N:
            total_height += max_height_on_row

        i+=1

    print("CLOUD {}: {}".format(cloud_count,total_height))
