entrance = input("Bitte geben Sie die Anzahl der Eingänge in Ihrem Haus ein: ")

if entrance.isdigit():
    entrance = int(entrance)
else:
    print(f"{entrance} Es ist keine Zahl. Bitte nur die Zahlen eingeben")

apartments_in_ent = input("Bitte geben Sie die Anzahl der Wohnungen in einem Eingang ein: ")

if apartments_in_ent.isdigit():
    apartments_in_ent = int(apartments_in_ent)
else:
    print(f"{apartments_in_ent} Es ist keine Zahl. Bitte nur die Zahlen eingeben")

amount_of_apart_in_floor = input("Bitte geben Sie die Anzahl der Wohnungen auf einer Etage ein: ")

if amount_of_apart_in_floor.isdigit():
    amount_of_apart_in_floor = int(amount_of_apart_in_floor)
else:
    print(f"{amount_of_apart_in_floor} Es ist keine Zahl. Bitte nur die Zahlen eingeben")

amount_of_apart = int(entrance * apartments_in_ent)
print("Anzahl der Wohnungen in Ihrem Haus:", amount_of_apart)

get_apart = input("Bitte geben Sie die Wohnungsnummer ein: ")

if get_apart.isdigit():
    get_apart = int(get_apart)
else:
    print(f"{get_apart} Es ist keine Zahl. Bitte nur die Zahlen eingeben")

get_ent = (get_apart - 1) // apartments_in_ent + 1
get_floor = (get_apart - 1) % apartments_in_ent // amount_of_apart_in_floor

if get_floor == 0:
    get_floor = "Erdgeschoss"
    print(f"Die Wohnung {get_apart} befindet sich im {get_ent}. Eingang und im {get_floor}")
else:
    print(f"Die Wohnung {get_apart} befindet sich im {get_ent}. Eingang und im {get_floor}. Stock")
