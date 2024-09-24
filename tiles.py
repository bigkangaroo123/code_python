import math

tiles = int(input("how many tiles?: "))

side_length = math.floor(math.sqrt(tiles))

#if side_length^2 = tiles, return side_length
#if not, check every number behind side_length and square it to see if that number is less than tiles, stop when found

if side_length*side_length == tiles:
    print(f"The largest square has the side length {side_length}")
else:
    i = side_length
    while i <= side_length and i >= 0:
        if i*i <= tiles:
            print(f"The largest square has the side length {i}")
            break
        i = i - 1
