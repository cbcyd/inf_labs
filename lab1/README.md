# Lab1

This project contains two Python scripts that perform various mathematical operations.

## Files

### `main.py`

This script contains a program that calculates the maximum area of a triangle that can be formed from a given list of side lengths. The side lengths are first sorted in descending order. Then, the script iterates over all possible combinations of three sides to find the one that forms a triangle with the maximum area.

Here is a brief overview of the code:

- `sides`: A list of integers representing the lengths of the sides.
- `smax`: A variable to keep track of the maximum area found so far.
- The nested for loops iterate over all combinations of three sides.
- The if statement checks if the three sides can form a triangle (i.e., the sum of the lengths of any two sides is greater than the length of the third side).
- If they can, it calculates the area of the triangle using Heron's formula and updates `smax` if this area is greater than the current `smax`.

### `hmw.py`

This script defines a function `solve` that solves quadratic equations. The function takes three arguments: `a`, `b`, and `c`, which are the coefficients of the quadratic equation ax^2 + bx + c = 0. The function returns a list of the real roots of the equation.

Here is a brief overview of the code:

- The function first checks if `a` is 0. If it is, the equation is linear, and the function returns the single root.
- The function then calculates the discriminant of the equation.
- If the discriminant is less than 0, the function returns `False`, indicating that the equation has no real roots.
- Otherwise, the function calculates and returns the roots.

If the script is run directly, it prompts the user to enter the coefficients of a quadratic equation, solves the equation, and prints the solutions.