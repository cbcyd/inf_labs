
# Define a function to solve quadratic equations via the quadratic formula
def solve(a, b, c):

    # Handling special case where a is 0 and equation is linear
    if a == 0: return [-c / b]

    # Calculating the discriminator d for the quadratic equation
    d = b**2 - 4 * a * c

    # If the discriminator is less than 0, return False indicating no real roots
    if d < 0: return False

    # Calculating the first root
    x1 = (-b + d**0.5) / (2 * a)

    # Calculating the second root
    x2 = (-b - d**0.5) / (2 * a)

    # Returning the roots as a list (removing duplicates with set in case of double root)
    return list(set([x1, x2]))

# If the module is invoked directly, test the solve function
if __name__ == "__main__":

    # Get a, b, c from user input and solve
    result = solve(*(map(int, input('Input a, b, c: ').split())))

    # Printing the solutions if they exist, otherwise indicating no solutions
    print(f'Solutions: {result}' if result else 'No solutions')