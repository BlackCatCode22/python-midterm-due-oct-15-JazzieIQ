import datetime

def gen_birth_day(year_old, birth_season):
    year = 2023 - year_old
    month_day = {
        "spring": "03-19",
        "summer": "05-21",
        "fall": "08-19",
        "winter": "12-19"
    }.get(birth_season, "01-01")
    new_date = f"{year}-{month_day}"
    return new_date

def gen_unique_id(species_name, num_of_species):
    if species_name == "hyena":
        return f"Hy0{num_of_species}"
    elif species_name == "lion":
        return f"Li0{num_of_species}"
    elif species_name == "tiger":
        return f"Ti0{num_of_species}"
    elif species_name == "bear":
        return f"Be0{num_of_species}"
    else:
        return "error"

def main():
    hyena_habitat = []
    lion_habitat = []
    tiger_habitat = []
    bear_habitat = []
    habs = [None] * 4
    hyenas = [None] * 13
    lions = [None] * 13
    tigers = [None] * 13
    bears = [None] * 13
    
    print("\n\n** Welcome to Mac Mac's Program for Creating Habitats. **\n")
    print("I will be using the info below:\n")

    try:
        with open("animalNames.txt", "r") as animal_names_file:
            names = animal_names_file.read()
            names = names.replace("Names:\n", "Habitat: ").replace("Ryker\n", "Ryker")
            print(names + "\n")

        with open("arrivingAnimals.txt", "r") as arriving_animals_file:
            animals = arriving_animals_file.readlines()
            print("New Animals to the Following Habitats.\n")
            for animal in animals[:16]:
                print(animal.strip())
            print("\nLet's begin!\n")
            print("\n\n Creating Habitats... \n\n")

        with open("zooHabitats.txt", "w") as output_file:
            output_file.write("Created Habitat Enclosures\n")
            output_file.write("New Animals to the Following Habitats.\n")
            
            current_date = datetime.date.today()
            in_taking_date = current_date - datetime.timedelta(days=7)
            pre_quart_date = current_date - datetime.timedelta(days=4 * 30 + 12)

            years_old = 0
            num_of_hyenas = 0
            num_of_lions = 0
            num_of_tigers = 0
            num_of_bears = 0
            j = 0
            index_key = 0
            end_key = 0

            data = names.replace(": \n", ", ").replace("\n\n", ", ").split(",", 52)
            print(data)
            print("\n")
            for j in range(13):
                if j < len(data):  # Add this check to prevent accessing invalid indices
                    if data[j] == "Hyena Habitat":
                        habs[0] = data[j]
                    else:
                        hyenas[j] = data[j]

            print(f"These names are for {habs[0]}:")
            for j in range(5):
                if hyenas[j] is not None:
                    print(hyenas[j])

            for j in range(13, 26):
                if j < len(data):  # Add this check to prevent accessing invalid indices
                    if data[j] == "Lion Habitat":
                        habs[1] = data[j]
                    else:
                        lions[j - 13] = data[j]

            print(f"These names are for {habs[1]}:")
            for j in range(13, 17):
                if lions[j - 13] is not None:
                    print(lions[j - 13])

            for j in range(26, 39):
                if j < len(data):  # Add this check to prevent accessing invalid indices
                    if data[j] == "Bear Habitat":
                        habs[2] = data[j]
                    else:
                        bears[j - 26] = data[j]

            print(f"These names are for {habs[2]}:")
            for j in range(26, 30):
                if bears[j - 26] is not None:
                    print(bears[j - 26])

            for j in range(39, 49):
                if j < len(data):  # Add this check to prevent accessing invalid indices
                    if data[j] == "Tiger Habitat":
                        habs[3] = data[j]
                    else:
                        tigers[j - 39] = data[j]

            print(f"These names are for {habs[3]}:")
            for j in range(39, 43):
                if tigers[j - 39] is not None:
                    print(tigers[j - 39])

            for i in range(16):
                split_animals = animals[i].split()
                split_str_comma = animals[i].split(",")

                print("\n")
                years_old = int(split_animals[0])
                season = split_animals[7]
                species = split_str_comma[0].split()[4]
                birthdate = gen_birth_day(years_old, season)
                sex = split_animals[3]
                color = split_str_comma[2]
                weight = split_str_comma[3]
                origin = split_str_comma[4] + "," + split_str_comma[5]

                if species == "hyena":
                    num_of_hyenas += 1
                    unique_id = gen_unique_id(species, num_of_hyenas)
                    animal = {
                        "id": unique_id,
                        "name": hyenas[num_of_hyenas - 1],
                        "birthday": birthdate,
                        "color": color.replace(" ", ""),
                        "sex": sex.replace(" ", ""),
                        "weight": weight.replace("  ", " "),
                        "arrival": current_date,
                        "age": years_old
                    }
                    print(f"{animal['id']}: {animal['name']}\n{animal['age']} years old {animal['sex']}.\nBirthday: {animal['birthday']}\n{animal['color']} {animal['weight']}\nArrival {animal['arrival']}")
                    hyena_habitat.append(animal)
                elif species == "lion":
                    num_of_lions += 1
                    unique_id = gen_unique_id(species, num_of_lions)
                    animal = {
                        "id": unique_id,
                        "name": lions[num_of_lions - 1],
                        "birthday": birthdate,
                        "color": color.replace(" ", ""),
                        "sex": sex.replace(" ", ""),
                        "weight": weight.replace("  ", " "),
                        "arrival": current_date,
                        "age": years_old
                    }
                    print(f"{animal['id']}: {animal['name']}\n{animal['age']} years old {animal['sex']}.\nBirthday: {animal['birthday']}\n{animal['color']} {animal['weight']}\nArrival {animal['arrival']}")
                    lion_habitat.append(animal)
                elif species == "tiger":
                    num_of_tigers += 1
                    unique_id = gen_unique_id(species, num_of_tigers)
                    animal = {
                        "id": unique_id,
                        "name": tigers[num_of_tigers - 1],
                        "birthday": birthdate,
                        "color": color.replace(" ", ""),
                        "sex": sex.replace(" ", ""),
                        "weight": weight.replace("  ", " "),
                        "arrival": current_date,
                        "age": years_old
                    }
                    print(f"{animal['id']}: {animal['name']}\n{animal['age']} years old {animal['sex']}.\nBirthday: {animal['birthday']}\n{animal['color']} {animal['weight']}\nArrival {animal['arrival']}")
                    tiger_habitat.append(animal)
                elif species == "bear":
                    num_of_bears += 1
                    unique_id = gen_unique_id(species, num_of_bears)
                    animal = {
                        "id": unique_id,
                        "name": bears[num_of_bears - 1],
                        "birthday": birthdate,
                        "color": color.replace(" ", ""),
                        "sex": sex.replace(" ", ""),
                        "weight": weight.replace("  ", " "),
                        "arrival": current_date,
                        "age": years_old
                    }
                    print(f"{animal['id']}: {animal['name']}\n{animal['age']} years old {animal['sex']}.\nBirthday: {animal['birthday']}\n{animal['color']} {animal['weight']}\nArrival {animal['arrival']}")
                    bear_habitat.append(animal)
                print("\n")

            print(f"numOfHyenas = {num_of_hyenas}")
            print(f"numOfLions = {num_of_lions}")
            print(f"numOfTigers = {num_of_tigers}")
            print(f"numOfBears = {num_of_bears}")

            # Printing linked lists
            output_file.write(f'\n"{habs[0]}"\n')
            for animal in hyena_habitat:
                output_file.write(f"{animal['id']} {animal['name']} {animal['age']} years old, birthday is {animal['birthday']}, {animal['color']}, sex is {animal['sex']}, weight is {animal['weight']}\n")

            output_file.write(f'\n"{habs[1]}"\n')
            for animal in lion_habitat:
                output_file.write(f"{animal['id']} {animal['name']} {animal['age']} years old, birthday is {animal['birthday']}, {animal['color']}, sex is {animal['sex']}, weight is {animal['weight']}\n")

            output_file.write(f'\n"{habs[2]}"\n')
            for animal in bear_habitat:
                output_file.write(f"{animal['id']} {animal['name']} {animal['age']} years old, birthday is {animal['birthday']}, {animal['color']}, sex is {animal['sex']}, weight is {animal['weight']}\n")

            output_file.write(f'\n"{habs[3]}"\n')
            for animal in tiger_habitat:
                output_file.write(f"{animal['id']} {animal['name']} {animal['age']} years old, birthday is {animal['birthday']}, {animal['color']}, sex is {animal['sex']}, weight is {animal['weight']}\n")

    except FileNotFoundError as e:
        print("A file error occurred...")
        print(e)

if __name__ == "__main__":
    main()
