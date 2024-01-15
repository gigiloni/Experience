x = int(input("Please, enter the value: "))
y = int(input("Please, enter the another value: "))

if x > 0 and y > 0:
    print("x is positive", end=" and ")
    print("y is positive")
elif x < 0 and y < 0:
    print("x is negative", end=" and ")
    print("y is negative")
elif x > 0 > y:
    print("x is positive", end=" and ")
    print("y is negative")
elif x < 0 < y:
    print("x is negative", end=" and ")
    print("y is positive")
elif x == 0 and y > 0:
    print("x is zero", end=" and ")
    print("y is positive")
elif x == 0 and y < 0:
    print("x is zero", end=" and ")
    print("y is negative")
elif x > 0 and y == 0:
    print("x is positive", end=" and ")
    print("y is zero")
elif x < 0 and y == 0:
    print("x is negative", end=" and ")
    print("y is zero")
else:
    print("x is zero", end=" and ")
    print("y is zero")
