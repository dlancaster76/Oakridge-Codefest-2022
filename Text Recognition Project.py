import math
import pytesseract as tess
import os
from PIL import Image
tess.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

physics_keywords = ['energy', 'closed system', 'conservation', 'efficiency', 'elastic potential', 'fossil', 'fuels', 'gravitational potential energy', 'gpe', 'joule', 'kinetic', 'power', 'renewable energy', 'specific heat capacity', 'spring constant ', 'system ', 'thermal conductivity ', 'waste energy ', 'watt ', 'work done', 'energy transfers', 'sankey', 'diagram', 'conduction', 'convection', 'insulation', 'insulating houses', 'evaporate', 'calories', 'kinetic energy', 'radiation', 'useful energy', 'total energy', 'useful energy output', 'total energy output', 'infrared', 'stores of energy', 'energy store', 'hydroelectric power', 'nuclear fuel', 'tidal power', 'wave energy', 'wind power', 'photovoltaic cell', 'solar power', 'heat', 'hemisphere', 'geothermal energy', 'fission', 'electricity', 'ampere', 'amp', 'coulomb', 'plug', 'socket ', 'volts ', 'voltage ', 'insulator ', 'conductor ', 'earth wire ', 'fuse ', 'circuit  ', 'heat ', 'resistance', 'watt', 'alternating', 'current', 'direct', 'series', 'parallel', 'hooke', 'law', 'graph', 'variable resistors', 'switch', 'thermistor', 'diode', 'charge', 'repel', 'attract', 'force', 'mains', 'ohm', 'waves', 'amplitude', 'longitudinal', 'transverse', 'wavelength', 'frequency', 'reflection', 'angle of incidence', 'angle of reflection ', 'tir ', 'pitch ', 'doppler ', 'vacuum ', 'spectrum ', 'electromagnetic ', 'refraction ', 'refractive index ', 'internal ', 'optical  ', 'fibres ', 'sound ', 'hertz ', 'period  ', 'microwave ', 'x-ray ', 'ultraviolet ', 'light ', 'radio ', 'gamma  ', 'rays ', 'speed ', 'loudness ', 'crest ', 'magnetism ', 'magnet ', 'field ', 'uniform ', 'poles ', 'north ', 'south ', 'electromagnet ', 'polarity ', 'coil ', 'effect ', 'tesla ', 'solenoid ', 'motor ', 'fleming ', 'induction ', 'generator ', 'transformer ', 'dynamo ', 'induce ', 'compass ', 'motion ', 'torque ', 'momentum ', 'moment ', 'acceleration ', 'velocity ', 'time ', 'distance ', 'graph ', 'newton ', 'gravitational  ', 'strength ', 'orbit ', 'metric ', 'gradient ', 'displacement ', 'apparatus ', 'stopping ', 'scalar ', 'quantity ', 'vector ', 'metre ', 'second ', 'minute ', 'kilometre ', 'hour ', 'friction ', 'air  ', 'mass ', 'tension ', 'elastic ', 'plastic ', 'thrust ', 'balance ', 'spring ', 'wire ', 'compress ', 'proportion ', 'rotate ', 'braking ', 'centre  ', 'limit ', 'inertia ', 'resultant ', 'speed ', 'thinking  ', 'work  ', 'done ', 'terminal ', 'weight ', 'collision ', 'explosion ', 'car ', 'safety ', 'gravity ', 'pivot ', 'temperature ', 'density ', 'pressure ', 'volume ', 'area ', 'gas ', 'liquid ', 'difference ', 'eureka  ', 'solid ', 'calculate ', 'exert ', 'depth ', 'state ', 'matter ', 'property ', 'heat ', 'boyle ', 'absolute ', 'zero ', 'burner ', 'kpa ', 'pascal ', 'kilo ', 'kelvin ', 'celsius  ', 'capacity ', 'sublimation ', 'atom ', 'electron ', 'neutron ', 'nucleus ', 'stability ', 'ionizing ', 'alpha ', 'beta ', 'emission ', 'decay ', 'particle ', 'isotopes ', 'becquerel ', 'disintegration ', 'radioactive ', 'electrode ', 'background ', 'earth ', 'living ', 'artificial ', 'tracers ', 'model ', 'bohr ', 'half-life ', 'nuclear ', 'radioisotope ', 'sievert ', 'activity ', 'fusion ', 'astro ', 'satellite ', 'planet ', 'moon', 'sun ', 'star ', 'big bang ', 'theory ', 'orbit ', 'circular ', 'dark  ', 'natural ', 'supernova ', 'milky ', 'galax ', 'protostar ', 'nebula ', 'red ', 'giant ', 'shift ', 'life ', 'cycle ', 'white ', 'dwarf ', 'solar ', 'system ', 'radius ', 'lightyear ', 'mars ', 'jupiter ', 'mercury ', 'uranus ', 'saturn ', 'venus ', 'neptune  ', 'comet ', 'elliptical ', 'elongate ', 'brightness ', 'blue ', 'dust ', 'compression ', 'black ', 'hole ', 'lumiosity ', 'main sequence ', 'super ', 'giant ', 'hertzsprung ', 'russel ', 'cool ', 'cloud ', 'telescope ', 'absorption ', 'equation ', 'asteroid ', 'filament ', 'parabola ', 'normal ', 'renewable ', 'sonar ', 'stroboscope ', 'tuning fork ', 'vibrate']

maths_keywords = ['x', 'prove', 'value', '-', '=', '+', '*', 'n', 'multiple', 'sum', 'add', 'subract', 'algebra', 'difference', 'positive', 'negative', 'integer', 'even', 'odd', 'consecutive', 'square', 'divided', 'shape', 'space', 'circle', 'radius', 'circumference', 'simplest', 'standard', 'form', 'rationalise', 'denomenator', 'numerator', 'right-angle', 'triangle', 'value', 'expand', 'simplify', 'product', 'whole', 'number', 'f()', 'graph', 'centre', 'term', 'equation', 'sequence', 'arithmetic', 'expression', 'roots', 'coefficient', 'turning ', 'coordinates', 'constant', 'solve', 'percentage', 'theorems', 'ratio', 'given', 'fraction', 'inequality', 'significant', 'figure', 'decimal place', 'percentage', 'gradient', 'quadrilateral', 'distance', 'average', 'time', 'minutes', 'solve', 'median', 'mean', 'mode', 'average', 'upper bound', 'lower bound', 'range', 'grid', 'y', 'straight', 'line', 'work out', 'scale', ':', 'length', 'height', 'width', 'area', 'surface', 'volume', 'exercise', 'power', 'prime', 'factor', 'rhombus', 'diagonal', 'highest common ', 'lowest common multiple', 'transformation', 'maps', 'triangle', 'cumulative ', 'frequency', 'estimate', 'random', 'probability', 'bag', 'replacement', 'total number', 'diagram', 'find', 'solution', 'curve', 'calculate', 'set', 'venn ', 'element', 'cm', 'm', 'cone', 'sphere', 'express', 'rectangle', 'point', 'vector', 'pythagoras', 'hyp', 'adj', 'opp', 'cylinder', 'trapezium', 'quadratic', 'plot', 'similar', 'sketch', 'simultaneous']

bio_keywords = []


images=[]

def get_images(path):
    for file in os.listdir(path):
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
    get_images(r'C:\Users\bielp\Desktop\Text_recognition') 
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



    

check_subject()
        

    



    









