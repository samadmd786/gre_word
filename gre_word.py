import csv

# open .xlsx file
import openpyxl
from openpyxl import Workbook
import argparse


wb = openpyxl.load_workbook('./GreWordMnemonic.xlsx')
# find index of a word
def find_index(word):
    return aa.index(word)
    
last_word  = ""
start_word_index = -9999
last_word_index = -9999
aa= ['Word', 'abate', 'abdicate', 'aberrant', 'abeyance', 'abjure', 'ablution', 'abnegate', 'abrogate', 'abscond', 'abstemious', 'abstruse', 'abut', 'acerbic', 'acme', 'acquiesce', 'admonish', 'adroit', 'adulterate', 'adumbrate', 'aesthetic', 'aggregate', 'alacrity', 'alleviate', 'altruism', 'amalgamate', 'ambiguous', 'ambivalence', 'ambulatory', 'ameliorate', 'amortize', 'anachronism', 'analogous', 'anarchy', 'ancillary', 'anomalous', 'antediluvian', 'anthropomorp hic', 'antipathy', 'apathy', 'aplomb', 'apostate', 'apothegm', 'apotheosis', 'appease', 'apprise', 'approbation', 'appropriate', 'arboreal', 'arduous', 'artless', 'ascetic', 'assiduous', 'assuage', 'attenuate', 'audacious', 'austere', 'autonomous', 'aver', 'bacchanalian', 'balk', 'banal', 'beatific', 'behemoth', 'belie', 'beneficent', 'benison', 'bifurcate', 'bilious', 'bolster', 'bombastic', 'bonhomie', 'boorish', 'bulwark', 'burgeon', 'burnish', 'buttress', 'cajole', 'calumny', 'canard', 'capricious', 'castigation', 'catalyst', 'caustic', 'cavalcade', 'chagrin', 'charlatan', 'chattel', 'chicanery', 'chimerical', 'choleric', 'churlish', 'cistern', 'coagulate', 'coalesce', 'coda', 'coffer', 'cogent', 'comeliness', 'commensurate', 'commodious', 'compendium', 'complaisant', 'compliant', 'conciliatory', 'condone', 'conflagration', 'confound', 'congenial', 'connoisseur', 'consanguineou s', 'contention', 'contentious', 'contrite', 'contumacious', 'conundrum', 'converge', 'convoluted', 'corpulence', 'cosset', 'coterie', 'coven', 'craven', 'curmudgeon', 'daunt', 'declivity', 'decorum', 'default', 'deference', 'deleterious', 'delineate', 'deluge', 'demagogue', 'denigrate', 'deride', 'derivative', 'descry', 'desiccate', 'desultory', 'deterrent', 'diaphanous', 'diatribe', 'dichotomy', 'dictum', 'didactic', 'diffidence', 'diffuse', 'digression', 'diminutive', 'dirge', 'disabuse', 'discerning', 'discomfit', 'discordant', 'discredit', 'discrepancy', 'discrete', 'disingenuous', 'disinterested', 'disparage', 'disparate', 'dissemble', 'disseminate', 'dissolution', 'dissonance', 'distaff', 'distend', 'distill', 'dither', 'diurnal', 'divest', 'doctrinaire', 'dogmatic', 'dormant', 'droll', 'dupe', 'dyspeptic', 'ebullient', 'eclectic', 'efficacy', 'effluvium', 'effrontery', 'effulgent', 'egregious', 'elegy', 'elicit', 'embellish', 'emend', 'emollient', 'empirical', 'emulate', 'encomium', 'endemic', 'enervate', 'engender', 'ennui', 'ephemeral', 'epicure', 'epitome', 'equanimity', 'equivocate', 'ersatz', 'erudite', 'eschew', 'esoteric', 'eulogy', 'euphemism', 'evince', 'exacerbate', 'exculpate', 'exigency', 'exorcise', 'expatiate', 'expiate', 'expunge', 'expurgate', 'extemporaneo\nus', 'extol', 'extrapolate', 'extrapolation', 'facetious', 'fallacious', 'fatuous', 'fawning', 'fealty', 'fecund', 'felicitous', 'fervor', 'fetid', 'filch', 'filial', 'flaccid', 'flag', 'fledgling', 'flout', 'foment', 'forestall', 'forswear', 'fracas', 'fractious', 'frenetic', 'frugality', 'fulminate', 'fulsome', 'furtive', 'futile', 'gainsay', 'gambol', 'garrulous', 'gauche', 'germinate', 'gibe', 'glib', 'goad', 'gouge', 'grandiloquent', 'gratuitous', 'gregarious', 'guileless', 'gullible', 'gustatory', 'hackneyed', 'harangue', 'hegemony', 'heretical', 'hermetic', 'hoary', 'husband', 'hyperbole', 'iconoclastic', 'idiosyncrasy', 'idolatry', 'ignominious', 'imbue', 'immutable', 'impair', 'impassive', 'impecunious', 'impede', 'imperious', 'impermeable', 'imperturbable', 'impervious', 'implacable', 'implicit', 'implode', 'impromptu', 'impugn', 'inadvertently', 'incendiary', 'inchoate', 'incongruity', 'inconsequentia l', 'inculcate', 'indefatigable', 'indigence', 'indigent', 'indolent', 'indubitable', 'inert', 'infallible', 'ingenious', 'ingenuous', 'ingratiate', 'inherent', 'innocuous', 'innuendo', 'insidious', 'insinuate', 'insipid', 'insularity', 'insuperable', 'interdict', 'interlocutor', 'interloper', 'internecine', 'interpolate', 'interstice', 'intractable', 'intransigence', 'intrepid', 'intrinsic', 'inundate', 'inure', 'inured', 'invective', 'inveterate', 'invidious', 'irascible', 'irresolute', 'itinerant', 'itinerary', 'jibe', 'jocular', 'juggernaut', 'jurisprudence', 'kismet', 'knell', 'lachrymose', 'laconic', 'lambaste', 'lapidary', 'largess', 'lassitude', 'latent', 'laud', 'legerdemain', 'lethargic', 'levee', 'levity', 'lexicon', 'libidinous', 'licentious', 'limpid', 'liniment', 'lionize', 'lissome', 'loquacious', 'lucid', 'lugubrious', 'luminous', 'macabre', 'machination', 'magnanimity', 'malapropism', 'malevolent', 'malingerer', 'malleable', 'manifold', 'martinet', 'maudlin', 'maverick', 'mawkish', 'megalomania', 'mendacious', 'mendicant', 'mercurial', 'meticulous', 'minatory', 'misanthrope', 'mitigate', 'mnemonic', 'mollify', 'molt', 'morose', 'mote', 'multifarious', 'mundane', 'munificent', 'nadir', 'nascent', 'nebulous', 'necromancy', 'nefarious', 'negate', 'neologism', 'neophyte', 'nihilism', 'noisome', 'noxious', 'numismatics', 'obdurate', 'obfuscate', 'obsequious', 'obstreperous', 'obviate', 'occlude', 'officious', 'omnipotent', 'omniscient', 'onerous', 'opprobrium', 'ostentatious', 'paean', 'palliate', 'panacea', 'panegyric', 'panoply', 'paragon', 'parley', 'parochial', 'parsimony', 'partisan', 'pastiche', 'pathological', 'paucity', 'peccadillo', 'peculation', 'pedantic', 'penchant', 'penumbra', 'penury', 'perambulate', 'perennial', 'perfidious', 'perfunctory', 'periphrastic', 'pernicious', 'perspicacious', 'pertinacious', 'pervasive', 'phalanx', 'philistine', 'phlegmatic', 'piety', 'placate', 'plait', 'plangent', 'platitude', 'plaudit', 'plethora', 'plummet', 'polemic', 'polyglot', 'posit', 'pragmatic', 'preamble', 'precarious', 'precept', 'precipitate', 'precursor', 'predilection', 'prescient', 'presumptuous', 'prevaricate', 'pristine', 'privation', 'probity', 'prodigal', 'profound', 'progenitor', 'prognosticate', 'proliferate', 'prolific', 'prolix', 'promulgate', 'propensity', 'propinquity', 'propitiate', 'propitious', 'propriety', 'proscribe', 'proselytize', 'prostrate', 'protagonist', 'provident', 'provincial', 'prurient', 'puerile', 'pulchritude', 'pundit', 'pungent', 'pusillanimous', 'qualified', 'querulous', 'quibble', 'quiescent', 'quotidian', 'raconteur', 'raillery', 'rancor', 'rapacious', 'rapprochement', 'rarefied', 'raze', 'recalcitrant', 'recant', 'recidivism', 'recluse', 'recondite', 'recreant', 'redress', 'refractory', 'refute', 'rejoinder', 'relegate', 'renege', 'repast', 'reproach', 'reprobate', 'repudiate', 'requite', 'rescind', 'resolution', 'respite', 'restive', 'reticent', 'retinue', 'revelry', 'reverent', 'ribald', 'rococo', 'rotund', 'ruminate', 'sacrosanct', 'sagacious', 'sage', 'salacious', 'salubrious', 'sanction', 'sanguine', 'sapient', 'satiate', 'saturate', 'savor', 'scabbard', 'scintilla', 'scintillate', 'scurrilous', 'secrete', 'sedition', 'senescent', 'sentient', 'seraphic', 'shard', 'shirk', 'simper', 'sinecure', 'sinuous', 'skeptic', 'slake', 'slovenly', 'sojourn', 'solecism', 'solicitous', 'solipsism', 'sonorous', 'sophist', 'soporific', 'specious', 'sporadic', 'squalid', 'staid', 'stentorian', 'stigma', 'stint', 'stipulate', 'stolid', 'striate', 'stringent', 'stymie', 'subpoena', 'subside', 'substantiate', 'subterfuge', 'sully', 'supercilious', 'supersede', 'supposition', 'surly', 'surreptitious', 'sybarite', 'sycophant', 'tacit', 'talisman', 'tangential', 'tantamount', 'temerity', 'temporal', 'tenable', 'tenet', 'tenuous', 'threnody', 'tirade', 'torpor', 'tortuous', 'tractable', 'trammel', 'transgression', 'trenchant', 'trite', 'truculence', 'truculent', 'turgid', 'turpitude', 'tyro', 'umbrage', 'unctuous', 'unfettered', 'unsullied', 'untoward', 'urbane', 'usury', 'vacillate', 'vacuous', 'variegated', 'venerate', 'veracious', 'verbose', 'viable', 'virile', 'viscous', 'vitiate', 'vitriolic', 'vituperate', 'vituperative', 'vociferous', 'volatile', 'voluble', 'wary', 'waspish', 'welter', 'whimsical', 'wizened', 'wraith', 'xenophobia', 'zealot', 'zenith']
print("aa length: ",len(aa))


parser = argparse.ArgumentParser()
parser.add_argument('--word', type=str, help='word to find', required=False)
parser.add_argument('--si', type=int, help='start index to find', required=False)
parser.add_argument('--ei', type=int, help='end index to find', required=False)
parser.add_argument('--type', type=str, help="search by word or index", required=True)


args = parser.parse_args()
args_last_word = args.word
args_start_index = args.si
args_end_index = args.ei
args_type = args.type

index = False
if args_type == "index":
    index = True

if args_start_index == None:
    args_start_index = 0

print("start_index: ", args_start_index)


if args_start_index != None:
    start_word_index = args_start_index
    
if args_end_index != None:
    # args_end_index = len(aa) - 1
    last_word_index = args_end_index
    print("end index: ", args_end_index)

if index == False:
    if args_last_word != None:
        last_word = args_last_word
    else:
        last_word = input("last word studied: ").lower()
        last_word_index = find_index(str(last_word))
 

# select the first sheet
sheet = wb.active
# read all data from excel file
data = []
for row in sheet.iter_rows(values_only=True):
    data.append(list(row))
total = len(data)
flashcard  = dict()

print("index: ", last_word_index)
# for i in data[:]:
for i in data[start_word_index:last_word_index+1]:
    flashcard[i[1]] = "meaning: "+ str(i[2])+"\n"+"Mnenomic: "+str(i[3])

print(flashcard.keys())

for word, meaning in flashcard.items():
    if word == "Word":
        continue
    print("Word: ", word)
    print()
    input("### press any key to reval meaning ###")
    print()
    print(meaning)
    print()