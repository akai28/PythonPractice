x = 2
y = 10

# Simple If statement

if x > y:
    print(f"{x} is greater than {y}")

# If else statement

if x > y:
    print(f"{x} is greater than {y}")

else:
    print(f"{y} is greater than {x}")


# Elif statement

if x > y:
    print(f"{x} is greater than {y}")

elif x == y:
    print(f'{x} is equal to {y}')

else:
    print(f"{y} is greater than {x}")

# Nested if

if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')

# Logical Operators(and, or, not)

# and

if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# or

if x > 2 or x <= 10:
    print(f'{x} is greater than 2 or less than or equal to 10')

# not

if not(x == y):
    print(f'{x} is not equal to {y}')

# Membership Operator (not, not in)

# in

numbers = [1, 2, 3, 4, 5]
if x in numbers:
    print(x in numbers)

# not in

numbers = [1, 2, 3, 4, 5]
if y not in numbers:
    print(y not in numbers)

# Identity Operator (is, is not)

# is
if x is y:
    print(x is y)

# is not
if x is not y:
    print(x is not y)
