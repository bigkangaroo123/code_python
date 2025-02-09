def print_calendar(start_day, num_days):
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    
    # Print header
    print(" ".join(days))
    
    # Compute the initial spacing
    current_day = 1
    start_pos = start_day - 1
    
    # Print initial spaces
    print("    " * start_pos, end="")
    
    # Print days
    for i in range(num_days):
        print(f"{current_day:3}", end=" ")
        if (start_pos + current_day) % 7 == 0:  # New line after Saturday
            print()
        current_day += 1
    
    print()  # Ensure the last line ends with a newline

# Read input
start_day = int(input())
num_days = int(input())

# Print the calendar
print_calendar(start_day, num_days)
