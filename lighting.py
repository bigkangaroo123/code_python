def min_lights_to_turn_on(n, k, s):
    s = list(s)  # Convert string to list for easy modification
    turned_on = 0  # Counter for number of lights turned on
    i = 0  # Start from the first index

    while i < n:
        # Check if the current student at index i is covered by a `1`
        has_light = False
        for j in range(max(0, i - k), min(n, i + k + 1)):  # Look in range [i-K, i+K]
            if s[j] == '1':
                has_light = True
                break
        
        if has_light:  # If already covered, move forward
            i += 1
            continue

        # Find the farthest `0` within range to turn into `1`
        best_position = -1
        for j in range(min(n - 1, i + k), max(-1, i - k - 1), -1):
            if s[j] == '0':
                best_position = j
                break

        # If no valid position was found, we cannot cover this student
        if best_position == -1:
            return -1  # Not possible to light all students

        # Flip the best position to `1`
        s[best_position] = '1'
        turned_on += 1

        # Move the pointer forward past the coverage of the newly placed light
        i = best_position + k + 1  

    return turned_on

# Read input
n = int(input())
k = int(input())
s = input().strip()

# Compute and print the result
print(min_lights_to_turn_on(n, k, s))