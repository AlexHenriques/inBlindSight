from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ttkbootstrap as tb
from PIL import ImageTk
import random

# IDBlindinTool: Original Labels
og_labels_list = [
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

# IDBlindingTool: Global Variables
labels_list = []
ids_list = []
id_label_pairs = []

# Tkinter: Global Variables
use_new_labels = None
seed = None
randomize_button = None


# IDBlindingTool: Functions
def validate_ids():
    global inputed_ids, ids_list
    i_ids = str(inputed_ids.get())
    space_i_ids = " " in i_ids
    duplicate_i_ids = len(list(i_ids.split(","))) != len(list(set(i_ids.split(","))))
    if space_i_ids:
        messagebox.showinfo("Error", "Input must NOT contains spaces. Please try again.")
    elif duplicate_i_ids:
        messagebox.showinfo("Error", "Input has duplicates. Please try again.")
    elif not space_i_ids and not duplicate_i_ids:
        if i_ids.endswith(","):
            i_ids = i_ids[:-1]
        ids_list += list(set(i_ids.split(",")) - set(ids_list))
        messagebox.showinfo("Success", f"In total, {len(ids_list)} IDs were successefuly imported.")
        ttk.Label(mode1_frame, text=f'You have inputed {len(ids_list)} ids').grid(row=5, column=0, pady=10)
        root.after(1000, check_random_condition)


def check_random_condition():
    global randomize_button
    if len(ids_list) > 0:
        if len(labels_list) >= len(ids_list):
            randomize_button.config(state='normal')
        else:
            randomize_button.config(state='disabled')


def validate_new_labels():
    global labels_list
    i_new_labels_list = str(inserted_labels_entry.get())
    if " " in i_new_labels_list:
        i_new_labels_list = i_new_labels_list.replace(' ', '')
    if i_new_labels_list.endswith(","):
        i_new_labels_list = i_new_labels_list[:-1]
    i_new_labels_list = i_new_labels_list.split(',')
    labels_list = list(set(i_new_labels_list))
    # TODO: Make sure there are the same or more number of labels than IDs and have messagebox for each condition
    # if len(IDs_list) < len(labels_list):
    # messagebox.showinfo("Information", f"You inserted {len(labels_list)} labels,
    # and you need at least {len(IDs_list)}")
    # else:
    messagebox.showinfo("Success", f"{len(labels_list)} labels were successfuly imported")
    ttk.Label(mode1_frame, text=f'You have inputed {len(labels_list)} labels').grid(row=4, column=2, pady=10)


def randomize():
    global id_label_pairs
    random.seed(seed)
    random_label_selection = random.sample(labels_list, len(ids_list))
    id_label_pairs = dict(zip(ids_list, random_label_selection))
    messagebox.showinfo('Success', 'IDs have been randomly assigned to a label.')


def rename():
    pass


# TKinter: Functions
def load_input_new_labels():
    global inserted_labels_entry, validate_labels_button, imported_labels_entry, imported_labels_button, format_label, \
        labels_list
    if use_new_labels.get() == 1:
        inserted_labels_entry.grid(row=8, column=2, padx=10, pady=10, sticky='ew')
        validate_labels_button.grid(row=8, column=3, padx=10, pady=10, sticky='ew')
        imported_labels_entry.grid(row=9, column=2, padx=10, pady=(10, 0), sticky='ew')
        imported_labels_button.grid(row=9, column=3, padx=10, pady=(10, 0), sticky='ew')
        format_label.grid(row=10, column=3, sticky='n')
    else:
        inserted_labels_entry.grid_remove()
        validate_labels_button.grid_remove()
        imported_labels_entry.grid_remove()
        imported_labels_button.grid_remove()
        format_label.grid_remove()
        labels_list = og_labels_list


def load_initial_frame():
    initial_frame.tkraise()
    initial_frame.grid_propagate(False)

    # Widget: Logo
    logo_img = ImageTk.PhotoImage(file='Images/logo-02.png')
    logo_widget = ttk.Label(initial_frame, image=logo_img)
    logo_widget.image = logo_img
    logo_widget.grid(row=0, column=0)

    ttk.Label(initial_frame, text='Blinding Tool for Experimental Research',
              font='Aptos').grid(row=1, column=0)

    ttk.Button(initial_frame, text='Randomly assign your IDs to labels',
               cursor='hand2', command=lambda: load_mode1()).grid(row=2, column=0, padx=20, pady=20)
    ttk.Button(initial_frame, text='Rename files using already randomly ID-label pairs',
               cursor='hand2', command=lambda: load_mode2()).grid(row=2, column=2, padx=20, pady=20)


def load_mode1():
    mode1_frame.tkraise()

    # Widget: Logo
    logo_img = ImageTk.PhotoImage(file='Images/logo-02.png')
    logo_widget = ttk.Label(mode1_frame, image=logo_img)
    logo_widget.image = logo_img
    logo_widget.grid(row=0, column=0)

    ttk.Label(mode1_frame, text='Randomly assign your IDs to labels',
              font='Aptos', width=100).grid(row=0, column=2, padx=10, sticky='n')

    (ttk.Label(mode1_frame,
               text='Placeholder Description')
     .grid(row=0, column=2, columnspan=2, padx=10, pady=(50, 0), sticky='nw'))

    # IDs Section
    inputed_ids = StringVar()
    inputed_ids_entry = (Entry(mode1_frame, textvariable=inputed_ids)
                         .grid(row=2, column=2, padx=(10, 0), pady=10, sticky='nsew'))
    validate_ids_button = (ttk.Button(mode1_frame, text='Insert IDs', command=lambda: validate_ids())
                           .grid(row=2, column=3, padx=10, pady=10, sticky='nsew'))
    imported_ids = StringVar()
    import_ids_entry = (Entry(mode1_frame, textvariable=imported_ids)
                        .grid(row=3, column=2, padx=(10, 0), pady=(10, 0), sticky='nsew'))
    import_ids_button = (ttk.Button(mode1_frame, text='Import IDs', command=lambda: validate_ids())
                         .grid(row=3, column=3, padx=10, pady=(10, 0), sticky='nsew'))
    ttk.Label(mode1_frame, text='.csv, .txt').grid(row=4, column=3)
    ttk.Label(mode1_frame, text=' BLANK SPACE ').grid(row=5, column=2)  # Space to be refreshed

    # Label Section
    ttk.Label(mode1_frame, text=' Placeholder Description ').grid(row=6, column=2)
    ttk.Label(mode1_frame, text=' Placeholder Number of Labels ').grid(row=7, column=2)  # Space to be refreshed
    ttk.Label(mode1_frame, text='Use Your Labels').grid(row=2, column=0, padx=(0, 25))
    global use_new_labels
    use_new_labels = IntVar()
    use_new_labels_check = (tb.Checkbutton(mode1_frame, style='info, round-toggle',
                                           variable=use_new_labels, onvalue=1, offvalue=0,
                                           command=lambda: load_input_new_labels())
                            .grid(row=2, column=0, padx=(100, 0), pady=10))

    global inserted_labels_entry, validate_labels_button, imported_labels_entry, imported_labels_button, format_label
    inserted_labels_entry = ttk.Entry(mode1_frame)
    validate_labels_button = ttk.Button(mode1_frame, text='Insert New Labels', command=lambda: validate_new_labels())
    imported_labels_entry = ttk.Entry(mode1_frame)
    imported_labels_button = ttk.Button(mode1_frame, text='Import New Labels', command=lambda: validate_new_labels())
    format_label = ttk.Label(mode1_frame, text='.csv, .txt')

    # Separators
    ttk.Separator(mode1_frame, orient='horizontal').grid(row=11, column=2, columnspan=2, padx=(0, 10), sticky="ew")
    ttk.Separator(mode1_frame, orient='vertical').grid(row=0, column=1, rowspan=15, sticky="ns")

    # Randomize TODO: Be able to insert a seed for generation (check if it makes sense)
    ttk.Label(mode1_frame, text='Seed:').grid(row=10, column=0, padx=10, sticky='ew')
    seed = IntVar(value=1)
    seed_entry = (Entry(mode1_frame, textvariable=seed).grid(row=10, column=0, padx=(45, 10), sticky='ew'))
    global randomize_button
    randomize_button = ttk.Button(mode1_frame, text='Randomize', state='disabled', command=lambda: randomize())
    randomize_button.grid(row=11, column=0, padx=10, pady=10, sticky='ew')

    # Return
    return_button = ttk.Button(mode1_frame, text='Return', command=lambda: load_initial_frame())
    return_button.grid(row=13, column=0, padx=10, pady=10, sticky='ew')

    # Rename Files Section
    rename_button = ttk.Button(mode1_frame, text='Rename',  state='disabled', command=lambda: rename())
    rename_button.grid(row=12, column=0, padx=10, pady=(10, 0), sticky='ew')
    ttk.Label(mode1_frame, text='Name of the File:').grid(row=12, column=2, padx=(10, 0), sticky='w')
    filename = StringVar()
    filename_entry = (Entry(mode1_frame, textvariable=filename)
                      .grid(row=12, column=2, columnspan=2, padx=(110, 10), sticky='ew'))
    ttk.Label(mode1_frame, text='Path of the File:').grid(row=13, column=2, padx=(10, 0), sticky='w')
    filepath = StringVar()
    filepath_entry = (Entry(mode1_frame, textvariable=filepath)
                      .grid(row=13, column=2, columnspan=2, padx=(110, 10), sticky='ew'))


def load_mode2():
    pass


root = Tk()
root.iconbitmap('Images/logo-02.ico')
root.title('ID Blinding Tool')

# Window Position:
# root.eval('tk::PlaceWindow . center')

# Frames
initial_frame = ttk.Frame(root, width=1280, height=600)
mode1_frame = ttk.Frame(root)
mode2_frame = ttk.Frame(root)
mode3_frame = ttk.Frame(root)

for frame in (initial_frame, mode1_frame, mode2_frame):
    frame.grid(row=0, column=0, sticky="nsew")

load_initial_frame()

# Run GUI
root.mainloop()
