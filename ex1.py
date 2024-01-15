entrance = input("Пожалуйста, введите количество подъездов в вашем доме: ")
if entrance.isdigit():
    entrance = int(entrance)
else: 
    print(f"{entrance} это не цифра. Пожалуйста, вводите только цифры")

apartments_in_ent = input("Пожалуйста, введите количество квартир в одном подъезде: ")
if apartments_in_ent.isdigit():
    apartments_in_ent = int(apartments_in_ent)
else: 
    print(f"{apartments_in_ent} это не цифра. Пожалуйста, вводите только цифры")

amount_of_apart_in_floor = input("Пожалуйста, введите количество квартир на одном этаже: ")
if amount_of_apart_in_floor.isdigit():
    amount_of_apart_in_floor = int(amount_of_apart_in_floor)
else: 
    print(f"{amount_of_apart_in_floor} это не цифра. Пожалуйста, вводите только цифры")

amount_of_apart = int(entrance * apartments_in_ent)
print("Количество квартир в вашем доме:", amount_of_apart)

get_apart = input("Пожалуйста, введите номер квартиры: ")
if get_apart.isdigit():
    get_apart = int(get_apart)
else: 
    print(f"{get_apart} это не цифра. Пожалуйста, вводите только цифры")

get_ent = (get_apart - 1) // apartments_in_ent + 1
get_floor = (get_apart - 1) % apartments_in_ent // amount_of_apart_in_floor + 1
print(f"Квартира {get_apart} находится в(о) {get_ent} подъезде и на {get_floor} этаже")
