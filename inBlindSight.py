import os
import random
import sys
import webbrowser
from datetime import datetime
import csv

import customtkinter as ctk
from customtkinter import filedialog
from CTkMessagebox import CTkMessagebox
import pandas as pd
from PIL import Image

# Directories
HOME_DIRECTORY = os.path.expanduser('~')
SCRIPT_DIRECTORY = os.path.dirname(sys.argv[0])

filenameS = ['logo.ico', 'logo.png', 'import.png', 'help.png', 'feedback.png', 'patch_notes.png', 'reset.png']
file_paths = {}
for file in filenameS:
    file_paths[file] = os.path.join(SCRIPT_DIRECTORY, 'resources', file).replace('\\', '\\\\')

# Bootstrap Basic
WHITE = '#ffffff'
LIGHT = '#e7efec'
GREY = '#D9D9D9'
DARK_GREY = '#808080'
DARK = '#212d30'

PRIMARY = '#1b4565'
SECONDARY = '#7da7c0'
TERTIARY = '#ebcd48'

INFO = '#554bd2'
SUCCESS = '#0db966'
WARNING = '#ebd00b'
DANGER = '#fe0406'

# Fonts
LV1_FONT = ('Josefin Sans Medium', 22)
LV2_FONT = ('Josefin Sans SemiBold', 32)
LV3_FONT = ('Josefin Sans Light', 20)
LV4_FONT = ('Josefin Sans Medium', 20)
LV5_FONT = ('Josefin Sans Light', 16)

COLORS_LIST = [
    'brunswick green', 'fluorescent cyan', 'umber', 'pine green', 'caput mortuum', 'platinum', 'peach', 'red brown',
    'wine', 'tang blue', 'lime', 'antique white', 'tea green', 'chili red', 'coyote', 'parchment', 'turquoise',
    'verdigris', 'dark spring green', 'ruddy blue', 'carnation pink', 'tomato', 'ucla blue', 'hot pink',
    'dark green', 'tangelo', 'carolina blue', 'beige', 'bistre', 'pale azure', 'medium slate blue', 'tyrian purple',
    'amaranth pink', 'taupe gray', 'coffee', 'lavender blush', 'resolution blue', 'byzantine blue', 'magnolia',
    'oxford blue', 'cosmic latte', 'cream', 'lavender pink', 'air superiority blue', 'cal poly green', 'mint',
    'cool gray', 'camel', 'liver', 'maize', 'snow', 'rosy brown', 'lawn green', 'raspberry', 'folly', 'citron',
    'orange peel', 'anti-flash white', 'tawny', 'rust', 'china rose', 'aqua', 'giants orange', 'yinmn blue',
    'blood red', 'khaki', 'vista blue', 'golden gate bridge', 'rojo', 'arylide yellow', 'ebony', 'bittersweet',
    'madder', 'cyan', 'slate gray', 'lemon chiffon', 'shamrock green', 'ut orange', 'denim', 'gray', 'poppy',
    'air force blue', 'powder blue', 'uranian blue', 'french violet', 'salmon pink', 'turkey red', 'rose quartz',
    'desert sand', 'rebecca purple', 'international klein blue', 'aureolin', 'grape', 'midnight green', 'brandeis blue',
    'wheat', 'pearl', 'sage', 'safety orange', 'office green', 'rosewood', "hooker's green", 'light blue', 'scarlet',
    'black', 'light yellow', 'reseda green', 'magenta', 'tufts blue', 'smoky black', 'finn', 'green',
    'hollywood cerise', "payne's gray", 'malachite', 'lapis lazuli', 'azul', 'tropical indigo', 'alice blue',
    'eminence', 'tiffany blue', 'zaffre', 'violet blue', "screamin'green", 'rose pink', 'off red', 'celestial blue',
    'tan', 'pakistan green', 'amaranth', 'dogwood rose', 'bittersweet shimmer', 'wenge', 'pomp and power',
    'argentinian blue', 'flame', 'maya blue', 'fire engine red', 'mikado yellow', 'quinacridone magenta', 'blue violet',
    'mauve', 'telemagenta', 'royal purple', 'rose pompadour', 'eggshell', 'aerospace orange', 'white smoke',
    'fuchsia rose', 'vanilla', 'coral', 'ivory', 'citrine', 'tangerine', 'eerie black', 'jet', 'navajo white',
    'majorelle blue', 'british racing green', 'azure', 'iris', 'navy blue', 'indigo dye', 'celtic blue',
    'shocking pink', 'red', 'rose red', 'yellow green', 'amethyst', 'pigment green', 'dark violet', 'gunmetal', 'puce',
    'ecru', 'cornell red', 'russet', 'school bus yellow', 'steel blue', 'white', 'silver', 'fulvous', 'mantis',
    'chocolate cosmos', 'dark moss green', 'buff', 'pink lavender', 'tea rose', 'champagne pink', 'sgbus green',
    'rufous', 'black olive', 'heliotrope', 'cherry blossom pink', 'claret', 'dark pastel green', 'candy apple red',
    'brown', 'seashell', 'outer space', 'electric indigo', 'harvest gold', 'burnt umber', 'federal blue',
    'silver lake blue', 'canary', 'imperial red', 'dark cyan', 'ghost white', 'teal', 'mimi pink', 'byzantium',
    'ash gray', 'cinnabar', 'moss green', 'crimson', 'non photo blue', 'hunter green', 'process cyan', 'mulberry',
    'bleu de france', 'japanese violet', 'misty rose', 'pink', 'dartmouth green', 'steel pink', 'purpureus',
    'bice blue', 'dark slate gray', 'viridian', 'aquamarine', 'rose bonbon', 'café noir', 'mahogany', 'celeste',
    'rose ebony', 'neon green', 'tiger’s eye', 'columbia blue', 'walnut brown', 'xanthous', 'charcoal', 'falu red',
    'duke blue', 'penn blue', 'ultra violet', 'black bean', 'onyx', 'persian red', 'beaver', 'lime green', 'jasmine',
    'murrey', 'india green', 'nyanza', 'hunyadi yellow', 'apricot', 'mint cream', 'polynesian blue', 'light red',
    'french blue', 'jade', 'indian red', 'butterscotch', 'persian pink', 'ice blue', 'dark purple', 'salmon',
    'penn red', 'cornsilk', 'champagne', 'palatinate blue', 'fire brick', 'sky blue', 'red violet', 'tekhelet',
    'mauveine', 'taupe', 'zomp', 'pacific cyan', 'persimmon', 'electric violet', 'spring green', 'lemon lime',
    'persian orange', 'gold', 'bronze', 'olivine', 'skobeloff', 'jordy blue', 'baby powder', 'seasalt', "davy's gray",
    'fairy tale', 'keppel', 'bone', 'violet', 'isabelline', 'chocolate', 'alabaster', 'cocoa brown', 'garnet', 'almond',
    'russian violet', 'persian green', 'floral white', 'dark goldenrod', 'cyclamen', 'satin sheen gold', 'plum',
    'prussian blue', 'periwinkle', 'ou crimson', 'united nations blue', 'saffron', 'selective yellow', 'bondi blue',
    'coral pink', 'field drab', 'feldgrau', 'rich black', 'picton blue', 'magenta dye', 'persian blue', 'glaucous',
    'golden brown', 'savoy blue', 'van dyke', 'light coral', 'jungle green', 'spring bud', 'pear', 'purple pizzazz',
    'baby blue', 'lilac', 'alloy orange', 'baker-miller pink', 'indigo', 'slate blue', 'sinopia', 'robin egg blue',
    'deep pink', 'true blue', 'light cyan', 'midnight blue', 'sky magenta', 'orchid pink', 'light sea green', 'orchid',
    'bright green', 'light sky blue', 'carmine', 'pistachio', 'old gold', 'orange', 'maroon', 'dark red', 'cordovan',
    'french rose', 'spanish orange', 'fern green', 'old rose', 'yellow', 'phlox', 'ochre', 'risd blue',
    'english violet', 'fawn', 'fuchsia', 'brown sugar', 'royal blue', 'chefchaouen blue', 'medium blue',
    'tickle me pink', 'pale dogwood', 'redwood', 'capri', 'timberwolf', 'cerulean', 'honeydew', 'sienna', 'licorice',
    'mexican pink', 'cobalt blue', 'dodger blue', 'atomic tangerine', 'electric purple', 'light green', 'dim gray',
    'berkeley blue', 'purple', 'hot magenta', 'neon blue', 'chartreuse', 'chamoisee', 'earth yellow', 'fandango',
    'ultramarine', 'light orange', 'cinereous', 'sandy brown', 'burgundy', 'raisin black', 'avocado', 'magenta haze',
    'chinese violet', 'celadon', 'bright pink', 'mustard', 'blue green', 'cantaloupe melon', 'caramel', 'green blue',
    'electric blue', 'carrot orange', 'rusty red', 'drab dark brown', 'bole', 'african violet', 'princeton orange',
    'sunset', 'goldenrod', 'syracuse red orange', 'mindaro', 'marian blue', 'lavender', 'jonquil', 'erin',
    'peach yellow', 'harlequin', 'amber', 'jasper', 'rose', 'moonstone', 'vermilion', 'rose taupe', 'apple green',
    'cardinal', 'chestnut', 'pumpkin', 'flax', 'blue', 'razzle dazzle rose', 'veronica', 'wisteria', 'sepia',
    'asparagus', 'emerald', 'pale purple', 'kelly green', 'castleton green', 'burnt orange', 'dark magenta',
    'blue gray', 'papaya whip', 'aero', 'persian rose', 'delft blue', 'battleship gray', 'french mauve', 'green yellow',
    'thistle', 'copper', 'phthalo blue', 'palatinate', 'raspberry rose', 'forest green', 'mardi gras', 'gamboge',
    'french gray', 'raw umber', 'vivid sky blue', 'engineering orange', 'night', 'icterine', 'myrtle green', 'straw',
    'barn red', 'space cadet', 'cadet gray', 'sapphire', 'cambridge blue', 'dark orange', 'cornflower blue',
    'seal brown', 'thulian pink', 'old lace', 'kobicha', 'caribbean current', 'olive', 'sunglow', 'coquelicot',
    'amaranth purple', 'naples yellow', 'persian indigo', 'eggplant', 'mint green', 'burnt sienna', 'mountbatten pink',
    'chrysler blue', 'dutch white', 'sea green', 'dun', 'razzmatazz', 'linen', 'cerise', 'egyptian blue', 'yale blue',
    'blush', 'honolulu blue']
ANIMALS_LIST = ['aardvark', 'aardwolf', 'abyssinian', 'addax', 'affenpinscher', 'agouti', 'aidi', 'ainu',
                'airedoodle', 'akbash', 'akita', 'albatross', 'albertonectes', 'allosaurus', 'alpaca', 'alusky',
                'amargasaurus', 'amberjack', 'anaconda', 'anchovies', 'andrewsarchus', 'angelfish', 'angelshark',
                'anglerfish', 'anhinga', 'anomalocaris', 'ant', 'anteater', 'antelope', 'anteosaurus', 'ape',
                'arambourgiania', 'arapaima', 'archaeoindris', 'archaeopteryx', 'archaeotherium', 'archerfish',
                'arctodus', 'arctotherium', 'argentinosaurus', 'armadillo', 'armyworm', 'arsinoitherium',
                'arthropleura', 'asp', 'aurochs', 'aussiedoodle', 'aussiedor', 'aussiepom', 'australopithecus',
                'avocet', 'axolotl', 'aye-aye', 'azawakh', 'babirusa', 'baboon', 'badger', 'baiji', 'balinese',
                'bandicoot', 'barb', 'barbet', 'barinasuchus', 'barnacle', 'barnevelder', 'barosaurus', 'barracuda',
                'barylambda', 'basilosaurus', 'bass', 'bassador', 'bassetoodle', 'bat', 'batfish', 'baya', 'bea-tzu',
                'beabull', 'beagador', 'beagle', 'beaglier', 'beago', 'bear', 'beaski', 'beauceron', 'beaver', 'bee',
                'bee-eater', 'beefalo', 'beetle', 'bergamasco', 'bernedoodle', 'bichir', 'bichpoo', 'bilby',
                'binturong', 'bird', 'birman', 'bison', 'blobfish', 'bloodhound', 'blowfly', 'bluefish', 'bluegill',
                'boas', 'bobcat', 'bobolink', 'boerboel', 'boggle', 'boiga', 'bombay', 'bonefish', 'bongo', 'bonobo',
                'booby', 'boomslang', 'borador', 'bordoodle', 'borkie', 'boskimo', 'bowfin', 'boxachi', 'boxador',
                'boxerdoodle', 'boxfish', 'boxsky', 'boxweiler', 'brachiosaurus', 'briard', 'brittany', 'brontosaurus',
                'brug', 'budgerigar', 'buffalo', 'bullboxer', 'bulldog', 'bullfrog', 'bullmastiff', 'bullsnake',
                'bumblebee', 'burmese', 'butterfly', 'caecilian', 'caiman', 'camel', 'cantil', 'canvasback', 'capuchin',
                'capybara', 'caracal', 'cardinal', 'caribou', 'carp', 'cascabel', 'cassowary', 'cat', 'caterpillar',
                'catfish', 'cavador', 'cavapoo', 'centipede', 'cephalaspis', 'ceratopsian', 'ceratosaurus', 'chameleon',
                'chamois', 'chartreux', 'cheagle', 'cheetah', 'chickadee', 'chicken', 'chigger', 'chihuahua',
                'chilesaurus', 'chimaera', 'chimpanzee', 'chinchilla', 'chinook', 'chipit', 'chipmunk', 'chipoo',
                'chiton', 'chiweenie', 'chorkie', 'chusky', 'cicada', 'cichlid', 'clownfish', 'coati', 'cobras',
                'cockalier', 'cockapoo', 'cockatiel', 'cockatoo', 'cockle', 'cockroach', 'codfish', 'coelacanth',
                'collie', 'compsognathus', 'conure', 'copperhead', 'coral', 'corella', 'corgidor', 'corgipoo', 'corkie',
                'cormorant', 'coryphodon', 'cottonmouth', 'cougar', 'cow', 'coyote', 'crab', 'crane', 'crayfish',
                'cricket', 'crocodile', 'crocodylomorph', 'crow', 'cryolophosaurus', 'cuckoo', 'cuttlefish',
                'dachsador', 'dachshund', 'daeodon', 'dalmadoodle', 'dalmador', 'dalmatian', 'damselfish', 'daniff',
                'danios', 'daug', 'deer', 'deinocheirus', 'deinosuchus', 'desmostylus', 'dhole', 'dickcissel',
                'dickinsonia', 'dik-dik', 'dilophosaurus', 'dimetrodon', 'dingo', 'dinocrocuta', 'dinofelis',
                'dinopithecus', 'dinosaurs', 'diplodocus', 'diprotodon', 'discus', 'dobsonfly', 'dodo', 'doedicurus',
                'dog', 'dolphin', 'donkey', 'dorgi', 'dorkie', 'dormouse', 'douc', 'doxiepoo', 'doxle', 'dragonfish',
                'dragonfly', 'dreadnoughtus', 'drever', 'duck', 'dugong', 'dunker', 'dunkleosteus', 'dunnock', 'eagle',
                'earthworm', 'earwig', 'echidna', 'eel', 'eelpout', 'egret', 'eider', 'eland', 'elasmosaurus',
                'elasmotherium', 'elephant', 'elk', 'embolotherium', 'emu', 'epidexipteryx', 'ermine', 'eryops',
                'escolar', 'eskipoo', 'euoplocephalus', 'eurasier', 'eurypterus', 'fairy-wren', 'falcon', 'fangtooth',
                'feist', 'ferret', 'finch', 'firefly', 'fish', 'fisher', 'flamingo', 'flea', 'flounder', 'fly',
                'flycatcher', 'fossa', 'fox', 'frenchton', 'frengle', 'frigatebird', 'frog', 'frogfish', 'frug',
                'gadwall', 'gar', 'gastornis', 'gazelle', 'gecko', 'genet', 'gerbil', 'gharial', 'gibbon',
                'gigantopithecus', 'giraffe', 'glechon', 'glowworm', 'gnat', 'goat', 'goberian', 'goldador',
                'goldcrest', 'goldendoodle', 'goldfish', 'gollie', 'gomphotherium', 'goose', 'gopher', 'goral',
                'gorgosaurus', 'gorilla', 'goshawk', 'gourami', 'grasshopper', 'grebe', 'greyhound', 'griffonshire',
                'groenendael', 'grouper', 'grouse', 'grunion', 'guppy', 'haddock', 'hagfish', 'haikouichthys',
                'hainosaurus', 'halibut', 'hallucigenia', 'hamster', 'hare', 'harrier', 'hartebeest', 'hatzegopteryx',
                'havamalt', 'havanese', 'havapoo', 'havashire', 'havashu', 'hawk', 'hedgehog', 'helicoprion',
                'hellbender', 'heron', 'herrerasaurus', 'herring', 'himalayan', 'hippopotamus', 'hogfish', 'hokkaido',
                'hoopoe', 'horgi', 'hornbill', 'hornet', 'horse', 'horsefly', 'housefly', 'hovasaurus', 'hovawart',
                'human', 'hummingbird', 'huntaway', 'huskador', 'huskita', 'husky', 'huskydoodle', 'hyaenodon', 'hyena',
                'ibex', 'ibis', 'icadyptes', 'ichthyosaurus', 'ichthyostega', 'iguana', 'iguanodon', 'impala',
                'inchworm', 'indri', 'insect', 'insects', 'jabiru', 'jacana', 'jack-chi', 'jackabee', 'jackal',
                'jackdaw', 'jackrabbit', 'jagdterrier', 'jaguar', 'javanese', 'jellyfish', 'jerboa', 'junglefowl',
                'kagu', 'kakapo', 'kangaroo', 'katydid', 'kea', 'keagle', 'keelback', 'keeshond', 'kestrel', 'kiang',
                'killdeer', 'killifish', 'kingfisher', 'kingklip', 'kinkajou', 'kishu', 'kiwi', 'klipspringer',
                'knifefish', 'koala', 'kodkod', 'komondor', 'kooikerhondje', 'koolie', 'kouprey', 'kowari', 'krait',
                'krill', 'kudu', 'kuvasz', 'labahoula', 'labmaraner', 'labrabull', 'labradane', 'labradoodle',
                'labraheeler', 'labrottie', 'ladybug', 'ladyfish', 'lamprey', 'lancetfish', 'leech', 'leedsichthys',
                'lemming', 'lemur', 'leonberger', 'leopard', 'leptocephalus', 'lhasapoo', 'liger', 'limpet', 'linnet',
                'lion', 'lionfish', 'liopleurodon', 'livyatan', 'lizard', 'lizardfish', 'llama', 'loach', 'lobster',
                'locust', 'lorikeet', 'loris', 'lowchen', 'lumpfish', 'lungfish', 'lurcher', 'lynx', 'lyrebird',
                'lystrosaurus', 'macaque', 'macaw', 'machaeroides', 'macrauchenia', 'maggot', 'magpie', 'magyarosaurus',
                'maiasaura', 'malchi', 'mallard', 'malteagle', 'maltese', 'maltipom', 'maltipoo', 'mamba', 'manatee',
                'mandrill', 'margay', 'markhor', 'marmoset', 'marmot', 'masiakasaurus', 'massasauga', 'mastador',
                'mastiff', 'mauzer', 'mayfly', 'meagle', 'mealybug', 'meerkat', 'megalania', 'megalochelys',
                'megalodon', 'meganeura', 'megatherium', 'meiolania', 'merganser', 'microraptor', 'miki', 'milkfish',
                'millipede', 'mink', 'mockingbird', 'mojarra', 'mole', 'mollusk', 'molly', 'mongoose', 'mongrel',
                'monkey', 'monkfish', 'moorhen', 'moose', 'morkie', 'mosasaurus', 'mosquito', 'moth', 'mouse', 'mudi',
                'mudpuppy', 'mudskipper', 'mule', 'muntjac', 'muskox', 'muskrat', 'muttaburrasaurus', 'nabarlek',
                'naegleria', 'narwhal', 'natterjack', 'nautilus', 'neanderthal', 'nebelung', 'needlefish', 'nematode',
                'newfoundland', 'newfypoo', 'newt', 'nightingale', 'nightjar', 'nilgai', 'norrbottenspets',
                'nudibranch', 'numbat', 'nuralagus', 'nuthatch', 'nutria', 'nyala', 'oarfish', 'ocelot', 'octopus',
                'oilfish', 'okapi', 'olingo', 'olm', 'onager', 'opabinia', 'opah', 'opossum', 'orangutan', 'ori-pei',
                'oribi', 'ornithocheirus', 'ornithomimus', 'osprey', 'ostracod', 'ostrich', 'otter', 'otterhound',
                'ovenbird', 'oviraptor', 'owl', 'ox', 'oxpecker', 'oyster', 'pachycephalosaurus', 'paddlefish',
                'pademelon', 'palaeophis', 'paleoparadoxia', 'pangolin', 'panther', 'papillon', 'parakeet',
                'parasaurolophus', 'parrot', 'parrotfish', 'parrotlet', 'partridge', 'patagotitan', 'peacock', 'peagle',
                'peekapoo', 'pekingese', 'pelagornis', 'pelagornithidae', 'pelican', 'pelycosaurs', 'penguin',
                'persian', 'pheasant', 'phorusrhacos', 'phytosaurs', 'pig', 'pigeon', 'pika', 'pinfish', 'pipefish',
                'piranha', 'pitador', 'pitsky', 'platybelodon', 'platypus', 'plesiosaur', 'pliosaur', 'pointer',
                'polacanthus', 'polecat', 'pomapoo', 'pomchi', 'pomeagle', 'pomeranian', 'pomsky', 'poochon', 'poodle',
                'poogle', 'porcupine', 'porcupinefish', 'possum', 'potoo', 'potoroo', 'prawn', 'procoptodon',
                'pronghorn', 'psittacosaurus', 'pteranodon', 'pterodactyl', 'pudelpointer', 'puertasaurus',
                'pufferfish', 'puffin', 'pug', 'pugapoo', 'puggle', 'pugshire', 'puli', 'puma', 'pumi', 'purussaurus',
                'pyrador', 'pyredoodle', 'pyrosome', 'python', 'quagga', 'quail', 'quetzal', 'quokka', 'quoll',
                'rabbit', 'raccoon', 'ragamuffin', 'ragdoll', 'raggle', 'rat', 'rattlesnake', 'redstart', 'reindeer',
                'repenomamus', 'rhamphosuchus', 'rhea', 'rhinoceros', 'roadrunner', 'robin', 'rockfish', 'rodents',
                'rooster', 'rotterman', 'rottle', 'rottsky', 'rottweiler', 'sable', 'saiga', 'sailfish', 'salamander',
                'salmon', 'saluki', 'sambar', 'samoyed', 'sandpiper', 'sandworm', 'saola', 'sapsali', 'sarcosuchus',
                'sardines', 'sarkastodon', 'sarplaninac', 'sauropoda', 'sawfish', 'scallops', 'schapendoes',
                'schipperke', 'schneagle', 'schnoodle', 'scorpion', 'sculpin', 'scutosaurus', 'seagull', 'seahorse',
                'seal', 'serval', 'seymouria', 'shantungosaurus', 'shark', 'shastasaurus', 'sheep', 'sheepadoodle',
                'shepadoodle', 'shepkita', 'shepweiler', 'shichi', 'shikoku', 'shiranian', 'shollie', 'shrew', 'shrimp',
                'siamese', 'siberian', 'siberpoo', 'sidewinder', 'simbakubwa', 'sinosauropteryx', 'sivatherium', 'skua',
                'skunk', 'sloth', 'slug', 'smilosuchus', 'snail', 'snailfish', 'snake', 'snorkie', 'snowshoe', 'somali',
                'spalax', 'spanador', 'sparrow', 'sparrowhawk', 'sphynx', 'spider', 'spinosaurus', 'sponge',
                'springador', 'springbok', 'springerdoodle', 'squid', 'squirrel', 'squirrelfish', 'stabyhoun',
                'starfish', 'stingray', 'stoat', 'stonechat', 'stonefish', 'stork', 'stromatolite', 'stupendemys',
                'sturgeon', 'styracosaurus', 'suchomimus', 'suckerfish', 'supersaurus', 'superworm', 'surgeonfish',
                'swallow', 'swan', 'swordfish', 'taipan', 'takin', 'tamarin', 'tamaskan', 'tang', 'tapir', 'tarantula',
                'tarbosaurus', 'tarpon', 'tarsier', 'tenrec', 'termite', 'terrier', 'tetra', 'thalassomedon',
                'thanatosdrakon', 'therizinosaurus', 'theropod', 'thrush', 'thylacoleo', 'thylacosmilus', 'tick',
                'tiffany', 'tiger', 'tiktaalik', 'titanoboa', 'titanosaur', 'toadfish', 'torkie', 'tornjak', 'tortoise',
                'tosa', 'toucan', 'towhee', 'toxodon', 'treecreeper', 'treehopper', 'triggerfish', 'troodon',
                'tropicbird', 'trout', 'tuatara', 'tuna', 'turaco', 'turkey', 'turnspit', 'turtles', 'tusoteuthis',
                'tylosaurus', 'uakari', 'uguisu', 'uintatherium', 'umbrellabird', 'urial', 'utonagan', 'vaquita',
                'veery', 'vegavis', 'velociraptor', 'vicuña', 'vinegaroon', 'viper', 'viperfish', 'vizsla', 'vole',
                'vulture', 'waimanu', 'wallaby', 'walrus', 'warbler', 'warthog', 'wasp', 'waterbuck', 'weasel',
                'weimaraner', 'weimardoodle', 'westiepoo', 'whimbrel', 'whinchat', 'whippet', 'whiting', 'whoodle',
                'wildebeest', 'wiwaxia', 'wolf', 'wolffish', 'wolverine', 'wombat', 'woodlouse', 'woodpecker',
                'woodrat', 'worm', 'wrasse', 'wryneck', 'xenacanthus', 'xenoceratops', 'xenoposeidon',
                'xenotarsosaurus', 'xerus', 'xiaosaurus', 'xiaotingia', 'xiongguanlong', 'xiphactinus',
                'xoloitzcuintli', 'yabby', 'yak', 'yarara', 'yellowhammer', 'yellowthroat', 'yoranian', 'yorkiepoo',
                'zebra', 'zebu', 'zokor', 'zonkey', 'zorse', 'zuchon']
COUNTRIES_LIST = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina',
                  'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados',
                  'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana',
                  'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada',
                  'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros',
                  'Democratic Republic of the Congo', 'Republic of the Congo', 'Costa Rica', "Côte d'Ivoire", 'Croatia',
                  'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor',
                  'Ecuador', 'Egypt', 'El Salvador', 'England', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini',
                  'Ethiopia', 'Federated States of Micronesia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia',
                  'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana',
                  'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel',
                  'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait',
                  'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
                  'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
                  'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia',
                  'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
                  'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'Macedonia', 'Northern Ireland',
                  'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru',
                  'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis',
                  'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'São Tome and Principe',
                  'Saudi Arabia', 'Scotland', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore',
                  'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan',
                  'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan',
                  'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
                  'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay',
                  'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Wales', 'Yemen', 'Zambia',
                  'Zimbabwe']


class InBlindSight:
    def __init__(self, root):
        self.ids_list = []
        self.labels_list = ANIMALS_LIST
        self.user_labels_list = []
        self.id_label_pairs = {}

        self.len_ids_list = ctk.StringVar(value=f'{len(self.ids_list)}')
        self.len_labels_list = ctk.StringVar(value=f'{len(self.labels_list)}')
        self.len_id_label_pairs = ctk.StringVar(value=f'{len(self.id_label_pairs)}')

        self.inputted_ids_entry = ctk.CTkEntry(None)
        self.sheet_entry_id = ctk.CTkEntry(None)
        self.column_entry_id = ctk.CTkEntry(None)
        self.inputted_labels_entry = ctk.CTkEntry(None)
        self.sheet_entry_label = ctk.CTkEntry(None)
        self.column_entry_label = ctk.CTkEntry(None)
        self.sheet_entry_file = ctk.CTkEntry(None)
        self.column_entry_file = ctk.CTkEntry(None)

        self.randomize_button = ctk.CTkButton(None)
        self.rename_datasets_button = ctk.CTkButton(None)
        self.rename_files_button = ctk.CTkButton(None)

        self.default_labels_switch_var = ctk.StringVar(value='Default')
        self.radio_var = ctk.StringVar(value='Animals')
        self.un_blind_button_var = ctk.StringVar(value='Blind')

        self.logo_img = ctk.CTkImage(light_image=Image.open(file_paths['logo.png']), size=(256, 132))
        self.help_img = ctk.CTkImage(light_image=Image.open(file_paths['help.png']), size=(30, 30))
        self.feedback_img = ctk.CTkImage(light_image=Image.open(file_paths['feedback.png']), size=(30, 30))
        self.patch_img = ctk.CTkImage(light_image=Image.open(file_paths['patch_notes.png']), size=(30, 30))
        self.reset_img = ctk.CTkImage(light_image=Image.open(file_paths['reset.png']), size=(16, 16))

        self.animals_example1 = ctk.CTkLabel(None)
        self.animals_example2 = ctk.CTkLabel(None)
        self.animals_example3 = ctk.CTkLabel(None)
        self.animals_example4 = ctk.CTkLabel(None)
        self.colors_example1 = ctk.CTkLabel(None)
        self.colors_example2 = ctk.CTkLabel(None)
        self.colors_example3 = ctk.CTkLabel(None)
        self.colors_example4 = ctk.CTkLabel(None)
        self.countries_example1 = ctk.CTkLabel(None)
        self.countries_example2 = ctk.CTkLabel(None)
        self.countries_example3 = ctk.CTkLabel(None)
        self.countries_example4 = ctk.CTkLabel(None)

        self.root = root
        self.root.title('inBlindSight')
        self.root.iconbitmap(file_paths['logo.ico'])
        self.root.resizable(False, False)

        self.page1 = ctk.CTkFrame(root, fg_color=GREY, corner_radius=1)
        self.page2 = ctk.CTkFrame(root, fg_color=LIGHT, corner_radius=1)
        self.page3 = ctk.CTkFrame(root, fg_color=LIGHT, corner_radius=1)

        self.create_page1()
        self.create_page2()
        self.create_page3()

        self.show_page(self.page1)

        def switch_callback(*args):
            if self.default_labels_switch_var.get() == 'Custom':
                self.labels_list = self.user_labels_list
                self.len_labels_list.set(str(len(self.user_labels_list)))
            else:
                self.labels_list = COLORS_LIST
                self.len_labels_list.set(str(len(COLORS_LIST)))
        self.default_labels_switch_var.trace_add('write', switch_callback)

    def create_page1(self):
        for r in range(0, 5):
            self.page1.rowconfigure(r, minsize=140)
        for c in range(0, 10):
            self.page1.columnconfigure(c, weight=1)

        ctk.CTkLabel(self.page1, image=self.logo_img, text='').grid(
            row=0, column=0, columnspan=9, pady=(20, 0))
        ctk.CTkLabel(self.page1, text='Data Blinding Made\nEffortless and Seamless',
                     text_color=DARK, font=LV1_FONT).grid(
            row=1, column=0, columnspan=9, padx=10, pady=(0, 10))

        ctk.CTkButton(self.page1, command=self.show_page2,
                      corner_radius=25, height=50,
                      fg_color=PRIMARY, hover_color=SECONDARY, anchor='center',
                      text='Generate Key', text_color=LIGHT, font=LV3_FONT).grid(
            row=2, column=0, columnspan=9, padx=10, sticky='swe')

        ctk.CTkButton(self.page1, command=self.show_page3,
                      corner_radius=25, height=50,
                      fg_color=PRIMARY, hover_color=SECONDARY, anchor='center',
                      text='Rename Datasets or Files', text_color=LIGHT, font=LV3_FONT).grid(
            row=3, column=0, columnspan=9, padx=10, pady=(10, 10), sticky='nwe')

        ctk.CTkButton(self.page1, command=lambda: InBlindSight.open_github('instructions'),
                      fg_color='transparent', image=self.help_img,
                      text='', hover=False, corner_radius=1, width=1).grid(
            row=4, column=0, sticky='s', pady=10)
        ctk.CTkButton(self.page1, command=lambda: InBlindSight.open_github('feedback'),
                      fg_color='transparent', image=self.feedback_img,
                      text='', hover=False, corner_radius=1, width=1).grid(
            row=4, column=1, sticky='s', pady=10)
        ctk.CTkButton(self.page1, command=lambda: InBlindSight.open_github('release'),
                      fg_color='transparent', image=self.patch_img,
                      text='', hover=False, corner_radius=1, width=1).grid(
            row=4, column=2, sticky='s', pady=10)

    def create_page2(self):
        for r in range(0, 16):
            self.page2.rowconfigure(r, minsize=30)
        for c in range(0, 16):
            self.page2.columnconfigure(c, minsize=80)

        # Title
        ctk.CTkLabel(self.page2, text='Randomly Generate a Key', text_color=DARK, font=LV1_FONT).grid(
            row=0, column=0, rowspan=2, columnspan=16, sticky='nsew')

        # Number of IDs & Reset Button
        ctk.CTkLabel(self.page2, textvariable=self.len_ids_list,
                     text_color=DARK, font=LV2_FONT, anchor='w').grid(
            row=2, column=1, columnspan=7, sticky='e', padx=(0, 10))
        ctk.CTkLabel(self.page2, text='Identifiers',
                     text_color=DARK, font=LV3_FONT, anchor='sw').grid(
            row=2, column=8, columnspan=4, sticky='w', pady=(5, 0))
        id_reset = ctk.CTkButton(self.page2, corner_radius=15, fg_color=GREY, hover=False, width=0, height=20,
                                 command=lambda: self.reset_list('ID'), image=self.reset_img, text='')
        id_reset.grid(row=2, column=14)

        # Insert IDs Entry & Button
        self.inputted_ids_entry = ctk.CTkEntry(self.page2, placeholder_text='id1,id2,id3...',
                                               corner_radius=5, height=30)
        self.inputted_ids_entry.grid(row=3, column=1, rowspan=2, columnspan=9, sticky='ew', padx=10)
        ctk.CTkButton(self.page2, command=lambda: self.validate_input_data('IDs', 'Entry'),
                      corner_radius=15, height=40,
                      fg_color=TERTIARY, hover_color=TERTIARY, anchor='center',
                      text='Insert IDs', text_color=DARK, font=LV4_FONT).grid(
            row=3, column=10, rowspan=2, columnspan=5, sticky='ew', padx=10)

        # Import IDs Entry & Button
        self.sheet_entry_id = ctk.CTkEntry(self.page2, placeholder_text='Sheet name', height=30)
        self.sheet_entry_id.grid(row=5, column=1, rowspan=2, columnspan=5, sticky='ew', padx=10)
        self.column_entry_id = ctk.CTkEntry(self.page2, placeholder_text='Column index', height=30)
        self.column_entry_id.grid(row=5, column=6, rowspan=2, columnspan=4, padx=(0, 10), sticky='ew')
        ctk.CTkButton(self.page2, command=lambda: self.validate_input_data('IDs', 'File'),
                      corner_radius=15, height=40,
                      fg_color=TERTIARY, hover_color=TERTIARY, anchor='center',
                      text='Import IDs', text_color=DARK, font=LV4_FONT).grid(
            row=5, column=10, rowspan=2, columnspan=5, sticky='ew', padx=10)

        # Separator
        ctk.CTkFrame(self.page2, fg_color=DARK, height=2).grid(
            row=4, column=1, rowspan=2, columnspan=14, sticky='ew', padx=15, pady=30)
        ctk.CTkLabel(self.page2, text='OR', fg_color=LIGHT,
                     width=40, height=10, font=('Josefin Sans Bold', 12), text_color=DARK).grid(
            row=4, column=9, rowspan=2, columnspan=2, padx=15, pady=(28, 30))

        # Number of Labels & Reset Button
        len_labels_text = ctk.CTkLabel(self.page2, textvariable=self.len_labels_list,
                                       text_color=DARK, font=LV2_FONT, anchor='w')
        len_labels_text.grid(row=7, column=1, columnspan=7, sticky='e', padx=(0, 10))

        ctk.CTkLabel(self.page2, text='Labels',
                     text_color=DARK, font=LV3_FONT, anchor='sw').grid(
            row=7, column=8, columnspan=4, sticky='w', pady=(5, 0))
        label_reset = ctk.CTkButton(self.page2, corner_radius=15, fg_color=GREY, hover=False, width=0, height=20,
                                    command=lambda: self.reset_list('Label'), image=self.reset_img, text='')
        label_reset.grid(row=7, column=14)
        label_reset.configure(state='disabled')

        # Default/Custom Segmented Button
        default_labels_switch = ctk.CTkSegmentedButton(self.page2, values=['Default', 'Custom'],
                                                       command=None, variable=self.default_labels_switch_var,
                                                       corner_radius=15, height=40,
                                                       font=LV3_FONT, text_color=WHITE, border_width=0,
                                                       fg_color=SECONDARY, unselected_hover_color=PRIMARY,
                                                       unselected_color=SECONDARY, selected_color=PRIMARY)
        default_labels_switch.grid(row=8, column=1, rowspan=2, columnspan=14, sticky='ew', pady=(0, 10))

        # Default Section
        (ctk.CTkFrame(self.page2, fg_color=LIGHT, border_width=2, border_color=DARK_GREY)
         .grid(row=10, column=1, rowspan=3, columnspan=14, sticky='ew'))

        animals_button = ctk.CTkRadioButton(self.page2, variable=self.radio_var, value='Animals',
                                            text='Animals', text_color=DARK, font=LV4_FONT,
                                            command=lambda: self.selection_of_labels_themes('animals'),
                                            border_color=DARK_GREY, fg_color=PRIMARY)
        colors_button = ctk.CTkRadioButton(self.page2, variable=self.radio_var, value='Colors',
                                           text='Colors', text_color=DARK, font=LV4_FONT,
                                           command=lambda: self.selection_of_labels_themes('colors'),
                                           border_color=DARK_GREY, fg_color=PRIMARY)
        countries_button = ctk.CTkRadioButton(self.page2, variable=self.radio_var, value='Countries',
                                              text='Countries', text_color=DARK, font=LV4_FONT,
                                              command=lambda: self.selection_of_labels_themes('countries'),
                                              border_color=DARK_GREY, fg_color=PRIMARY)
        divider = ctk.CTkFrame(self.page2, height=65, width=2, fg_color=DARK_GREY)
        examples_frame = ctk.CTkFrame(self.page2, fg_color='transparent')

        animals_button.grid(row=10, column=0, columnspan=5, sticky='w', padx=100, pady=(10, 0))
        colors_button.grid(row=11, column=0, columnspan=5, sticky='w', padx=100)
        countries_button.grid(row=12, column=0, columnspan=5, sticky='w', padx=100, pady=(0, 10))
        divider.grid(row=10, column=5, rowspan=3, sticky='ns'+'w', pady=20)
        examples_frame.grid(row=10, column=6, rowspan=3, columnspan=9, sticky='nsew', padx=5, pady=5)

        for c in range(0, 4):
            examples_frame.columnconfigure(c, weight=1)

        self.animals_example1 = ctk.CTkLabel(examples_frame, text_color=DARK, font=LV5_FONT,
                                             text='ape\noctopus\naxolotl\nbaboon\nswan\nrabbit\nturkey', justify='left')
        self.animals_example2 = ctk.CTkLabel(examples_frame, text_color=DARK, font=LV5_FONT,
                                             text='bass\nhorse\niguana\nbee\ncoral\nsnail\nlynx', justify='left')
        self.animals_example3 = ctk.CTkLabel(examples_frame, text_color=DARK, font=LV5_FONT,
                                             text='dolphin\ngorilla\nocelot\nprawn\nsparrow\nhuman\ndeer',
                                             justify='left')
        self.animals_example4 = ctk.CTkLabel(examples_frame, text_color=DARK, font=LV5_FONT,
                                             text='zebra\nlemur\njaguar\npug\nmouse\nduck\n ...', justify='left')

        self.colors_example1 = ctk.CTkLabel(examples_frame, text_color=DARK, font=LV5_FONT,
                                            text='umber\npeach\nlilac\ncamel\nlime\nsnow\ncyan', justify='left')
        self.colors_example2 = ctk.CTkLabel(examples_frame, text_color=DARK, font=LV5_FONT,
                                            text='beige\nmint\naqua\ngreen\nred\nivory\nmauve', justify='left')
        self.colors_example3 = ctk.CTkLabel(examples_frame, text_color=DARK, font=LV5_FONT,
                                            text='salmon\nplum\nyellow\npurple\nmustard\nviolet\nolive', justify='left')
        self.colors_example4 = ctk.CTkLabel(examples_frame, text_color=DARK, font=LV5_FONT,
                                            text='blue\nemerald\ncopper\norange\nsunset\ncerise\n ...', justify='left')

        self.countries_example1 = ctk.CTkLabel(examples_frame, text_color=DARK, font=LV5_FONT,
                                               text='Uruguay\nLesotho\nGrenada\nBelarus\nBolivia\nIndia\nQatar',
                                               justify='left')
        self.countries_example2 = ctk.CTkLabel(examples_frame, text_color=DARK, font=LV5_FONT,
                                               text='Iceland\nHaiti\nPoland\nEcuador\nAngola\nGreece\nNepal',
                                               justify='left')
        self.countries_example3 = ctk.CTkLabel(examples_frame, text_color=DARK, font=LV5_FONT,
                                               text='Vietnam\nEstonia\nMyanmar\nSweden\nAndorra\nNorway\nPeru',
                                               justify='left')
        self.countries_example4 = ctk.CTkLabel(examples_frame, text_color=DARK, font=LV5_FONT,
                                               text='Japan\nMalta\nUkraine\nMonaco\nPortugal\nWales\n ...',
                                               justify='left')

        self.selection_of_labels_themes('animals')

        # Custom Section
        self.inputted_labels_entry = ctk.CTkEntry(self.page2, placeholder_text='label1,label2,label3...',
                                                  corner_radius=5, height=30)
        inputted_labels_button = ctk.CTkButton(self.page2,
                                               command=lambda: self.validate_input_data('Labels', 'Entry'),
                                               corner_radius=15, height=40,
                                               fg_color=TERTIARY, hover_color=TERTIARY, anchor='center',
                                               text='Insert Labels', text_color=DARK, font=LV4_FONT)

        custom_divider = ctk.CTkFrame(self.page2, fg_color=DARK, height=2, width=350)
        custom_or = ctk.CTkLabel(self.page2, text='OR', fg_color=LIGHT,
                                 width=40, height=10, font=('Josefin Sans Bold', 12), text_color=DARK)

        self.sheet_entry_label = ctk.CTkEntry(self.page2, placeholder_text='Sheet name', width=90, height=30)
        self.column_entry_label = ctk.CTkEntry(self.page2, placeholder_text='Column index', width=60, height=30)
        imported_labels_button = ctk.CTkButton(self.page2, text='Import Labels',
                                               command=lambda: self.validate_input_data('Labels', 'File'),
                                               corner_radius=15, height=40, width=175,
                                               fg_color=TERTIARY, hover_color=TERTIARY, anchor='center',
                                               text_color=DARK, font=LV4_FONT, text_color_disabled=LIGHT)

        def toggle_labels_widgets(*args):
            if self.default_labels_switch_var.get() == 'Default':
                label_reset.configure(state='disabled')
                # Default
                animals_button.grid(row=10, column=0, columnspan=5, sticky='w', padx=100, pady=(10, 0))
                colors_button.grid(row=11, column=0, columnspan=5, sticky='w', padx=100)
                countries_button.grid(row=12, column=0, columnspan=5, sticky='w', padx=100, pady=(0, 10))
                divider.grid(row=10, column=5, rowspan=3, sticky='ns'+'w', pady=20)
                if self.radio_var.get() == 'Animals':
                    self.selection_of_labels_themes('animals')
                    self.animals_example1.grid(row=0, column=0, sticky='w', pady=10)
                    self.animals_example2.grid(row=0, column=1, sticky='w', pady=10)
                    self.animals_example3.grid(row=0, column=2, sticky='w', pady=10)
                    self.animals_example4.grid(row=0, column=3, sticky='w', pady=10)
                elif self.radio_var.get() == 'Colors':
                    self.selection_of_labels_themes('colors')
                    self.colors_example1.grid(row=0, column=0, sticky='w', pady=10)
                    self.colors_example2.grid(row=0, column=1, sticky='w', pady=10)
                    self.colors_example3.grid(row=0, column=2, sticky='w', pady=10)
                    self.colors_example4.grid(row=0, column=3, sticky='w', pady=10)
                elif self.radio_var.get() == 'Countries':
                    self.selection_of_labels_themes('countries')
                    self.countries_example1.grid(row=0, column=0, sticky='w', pady=10)
                    self.countries_example2.grid(row=0, column=1, sticky='w', pady=10)
                    self.countries_example3.grid(row=0, column=2, sticky='w', pady=10)
                    self.countries_example4.grid(row=0, column=3, sticky='w', pady=10)

                self.inputted_labels_entry.grid_forget()
                inputted_labels_button.grid_forget()
                self.sheet_entry_label.grid_forget()
                self.column_entry_label.grid_forget()
                imported_labels_button.grid_forget()
                custom_divider.grid_forget()
                custom_or.grid_forget()

            else:
                self.selection_of_labels_themes('custom')
                label_reset.configure(state='normal')
                # Custom
                self.inputted_labels_entry.grid(row=10, column=1, rowspan=1, columnspan=9, sticky='ew', padx=10,
                                                pady=(45, 0))
                inputted_labels_button.grid(row=10, column=10, rowspan=1, columnspan=5, sticky='ew', padx=10,
                                            pady=(45, 0))
                self.sheet_entry_label.grid(row=12, column=1, rowspan=1, columnspan=5, sticky='ew', padx=10,
                                            pady=(0, 45))
                self.column_entry_label.grid(row=12, column=6, rowspan=1, columnspan=4, sticky='ew', padx=(0, 10),
                                             pady=(0, 45))
                imported_labels_button.grid(row=12, column=10, rowspan=1, columnspan=5, sticky='ew', padx=10,
                                            pady=(0, 40))
                custom_divider.grid(row=11, column=1, columnspan=14, sticky='ew', padx=15, pady=10)
                custom_or.grid(row=11, column=9, columnspan=2, padx=15, pady=(8, 10))

                # Forget Default
                animals_button.grid_forget()
                colors_button.grid_forget()
                countries_button.grid_forget()
                divider.grid_forget()
                if self.radio_var.get() == 'Animals':
                    self.animals_example1.grid_forget()
                    self.animals_example2.grid_forget()
                    self.animals_example3.grid_forget()
                    self.animals_example4.grid_forget()
                elif self.radio_var.get() == 'Colors':
                    self.colors_example1.grid_forget()
                    self.colors_example2.grid_forget()
                    self.colors_example3.grid_forget()
                    self.colors_example4.grid_forget()
                elif self.radio_var.get() == 'Countries':
                    self.countries_example1.grid_forget()
                    self.countries_example2.grid_forget()
                    self.countries_example3.grid_forget()
                    self.countries_example4.grid_forget()

            if 0 < len(self.ids_list) <= len(self.labels_list):
                self.randomize_button.configure(state='normal')
            else:
                self.randomize_button.configure(state='disabled')

        self.default_labels_switch_var.trace_add('write', toggle_labels_widgets)

        # Generate Key Button
        self.randomize_button = ctk.CTkButton(self.page2, command=self.generate_key, state='disabled',
                                              corner_radius=25, height=45,
                                              fg_color=PRIMARY, hover_color=SECONDARY, anchor='center',
                                              text='Generate Key', text_color=LIGHT, font=LV3_FONT,
                                              text_color_disabled=LIGHT)
        self.randomize_button.grid(row=13, column=1, rowspan=3, columnspan=14, sticky='ew')

    def create_page3(self):
        for r in range(0, 16):
            self.page3.rowconfigure(r, minsize=30)
        for c in range(0, 16):
            self.page3.columnconfigure(c, minsize=78)

        # Title
        ctk.CTkLabel(self.page3, text='Rename Datasets or Files',
                     text_color=DARK, font=LV1_FONT).grid(
            row=1, column=0, rowspan=2, columnspan=16, sticky='nsew')

        # Import Key Button
        ctk.CTkButton(self.page3, text='Import Key', command=lambda: self.load_key(),
                      corner_radius=25, height=50,
                      fg_color=PRIMARY, hover_color=SECONDARY,
                      text_color=LIGHT, font=LV3_FONT).grid(
            row=3, column=1, rowspan=2, columnspan=14, sticky='ew', pady=(30, 0))

        # Number of Imported Key Pairs & Reset Button
        ctk.CTkLabel(self.page3, textvariable=self.len_id_label_pairs,
                     text_color=DARK, font=(LV2_FONT[0], LV2_FONT[1] * 1.5), anchor='w').grid(
            row=6, column=1, columnspan=7, sticky='e', padx=(0, 10))
        ctk.CTkLabel(self.page3, text='ID/Label pairs',
                     text_color=DARK, font=(LV3_FONT[0], LV3_FONT[1] * 1.5), anchor='sw').grid(
            row=6, column=8, columnspan=6, sticky='w', pady=(5, 0))
        id_label_reset = ctk.CTkButton(self.page3, corner_radius=15, fg_color=GREY, hover=False, width=0, height=20,
                                       command=lambda: self.reset_list('Key'), image=self.reset_img, text='')
        id_label_reset.grid(row=6, column=14)

        # Blind/Unblind Segmented Button
        un_blind_button = ctk.CTkSegmentedButton(self.page3, values=['Blind', 'Unblind'],
                                                 command=None, variable=self.un_blind_button_var,
                                                 corner_radius=15, height=60,
                                                 font=LV3_FONT, text_color=WHITE, border_width=0,
                                                 fg_color=SECONDARY, unselected_hover_color=PRIMARY,
                                                 unselected_color=SECONDARY, selected_color=PRIMARY)
        un_blind_button.grid(row=8, column=1, rowspan=2, columnspan=14, sticky='ew', padx=10)

        # Sheet & Column Entry and Rename Dataset Button
        self.sheet_entry_file = ctk.CTkEntry(self.page3, placeholder_text='Sheet name', height=30)
        self.sheet_entry_file.grid(row=11, column=1, rowspan=2, columnspan=5, sticky='ew', padx=10)
        self.column_entry_file = ctk.CTkEntry(self.page3, placeholder_text='Column index', height=31)
        self.column_entry_file.grid(row=11, column=6, rowspan=2, columnspan=2, padx=(0, 10), sticky='ew')
        self.rename_datasets_button = ctk.CTkButton(self.page3, text='Rename Dataset',
                                                    command=lambda: self.rename_datasets(), state='disabled',
                                                    corner_radius=15, height=40,
                                                    fg_color=TERTIARY, hover_color=TERTIARY, anchor='center',
                                                    text_color=DARK, font=LV4_FONT, text_color_disabled=LIGHT)
        self.rename_datasets_button.grid(row=11, column=8, rowspan=2, columnspan=7, sticky='ew', padx=10)

        # Separator
        ctk.CTkFrame(self.page3, fg_color=DARK, height=2).grid(
            row=12, column=1, rowspan=2, columnspan=14, sticky='ew', padx=15, pady=80)
        ctk.CTkLabel(self.page3, text='OR', fg_color=LIGHT,
                     width=40, height=10, font=('Josefin Sans Bold', 12), text_color=DARK).grid(
            row=12, column=7, rowspan=2, columnspan=2, padx=15, pady=(28, 30))

        # Rename Files Button
        self.rename_files_button = ctk.CTkButton(self.page3, text='Rename Files',
                                                 command=lambda: self.rename_files(), state='disabled',
                                                 corner_radius=25, height=40,
                                                 fg_color=TERTIARY, hover_color=TERTIARY, anchor='center',
                                                 text_color=DARK, font=LV4_FONT, text_color_disabled=LIGHT)
        self.rename_files_button.grid(row=13, column=1, rowspan=2, columnspan=14, sticky='ew', padx=10)

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
        self.page2.grid_propagate(True)

    def show_page3(self):
        if self.page3.winfo_ismapped():
            self.page3.grid_forget()
        else:
            self.show_page(self.page3)
        self.page3.grid_propagate(True)

    @staticmethod
    def open_github(sub_link):
        if sub_link == 'instructions':
            webbrowser.open('https://github.com/AlexHenriques/inBlindSight?tab=readme-ov-file#how-to-use')
        elif sub_link == 'feedback':
            webbrowser.open('https://github.com/AlexHenriques/inBlindSight?tab=readme-ov-file#bugs--feature-requests')
        elif sub_link == 'release':
            webbrowser.open('https://github.com/AlexHenriques/inBlindSight/releases')

    @staticmethod
    def find_delimiter(file_path):
        with open(file_path, 'r', newline='') as csvfile:
            sample = csvfile.read(1024)
            sniffer = csv.Sniffer()
            try:
                dialect = sniffer.sniff(sample)
                return dialect.delimiter
            except csv.Error:
                return ','

    def selection_of_labels_themes(self, theme):
        if theme == 'animals':
            self.labels_list = ANIMALS_LIST
            self.animals_example1.grid(row=0, column=0, sticky='w', pady=10)
            self.animals_example2.grid(row=0, column=1, sticky='w', pady=10)
            self.animals_example3.grid(row=0, column=2, sticky='w', pady=10)
            self.animals_example4.grid(row=0, column=3, sticky='w', pady=10)

            self.colors_example1.grid_forget()
            self.colors_example2.grid_forget()
            self.colors_example3.grid_forget()
            self.colors_example4.grid_forget()

            self.countries_example1.grid_forget()
            self.countries_example2.grid_forget()
            self.countries_example3.grid_forget()
            self.countries_example4.grid_forget()

        elif theme == 'colors':
            self.labels_list = COLORS_LIST
            self.colors_example1.grid(row=0, column=0, sticky='w', pady=10)
            self.colors_example2.grid(row=0, column=1, sticky='w', pady=10)
            self.colors_example3.grid(row=0, column=2, sticky='w', pady=10)
            self.colors_example4.grid(row=0, column=3, sticky='w', pady=10)

            self.animals_example1.grid_forget()
            self.animals_example2.grid_forget()
            self.animals_example3.grid_forget()
            self.animals_example4.grid_forget()

            self.countries_example1.grid_forget()
            self.countries_example2.grid_forget()
            self.countries_example3.grid_forget()
            self.countries_example4.grid_forget()

        elif theme == 'countries':
            self.labels_list = COUNTRIES_LIST
            self.countries_example1.grid(row=0, column=0, sticky='w', pady=10)
            self.countries_example2.grid(row=0, column=1, sticky='w', pady=10)
            self.countries_example3.grid(row=0, column=2, sticky='w', pady=10)
            self.countries_example4.grid(row=0, column=3, sticky='w', pady=10)

            self.animals_example1.grid_forget()
            self.animals_example2.grid_forget()
            self.animals_example3.grid_forget()
            self.animals_example4.grid_forget()

            self.colors_example1.grid_forget()
            self.colors_example2.grid_forget()
            self.colors_example3.grid_forget()
            self.colors_example4.grid_forget()
        elif theme == 'custom':
            self.labels_list = self.user_labels_list

        self.len_labels_list.set(value=f'{len(self.labels_list)}')

    def reset_list(self, list_to_delete):
        if list_to_delete == 'ID':
            self.ids_list.clear()
            self.len_ids_list.set(value=f'{len(self.ids_list)}')
            self.randomize_button.configure(state='disabled')
        elif list_to_delete == 'Label':
            self.labels_list.clear()
            self.len_labels_list.set(value=f'{len(self.labels_list)}')
            self.randomize_button.configure(state='disabled')
        elif list_to_delete == 'Key':
            self.id_label_pairs.clear()
            self.len_id_label_pairs.set(value=f'{len(self.id_label_pairs)}')
            self.rename_datasets_button.configure(state='disabled')
            self.rename_files_button.configure(state='disabled')

    def validate_input_data(self, data_type, data_format):
        data_input = ''
        if data_format == 'Entry':
            if data_type == 'IDs':
                data_input = self.inputted_ids_entry.get()
            elif data_type == 'Labels':
                data_input = self.inputted_labels_entry.get()
        elif data_format == 'File':
            file_path = filedialog.askopenfilename(
                initialdir=HOME_DIRECTORY,
                title='Select File',
                filetypes=(('Supported Files: .csv;.xlsx;.xls', '*.csv;*.xlsx;*.xls'), ('All files', '*.*')))
            if not file_path:
                CTkMessagebox(title='File Selection Error',
                              message='No file selected.\nPlease select a file and try again.',
                              icon='cancel')
                return
            if not file_path.endswith(('.csv', '.xlsx', '.xls')):
                CTkMessagebox(title='Unsupported File Format',
                              message='Please select a supported file format.'
                                      '\nSupported formats: .csv, .xlsx, .xls',
                              icon='cancel')
                return

            if data_type == 'IDs':
                sheet_name = self.sheet_entry_id.get() if not file_path.endswith('.csv') else '_'
                column_index = self.column_entry_id.get()
            elif data_type == 'Labels':
                sheet_name = self.sheet_entry_label.get() if not file_path.endswith('.csv') else '_'
                column_index = self.column_entry_label.get()
            else:
                return

            if not sheet_name.strip() or not column_index.isdigit():
                if not sheet_name.strip():
                    CTkMessagebox(title='Dataset Localization Error - Sheet',
                                  message='Please enter a valid string in the sheet_name name',
                                  icon='cancel')
                    return
                if not column_index.isdigit():
                    CTkMessagebox(title='Dataset Localization Error - Column',
                                  message='Please enter a positive integer in the column_index number.',
                                  icon='cancel')
                    return
            else:
                column_index = int(column_index) - 1 if int(column_index) > 0 else 0

                header_prompt = CTkMessagebox(title='Header Question',
                                               message='Does the file have an header at the first row?',
                                               icon='question', option_1='Yes', option_2='No')
                if header_prompt.get() == 'Yes':
                    header = 0
                else:
                    header = None

                if file_path.endswith('.csv'):
                    delimiter = inBlindSight.find_delimiter(file_path)
                    data_input = pd.read_csv(file_path, header=header, sep=delimiter)

                elif file_path.endswith(('.xlsx', '.xls')):
                    sheet_names = pd.ExcelFile(file_path).sheet_names
                    if sheet_name in sheet_names:
                        data_input = pd.read_excel(file_path, sheet_name=sheet_name, header=header, keep_default_na=False)
                    else:
                        CTkMessagebox(title='Sheet Name Not Found',
                                      message=f'Could not find a sheet_name with the name: {sheet_name}.\n'
                                              f'Here are the available sheets: {", ".join(sheet_names)}',
                                      icon='cancel')
                        return
                else:
                    return

                data_input = data_input.iloc[:, column_index]
                data_input = data_input.astype(str)
                data_input = ','.join(data_input)

        if data_input.strip():
            replace_patterns = ['\n', '\t', ' ,', ', ', ',,']
            for pattern in replace_patterns:
                data_input = data_input.replace(pattern, ',')

            data_input = [x.strip() for x in data_input.strip(',').split(',') if x != '']
            duplicate_data = len(data_input) != len(set(data_input))
            if duplicate_data:
                CTkMessagebox(title='Duplicates Detected',
                              message='The inserted data_input contains duplicates.\n'
                                      'Please ensure each entry is unique and try again',
                              icon='cancel')
            else:
                initial_len = len(self.ids_list) if data_type == 'IDs' else\
                    len(self.user_labels_list) if data_type == 'Labels' else\
                    None

                if data_type == 'IDs':
                    self.ids_list += list(set(data_input) - set(self.ids_list))
                elif data_type == 'Labels':
                    self.user_labels_list += list(set(data_input) - set(self.user_labels_list))

                self.len_ids_list.set(str(len(self.ids_list)))
                self.len_labels_list.set(str(len(self.labels_list)))

                if 0 < len(self.ids_list) <= len(self.labels_list):
                    self.randomize_button.configure(state='normal')
                else:
                    self.randomize_button.configure(state='disabled')

                added_len = (len(self.ids_list) if data_type == 'IDs' else
                             len(self.user_labels_list) if data_type == 'Labels' else
                             None) - initial_len

                if added_len != len(data_input):
                    CTkMessagebox(title=f'Duplicate {data_type} Detected',
                                  message=f'It seems that some {data_type} entered have been previously added.\n'
                                          f'Only {added_len} out of {len(data_input)} {data_type} were actually added.\n'
                                          f'Please review your data_input.',
                                  icon='cancel')

    def generate_key(self):
        random.shuffle(self.labels_list)  # Increase randomness
        random_label_selection = random.sample(self.labels_list, len(self.ids_list))  # Randomly select labels
        self.id_label_pairs = list(zip(self.ids_list, random_label_selection))  # Randomly pairs unique IDs to labels

        key = pd.DataFrame(self.id_label_pairs, columns=['ID', 'Label'])

        key_file_path = filedialog.asksaveasfilename(
            initialdir=HOME_DIRECTORY,
            title='Save As',
            filetypes=(('.xlsx', '*.xlsx'), ('All files', '*.*'))
        )
        if key_file_path:
            current_time = datetime.now().strftime('%Y_%m_%d_%H_%M')
            key_file_path += f' [{current_time}]'
            if not key_file_path.endswith('.xlsx'):
                key_file_path += '.xlsx'
            key.to_excel(key_file_path, index=False)
            CTkMessagebox(title='Success',
                          message=f'{key_file_path} was successfully created',
                          icon='check')
        else:
            CTkMessagebox(title='File Selection Error',
                          message='No file selected.\nPlease select a file and try again.',
                          icon='cancel')

    def load_key(self):
        key_file = filedialog.askopenfilename(
            initialdir=HOME_DIRECTORY,
            title='Select File',
            filetypes=(('Supported Files: .csv;.xlsx;.xls', '*.csv;*.xlsx;*.xls'), ('All files', '*.*')))

        if not key_file:
            CTkMessagebox(title='File Selection Error',
                          message='No file selected.\nPlease select a file and try again.',
                          icon='cancel')
        elif not key_file.endswith(('.xlsx', '.xls', '.csv')):
            CTkMessagebox(title='Unsupported File Format',
                          message='Please select a supported file format.'
                                  '\nSupported formats: .csv, .xlsx, .xls',
                          icon='cancel')
            return
        else:
            header_prompt = CTkMessagebox(title='Header Question',
                                          message='Does the file have an header?',
                                          icon='question', option_1='Yes', option_2='No')
            header = 0 if header_prompt.get() == 'Yes' else None

            if key_file.endswith('.csv'):
                delimiter = inBlindSight.find_delimiter(key_file)
                key = pd.read_csv(key_file, header=header, keep_default_na=False, sep=delimiter)
            elif key_file.endswith(('.xlsx', '.xls')):
                key = pd.read_excel(key_file, header=header, keep_default_na=False)
            else:
                return

            if 'Unnamed: 0' in key.columns:
                del key['Unnamed: 0']

            ids = key.iloc[:, 0]
            non_empty_ids = [key for key in ids if str(key).strip() != '']
            labels = key.iloc[:, 1]
            non_empty_labels = [value for value in labels if str(value).strip() != '']

            if len(non_empty_ids) != len(ids) or len(non_empty_labels) != len(labels):
                if len(non_empty_ids) != len(ids) and len(non_empty_labels) != len(labels):
                    CTkMessagebox(title='Inconsistent Data',
                                  message=f'Key only contains {len(non_empty_ids)} out of {len(ids)} IDs '
                                          f'and {len(non_empty_labels)} out of {len(labels)} labels.\n'
                                          'Please ensure the data is correctly filled in and try again.',
                                  icon='cancel')
                elif len(non_empty_ids) != len(ids):
                    CTkMessagebox(title='Empty IDs Detected',
                                  message=f'Key only contains {len(non_empty_ids)} out of {len(ids)} IDs.\n'
                                          'Please ensure all IDs are properly filled in and try again.',
                                  icon='cancel')
                elif len(non_empty_labels) != len(labels):
                    CTkMessagebox(title='Empty Labels Detected',
                                  message=f'Key only contains {len(non_empty_labels)} out of {len(labels)} labels.\n'
                                          'Please ensure all labels are properly filled in and try again.',
                                  icon='cancel')
                return
            elif len(set(ids)) != len(ids) or len(set(labels)) != len(labels):
                if len(set(ids)) != len(ids) and len(set(labels)) != len(labels):
                    CTkMessagebox(title='Duplicated Data',
                                  message=f'Key has {len(ids) - len(set(ids))} duplicate IDs '
                                          f'and {len(labels) - len(set(labels))} duplicate labels.\n'
                                          'Please ensure the data is correctly structured and try again.',
                                  icon='cancel')
                elif len(set(ids)) != len(ids):
                    CTkMessagebox(title='Duplicate IDs Detected',
                                  message=f'Key has {len(ids) - len(set(ids))} duplicate IDs.\n'
                                          'Please revise the key and try again.',
                                  icon='cancel')
                elif len(set(labels)) != len(labels):
                    CTkMessagebox(title='Duplicate Labels Detected',
                                  message=f'Key has {len(labels) - len(set(labels))} duplicate labels.\n'
                                          'Please revise the key and try again.',
                                  icon='cancel')
                return
            else:
                self.id_label_pairs = dict(zip(map(str, ids), map(str, labels)))

            if self.id_label_pairs:
                self.len_id_label_pairs.set(str(len(self.id_label_pairs)))
                self.rename_datasets_button.configure(state='normal')
                self.rename_files_button.configure(state='normal')

    def rename_datasets(self):
        dataset_file = filedialog.askopenfilename(
            initialdir=HOME_DIRECTORY,
            title='Select File',
            filetypes=(('Supported Files: .xlsx, .xls, .csv', '*.xlsx; *.xls; *.csv'), ('All files', '*.*')))
        if not dataset_file.endswith(('.xlsx', ',xls', '.csv')):
            CTkMessagebox(title='Unsupported File Format',
                          message='Please select a supported file format.'
                                  '\nSupported formats: .xlsx, .csv',
                          icon='cancel')
        else:
            sheet_name = self.sheet_entry_file.get() if not dataset_file.endswith('.csv') else '_'
            column_index = self.column_entry_file.get()
            if not sheet_name.strip() or not column_index.isdigit():
                if not sheet_name.strip():
                    CTkMessagebox(title='Dataset Localization Error - Sheet',
                                  message='Please enter a valid string in the sheet_name name',
                                  icon='cancel')
                if not column_index.isdigit():
                    CTkMessagebox(title='Dataset Localization Error - Column',
                                  message='Please enter a positive integer in the column_index number.',
                                  icon='cancel')
            else:
                column_index = int(column_index) - 1 if int(column_index) > 0 else 0

                if self.un_blind_button_var.get() == 'Unblind':
                    pairs = {value: key for key, value in self.id_label_pairs.items()}
                else:
                    pairs = self.id_label_pairs

                header_prompt = CTkMessagebox(title='Header Question',
                                              message='Does the file have an header at the first row?',
                                              icon='question', option_1='Yes', option_2='No')
                if header_prompt.get() == 'Yes':
                    header = 0
                else:
                    header = None

                if dataset_file.endswith('.csv'):
                    delimiter = inBlindSight.find_delimiter(dataset_file)
                    dataset = pd.read_csv(dataset_file, header=header, sep=delimiter)

                elif dataset_file.endswith(('.xlsx', '.xls')):
                    sheet_names = pd.ExcelFile(dataset_file).sheet_names
                    if sheet_name in sheet_names:
                        dataset = pd.read_excel(dataset_file, sheet_name=sheet_name, header=header, keep_default_na=False)
                    else:
                        CTkMessagebox(title='Sheet Name Not Found',
                                      message=f'Could not find a sheet_name with the name: {sheet_name}.\n'
                                              f'Here are the available sheets: {", ".join(sheet_names)}',
                                      icon='cancel')
                        return
                else:
                    return

                for index, row in dataset.iterrows():
                    original_cell_value = str(row.iloc[column_index])
                    if original_cell_value in pairs:
                        new_cell_value = pairs[original_cell_value]
                        dataset.iloc[index, column_index] = new_cell_value

                rows_shuffled = [row.tolist() for _, row in dataset.iterrows()]
                random.shuffle(rows_shuffled)  # Shuffle the rows in the original df
                shuffled_df = pd.DataFrame(rows_shuffled, columns=dataset.columns)  # Create a new DataFrame

                file_action_prompt = CTkMessagebox(title='New File Question',
                                                   message=f'Would you like to overwrite the existing file '
                                                           f'or create a new one?',
                                                   icon='question', option_1='Overwrite', option_2='Create File',
                                                   option_focus=2)

                if file_action_prompt.get() == 'Overwrite':
                    if dataset_file.endswith(('.xlsx', '.xls')):
                        shuffled_df.to_excel(dataset_file, sheet_name=sheet_name, index=False)
                    else:
                        shuffled_df.to_csv(dataset_file, index=False)
                    CTkMessagebox(title='Success',
                                  message=f'{dataset_file} was successfully renamed.',
                                  icon='check')
                else:
                    extension = '.xlsx' if dataset_file.endswith('.xlsx') \
                        else ('xls' if dataset_file.endswith('.xlsx')
                              else '.csv')
                    new_file_path = filedialog.asksaveasfilename(
                        initialdir=HOME_DIRECTORY,
                        title='Save As',
                        filetypes=((f'Supported Files: {extension}', f'*{extension}'), ('All files', '*.*')))
                    if dataset_file.endswith(('.xlsx', 'xls')):
                        if not new_file_path.endswith(extension):
                            new_file_path += extension
                        shuffled_df.to_excel(new_file_path, sheet_name=sheet_name, index=False)
                    else:
                        new_file_path += '.csv'
                        shuffled_df.to_csv(new_file_path, index=False)

                    CTkMessagebox(title='Success',
                                  message=f'{new_file_path} was successfully renamed.',
                                  icon='check')

    def rename_files(self):
        selected_folder = filedialog.askdirectory(initialdir=HOME_DIRECTORY, title='Select Folder')
        if not selected_folder:
            CTkMessagebox(title='Folder Selection Error',
                          message='Please select a folder.',
                          icon='cancel')
        else:
            renamed_files_counter = 0
            if self.un_blind_button_var.get() == 'Unblind':
                pairs = {value: key for key, value in self.id_label_pairs.items()}
            else:
                pairs = self.id_label_pairs

            for filename in os.listdir(selected_folder):
                file_path = os.path.join(selected_folder, filename)
                if os.path.isfile(file_path):
                    filename_without_extension, file_extension = os.path.splitext(filename)
                    new_filename = pairs.get(filename_without_extension)
                    if new_filename is not None:
                        new_filename = f'{new_filename}{file_extension}'
                        new_file_path = os.path.join(selected_folder, new_filename)
                        os.rename(file_path, new_file_path)
                        renamed_files_counter += 1

            if renamed_files_counter == len(self.id_label_pairs.keys()):
                CTkMessagebox(title='Success',
                              message=f'{renamed_files_counter} files were successfully renamed'
                                      f'in the folder {selected_folder}',
                              icon='check')
            else:
                if renamed_files_counter == 0:
                    CTkMessagebox(title='Renaming Files Error',
                                  message=f'{renamed_files_counter} files were renamed',
                                  icon='cancel')
                else:
                    CTkMessagebox(title='Renaming Files Error',
                                  message=f'Only {renamed_files_counter} files were renamed, '
                                          f'out of {len(self.id_label_pairs.keys())} keys',
                                  icon='warning')


if __name__ == '__main__':
    window = ctk.CTk()
    inBlindSight = InBlindSight(window)
    window.mainloop()
