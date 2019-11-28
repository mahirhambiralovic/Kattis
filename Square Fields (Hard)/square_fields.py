#### FÖRSLAG
# Istället för att kolla fyra kvadranter, så vill vi kolla på alla möjliga kvadrater med punkten som kant!
# Hur gör vi detta utan att flytta kvadraten bara 1 steg i taget?
# Minsta sidlängden kan vara 1. Med en radie på 1000+ blir detta många steg

# Istället:
# Gör en array av alla möjliga x värden och en med alla y värden på punkter
# Flytta kvadraten till nästa möjliga x värde
# Flytta kvadraten till nästa möjliga y värde
# Kolla alltid så att avståndet inte är större än radien
# Ta den maximala kvadraten av alla dessa möjligheter.
# Bör bli max 10 punkter * (9*9) = 810 per iteration. Nemas problemas.


import sys

def apply_largest_square(points_array):
    coverage_array = []
    #print("Possible quadrants:")
    for center_point in points_array:
        q1,q2,q3,q4 = get_possible_squares(points_array,center_point,radius)
        arr = [q1,q2,q3,q4]
        coverage_array.append(arr)
        #print("max: {}, p: {}, q: {}, {}, {}, {}".format(max(len(q1),len(q2),len(q3),len(q4)),center_point,q1,q2,q3,q4))

    max_size = 0
    max_point_index = 0
    # Find largest array of non-covered points
    for center_point in range(len(coverage_array)):
        # Make largest quadrant first
        coverage_array[center_point].sort(key=len,reverse=True)
        if max_size < len(coverage_array[center_point][0]):
            max_size = len(coverage_array[center_point][0])
            max_point_index = center_point
    #print("Max point to remove {}, at index {}, and it covers {} points:".format(points_array[max_point_index],max_point_index,max_size))
    #####print("{}".format(coverage_array[max_point_index]))
    #print("Removing points {}, {}".format(points_array[max_point_index],coverage_array[max_point_index][0]))
    # We now have the index of the point that covers most other points, with largest quadrant as first index
    # Remove the points this square covers, and finally the point itself

    for point_to_remove in coverage_array[max_point_index][0]:
        # Find which point it is, at this index
        to_remove_index = 0
        for i in range(len(points_array)):
            if points_array[i] == point_to_remove:
                coverage_array.remove(coverage_array[i])
                points_array.pop(i)
                if i < max_point_index:
                    max_point_index -=1
                break
    #####print("Removing initial centerpoint: {}, index {}".format(points_array[max_point_index], max_point_index))
    coverage_array.remove(coverage_array[max_point_index])
    points_array.pop(max_point_index)

    #####print()
    ##print("Points array remaining: {}".format(points_array))
    #####print()
    return points_array

def check_quadrant(p1,p2,r):
    x_d = (p2[0] - p1[0])
    y_d = (p2[1] - p1[1])
    # Too far
    if max(abs(x_d),abs(y_d)) > r:
        return 0
    # First and Second
    if x_d > 0 and y_d == 0:
        return [1,2]
    # Second and Third
    if x_d == 0 and y_d < 0:
        return [2,3]
    # Third and Fourth
    if x_d < 0 and y_d == 0:
        return [3,4]
    # Fourth and First
    if x_d == 0 and y_d > 0:
        return [4,1]

    # First quadrant
    elif x_d > 0 and y_d > 0:
        return 1
    # Second
    elif x_d > 0 and y_d < 0:
        return 2
    # Third
    elif x_d < 0 and y_d < 0:
        return 3
    # Fourth
    elif x_d < 0 and y_d > 0:
        return 4

def get_possible_squares(points_array,center_point,r):
        q1 = []
        q2 = []
        q3 = []
        q4 = []
        for neighbour_point in points_array:
            if center_point == neighbour_point:
                continue
            q = check_quadrant(center_point,neighbour_point,r)
            if q == 0:
                continue
            elif q == [1,2]:
                q1.append(neighbour_point)
                q2.append(neighbour_point)
            elif q == [2,3]:
                q2.append(neighbour_point)
                q3.append(neighbour_point)
            elif q == [3,4]:
                q3.append(neighbour_point)
                q4.append(neighbour_point)
            elif q == [4,1]:
                q4.append(neighbour_point)
                q1.append(neighbour_point)

            elif q == 1:
                q1.append(neighbour_point)
            elif q == 2:
                q2.append(neighbour_point)
            elif q == 3:
                q3.append(neighbour_point)
            elif q == 4:
                q4.append(neighbour_point)

        return q1, q2, q3, q4

def get_radius_array(points_array):
    radius_array = []
    for i in points_array:
        for j in points_array:
            if i != j:
                radius_array.append(max(abs(i[0] - j[0]),abs(i[1] - j[1])))
    # Remove duplicates and sort
    return sorted(list(set(radius_array)))

cases = int(sys.stdin.readline())
for case in range(cases):
    points_covered_table = {}
    points_array = []
    n, k = list(map(int, sys.stdin.readline().split()))
    min_x = 0
    min_y = 0
    for i in range(n):
        x, y = list(map(int, sys.stdin.readline().split()))
        points_array.append((x,y))
    #print("n = {}, k = {} , {}".format(n,k,points_array))
    if k == 1:
        radius = max(min_x,min_y)
        #print("Case #{}: {}".format(case+1,radius))
        ###print("\n------\n")
        break
    # We now have a hash table of all coordinates (k) with False as (v)
    # And an array of all coordinates
    #print(points_array)
    # Let's make a sorted list of the minimum radiuses between all points
    radius_array = get_radius_array(points_array)
    ##print("Radiuses: {}".format(radius_array))

    # Kolla alla punkter omkring vald punkt i minsta radius. Kolla vilken punkt som täcker flest i vår riktning
    # Iterate over possible radiuses from smallest
    for radius in radius_array:
        squares = 0
        t_points_covered_table = points_covered_table.copy()
        test_points_array = points_array.copy()
        #print("\n -------- \n\nR = {}".format(radius))
        # Find best squares and remove points inside
        while(len(test_points_array) > 0):
            # If squares used up, increase radius
            if squares >= k:
                break
            test_points_array = apply_largest_square(test_points_array)
            squares += 1
            #print("Laid square: {}".format(squares))
        ###print("Remaining array",test_points_array)
        if len(test_points_array) != 0:
            #####print("TOO MANY SQUARES")
            continue
        print("Case #{}: {}".format(case+1,radius))
        ###print("\n------\n")
        break
