numbers = range(1, 11)
num_range = range(1, 11)
result = []
for x in numbers:
    for y in num_range:
        result = x * y
        print(f"{x} * {y} = {result}\t", end="")
    print()
