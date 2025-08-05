
def print_pyramid(height):
    for i in range(1, height + 1):
        # Print spaces
        for j in range(height - i):
            print( end="")
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        print()
# Example usage:
print_pyramid(5)
