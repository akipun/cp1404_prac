"""# a"""
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end='')
print()

# c
number_of_stars = int(input("Number of Stars: "))
for i in range(number_of_stars):
    print('*', end='')
print()

# d
for i in range(number_of_stars):
    print('*' * (i+1), end='')
    print()
print()
