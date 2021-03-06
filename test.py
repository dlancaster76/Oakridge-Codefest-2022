from fileinput import filename
from re import T
from tkinter import *
import shutil
import pytesseract as tess
import os
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import Tk
tess.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

physics_keywords = ['energy', 'closed system', 'conservation', 'efficiency', 'elastic potential', 'fossil', 'fuels', 'gravitational potential energy', 'gpe', 'joule', 'kinetic', 'power', 'renewable energy', 'specific heat capacity', 'spring constant ', 'system ', 'thermal conductivity ', 'waste energy ', 'watt ', 'work done', 'energy transfers', 'sankey', 'diagram', 'conduction', 'convection', 'insulation', 'insulating houses', 'evaporate', 'calories', 'kinetic energy', 'radiation', 'useful energy', 'total energy', 'useful energy output', 'total energy output', 'infrared', 'stores of energy', 'energy store', 'hydroelectric power', 'nuclear fuel', 'tidal power', 'wave energy', 'wind power', 'photovoltaic cell', 'solar power', 'heat', 'hemisphere', 'geothermal energy', 'fission', 'electricity', 'ampere', 'amp', 'coulomb', 'plug', 'socket ', 'volts ', 'voltage ', 'insulator ', 'conductor ', 'earth wire ', 'fuse ', 'circuit  ', 'heat ', 'resistance', 'watt', 'alternating', 'current', 'direct', 'series', 'parallel', 'hooke', 'law', 'graph', 'variable resistors', 'switch', 'thermistor', 'diode', 'charge', 'repel', 'attract', 'force', 'mains', 'ohm', 'waves', 'amplitude', 'longitudinal', 'transverse', 'wavelength', 'frequency', 'reflection', 'angle of incidence', 'angle of reflection', 'tir', 'pitch', 'doppler', 'vacuum', 'spectrum', 'electromagnetic', 'refraction', 'refractive index', 'internal', 'optical', 'fibre', 'sound', 'hertz', 'period', 'microwave', 'x-ray', 'ultraviolet', 'light', 'radio', 'gamma', 'rays', 'speed', 'loudness', 'crest', 'magnetism', 'magnet', 'field', 'uniform', 'poles', 'north', 'south', 'electromagnet', 'polarity', 'coil', 'effect', 'tesla', 'solenoid', 'motor', 'fleming', 'induction', 'generator', 'transformer', 'dynamo', 'induce', 'compass', 'motion', 'torque', 'momentum', 'moment', 'acceleration', 'velocity', 'time', 'distance', 'graph', 'newton', 'gravitational', 'strength', 'orbit', 'metric', 'gradient', 'displacement', 'apparatus', 'stopping', 'scalar', 'quantity', 'vector', 'metre', 'second', 'minute', 'kilometre', 'hour', 'friction', 'air', 'mass', 'tension', 'elastic', 'plastic', 'thrust', 'balance', 'spring', 'wire', 'compress', 'proportion', 'rotate', 'braking', 'centre', 'limit', 'inertia', 'resultant', 'speed', 'thinking', 'work', 'done', 'terminal', 'weight', 'collision', 'explosion', 'car', 'safety', 'gravity', 'pivot', 'temperature', 'density', 'pressure', 'volume', 'area', 'gas', 'liquid', 'difference', 'eureka', 'solid', 'calculate', 'exert', 'depth', 'state', 'matter', 'property', 'heat', 'boyle', 'absolute', 'zero', 'burner', 'kpa', 'pascal', 'kilo', 'kelvin', 'celsius', 'capacity', 'sublimation', 'atom', 'electron', 'neutron', 'nucleus', 'stability', 'ionizing', 'alpha', 'beta', 'emission', 'decay', 'particle', 'isotopes', 'becquerel', 'disintegration', 'radioactive', 'electrode', 'background', 'earth', 'living', 'artificial', 'tracers', 'model', 'bohr', 'half-life', 'nuclear', 'radioisotope', 'sievert', 'activity', 'fusion', 'astro', 'satellite', 'planet', 'moon', 'sun', 'star', 'big bang', 'theory', 'orbit', 'circular', 'dark', 'natural', 'supernova', 'milky', 'galax', 'protostar', 'nebula', 'red', 'giant', 'shift', 'life', 'cycle', 'white', 'dwarf', 'solar', 'system', 'radius', 'lightyear', 'mars', 'jupiter', 'mercury', 'uranus', 'saturn', 'venus', 'neptune', 'comet', 'elliptical', 'elongate', 'brightness', 'blue', 'dust', 'compression', 'black', 'hole', 'lumiosity', 'main sequence', 'super', 'giant', 'hertzsprung', 'russel', 'cool', 'cloud', 'telescope', 'absorption', 'equation', 'asteroid', 'filament', 'parabola', 'normal', 'renewable', 'sonar', 'stroboscope', 'tuning fork', 'vibrate']

maths_keywords = ['x', 'prove', 'value', '-', '=', '+', '*', 'n', 'multiple', 'sum', 'add', 'subract', 'algebra', 'difference', 'positive', 'negative', 'integer', 'even', 'odd', 'consecutive', 'square', 'divided', 'shape', 'space', 'circle', 'radius', 'circumference', 'simplest', 'standard', 'form', 'rationalise', 'denomenator', 'numerator', 'right-angle', 'triangle', 'value', 'expand', 'simplify', 'product', 'whole', 'number', 'f(x)', 'graph', 'centre', 'term', 'equation', 'sequence', 'arithmetic', 'expression', 'roots', 'coefficient', 'turning ', 'coordinates', 'constant', 'solve', 'percentage', 'theorems', 'ratio', 'given', 'fraction', 'inequality', 'significant', 'figure', 'decimal place', 'percentage', 'gradient', 'quadrilateral', 'distance', 'average', 'time', 'minutes', 'solve', 'median', 'mean', 'mode', 'average', 'upper bound', 'lower bound', 'range', 'grid', 'y', 'straight', 'line', 'work out', 'scale', ':', 'length', 'height', 'width', 'area', 'surface', 'volume', 'exercise', 'power', 'prime', 'factor', 'rhombus', 'diagonal', 'highest common ', 'lowest common multiple', 'transformation', 'maps', 'triangle', 'cumulative ', 'frequency', 'estimate', 'random', 'probability', 'bag', 'replacement', 'total number', 'diagram', 'find', 'solution', 'curve', 'calculate', 'set', 'venn ', 'element', 'cm', 'm', 'cone', 'sphere', 'express', 'rectangle', 'point', 'vector', 'pythagoras', 'hyp', 'adj', 'opp', 'cylinder', 'trapezium', 'quadratic', 'plot', 'similar', 'sketch', 'simultaneous', 'calculator', 'statical', 'investigation', 'data', 'misleading', 'tangent', 'continuous', 'compound', 'inverse', 'indices', 'formulae', 'sine', 'cosine', 'angle', 'quartile', 'round', 'perpendicular', 'mid', 'translation', 'enlargement', 'reflection', 'rotation', 'experimental', 'theoretical', 'addition', 'bar', 'chart', 'histogram', 'corresponding', 'semi', 'table', 'diameter ', 'symmetry', 'proportion', 'cubic', 'condition', 'reciprocal', 'solid', 'domain', 'scalar', 'tree', 'tax', 'stretch', 'trigonometry', '3d', 'surds', 'rational', 'irrational', 'function', 'differentiation']

bio_keywords = ['abdomen', 'abiogenesis', 'abiotic', 'abscisic', 'absorption', 'accelerator', 'accommodation', 'acid', 'action', 'activation', 'active', 'adaptation', 'adenosine', 'adrenaline', 'aerobic', 'afterbirth', 'agar', 'agrobacterium', 'aids', 'alcoholic', 'algae', 'allele', 'alternation', 'amino', 'ammonia', 'anabolism', 'anaemie', 'anaerobic', 'anaphase', 'anesthetics', 'animal', 'anther', 'antibiotic', 'antibod', 'antidiuretic', 'antigen', 'anus', 'aorta', 'appendicular', 'appendix', 'arc', 'arteries', 'arterioles', 'aseptic', 'asexual', 'assimilation', 'atp', 'atria', 'atrium', 'auxin', 'axial', 'axon', 'bacteria', 'bacterium', 'base', 'benedict', 'beri-beri', 'bicuspid', 'bicuspid', 'bilateral symmetry', 'bile', 'bioaccumulation', 'biodiversity', 'biomass', 'biome', 'biosynthesis', 'biotechnology', 'biotic', 'biuret', 'bivalve', 'bladder', 'blood', 'bone', 'botany', 'bovine', 'brain', 'breathing', 'bronchial', 'calcium', 'cancer', 'capillaries', 'carbon', 'carcinogens', 'cardiac', 'cartilage', 'catabolism', 'catalase', 'catalyst', 'cava', 'cavity', 'cell', 'cellulose', 'centromere', 'cerebellum', 'cerebrum', 'chain', 'change', 'chitin', 'chlorine', 'chlorophyll', 'chloroplast', 'cholesterol', 'choroid', 'chromatin', 'chromosome', 'chronic', 'cilia', 'ciliary', 'circulatory', 'cloning', 'codominance', 'codon', 'cohesion', 'coleoptile', 'colon', 'commensalism', 'community', 'compound eye', 'concentration', 'cone', 'conjugation', 'connective', 'conservation', 'consumer', 'continuous', 'cornea', 'coronary', 'cortex', 'cotyledon', 'cross', 'cuticle', 'cycle', 'cytokinin', 'cytology', 'cytolysis', 'cytoplasm', 'cytoskeleton', 'darwin', 'deciduous', 'decomposer', 'decomposition', 'denatured', 'dendrite', 'dendron', 'desertification', 'detoxification', 'diabete', 'diaphragm', 'diet', 'dietary', 'differentiation', 'diffusion', 'digestion', 'dihybrid cross', 'diploid', 'disease', 'distal', 'dominant', 'duct', 'duodenum', 'e-cigarette', 'ecology', 'ecosystem', 'ectoplasm', 'ectothermic', 'effect', 'egestion', 'element', 'embryo', 'emulsion', 'endocrine', 'endoplasm', 'endoskeleton', 'endospore', 'endothermic', 'energy', 'environment', 'enzymes', 'epidermis', 'epithelium', 'ethanol', 'euglena', 'eutrophication', 'excretion', 'exhalation', 'exocrine', 'exoskeleton', 'extracellular', 'eye', 'eyespot', 'faeces', 'fallopian', 'farming', 'fatty', 'feeding', 'fermentation', 'fertilisation', 'fetus', 'fibre', 'fibrin', 'fibrinogen', 'flaccid', 'flagella', 'fleming', 'fluid', 'focusing', 'follicle', 'food', 'foot', 'fossil', 'fovea', 'fructose', 'fruit', 'fungi', 'fungicide', 'gall', 'gamete', 'ganglio', 'gas', 'gemmule', 'gene', 'generation', 'genetic', 'genome', 'genotype', 'geotropism', 'germination', 'gestation', 'gland', 'glucagon', 'glucose', 'glycerine', 'glycogen', 'gonad', 'gravity', 'greenhouse', 'gut', 'habitat', 'haemoglobin', 'haploid', 'haustorium', 'head', 'heart', 'hepatic', 'herbicide', 'hermaphroditic', 'heterozygous', 'hibernation', 'hiv', 'holdfast', 'homeostasis', 'homologous', 'homozygous', 'hormone', 'hoverflies', 'human', 'hydra', 'hydrogen bond', 'hydrolysis', 'hydrophobic', 'hydroponic', 'hypha', 'hypodermis', 'hypothalamus', 'hypothesis', 'ileum', 'immune', 'immunity', 'implant', 'infrared', 'inheritance', 'inorganic', 'insecticide', 'insulin', 'intercostal', 'intestine', 'intracellular', 'invertebrates', 'iodine', 'iris', 'iron', 'irritability', 'isotope', 'karyotic', 'karyotype', 'kinetic', 'knop', 'kwashiorkor', 'lactate', 'lactic', 'lactose', 'ladybirds', 'legumes', 'life', 'ligases', 'lignin', 'limeys', 'lipase', 'lipid', 'liver', 'livestock', 'loam', 'lungs', 'luteinizing', 'lymph', 'lymphocyte', 'lysosome', 'macroevolution', 'magnesium', 'mantle', 'marrow', 'matter', 'medulla', 'medusa', 'meiosis', 'membrane', 'membrane', 'memory', 'mendel', 'menstrual', 'mesenchyme', 'mesophyll', 'messenger', 'metabolism', 'metaphase', 'methane', 'microevolution', 'microvilli', 'mineral', 'mitochondria', 'mitosis', 'model', 'molluscicides', 'molt', 'monocots', 'monohybrid', 'monoxide', 'mother cell', 'mouth', 'mucus', 'muscle', 'mushroom', 'mutagen', 'mutation', 'mutualism', 'mycelium', 'myelin', 'myxomatosis', 'natural', 'neonicotinoid', 'nephron', 'nerve', 'nervous system', 'neuromuscular', 'neuron', 'neurotoxin', 'neurotransmitter', 'nicotine', 'nitrification', 'nitrifying', 'nitrogen', 'notochord', 'nucleus', 'nutrient', 'nutrition', 'oblongata', 'oesophagus', 'optic', 'optimum', 'organ', 'organelle', 'organic', 'osmoregulation', 'osmosis', 'ovaries', 'oviduct', 'oxygen', 'pain', 'paleontology', 'palisade', 'pancreas', 'paramecium', 'parasite', 'parasitism', 'passive', 'pasteurization', 'pathogen', 'pedigree', 'pellicle', 'pelvis', 'peptide', 'bond', 'peristalsis', 'permeable', 'pesticide', 'ph', 'phagocyte', 'phagocytosis', 'phase', 'phenotype', 'phloem', 'phospholipid', 'phosphorus', 'photosynthesis', 'phototropism', 'physical change', 'physiology', 'phytoplankton', 'pituitary', 'placenta', 'plankton', 'plant', 'plasma', 'plasmid', 'platelet', 'pleural', 'pollen', 'pollination', 'pollution', 'polygenic', 'polyp', 'polytunnel', 'population', 'potassium', 'potato', 'predator', 'pregnancy', 'pressure', 'producer', 'progesterone', 'protein', 'protozoa', 'pseudopodia', 'puberty', 'pupil', 'receptor', 'recessive', 'rectum', 'reducing', 'reduction', 'reflex', 'refraction', 'regeneration', 'renal', 'repolarization', 'repressor', 'reproduction', 'respiration', 'retina', 'ribosomal', 'ribosome', 'rna', 'rod', 'roots', 'rough', 'saccharose', 'sacarose', 'salivary', 'salmon', 'saprophyte', 'saprotrophic', 'sclera', 'scurvy', 'secretion', 'seed', 'selection', 'semen', 'semilunar', 'semipermeable', 'sensitivity', 'sexual', 'sheep', 'shell', 'skeleton', 'skin', 'smoking', 'sodium', 'solution', 'species', 'sperm', 'sphincter', 'spinal', 'spiral', 'spleen', 'spore', 'sporophore', 'starch', 'stem', 'stigma', 'stimulus', 'stolon', 'stomach', 'stomata', 'streptococcus', 'succulent', 'sucrose', 'sugar', 'symbiosis', 'symmetry', 'synapse', 'taxonomy', 'telophase', 'temperature', 'thallus', 'theory', 'thermometer', 'thorax', 'thyroid', 'thyroxine', 'tissue', 'tobacco', 'trachea', 'transduction', 'transformation', 'transgenic', 'translocation', 'transpiration', 'transport', 'tricuspid', 'tristearin', 'tube', 'tumor', 'turgor', 'twins', 'ultraviolet', 'univalve', 'unsaturated', 'urea', 'urinary', 'vaccine', 'vacuole', 'vaping', 'variation', 'vascular', 'vasoconstriction', 'vegetable', 'vein', 'ventricle', 'virus', 'vitamin', 'voluntary', 'wall', 'waste', 'water', 'watershed', 'web', 'whiteflies', 'wilt', 'xylem', 'yeast', 'yogurt', 'zooplankton', 'zygospore', 'zygote']


images=[]


root = Tk()

def return_dir():
    global my_image
    filename = filedialog.askopenfilename()
    filename = str(filename)
    my_label = Label(root, text=filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(filename))
    my_image_label = Label(image=my_image).pack()
    btn2.destroy()

def image2text():
    text = tess.image_to_string(filename)
    print(text)

#confirm/photo buttons 
btn1 = Button(root, text = 'Confirm', command=image2text)
btn1.place(x = 325, y = 550)

btn2 = Button(root, text = 'Import Photo', command=return_dir)
btn2.place(x = 390, y = 550)
 


def get_images(path):
    for file in os.listdir(filename):
       if file.endswith(".jpg") or file.endswith('.png'):
            images.append(os.path.join(path, file))

def is_word_in(glossary, text, count):
    count = 0
    for word in glossary:
        if word in text:
            count += 1

    return count 

def words_into_list(string, list):
    word = ''
    for char in string:
        if char == '\n' or char == ' ':
            list.append(word)
            word = ""
        else:
            word += char
    for word in list:
        if word == '':
            list.remove(word)

    return list



def check_subject():
    get_images(filename) 
    print(images)
    for image in images:
        phy = 0
        maths = 0
        bio = 0
        text_list = []
        img_name = image[40:]
        img = Image.open(img_name)
        text = tess.image_to_string(img)
        text_list = words_into_list(text, text_list)
        print("""-----------------------------
        {}
        -----------------------------""".format(text_list))
        #comparing text in image to subject glossaries
        phy = is_word_in(physics_keywords, text_list, phy)
        maths = is_word_in(maths_keywords, text_list, maths)
        bio = is_word_in(bio_keywords, text_list, bio)
        
        total_tallies = {'physics':phy, 'maths':maths, 'biology':bio}
    
#decide which subject the image belongs to
        max_subj = max(total_tallies, key=total_tallies.get)
        print(max_subj)
        if max_subj == 'physics':
            dir_name = 'physics'
            try:
                os.mkdir(dir_name)
                print(dir_name, 'created')
                print("Adding", img_name, "to", dir_name)
                src = image
                dst = str(root.filename)
                shutil.copy(src, dst)

            except FileExistsError:
                print("Adding", img_name, "to", dir_name)
                src = image
                dst = str(root.filename)
                shutil.copy(src, dst)
        
        elif max_subj == 'maths':
            dir_name = 'maths'
            try:
                os.mkdir(dir_name)
                print(dir_name, 'created')
                print("Adding", img_name, "to", dir_name)
                src = image
                dst = str(root.filename)
                shutil.copy(src, dst)

            except FileExistsError:
                print("Adding", img_name, "to", dir_name)
                src = image
                dst = str(root.filename)
                shutil.copy(src, dst)

        elif max_subj == 'biology':
            dir_name = 'biology'
            try:
                os.mkdir(dir_name)
                print(dir_name, 'created')
                print("Adding", img_name, "to", dir_name)
                src = image
                dst = str(root.filename)
                shutil.copy(src, dst)

            except FileExistsError:
                print("Adding", img_name, "to", dir_name)
                src = image
                dst = str(root.filename)
                shutil.copy(src, dst)
        
        else: 
            print('Sorry, we could not find a subject for this image...')
        

check_subject()




