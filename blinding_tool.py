import random
import os
import platform

user_pairs = {}
id_label_pairs = {}
ids_list = []
blind_file_directory = ""
i_rename_folder_path = ""
i_re_rename_folder_path = ""
blind_file_path = ""
op_system = platform.system()

# List of Labels:
labels_list = [
    "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard",
    "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree",
    "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata",
    "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu",
    "Sandshrew", "Sandslash", "Nidoran", "Nidorina", "Nidoqueen",
    "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales",
    "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume",
    "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth",
    "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine",
    "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam",
    "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel",
    "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash",
    "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio",
    "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter",
    "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode",
    "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan",
    "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela",
    "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie",
    "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros",
    "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon",
    "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl",
    "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite",
    "Mewtwo", "Mew", "Chikorita", "Bayleef", "Meganium", "Cyndaquil", "Quilava",
    "Typhlosion", "Totodile", "Croconaw", "Feraligatr", "Sentret", "Furret", "Hoothoot",
    "Noctowl", "Ledyba", "Ledian", "Spinarak", "Ariados", "Crobat", "Chinchou",
    "Lanturn", "Pichu", "Cleffa", "Igglybuff", "Togepi", "Togetic", "Natu", "Xatu",
    "Mareep", "Flaaffy", "Ampharos", "Bellossom", "Marill", "Azumarill", "Sudowoodo",
    "Politoed", "Hoppip", "Skiploom", "Jumpluff", "Aipom", "Sunkern", "Sunflora",
    "Yanma", "Wooper", "Quagsire", "Espeon", "Umbreon", "Murkrow", "Slowking",
    "Misdreavous", "Unown", "Wobbuffet", "Girafarig", "Pineco", "Forretress",
    "Dunsparce", "Gligar", "Steelix", "Snubbull", "Granbull", "Qwilfish", "Scizor",
    "Shuckle", "Heracross", "Sneasel", "Teddiursa", "Ursaring", "Slugma", "Magcargo",
    "Swinub", "Piloswine", "Corsola", "Remoraid", "Octillery", "Delibird", "Mantine",
    "Skarmory", "Houndour", "Houndoom", "Kingdra", "Phanpy", "Donphan", "Porygon2",
    "Stantler", "Smeargle", "Tyrogue", "Hitmontop", "Smoochum", "Elekid", "Magby",
    "Miltank", "Blissey", "Raikou", "Entei", "Suicune", "Larvitar", "Pupitar",
    "Tyranitar", "Lugia", "Ho-Oh", "Celebi", "Treecko", "Grovyle", "Sceptile",
    "Torchic", "Combusken", "Blaziken", "Mudkip", "Marshtomp", "Swampert",
    "Poochyena", "Mightyena", "Zigzagoon", "Linoone", "Wurmple", "Silcoon", "Beautifly",
    "Cascoon", "Dustox", "Lotad", "Lombre", "Ludicolo", "Seedot", "Nuzleaf",
    "Shiftry", "Taillow", "Swellow", "Wingull", "Pelipper", "Ralts", "Kirlia",
    "Gardevoir", "Surskit", "Masquerain", "Shroomish", "Breloom", "Slakoth",
    "Vigoroth", "Slaking", "Nincada", "Ninjask", "Shedinja", "Whismur", "Loudred",
    "Exploud", "Makuhita", "Hariyama", "Azurill", "Nosepass", "Skitty", "Delcatty",
    "Sableye", "Mawile", "Aron", "Lairon", "Aggron", "Meditite", "Medicham",
    "Electrike", "Manectric", "Plusle", "Minun", "Volbeat", "Illumise", "Roselia",
    "Gulpin", "Swalot", "Carvanha", "Sharpedo", "Wailmer", "Wailord", "Numel",
    "Camerupt", "Torkoal", "Spoink", "Grumpig", "Spinda", "Trapinch", "Vibrava",
    "Flygon", "Cacnea", "Cacturne", "Swablu", "Altaria", "Zangoose", "Seviper",
    "Lunatone", "Solrock", "Barboach", "Whiscash", "Corphish", "Crawdaunt",
    "Baltoy", "Claydol", "Lileep", "Cradily", "Anorith", "Armaldo", "Feebas",
    "Milotic", "Castform", "Kecleon", "Shuppet", "Banette", "Duskull", "Dusclops",
    "Tropius", "Chimecho", "Absol", "Wynaut", "Snorunt", "Glalie", "Spheal",
    "Sealeo", "Walrein", "Clamperl", "Huntail", "Gorebyss", "Relicanth", "Luvdisc",
    "Bagon", "Shelgon", "Salamence", "Beldum", "Metang", "Metagross", "Regirock",
    "Regice", "Registeel", "Latias", "Latios", "Kyogre", "Groudon", "Rayquaza",
    "Jirachi", "Deoxys", "Turtwig", "Grotle", "Torterra", "Chimchar", "Monferno",
    "Infernape", "Piplup", "Prinplup", "Empoleon", "Starly", "Staravia", "Staraptor",
    "Bidoof", "Bibarel", "Kricketot", "Kricketune", "Shinx", "Luxio", "Luxray",
    "Budew", "Roserade", "Cranidos", "Rampardos", "Shieldon", "Bastiodon",
    "Burmy", "Wormadam", "Mothim", "Combee", "Vespiquen", "Pachirisu", "Buizel",
    "Floatzel", "Cherubi", "Cherrim", "Shellos", "Gastrodon", "Ambipom", "Drifloon",
    "Drifblim", "Buneary", "Lopunny", "Mismagius", "Honchkrow", "Glameow", "Purugly",
    "Chingling", "Stunky", "Skuntank", "Bronzor", "Bronzong", "Bonsly", "Mime Jr.",
    "Happiny", "Chatot", "Spiritomb", "Gible", "Gabite", "Garchomp", "Munchlax",
    "Riolu", "Lucario", "Hippopotas", "Hippowdon", "Skorupi", "Drapion", "Croagunk",
    "Toxicroak", "Carnivine", "Finneon", "Lumineon", "Mantyke", "Snover", "Abomasnow",
    "Weavile", "Magnezone", "Lickilicky", "Rhyperior", "Tangrowth", "Electivire",
    "Magmortar", "Togekiss", "Yanmega", "Leafeon", "Glaceon", "Gliscor", "Mamoswine",
    "Porygon-Z", "Gallade", "Probopass", "Dusknoir", "Froslass", "Rotom", "Uxie",
    "Mesprit", "Azelf", "Dialga", "Palkia", "Heatran", "Regigigas", "Giratina",
    "Cresselia", "Phione", "Manaphy", "Darkrai", "Shaymin", "Arceus"
]

# Brief Description of the Program and its Functions to the User
print("---------------------------------------------------------")

i_mode = input("What would you like to do?\n"
               "(1) Randomly assign your IDs to labels\n"
               "(2) Rename files using already randomly ID-label pairs\n"
               "(3) Unblind file names using ID-label pairs\n"
               "(1/2/3): ")

# Insert user ID-label pairs
if i_mode in ["2", "3"]:
    print("You'll have to input the ID-labels pairs.\n"
          "Here's an example of the required format:\nID1,label1,ID2,label2,...IDn,labeln")
    while True:
        i_user_pairs = input()
        space_in_i_user_pairs = " " in i_user_pairs
        duplicates_in_i_user_pairs = len(list(i_user_pairs.split(","))) != len(list(set(i_user_pairs.split(","))))
        pairs_in_i_user_pairs = len(i_user_pairs.split(",")) % 2 != 0
        if space_in_i_user_pairs:
            print("Error: Your input contains spaces. Please try again.")
        elif duplicates_in_i_user_pairs:
            print("Error: Your input contains duplicate IDs, labels, or pairs. Please try again.")
        elif pairs_in_i_user_pairs:
            print("Error: Your input does not contain the same amount of IDs and labels. Please try again.")
        elif not space_in_i_user_pairs and not duplicates_in_i_user_pairs and not pairs_in_i_user_pairs:
            if i_user_pairs.endswith(","):
                i_user_pairs = i_user_pairs[:-1]
                print("Your input ended with a comma, but it was deleted.")
            break
    i_user_pairs = i_user_pairs.split(",")
    id_label_pairs = dict(zip(i_user_pairs[::2], i_user_pairs[1::2]))
    print(f"{int(len(i_user_pairs)/2)} ID-label pairs were successfully imported.")
    i_print_user_pairs = input("Would you like to see your pairs?(yes/no): ")
    if i_print_user_pairs == "yes":
        print("ID,Label")
        for ID, label in id_label_pairs.items():
            print(f"{ID},{label}")
        print(f"All ID-label pairs were printed.")

# Unblind File Names using the ID-label pairs:
if i_mode == "3":
    i_re_rename_folder_path = input("What's the path to the folder?:\n")
    id_label_pairs_inverted = {value: key for key, value in id_label_pairs.items()}
    for file_name in os.listdir(i_re_rename_folder_path):
        file_path = os.path.join(i_re_rename_folder_path, file_name)
        if os.path.isfile(file_path):
            file_name_without_extension, file_extension = os.path.splitext(file_name)
            for label, ID in id_label_pairs_inverted.items():
                if label in file_name_without_extension:
                    new_file_name = f"{id}{file_extension}"
                    new_file_path = os.path.join(i_re_rename_folder_path, new_file_name)
                    os.rename(file_path, new_file_path)
                    print(f"The file {file_name} was re-renamed successfully.")
                    break

# Randomly assign IDs to labels:
if i_mode == "1":
    # Ask if the User wants to use the default labels and/or Update them if needed
    i_which_label = input("Would you like to use the default labels, Pokémon Names? (yes/no): ")
    if i_which_label == "no":
        labels_list = []
        while True:
            i_new_labels_list = input("Insert new labels separated only by commas (,):\n")
            space_i_new_labels_list = " " in i_new_labels_list
            if space_i_new_labels_list:
                print("Error: Your input contains spaces. Please try again.")
            else:
                if i_new_labels_list.endswith(","):
                    i_new_labels_list = i_new_labels_list[:-1]
                    print("Your input ended with a comma, but it was deleted")
                labels_list += list(set(i_new_labels_list))
                print(f"You have now {len(labels_list)} labels.\nIf needed, you'll be able to add more later.")

    # Check For No Spaces and Duplicates in the inputted IDs List
    while True:
        i_ids = input("Please input the list of IDs. They must be separated by only a comma (,):\n")
        space_i_ids = " " in i_ids
        duplicate_i_ids = len(list(i_ids.split(","))) != len(list(set(i_ids.split(","))))
        if space_i_ids:
            print("Error: Your input contains spaces. Please try again.")
        elif duplicate_i_ids:
            print("Error: Your input contains duplicate IDs. Please try again.")
        elif not space_i_ids and not duplicate_i_ids:
            if i_ids.endswith(","):
                i_ids = i_ids[:-1]
                print("Your input ended with a comma, but it was handled")
            ids_list = list(set(i_ids.split(",")))  # Convert the inputted IDs into an ID list
            break

    # Check if there enough labels for every ID
    if len(labels_list) < len(ids_list):
        print(f"You'll have to insert {len(ids_list) - len(labels_list)} more unique labels.")
        while len(labels_list) < len(ids_list):
            i_new_labels = input("Add more labels, separated by commas (,):\n")
            space_i_new_labels = " " in i_new_labels
            if space_i_new_labels:
                print("Error: Your input contains spaces. Please try again.")
            else:
                if i_new_labels.endswith(","):
                    i_new_labels = i_new_labels[:-1]
                new_labels = i_new_labels.split(",")
                labels_list += new_labels
                labels_list = list(set(labels_list))
                print(f"Now, you have enough labels.")

    # Randomly Associate an ID to a Label
    print(f"You have entered {len(ids_list)} unique IDs.")
    print(f"There are {len(labels_list)} labels.")
    random_label_selection = random.sample(labels_list, len(ids_list))
    id_label_pairs = dict(zip(ids_list, random_label_selection))
    print("IDs have been randomly assigned to a label.")

    # Reveal Associations. Either Printing them or Create a file
    while True:
        print("Should the ID-label pairs be displayed here or create a file instead?")
        print("If you are the experimenter, it is suggested that a file is created.")
        i_view_file = input("(print/file): ")
        if i_view_file == "print":
            i_warning = input("You will see the ID-label pairs if you print. Are you sure? (yes/no): ")
            if i_warning == "yes":
                print("ID,Label")
                for ID, label in id_label_pairs.items():
                    print(f"{ID},{label}")
                print("All ID-label pairs have been printed.")
                break
            else:
                i_view_file = "file"
        else:
            blind_file_name = input("Name of the file: ")
            blind_file_path = input("Location of the file:\n")
            blind_file_directory = blind_file_path + "\\" + blind_file_name
            with open(blind_file_directory, "w") as file_blind_ids:
                file_blind_ids.write("ID,Label\n")
                for ID, label in id_label_pairs.items():
                    file_blind_ids.write(f"{ID},{label}\n")
                print(f"The file in CSV format (Comma-Separated Values) was created in:\n{blind_file_directory}")
                i_open_folder = input("Would you like to open the folder? (yes/no): ")
                if i_open_folder == "yes":
                    print("If you are the experimenter, it is not recommended for you open the file.")
                    i_warning = input("Are you sure you want to open the folder? (yes/no): ")
                    if i_warning == "yes":
                        if op_system == "Windows":
                            os.system(f'explorer "{blind_file_path}"')
                            print("Opened!")
                        elif op_system == "Darwin":
                            os.system(f'open "{blind_file_path}"')
                            print("Opened!")
                        else:
                            print("Unsupported operating system.")
                        break

# Rename Files according to id_label_pairs
if i_mode in ["1", "2"]:
    i_rename_files = input("Would you like to rename files according to the ID-label pairs? (yes/no): ")
    if i_rename_files != "yes":
        print("All Done!")
        exit()
    else:
        i_rename_folder_path = input("What's the path to the folder?:\n")
        for file_name in os.listdir(i_rename_folder_path):
            file_path = os.path.join(i_rename_folder_path, file_name)
            if os.path.isfile(file_path):
                file_name_without_extension, file_extension = os.path.splitext(file_name)
                file_id = id_label_pairs.get(file_name_without_extension)
                if file_id is not None:
                    new_file_name = f"{file_id}{file_extension}"
                    new_file_path = os.path.join(i_rename_folder_path, new_file_name)
                    os.rename(file_path, new_file_path)
                    print(f"The file {file_name} was renamed successfully")

# Open The Folder
i_open_folder = input("Would you like to open the folder? (yes/no): ")
if i_mode in ["1", "2"]:
    if i_open_folder == "yes" and i_rename_folder_path != blind_file_path:
        os.system(f'explorer "{i_rename_folder_path}"')
        print("Opened!")
    elif i_open_folder == "yes" and i_rename_folder_path == blind_file_path:
        print("If you are the experimenter, it is not recommended for you open the ID-label pairs file.")
        i_warning = input("Are you sure you want to open the folder? (yes/no): ")
        if i_warning == "yes":
            if op_system == "Windows":
                os.system(f'explorer "{i_rename_folder_path}"')
                print("Opened!")
            elif op_system == "Darwin":
                os.system(f'open "{i_rename_folder_path}"')
                print("Opened!")
            else:
                print("Unsupported operating system.")
elif i_mode == "3":
    if op_system == "Windows":
        os.system(f'explorer "{i_re_rename_folder_path}"')
        print("Opened!")
    elif op_system == "Darwin":
        os.system(f'open "{i_rename_folder_path}"')
        print("Opened!")
    else:
        print("Unsupported operating system.")

print("All done!")
exit()
