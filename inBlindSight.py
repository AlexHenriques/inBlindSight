import os
import random
import sys
import webbrowser

import customtkinter as ctk
from customtkinter import filedialog
from CTkMessagebox import CTkMessagebox
import pandas as pd
from PIL import Image

# Directories
home_directory = os.path.expanduser('~')
script_directory = os.path.dirname(sys.argv[0])

FILE_NAMES = ['logo.ico', 'logo.png', 'import.png', 'help.png', 'feedback.png', 'patch_notes.png',
              'JosefinSans-VariableFont_wght.ttf']
file_paths = {}
for file in FILE_NAMES:
    file_paths[file] = os.path.join(script_directory, 'resources', file).replace('\\', '\\\\')

# Bootstrap Basic
light = '#e7efec'
dark = '#212c2f'
primary = '#1b4565'
secondary = '#7da7c0'
tertiary = '#ebcd48'
white = '#ffffff'
info = '#554bd2'
success = '#0db966'
warning = '#ebd00b'
danger = '#fe0406'

# Fonts
lv1_text = ('Josefin Sans Medium', 24)
lv2_text = ('Josefin Sans Bold', 30)
lv3_text = ('Josefin Sans Light', 22)
lv4_text = ('Josefin Sans Regular', 18)
lv5_text = ('Josefin Sans Light', 14)

og_labels_list = [
    'brunswick green', 'fluorescent cyan', 'umber', 'pine green', 'caput mortuum', 'platinum', 'peach', 'red brown',
    'wine', 'tang blue', 'lime', 'antique white', 'tea green', 'chili red', 'coyote', 'parchment', 'turquoise',
    'verdigris', 'dark spring green', 'ruddy blue', 'carnation pink', 'tomato', 'ucla blue', 'hot pink', 'dark green',
    'tangelo', 'carolina blue', 'beige', 'bistre', 'pale azure', 'medium slate blue', 'tyrian purple', 'amaranth pink',
    'taupe gray', 'coffee', 'lavender blush', 'resolution blue', 'byzantine blue', 'magnolia', 'oxford blue',
    'cosmic latte', 'cream', 'lavender pink', 'air superiority blue', 'cal poly green', 'mint', 'cool gray', 'camel',
    'liver', 'maize', 'snow', 'rosy brown', 'lawn green', 'raspberry', 'folly', 'citron', 'orange peel',
    'anti-flash white', 'tawny', 'rust', 'china rose', 'aqua', 'giants orange', 'yinmn blue', 'blood red', 'khaki',
    'vista blue', 'golden gate bridge', 'rojo', 'arylide yellow', 'ebony', 'bittersweet', 'madder', 'cyan',
    'slate gray', 'lemon chiffon', 'shamrock green', 'ut orange', 'denim', 'gray', 'poppy', 'air force blue',
    'powder blue', 'uranian blue', 'french violet', 'salmon pink', 'turkey red', 'rose quartz', 'desert sand',
    'rebecca purple', 'international klein blue', 'aureolin', 'grape', 'midnight green', 'brandeis blue', 'wheat',
    'pearl', 'sage', 'safety orange', 'office green', 'rosewood', "hooker's green", 'light blue', 'scarlet', 'black',
    'light yellow', 'reseda green', 'magenta', 'tufts blue', 'smoky black', 'finn', 'green', 'hollywood cerise',
    "payne's gray", 'malachite', 'lapis lazuli', 'azul', 'tropical indigo', 'alice blue', 'eminence', 'tiffany blue',
    'zaffre', 'violet blue', "screamin'green", 'rose pink', 'off red', 'celestial blue', 'tan', 'pakistan green',
    'amaranth', 'dogwood rose', 'bittersweet shimmer', 'wenge', 'pomp and power', 'argentinian blue', 'flame',
    'maya blue', 'fire engine red', 'mikado yellow', 'quinacridone magenta', 'blue violet', 'mauve', 'telemagenta',
    'royal purple', 'rose pompadour', 'eggshell', 'aerospace orange', 'white smoke', 'fuchsia rose', 'vanilla', 'coral',
    'ivory', 'citrine', 'tangerine', 'eerie black', 'jet', 'navajo white', 'majorelle blue', 'british racing green',
    'azure', 'iris', 'navy blue', 'indigo dye', 'celtic blue', 'shocking pink', 'red', 'rose red', 'yellow green',
    'amethyst', 'pigment green', 'dark violet', 'gunmetal', 'puce', 'ecru', 'cornell red', 'russet',
    'school bus yellow', 'steel blue', 'white', 'silver', 'fulvous', 'mantis', 'chocolate cosmos', 'dark moss green',
    'buff', 'pink lavender', 'tea rose', 'champagne pink', 'sgbus green', 'rufous', 'black olive', 'heliotrope',
    'cherry blossom pink', 'claret', 'dark pastel green', 'candy apple red', 'brown', 'seashell', 'outer space',
    'electric indigo', 'harvest gold', 'burnt umber', 'federal blue', 'silver lake blue', 'canary', 'imperial red',
    'dark cyan', 'ghost white', 'teal', 'mimi pink', 'byzantium', 'ash gray', 'cinnabar', 'moss green', 'crimson',
    'non photo blue', 'hunter green', 'process cyan', 'mulberry', 'bleu de france', 'japanese violet', 'misty rose',
    'pink', 'dartmouth green', 'steel pink', 'purpureus', 'bice blue', 'dark slate gray', 'viridian', 'aquamarine',
    'rose bonbon', 'café noir', 'mahogany', 'celeste', 'rose ebony', 'neon green', 'tiger’s eye', 'columbia blue',
    'walnut brown', 'xanthous', 'charcoal', 'falu red', 'duke blue', 'penn blue', 'ultra violet', 'black bean', 'onyx',
    'persian red', 'beaver', 'lime green', 'jasmine', 'murrey', 'india green', 'nyanza', 'hunyadi yellow', 'apricot',
    'mint cream', 'polynesian blue', 'light red', 'french blue', 'jade', 'indian red', 'butterscotch', 'persian pink',
    'ice blue', 'dark purple', 'salmon', 'penn red', 'cornsilk', 'champagne', 'palatinate blue', 'fire brick',
    'sky blue', 'red violet', 'tekhelet', 'mauveine', 'taupe', 'zomp', 'pacific cyan', 'persimmon', 'electric violet',
    'spring green', 'lemon lime', 'persian orange', 'gold', 'bronze', 'olivine', 'skobeloff', 'jordy blue',
    'baby powder', 'seasalt', "davy's gray", 'fairy tale', 'keppel', 'bone', 'violet', 'isabelline', 'chocolate',
    'alabaster', 'cocoa brown', 'garnet', 'almond', 'russian violet', 'persian green', 'floral white', 'dark goldenrod',
    'cyclamen', 'satin sheen gold', 'plum', 'prussian blue', 'periwinkle', 'ou crimson', 'united nations blue',
    'saffron', 'selective yellow', 'bondi blue', 'coral pink', 'field drab', 'feldgrau', 'rich black', 'picton blue',
    'magenta dye', 'persian blue', 'glaucous', 'golden brown', 'savoy blue', 'van dyke', 'light coral', 'jungle green',
    'spring bud', 'pear', 'purple pizzazz', 'baby blue', 'lilac', 'alloy orange', 'baker-miller pink', 'indigo',
    'slate blue', 'sinopia', 'robin egg blue', 'deep pink', 'true blue', 'light cyan', 'midnight blue', 'sky magenta',
    'orchid pink', 'light sea green', 'orchid', 'bright green', 'light sky blue', 'carmine', 'pistachio', 'old gold',
    'orange', 'maroon', 'dark red', 'cordovan', 'french rose', 'spanish orange', 'fern green', 'old rose', 'yellow',
    'phlox', 'ochre', 'risd blue', 'english violet', 'fawn', 'fuchsia', 'brown sugar', 'royal blue', 'chefchaouen blue',
    'medium blue', 'tickle me pink', 'pale dogwood', 'redwood', 'capri', 'timberwolf', 'cerulean', 'honeydew', 'sienna',
    'licorice', 'mexican pink', 'cobalt blue', 'dodger blue', 'atomic tangerine', 'electric purple', 'light green',
    'dim gray', 'berkeley blue', 'purple', 'hot magenta', 'neon blue', 'chartreuse', 'chamoisee', 'earth yellow',
    'fandango', 'ultramarine', 'light orange', 'cinereous', 'sandy brown', 'burgundy', 'raisin black', 'avocado',
    'magenta haze', 'chinese violet', 'celadon', 'bright pink', 'mustard', 'blue green', 'cantaloupe melon', 'caramel',
    'green blue', 'electric blue', 'carrot orange', 'rusty red', 'drab dark brown', 'bole', 'african violet',
    'princeton orange', 'sunset', 'goldenrod', 'syracuse red orange', 'mindaro', 'marian blue', 'lavender', 'jonquil',
    'erin', 'peach yellow', 'harlequin', 'amber', 'jasper', 'rose', 'moonstone', 'vermilion', 'rose taupe',
    'apple green', 'cardinal', 'chestnut', 'pumpkin', 'flax', 'blue', 'razzle dazzle rose', 'veronica', 'wisteria',
    'sepia', 'asparagus', 'emerald', 'pale purple', 'kelly green', 'castleton green', 'burnt orange', 'dark magenta',
    'blue gray', 'papaya whip', 'aero', 'persian rose', 'delft blue', 'battleship gray', 'french mauve', 'green yellow',
    'thistle', 'copper', 'phthalo blue', 'palatinate', 'raspberry rose', 'forest green', 'mardi gras', 'gamboge',
    'french gray', 'raw umber', 'vivid sky blue', 'engineering orange', 'night', 'icterine', 'myrtle green', 'straw',
    'barn red', 'space cadet', 'cadet gray', 'sapphire', 'cambridge blue', 'dark orange', 'cornflower blue',
    'seal brown', 'thulian pink', 'old lace', 'kobicha', 'caribbean current', 'olive', 'sunglow', 'coquelicot',
    'amaranth purple', 'naples yellow', 'persian indigo', 'eggplant', 'mint green', 'burnt sienna', 'mountbatten pink',
    'chrysler blue', 'dutch white', 'sea green', 'dun', 'razzmatazz', 'linen', 'cerise', 'egyptian blue', 'yale blue',
    'blush', 'honolulu blue'
]


class InBlindSight:
    def __init__(self, root):
        self.ids_list = []
        self.labels_list = og_labels_list
        self.id_label_pairs = {}

        self.root = root
        self.root.title('inBlindSight')
        self.root.iconbitmap(file_paths['logo.ico'])

        self.page1 = ctk.CTkFrame(root, fg_color=light, corner_radius=1)
        self.page2 = ctk.CTkFrame(root, fg_color=light, corner_radius=1)
        self.page3 = ctk.CTkFrame(root, fg_color=light, corner_radius=1)

        self.create_page1()
        self.create_page2()
        self.create_page3()

        self.show_page(self.page1)

        self.user_labels_list = []

        def switch_callback(*args):
            if self.default_labels_switch_var.get() == 'n':
                self.labels_list = self.user_labels_list
                self.len_labels_list.set(str(len(self.user_labels_list)))
            else:
                self.labels_list = og_labels_list
                self.len_labels_list.set(str(len(og_labels_list)))
        self.default_labels_switch_var.trace_add("write", switch_callback)

    def create_page1(self):
        for r in range(1, 5):
            self.page1.rowconfigure(r, weight=1)
        for c in range(0, 10):
            self.page1.columnconfigure(c, weight=1)

        logo_img = ctk.CTkImage(light_image=Image.open(file_paths['logo.png']), size=(256, 132))
        ctk.CTkLabel(self.page1, image=logo_img, text='').grid(
            row=0, column=0, columnspan=9, pady=(20, 0))
        ctk.CTkLabel(self.page1, text="Data Blinding Made\nEffortless and Seamless",
                     text_color=dark, font=lv1_text).grid(
            row=1, column=0, columnspan=9, padx=10, pady=(0, 10))

        ctk.CTkButton(self.page1, command=self.show_page2,
                      corner_radius=25, height=50,
                      fg_color=primary, hover_color=secondary, anchor='center',
                      text="Generate Key", text_color=light, font=lv3_text).grid(
            row=2, column=0, columnspan=9, padx=10, sticky='swe')

        ctk.CTkButton(self.page1, command=self.show_page3,
                      corner_radius=25, height=50,
                      fg_color=primary, hover_color=secondary, anchor='center',
                      text="Rename Datasets or Files", text_color=light, font=lv3_text).grid(
            row=3, column=0, columnspan=9, padx=10, pady=(10, 10), sticky='nwe')

        help_img = ctk.CTkImage(light_image=Image.open(file_paths['help.png']), size=(30, 30))
        ctk.CTkButton(self.page1, command=lambda: InBlindSight.open_github('instructions'),
                      fg_color=light, image=help_img,
                      text='', hover=False,
                      corner_radius=1, width=1).grid(
            row=4, column=0, sticky='s', pady=10)
        feedback_img = ctk.CTkImage(light_image=Image.open(file_paths['feedback.png']), size=(30, 30))
        ctk.CTkButton(self.page1, command=lambda: InBlindSight.open_github('feedback'),
                      fg_color=light, image=feedback_img,
                      text='', hover=False,
                      corner_radius=1, width=1).grid(
            row=4, column=1, sticky='s', pady=10)
        patch_img = ctk.CTkImage(light_image=Image.open(file_paths['patch_notes.png']), size=(30, 30))
        ctk.CTkButton(self.page1, command=lambda: InBlindSight.open_github('release'),
                      fg_color=light, image=patch_img,
                      text='', hover=False,
                      corner_radius=1, width=1).grid(
            row=4, column=2, sticky='s', pady=10)

    def create_page2(self):
        for r in range(0, 9):
            self.page2.rowconfigure(r, weight=1)
        for c in range(0, 4):
            self.page2.columnconfigure(c, weight=1)

        ctk.CTkLabel(self.page2, text="Randomly Generate a Key",
                     text_color=dark, font=lv1_text).grid(
            row=0, column=0, columnspan=5, sticky='s')

        self.len_ids_list = ctk.StringVar(value=f'{len(self.ids_list)}')
        ctk.CTkLabel(self.page2, textvariable=self.len_ids_list,
                     text_color=dark, font=lv2_text, anchor='w').grid(
            row=1, column=0, columnspan=3, sticky='e', padx=(10, 5))
        ctk.CTkLabel(self.page2, text="Identifiers",
                     text_color=dark, font=lv3_text, anchor='sw').grid(
            row=1, column=3, columnspan=2, sticky='w', padx=(5, 10))

        self.inputted_ids_entry = ctk.CTkEntry(self.page2, placeholder_text='id1,id2,id3',
                                               corner_radius=5, height=30, width=200)
        self.inputted_ids_entry.grid(row=2, column=0, columnspan=4, sticky='ew', padx=(10, 5))
        ctk.CTkButton(self.page2, command=lambda: self.validate_inserted_data('IDs', 'Entry'),
                      corner_radius=15, height=25,
                      fg_color=tertiary, hover_color=tertiary, anchor='center',
                      text="Insert IDs", text_color=dark, font=lv4_text).grid(
            row=2, column=4, sticky='ew', padx=(5, 10))

        ctk.CTkLabel(self.page2, text='Sheet:',
                     text_color=dark, font=lv5_text).grid(
            row=3, column=0, padx=(10, 0), sticky='e')
        self.sheet_entry_id = ctk.CTkEntry(self.page2, placeholder_text='1', width=20)
        self.sheet_entry_id.grid(row=3, column=1)
        ctk.CTkLabel(self.page2, text='Column:',
                     text_color=dark, font=lv5_text).grid(
            row=3, column=2)
        self.column_entry_id = ctk.CTkEntry(self.page2, placeholder_text='1', width=20)
        self.column_entry_id.grid(
            row=3, column=3, padx=(0, 0), sticky='w')
        ctk.CTkButton(self.page2, command=lambda: self.validate_inserted_data('IDs', 'File'),
                      corner_radius=15, height=25,
                      fg_color=tertiary, hover_color=tertiary, anchor='center',
                      text="Import IDs from File", text_color=dark, font=lv4_text).grid(
            row=3, column=4, sticky='ew', padx=(5, 10))

        self.len_labels_list = ctk.StringVar(value=f'{len(self.labels_list)}')
        ctk.CTkLabel(self.page2, textvariable=self.len_labels_list,
                     text_color=dark, font=lv2_text, anchor='w').grid(
            row=4, column=0, columnspan=3, sticky='e', padx=(10, 0))
        ctk.CTkLabel(self.page2, text="Labels",
                     text_color=dark, font=lv3_text, anchor='sw').grid(
            row=4, column=3, columnspan=2, sticky='w', padx=10)

        self.default_labels_switch_var = ctk.StringVar(value="y")
        default_labels_switch = ctk.CTkSwitch(self.page2, variable=self.default_labels_switch_var,
                                              text='Use Default Labels', font=lv4_text, text_color=dark,
                                              switch_width=50, switch_height=20, button_hover_color=dark,
                                              fg_color=dark, progress_color=success, button_color=dark,
                                              onvalue="y", offvalue="n")
        default_labels_switch.grid(row=5, column=0, columnspan=5, sticky='w', padx=(20, 0))

        self.inputted_labels_entry = ctk.CTkEntry(self.page2, placeholder_text='label1,label2,label3',
                                                  corner_radius=5, height=30, width=200)
        inputted_labels_button = ctk.CTkButton(self.page2,
                                               command=lambda: self.validate_inserted_data('Labels', 'Entry'),
                                               corner_radius=15, height=25,
                                               fg_color=tertiary, hover_color=tertiary, anchor='center',
                                               text="Insert Labels", text_color=dark, font=lv4_text)

        self.sheet_label_label = ctk.CTkLabel(self.page2, text='Sheet:', text_color=dark, font=lv5_text)
        self.sheet_entry_label = ctk.CTkEntry(self.page2, placeholder_text='1', width=20, corner_radius=5)
        self.column_label_label = ctk.CTkLabel(self.page2, text='Column:', text_color=dark, font=lv5_text)
        self.column_entry_label = ctk.CTkEntry(self.page2, placeholder_text='1', width=20, corner_radius=5)
        imported_labels_button = ctk.CTkButton(self.page2,
                                               command=lambda: self.validate_inserted_data('Labels', 'File'),
                                               corner_radius=15, height=25,
                                               fg_color=tertiary, hover_color=tertiary, anchor='center',
                                               text="Import Labels from File", text_color=dark, font=lv4_text)

        def toggle_labels_widgets():
            if self.default_labels_switch_var.get() == "y":
                self.inputted_labels_entry.grid_forget()
                inputted_labels_button.grid_forget()
                self.sheet_label_label.grid_forget()
                self.sheet_entry_label.grid_forget()
                self.column_label_label.grid_forget()
                self.column_entry_label.grid_forget()
                imported_labels_button.grid_forget()
            else:
                self.inputted_labels_entry.grid(row=6, column=0, columnspan=4, sticky='ew', padx=(10, 5))
                inputted_labels_button.grid(row=6, column=4, sticky='ew', padx=(5, 10))
                self.sheet_label_label.grid(row=7, column=0, padx=(10, 0), sticky='e')
                self.sheet_entry_label.grid(row=7, column=1)
                self.column_label_label.grid(row=7, column=2)
                self.column_entry_label.grid(row=7, column=3, padx=(0, 0), sticky='w')
                imported_labels_button.grid(row=7, column=4, sticky='ew', padx=(5, 10))

            if 0 < len(self.ids_list) <= len(self.labels_list):
                self.randomize_button.configure(state='normal')
            else:
                self.randomize_button.configure(state='disabled')

        self.default_labels_switch_var.trace_add("write", lambda *args: toggle_labels_widgets())

        self.randomize_button = ctk.CTkButton(self.page2, command=self.generate_key, state='disabled',
                                              corner_radius=15, height=40,
                                              fg_color=primary, hover_color=secondary, anchor='center',
                                              text='Generate Key', text_color=light, font=lv3_text,
                                              text_color_disabled=light)
        self.randomize_button.grid(
            row=8, column=0, columnspan=5, sticky='ew', padx=10, pady=10)

    def create_page3(self):
        for r in range(0, 6):
            self.page3.rowconfigure(r, weight=1)
        for c in range(0, 4):
            self.page3.columnconfigure(c, weight=1)

        ctk.CTkLabel(self.page3, text="Rename Datasets or Files",
                     text_color=dark, font=lv1_text).grid(
            row=0, column=0, columnspan=5, sticky='s')

        ctk.CTkButton(self.page3, text='Import Key', command=lambda: self.load_id_label_pairs(),
                      corner_radius=15, height=40,
                      fg_color=primary, hover_color=secondary, anchor='center',
                      text_color=light, font=lv3_text).grid(
            row=1, column=0, columnspan=5, padx=10, sticky='ew'+'s')

        self.len_pairs = ctk.StringVar(value=f'{len(self.id_label_pairs)}')
        ctk.CTkLabel(self.page3, textvariable=self.len_pairs,
                     text_color=dark, font=lv2_text, anchor='w').grid(
            row=2, column=0, columnspan=3, sticky='e', padx=(10, 5))
        ctk.CTkLabel(self.page3, text="pairs of ID/label",
                     text_color=dark, font=lv3_text, anchor='sw').grid(
            row=2, column=3, columnspan=2, padx=(5, 10), sticky='w')

        ctk.CTkLabel(self.page3, text='Unblind', font=lv4_text, text_color=dark, width=125).grid(
            row=3, column=0, columnspan=3, padx=(20, 0), sticky='e')
        self.unblind_switch_var = ctk.StringVar(value="blind")
        unblind_switch = ctk.CTkSwitch(self.page3, variable=self.unblind_switch_var,
                                       text='', switch_width=50, switch_height=20, button_hover_color=dark,
                                       fg_color=dark, progress_color=secondary, button_color=dark,
                                       onvalue="blind", offvalue="unblind").grid(
            row=3, column=0, columnspan=5, padx=(70, 0))
        ctk.CTkLabel(self.page3, text='Blind', font=lv4_text, text_color=dark).grid(
            row=3, column=3, columnspan=2, padx=(100, 0), sticky='w')

        ctk.CTkLabel(self.page3, text='Sheet:', text_color=dark, font=lv5_text).grid(
            row=4, column=0, padx=(10, 0))
        self.sheet_entry = ctk.CTkEntry(self.page3, placeholder_text='1', width=20)
        self.sheet_entry.grid(row=4, column=1)
        ctk.CTkLabel(self.page3, text='Column:', text_color=dark, font=lv5_text).grid(row=4, column=2)
        self.column_entry = ctk.CTkEntry(self.page3, placeholder_text='1', width=20)
        self.column_entry.grid(row=4, column=3, padx=(0, 10))
        self.rename_datasets_button = ctk.CTkButton(self.page3, text='Rename Dataset',
                                                    command=lambda: self.rename_datasets(), state='disabled',
                                                    corner_radius=15, height=25,
                                                    fg_color=tertiary, hover_color=tertiary, anchor='center',
                                                    text_color=dark, font=lv4_text, text_color_disabled=light)
        self.rename_datasets_button.grid(row=4, column=4, sticky='ew', padx=(5, 10))

        self.rename_files_button = ctk.CTkButton(self.page3, text='Rename Files',
                                                 command=lambda: self.rename_files(), state='disabled',
                                                 corner_radius=15, height=25,
                                                 fg_color=tertiary, hover_color=tertiary, anchor='center',
                                                 text_color=dark, font=lv4_text, text_color_disabled=light)
        self.rename_files_button.grid(row=5, column=0, columnspan=5, padx=10, sticky='ew'+'n')

    def show_page(self, page):
        self.page2.grid_forget()
        self.page3.grid_forget()
        if page == self.page1:
            page.grid(row=0, column=0, sticky='nsew')
        else:
            page.grid(row=0, column=1, sticky='nsew')

    def show_page2(self):
        if self.page2.winfo_ismapped():
            self.page2.grid_forget()
        else:
            self.show_page(self.page2)
        self.page2.grid_propagate(False)

    def show_page3(self):
        if self.page3.winfo_ismapped():
            self.page3.grid_forget()
        else:
            self.show_page(self.page3)
        self.page3.grid_propagate(False)

    @staticmethod
    def open_github(sublink):
        if sublink == 'instructions':
            webbrowser.open('https://github.com/AlexHenriques/inBlindSight?tab=readme-ov-file#How-to-Use')
        elif sublink == 'feedback':
            webbrowser.open('https://github.com/AlexHenriques/inBlindSight?tab=readme-ov-file#Bugs-&-Feature-Requests')
        elif sublink == 'release':
            webbrowser.open('https://github.com/AlexHenriques/inBlindSight/releases')

    def validate_inserted_data(self, data_type, data_format):
        data = None
        if data_format == 'Entry':
            if data_type == 'IDs':
                data = self.inputted_ids_entry.get()
            elif data_type == 'Labels':
                data = self.inputted_labels_entry.get()
        elif data_format == 'File':
            if data_type == 'IDs':
                sheet = self.sheet_entry_id.get()
                column = self.column_entry_id.get()
            elif data_type == 'Labels':
                sheet = self.sheet_entry_label.get()
                column = self.column_entry_label.get()
            else:
                sheet, column = None, None

            if not (sheet.isdigit() or column.isdigit()):
                CTkMessagebox(title='Dataset Localization Error',
                              message='Please enter a positive integer for sheet and column numbers.',
                              icon='cancel')
            else:
                filename = filedialog.askopenfilename(
                    initialdir=home_directory,
                    title='Select File',
                    filetypes=(('Supported Files: .csv;.xlsx;.xls', '*.csv;*.xlsx;*.xls'), ('All files', '*.*')))
                if not filename:
                    CTkMessagebox(title='File Selection Error',
                                  message='No file selected.\nPlease select a file and try again.',
                                  icon='cancel')
                else:
                    header_id_label_message = CTkMessagebox(title='Header Question',
                                                            message='Does the file have an header?',
                                                            icon='question', option_1='Yes', option_2='No')
                    if header_id_label_message.get() == 'Yes':
                        header_id_label = 0
                    else:
                        header_id_label = None
                    if not filename.endswith(('.csv', '.xlsx', '.xls')):
                        CTkMessagebox(title='Unsupported File Format',
                                      message='Please select a supported file format.'
                                              '\nSupported formats: .csv, .xlsx, .xls',
                                      icon='cancel')
                    else:
                        if sheet == '' or sheet == '0':
                            sheet = 1
                        else:
                            sheet = int(sheet) - 1
                        if column == '' or column == '0':
                            column = 1
                        else:
                            column = int(column) - 1

                        if filename.endswith('.csv'):
                            data = pd.read_csv(filename, header=header_id_label)

                        elif filename.endswith(('.xlsx', '.xls')):
                            data = pd.read_excel(filename, sheet_name=(sheet-1), header=header_id_label)
                        data = data.iloc[:, column]
                        data = data.astype(str)
                        data = ','.join(data)

        if data is not None:
            duplicate_data = len(data.split(',')) != len(set(data.split(',')))
            if duplicate_data:
                CTkMessagebox(title='Duplicates Detected',
                              message='The inserted data contains duplicates.\n'
                                      'Please ensure each entry is unique and try again',
                              icon='cancel')
            else:
                replace_patterns = ['\n', ',,', ' ,', ', ']
                for pattern in replace_patterns:
                    data = data.replace(pattern, ',')

                data = data.strip(',').split(',')

                initial_len = len(self.ids_list) if data_type == 'IDs' else\
                    len(self.user_labels_list) if data_type == 'Labels' else\
                    None

                if data_type == 'IDs':
                    self.ids_list += list(set(data) - set(self.ids_list))
                elif data_type == 'Labels':
                    self.user_labels_list += list(set(data) - set(self.user_labels_list))

                self.len_ids_list.set(str(len(self.ids_list)))
                self.len_labels_list.set(str(len(self.labels_list)))

                if 0 < len(self.ids_list) <= len(self.labels_list):
                    self.randomize_button.configure(state='normal')
                else:
                    self.randomize_button.configure(state='disabled')

                added_len = (len(self.ids_list) if data_type == 'IDs' else
                             len(self.user_labels_list) if data_type == 'Labels' else
                             None) - initial_len

                if added_len != len(data):
                    CTkMessagebox(title=f'Duplicate {data_type} Detected',
                                  message=f'It seems that some {data_type} entered have been previously added.\n'
                                          f'Only {added_len} out of {len(data)} {data_type} were actually added.\n'
                                          f'Please review your input and try again',
                                  icon='cancel')

    def generate_key(self):
        random.shuffle(self.labels_list)  # Increase randomness
        random_label_selection = random.sample(self.labels_list, len(self.ids_list))  # Randomly select labels
        self.id_label_pairs = list(zip(self.ids_list, random_label_selection))  # Randomly pairs unique IDs to labels

        key_df = pd.DataFrame(self.id_label_pairs, columns=['ID', 'Label'])

        output_filepath = filedialog.asksaveasfilename(
            initialdir=home_directory,
            title='Save As',
            filetypes=(('.xlsx', '*.xlsx'), ('All files', '*.*'))
        )
        if output_filepath:
            key_df.to_excel(output_filepath + '.xlsx', index=False)
            CTkMessagebox(title='Success',
                          message=f'{output_filepath} was successfully renamed',
                          icon='check')
        else:
            CTkMessagebox(title='File Selection Error',
                          message='No file selected.\nPlease select a file and try again.',
                          icon='cancel')

    def load_id_label_pairs(self):
        ids_label_pairs_filename = filedialog.askopenfilename(
            initialdir=home_directory,
            title='Select File',
            filetypes=(('Supported Files: .csv;.xlsx;.xls', '*.csv;*.xlsx;*.xls'), ('All files', '*.*')))

        if not ids_label_pairs_filename:
            CTkMessagebox(title='File Selection Error',
                          message='No file selected.\nPlease select a file and try again.',
                          icon='cancel')
        else:
            header = CTkMessagebox(title='Header Question',
                                   message='Does the file have an header?',
                                   icon='question', option_1='Yes', option_2='No')
            df = None
            if ids_label_pairs_filename.endswith('.csv'):
                df = pd.read_csv(ids_label_pairs_filename, header=0 if header.get() == 'Yes' else None)
            elif ids_label_pairs_filename.endswith('.xlsx'):
                df = pd.read_excel(ids_label_pairs_filename, header=0 if header.get() == 'Yes' else None)
            elif ids_label_pairs_filename.endswith('.xls'):
                df = pd.read_excel(ids_label_pairs_filename, header=0 if header.get() == 'Yes' else None, engine='xlrd')
            else:
                CTkMessagebox(title='Unsupported File Format',
                              message='Please select a supported file format.'
                                      '\nSupported formats: .csv, .xlsx, .xls',
                              icon='cancel')

            if 'Unnamed: 0' in df.columns:
                del df['Unnamed: 0']

            self.id_label_pairs = dict(zip(df.iloc[:, 0], df.iloc[:, 1]))

            non_empty_keys = [key for key in self.id_label_pairs.keys() if str(key).strip() != '']
            non_empty_values = [value for value in self.id_label_pairs.values() if str(value).strip() != '']
            if len(non_empty_keys) != len(self.id_label_pairs.keys()):
                CTkMessagebox(title='Empty IDs Detected',
                              message='Key contains empty IDs.\n'
                                      'Please ensure all IDs are properly filled in and try again.',
                              icon='cancel')
            if len(non_empty_values) != len(self.id_label_pairs.values()):
                CTkMessagebox(title='Empty Labels Detected',
                              message='Key contains empty labels.\n'
                                      'Please ensure all labels are properly filled in and try again.',
                              icon='cancel')
            if len(non_empty_keys) != len(non_empty_values):
                CTkMessagebox(title='Inconsistent Data',
                              message='The number of IDs does not match the number of labels.\n'
                                      'Please ensure the data is correctly structured and try again.',
                              icon='cancel')

            if self.id_label_pairs:
                self.len_pairs.set(str(len(self.id_label_pairs)))
                self.rename_datasets_button.configure(state='normal')
                self.rename_files_button.configure(state='normal')

    def rename_datasets(self):
        sheet = self.sheet_entry.get()
        column = self.column_entry.get()
        if not (sheet.isdigit() or column.isdigit()):
            CTkMessagebox(title='Dataset Localization Error',
                          message='Please enter a positive integer for sheet and column numbers.',
                          icon='cancel')
        else:
            dataset_filename = filedialog.askopenfilename(
                initialdir=home_directory,
                title='Select File',
                filetypes=(('Supported Files: .xlsx', '*.xlsx'), ('All files', '*.*')))
            if not dataset_filename.endswith('.xlsx'):
                CTkMessagebox(title='Unsupported File Format',
                              message='Please select a supported file format.'
                                      '\nSupported formats: .xlsx',
                              icon='cancel')
            else:
                if self.unblind_switch_var.get() == 'unblind':
                    pairs = {value: key for key, value in self.id_label_pairs.items()}
                else:
                    pairs = self.id_label_pairs

                header_id_label_message = CTkMessagebox(title='Header Question',
                                                        message='Does the file have an header?',
                                                        icon='question', option_1='Yes', option_2='No')
                if header_id_label_message.get() == 'Yes':
                    header = 0
                else:
                    header = None
                if sheet == '' or sheet == '0':
                    sheet = 1
                else:
                    sheet = int(sheet) - 1
                if column == '' or column == '0':
                    column = 1
                else:
                    column = int(column) - 1

                dataset_name = dataset_filename.split("\\")[-1]
                excel_file = pd.ExcelFile(dataset_filename)
                sheet_names = excel_file.sheet_names
                desired_sheet_name = sheet_names[int(self.sheet_entry.get()) - 1]
                df = pd.read_excel(dataset_filename, sheet_name=desired_sheet_name, header=header)
                for index, row in df.iterrows():
                    cell_value = row[column]
                    cell_value_str = str(cell_value)
                    if cell_value_str in pairs:
                        new_value = pairs[cell_value_str]
                        df.iloc[index, column] = new_value

                rows_shuffled = [row.tolist() for _, row in df.iterrows()]
                random.shuffle(rows_shuffled)  # Shuffle the rows in the original df
                shuffled_df = pd.DataFrame(rows_shuffled, columns=df.columns)  # Create a new DataFrame

                new_file = CTkMessagebox(title='New File Question',
                                         message=f'Would you like to overwrite the existing file "{dataset_filename}" '
                                                 f'or create a new one?',
                                         icon='question', option_1='Overwrite', option_2='Create File',
                                         option_focus=2)

                if new_file.get() == 'Overwrite':
                    shuffled_df.to_excel(dataset_filename, sheet_name=desired_sheet_name, index=False)
                    CTkMessagebox(title='Success',
                                  message=f'{dataset_filename} was successfully renamed.',
                                  icon='check')
                else:
                    new_dataset_filename = filedialog.asksaveasfilename(
                        initialdir=home_directory,
                        title='Save As',
                        filetypes=(('Supported Files: xlsx', '*.xlsx'), ('All files', '*.*')))
                    new_dataset_filename += '.xlsx'
                    shuffled_df.to_excel(new_dataset_filename, sheet_name=desired_sheet_name, index=False)
                    CTkMessagebox(title='Success',
                                  message=f'{new_dataset_filename} was successfully renamed.',
                                  icon='check')

    def rename_files(self):
        folder_to_rename = filedialog.askdirectory(initialdir=home_directory, title="Select Folder")
        if not folder_to_rename:
            CTkMessagebox(title='Folder Selection Error',
                          message='Please select a folder.',
                          icon='cancel')
        else:
            file_counter = 0
            if self.unblind_switch_var.get() == 'unblind':
                pairs = {value: key for key, value in self.id_label_pairs.items()}
            else:
                pairs = self.id_label_pairs

            for file_name in os.listdir(folder_to_rename):
                file_path = os.path.join(folder_to_rename, file_name)
                if os.path.isfile(file_path):
                    file_name_without_extension, file_extension = os.path.splitext(file_name)
                    file_id = pairs.get(file_name_without_extension)
                    if file_id is not None:
                        new_file_name = f"{file_id}{file_extension}"
                        new_file_path = os.path.join(folder_to_rename, new_file_name)
                        os.rename(file_path, new_file_path)
                        file_counter += 1

            if file_counter == len(self.id_label_pairs.keys()):
                CTkMessagebox(title='Success',
                              message=f'{file_counter} files were successfully renamed'
                                      f'in the folder {folder_to_rename}',
                              icon='check')
            else:
                if file_counter == 0:
                    CTkMessagebox(title='Renaming Files Error',
                                  message=f'{file_counter} files were renamed',
                                  icon='cancel')
                else:
                    CTkMessagebox(title='Renaming Files Error',
                                  message=f'Only {file_counter} files were renamed, '
                                          f'out of {len(self.id_label_pairs.keys())} keys',
                                  icon='warning')


if __name__ == "__main__":
    window = ctk.CTk()
    inBlindSight = InBlindSight(window)
    window.mainloop()
