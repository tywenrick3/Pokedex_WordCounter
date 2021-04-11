import csv


def create_entry(number, name, type_1, type_2, health_points, attack, defense, special_attack, special_defense, speed,
                 generation, is_legendary):
    """
    Returns a dictionary containing a Pokemon's information.

    :param number: A number denoting the ID number of this Pokemon.
    :param name: A string contrining a Pokemon's name.
    :param type_1: A string containing a Pokemon's main type.
    :param type_2: A string containing a Pokemon's secondary type.
    :param health_points: An integer containing a Pokemon's HP (health point) value.
    :param attack: An integer containing a Pokemon's attack value.
    :param defense: An integer containing a Pokemon's defence value.
    :param special_attack: An integer containing a Pokemon's Sp. Atk. (special attack) value.
    :param special_defense: An integer containing a Pokemon's Sp. Def. (special defense) value.
    :param speed: An integer containing a Pokemon's speed value.
    :param generation: An integer denoting batches of Pokemon are released on a game-by-game basis, known as
                       "Generations."
    :param is_legendary: A bool representing whether or not a Pokemon is legendary.
    :return: A dictionary containing a Pokemon's information.
    """
    if type_2 == '':
        type_2 = None

    types = (type_1, type_2)

    battle_stats = {"HP": health_points, "Attack": attack, "Defense": defense, "Sp. Atk": special_attack,
                    "Sp. Def": special_defense, "Speed": speed, }
    entry = {
        "Number": number,
        "Name": name,
        "Types": types,
        "Battle Stats": battle_stats,
        "Generation": generation,
        "Legendary": is_legendary
    }

    return entry


def create_pokedex(filepath):
    """
    Creates a dictionary of Pokemon dictionary entries created from information extracted from file filepath.

    :param filepath: A string containing the location of a file from which to read information from.
    :return: A dictionary of dictionaries.
    """
    try:
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            pokedex = dict()
            for row in reader:
                pokedex[row["Name"]] = create_entry(row["#"], row["Name"], row["Type 1"], row["Type 2"], row["HP"],
                                                    row["Attack"], row["Defense"], row["Sp. Atk"], row["Sp. Def"],
                                                    row["Speed"], row["Generation"], row["Legendary"])

        return pokedex

    except FileNotFoundError as e:
        return dict()


def main():
    """
    Some sample behavior based on the README.
    """
    # P R O B L E M   2
    a_random_pokemon = create_entry(81, "Magnemite", "Electric", "Steel", 25, 35, 70, 95, 55, 45, 1, False)

    for key in a_random_pokemon.keys():
        print("{}: {}".format(key, a_random_pokemon[key]))

    print(a_random_pokemon["Battle Stats"])
    print(a_random_pokemon["Battle Stats"]["HP"])
    print(a_random_pokemon["Battle Stats"]["Attack"])

    print()  # For formatting
    # P R O B L E M   3
    filepath = "pokemon.csv"
    pokedex = create_pokedex(filepath)
    pokemon_key = "Glaceon"
    #
    # # This is one of the many ways to check if a certain key exists in a dictionary!
    try:
        #     # This step could potentially fail, so we "try" it first.
        my_favorite_pokemon = pokedex[pokemon_key]
    except KeyError:
        #     # If it does fail under a KeyError, we'll print an error message.
        print("ERROR: Pokemon {} does not exist!".format(pokemon_key))
    else:
        #     # If it doesn't fail under a KeyError, we'll print the Pokemon's info!
        print("PRINTING {}'S INFORMATION...".format(pokemon_key))
        for key in my_favorite_pokemon.keys():
            print("{}: {}".format(key, my_favorite_pokemon[key]))


# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
