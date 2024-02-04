people = [
    {'name': 'George', 'age': 18},
    {'name': 'Bob', 'age': 18},
    {'name': 'Lucas', 'age': 16},
    {'name': 'Oliwia', 'age': 16}
]

sorted_people_by_name_and_age = min(people, key=lambda x: (x['name'], x['age']))
print(sorted_people_by_name_and_age)

fruits = ["apple", "banana", "cherry", "orange"]
sorted_fruits = sorted(fruits, key=lambda fruit: len(fruit))
print(sorted_fruits)
