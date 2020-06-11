number_of_lines = int(input("Enter an odd number"))
number_of_lines = int(number_of_lines / 2)+1
star_count = 1
for row in range(0,number_of_lines):
    for column in range(0,star_count):
        print("*",end="")
    star_count += 2
    print()
star_count -= 4
for row in range(number_of_lines,1,-1):
    for column in range(0,star_count):
        print("*", end="")
    star_count -= 2
    print()