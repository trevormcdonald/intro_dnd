#!usr/bin/env python
#need fdfgen from github, pip install its requirements
#sudo apt-get install pdftk as well
import csv
import sys
import os
import subprocess
import random
from fdfgen import forge_fdf
from shutil import copy2
from lookups import race_dicts, class_dicts, background_dicts, keys_plus
from pages import save_race, save_class, save_background, background_pages

#assume responses are in responses.csv

field_names=['ClassLevel', 'Background', 'PlayerName', 'CharacterName', 'Race ',
 'Alignment', 'XP', 'Inspiration', 'STR', 'ProfBonus', 'AC', 'Initiative',
 'Speed', 'PersonalityTraits ', 'STRmod', 'HPMax', 'ST Strength', 'DEX',
 'HPCurrent', 'Ideals', 'DEXmod ', 'HPTemp', 'Bonds', 'CON', 'HDTotal',
 'Check Box 12', 'Check Box 13', 'Check Box 14', 'CONmod', 'Check Box 15',
 'Check Box 16', 'Check Box 17', 'HD', 'Flaws', 'INT', 'ST Dexterity',
 'ST Constitution', 'ST Intelligence', 'ST Wisdom', 'ST Charisma', 'Acrobatics',
  'Animal', 'Athletics', 'Deception ', 'History ', 'Insight', 'Intimidation',
  'Check Box 11', 'Check Box 18', 'Check Box 19', 'Check Box 20',
  'Check Box 21', 'Check Box 22', 'Wpn Name', 'Wpn1 AtkBonus', 'Wpn1 Damage',
  'INTmod', 'Wpn Name 2', 'Wpn2 AtkBonus ', 'Wpn2 Damage ', 'Investigation ',
  'WIS', 'Wpn Name 3', 'Wpn3 AtkBonus  ', 'Arcana', 'Wpn3 Damage ',
  'Perception ', 'WISmod', 'CHA', 'Nature', 'Performance', 'Medicine',
  'Religion', 'Stealth ', 'Check Box 23', 'Check Box 24', 'Check Box 25',
  'Check Box 26', 'Check Box 27', 'Check Box 28', 'Check Box 29',
  'Check Box 30', 'Check Box 31', 'Check Box 32', 'Check Box 33',
  'Check Box 34', 'Check Box 35', 'Check Box 36', 'Check Box 37',
  'Check Box 38', 'Check Box 39', 'Check Box 40', 'Persuasion', 'SleightofHand',
   'CHamod', 'Survival', 'AttacksSpellcasting', 'Passive', 'CP',
   'ProficienciesLang', 'SP', 'EP', 'GP', 'PP', 'Equipment',
   'Features and Traits']

surveyname_to_fieldname ={'New Phone, Who Dis?':'PlayerName',
                          'What did you choose for Race?':'Race',
                          'What did you choose for Class?':'ClassLevel',
                          'What is your first Proficiency?':'Prof1',
                          'What is your second Proficiency?':'Prof2',
                          'What is your third Proficiency?':'Prof3',
                          'What is your fourth Proficiency?':'Prof4',
                          'Best (1)':'Ability1',
                          '2':'Ability2',
                          '3':'Ability3',
                          '4':'Ability4',
                          '5':'Ability5',
                          'Worst (6)':'Ability6',
                          'What is their sex?': 'Sex',
                          'Tall, medium or short or RANDOM?':'Height',
                          'Heavy, medium or light or RANDOM?':'Weight',
                          'Does your character have any unique or distinguishing physical features (and maybe a story about it too...)?':'Feat+Traits1',
                          'What is your character like? Now that we know the Race and Class, write one sentence about who they are, and one sentence about how they resolve conflicts.':'PersonalityTraits',
                          'Is your character Lawful, Neutral, or Chaotic?':'Alignment1',
                          'Is your character Good, Neutral, or Evil?':'Alignment2',
                          'Which background did you pick?':'Background',
                          'Describe your own unique background, focusing on your previous life, skills, languages or equipment you have from it.':'Feat+Traits2',
                          'Any thoughts based on above?':'Backstory',
                          'Did you have fun?':'Inspiration'}
fieldname_to_surveyname={'Backstory': 'Any thoughts based on above?',
                        'Sex': 'What is their sex?',
                        'Alignment2': 'Is your character Good, Neutral, or Evil?',
                        'Alignment1': 'Is your character Lawful, Neutral, or Chaotic?',
                        'Prof2': 'What is your second Proficiency?',
                        'Prof3': 'What is your third Proficiency?',
                        'Prof1': 'What is your first Proficiency?',
                        'Prof4': 'What is your fourth Proficiency?',
                        'Feat+Traits1': 'Does your character have any unique or distinguishing physical features (and maybe a story about it too...)?',
                        'Feat+Traits2': 'Describe your own unique background, focusing on your previous life, skills, languages or equipment you have from it.',
                        'Background': 'Which background did you pick?',
                        'PersonalityTraits': 'What is your character like? Now that we know the Race and Class, write one sentence about who they are, and one sentence about how they resolve conflicts.',
                        'Inspiration': 'Did you have fun?',
                        'ClassLevel': 'What did you choose for Class?',
                        'PlayerName': 'New Phone, Who Dis?',
                        'Ability6': 'Worst (6)',
                        'Ability4': '4',
                        'Ability5': '5',
                        'Ability2': '2',
                        'Ability3': '3',
                        'Ability1': 'Best (1)',
                        'Race': 'What did you choose for Race?',
                        'Weight': 'Heavy, medium or light or RANDOM?',
                        'Height': 'Tall, medium or short or RANDOM?'}


proficiency_to_checkbox={'Acrobatics':23, 'Animal':24, 'Arcana':25,
                         'Athletics':26, 'Deception':27, 'History':28,
                         'Insight':29, 'Intimidation':30, 'Investigation':31,
                         'Medicine':32, 'Nature':33, 'Perception':34,
                         'Performance':35, 'Persuasion':36, 'Religion':37,
                         'SleightofHand':38, 'Stealth':39, 'Survival':40}

ability_proficiency_to_checkbox={'Strength':11, 'Dexterity':18, 'Constitution':19,
                                 'Intelligence':20, 'Wisdom':21, 'Charisma':22}

class_to_num_proficiencies={'Barbarian':2, 'Bard':3, 'Cleric':2, 'Druid':2,
                            'Fighter':2, 'Monk':2, 'Paladin':2, 'Ranger':3,
                            'Rogue':4, 'Sorcerer':2, 'Warlock':2, 'Wizard':2}

race_to_num_proficiencies={"Dwarf (Hill)":0, "Dwarf (Mountain)":0, "Elf (High)":1,
                         "Elf (Wood)":1, "Drow":1, "Halfling (Lightfoot)":0,
                         "Halfling (Stout)":0, "Human":0, "Dragonborn (Chromatic)":0,
                         "Dragonborn (Metallic)":0, "Gnome (Forest)":0,
                         "Gnome (Rock)":0, "Half-Elf":0, "Half-Orc":1,
                         "Tiefling":0, "Aasimar":0}

abilityscore_to_mod={1:-5, 2:-4, 3:-4, 4:-3, 5:-3, 6:-2, 7:-2, 8:-1, 9:-1, 10:0,
                    11:0, 12:1, 13:1, 14:2, 15:2, 16:3, 17:3, 18:4, 19:4, 20:5,
                    21:5, 22:6, 23:6, 24:7, 25:7, 26:8, 27:8, 28:9, 29:9, 30:10}




#this is just for testing now
#eventually, put all data here before writing to formname.fdf then merging
fields = [('name','John Smith'),('telephone','555-1234')]

#read in survey responses, for now only deal with one response
with open('responses.csv', 'rb') as f:
    reader = csv.reader(f)
    response_list = list(reader)
#print(response_list)
col_names = response_list[0]
first_response = response_list[1]
all_responses = response_list[1:]

def response_to_dict(response_list):
    #returns a dict of only the question-response pairs that had answers
    keys=[]
    values=[]
    for i in range(len(response_list)):
        if response_list[i] != '':
            keys.append(col_names[i])
            values.append(response_list[i])

    dictionary= dict(zip(keys, values))
    return dictionary


def num_to_box(n):
    return "Check Box "+str(n)

def filter_classname(name):
    i = name.index('(')
    return name[:i]

def get_player(response_dict):
    return response_dict['New Phone, Who Dis?']



def add_race_bonuses(sheet, race, height, weight):
    race_bonuses = race_dicts[race]

    #first, Abilities
    for ability, bonus in race_bonuses["Abilities"].items():
        sheet[ability[0:3].upper()] += bonus

    #second base Height
    sheet["Height"] = race_bonuses["Height"]
    #third base Weight
    sheet["Weight"] = race_bonuses["Weight"]
    #fourth Speed
    sheet["Speed"] = race_bonuses["Speed"]
    #fifth Languages
    sheet["ProficienciesLang"].extend( race_bonuses["Languages"] )
    #Sixth any extras
    if "HP" in race_bonuses.keys():
        sheet["HPMax"] += 1
    else:
        sheet["HPMax"] += 0

    if "Proficiencies" in race_bonuses.keys():
        for p in race_bonuses["Proficiencies"]:
            if not sheet[num_to_box(proficiency_to_checkbox[p])]:
                sheet[num_to_box(proficiency_to_checkbox[p])] = True
                sheet[p] += 2

    #now add the height and weight modifiers
    wm = race_bonuses["Weightmod"]
    hm = race_bonuses["Heightmod"]
    rand_height = random.randint(1,hm) + random.randint(1,hm)

    if height == "Gimme the RANDOM":
        sheet["Height"] += round(rand_height/12.0, 1)
    elif height == "Extra Tall":
        sheet["Height"] += round(2 *hm / 12.0, 1)
    elif height == "Tall":
        sheet["Height"] += round(1.5 *hm / 12.0, 1)
    elif height == "Medium":
        sheet["Height"] += round(hm / 12.0, 1)
    elif height == "Short":
        sheet["Height"] += round(0.5 *hm / 12.0, 1)
    else:
        #extra short
        sheet["Height"] += -0.3

    if weight == "Gimme the RANDOM":
        rand_weight = reduce((lambda x,y: random.randint(1,x)+random.randint(1,y)), wm)
        sheet["Weight"] += rand_height * rand_weight
    elif weight == "Extra Heavy":
        sheet["Weight"] += sum(wm)
    elif weight == "Heavy":
        sheet["Weight"] += round(sum(wm) *.75, 1)
    elif weight == "Medium":
        sheet["Weight"] += round(sum(wm) *0.5, 1)
    elif weight == "Light":
        sheet["Weight"] += round(sum(wm) *0.25, 1)
    else:
        #extra light
        sheet["Weight"] += -10


    return sheet

def add_class_bonuses(sheet, dndclass):

    class_bonuses = class_dicts[dndclass]

    #first increase HPMax by hit Dice
    sheet["HPMax"] += class_bonuses["Hit Dice"]
    sheet["HPCurrent"] = sheet["HPMax"]
    #second, set hit dice and total
    sheet["HD"] = "1d" + str(class_bonuses["Hit Dice"])
    sheet["HDTotal"] = sheet["HD"]

    #third, set saving throws
    for st in class_bonuses["ST"]:
        if not sheet[num_to_box(ability_proficiency_to_checkbox[st])]:
            sheet[num_to_box(ability_proficiency_to_checkbox[st])] = True
            sheet["ST "+st] += 2
    #fourth, add languages
    sheet["ProficienciesLang"].extend( class_bonuses["Languages"] )

    return sheet

def add_background_bonuses(sheet, background):
    #may have come up with onw background, exit early
    if background not in background_dicts.keys():
        sheet["Backstory"] = ""
        return sheet

    background_bonuses = background_dicts[background]

    #add skill Proficiencies
    for p in background_bonuses["Proficiencies"]:
        if not sheet[num_to_box(proficiency_to_checkbox[p])]:
            sheet[num_to_box(proficiency_to_checkbox[p])] = True
            sheet[p] += 2

    return sheet

def init_sheet(response_list):
    #response list is just the list read in from the csv
    #should return a dict that can be written to an fdf file


    #convert to dictionary
    response_dict = response_to_dict(response_list)

    #next, take response_dict and convert keys to PDF Field names
    field_dict={}
    for k, v in response_dict.items():
        #want to discard a couple, so check here if it is meaningful before add

        if k in surveyname_to_fieldname.keys():
            new_key = surveyname_to_fieldname[k]
            if v == "Animal Handling":
                field_dict[new_key] = "Animal"
            elif v == "Sleight of Hand":
                field_dict[new_key] = "SleightofHand"
            else:
                field_dict[new_key] = v
    print(field_dict)
    #now we have a dict of fieldnames to survey responses
    #need to initialize the rest of fields we want with base values
    string_keys=["Alignment", "PersonalityTraits", "Ideals", "Bonds", "Flaws",
                 "Features and Traits", "Backstory", "Feat+Traits", "Allies"]
    int_keys=["XP", "STR", "DEX", "CON", "INT", "WIS", "CHA", "STRmod", "DEXmod",
             "CONmod", "INTmod", "WISmod", "CHamod", 'ST Strength',
             'ST Dexterity', 'ST Constitution', 'ST Intelligence', 'ST Wisdom',
             'ST Charisma', 'Speed', "HPMax", "HPCurrent", "Initiative",
             "ProfBonus", "AC", "Initiative", "Acrobatics", "Animal", "Arcana",
             "Athletics", "Deception", "History", "Insight", "Intimidation",
             "Investigation", "Medicine", "Nature", "Perception", "Performance",
             "Persuasion", "Religion", "SleightofHand", "Stealth", "Survival",
             "Passive", "Height", "Weight"]
    list_keys=["ProficienciesLang", "Equipment", "Treasure"]

    sheet = {}

    #add placeholder for check boxes for proficiencies
    sheet[num_to_box(11)] = None
    for i in range(18,41):
        sheet[num_to_box(i)] = None


    for sk in string_keys:
        sheet[sk] = ""
    for ik in int_keys:
        sheet[ik] = 0
    for lk in list_keys:
        sheet[lk] = []

    #now, add easy fields to initialize, e.g. no real modifications needed
    sheet["PlayerName"] = get_player(response_dict)
    sheet["ProfBonus"] = 2
    sheet["Alignment"] = field_dict["Alignment1"]+ " " +field_dict["Alignment2"]

    sheet["Race"] = field_dict["Race"]
    #save class name and save it as filtered, writing back to dict
    dndclass = filter_classname(field_dict["ClassLevel"]).strip()
    field_dict["ClassLevel"] = dndclass + " 1"
    sheet["ClassLevel"] = field_dict["ClassLevel"]

    sheet["Background"] = field_dict["Background"]
    #now check if player used provided background and add any backstory.
    #But if player chose their own, skip
    if sheet["Background"] in background_dicts.keys():
        sheet["Backstory"] = field_dict["Backstory"]



    #first, add Race Class Background bonuses
    sheet = add_race_bonuses(sheet, sheet["Race"], field_dict["Height"], field_dict["Weight"])
    sheet = add_class_bonuses(sheet, dndclass)
    sheet = add_background_bonuses(sheet, sheet["Background"])

    #add player-indicated Ability base scores and abilities

    for k, v in field_dict.items():
        #first do ability scores and modifiers and ST with two proficiencies
        if k == 'Ability1':
            sheet[v[0:3].upper()] +=  15
            #sheet[v[0:3].upper()+'mod'] += 2
        elif k == 'Ability2':
            sheet[v[0:3].upper()] +=  14
            #sheet[v[0:3].upper()+'mod'] += 2

        elif k == 'Ability3':
            sheet[v[0:3].upper()] +=  13
            #sheet[v[0:3].upper()+'mod'] += 1

        elif k == 'Ability4':
            sheet[v[0:3].upper()] +=  12
            #sheet[v[0:3].upper()+'mod'] =  '+1'

        elif k == 'Ability5':
            sheet[v[0:3].upper()] +=  10
            #sheet[v[0:3].upper()+'mod'] =  '0'

        elif k == 'Ability6':
            sheet[v[0:3].upper()] +=  8
            #sheet[v[0:3].upper()+'mod'] =  '-1'

        elif k == 'Prof1':
            if not sheet[num_to_box(proficiency_to_checkbox[v])]:
                sheet[num_to_box(proficiency_to_checkbox[v])] = True
                sheet[v] += 2
        elif k == 'Prof2':
            if not sheet[num_to_box(proficiency_to_checkbox[v])]:
                sheet[num_to_box(proficiency_to_checkbox[v])] = True
                sheet[v] += 2
        elif k == 'Prof3':
            if not sheet[num_to_box(proficiency_to_checkbox[v])]:
                sheet[num_to_box(proficiency_to_checkbox[v])] = True
                sheet[v] += 2
        elif k == 'Prof4':
            if not sheet[num_to_box(proficiency_to_checkbox[v])]:
                sheet[num_to_box(proficiency_to_checkbox[v])] = True
                sheet[v] += 2

    #now calculate ability modifiers
    sheet["STRmod"] = abilityscore_to_mod[sheet["STR"]]
    sheet["DEXmod"] = abilityscore_to_mod[sheet["DEX"]]
    sheet["CONmod"] = abilityscore_to_mod[sheet["CON"]]
    sheet["INTmod"] = abilityscore_to_mod[sheet["INT"]]
    sheet["WISmod"] = abilityscore_to_mod[sheet["WIS"]]
    sheet["CHamod"] = abilityscore_to_mod[sheet["CHA"]]
    #now we can add these modifiers to saving throws
    sheet["ST Strength"] += sheet["STRmod"]
    sheet["ST Dexterity"] += sheet["DEXmod"]
    sheet["ST Constitution"] += sheet["CONmod"]
    sheet["ST Intelligence"] += sheet["INTmod"]
    sheet["ST Wisdom"] += sheet["WISmod"]
    sheet["ST Charisma"] += sheet["CHamod"]
    #and also skill modifiers
    sheet["Acrobatics"] += sheet["DEXmod"]
    sheet["Animal"]+= sheet["WISmod"]
    sheet["Arcana"]+= sheet["INTmod"]
    sheet["Athletics"]+= sheet["STRmod"]
    sheet["Deception"]+= sheet["CHamod"]
    sheet["History"]+= sheet["INTmod"]
    sheet["Insight"]+= sheet["WISmod"]
    sheet["Intimidation"]+= sheet["CHamod"]
    sheet["Investigation"]+= sheet["INTmod"]
    sheet["Medicine"]+= sheet["WISmod"]
    sheet["Nature"]+= sheet["INTmod"]
    sheet["Perception"]+= sheet["WISmod"]
    sheet["Performance"]+= sheet["CHamod"]
    sheet["Persuasion"]+= sheet["CHamod"]
    sheet["Religion"]+= sheet["INTmod"]
    sheet["SleightofHand"]+= sheet["DEXmod"]
    sheet["Stealth"]+= sheet["DEXmod"]
    sheet["Survival"]+= sheet["WISmod"]
    #can also do passive Perception
    sheet["Passive"] = 10 + sheet["Perception"]
    #and Initiative
    sheet["Initiative"] += sheet["DEXmod"]

    #Lastly, add paragraph-type info from player
    sheet["PersonalityTraits"] = field_dict["PersonalityTraits"]
    sheet["Feat+Traits"] += field_dict["Sex"] +". "
    sheet["Feat+Traits"] += field_dict["Feat+Traits1"] + "  "
    #only if they put other for background
    if "Feat+Traits2" in field_dict.keys():
        sheet["Feat+Traits"] += field_dict["Feat+Traits2"]
    #Inspiration
    #if field_dict["Inspiration"] is "No" or field_dict["Inspiration"] is "Maybe":
    #    sheet["Inspiration"] = 0
    #else:
    #    sheet["Inspiration"] = 1

    #put in Features and Traits how many proficiencies they should have
    sheet["Features and Traits"] = "You should have " + str(race_to_num_proficiencies[sheet["Race"]] + class_to_num_proficiencies[dndclass] + 2) + " proficiencies checked off."

    #Now loop through entire sheet, converting ints and lists to strings as needed
    for k,v in sheet.items():
        if k in keys_plus:
            if v > 0:
                sheet[k] = "+"+str(v)
            else:
                sheet[k] = str(v)
        elif type(v) == list:
            sheet[k] = ", ".join(map(str, v))
        elif type(v) == bool:
            sheet[k] = v
        elif v is not None:
            sheet[k] = str(v)
        else:
            sheet[k] = ''


    #before returning, add duplicate entries but with keys spaces (1 and 2)
    #Do this because form data fields are inconsistently named
    for k, v in sheet.items():
        sheet[k+' '] = v
        sheet[k+'  '] = v

    return sheet


def init_player_dir(name):
    #creates a directory with the PlayerName and copies the Char sheet there
    #returns the location of that char sheet copy
    cwd = os.getcwd()

    name = name.replace(" ", "")

    path = cwd + '/' + name

    if not os.path.exists(path):
        os.makedirs(path)

    copy2(cwd+'/charsheet3pg.pdf', cwd+'/'+name+'/'+name+'_char_sheet.pdf')

    return cwd+'/'+name+'/'+'char_sheet.pdf'


def get_char_sheet_filename(name):
    cwd = os.getcwd()
    return cwd+'/'+name+'/'+name+'_char_sheet.pdf'


def fill_out_char_sheet(response_list):
    cwd = os.getcwd()
    email = response_list[1]
    #heavy lifting done here
    sheet = init_sheet(response_list)

    name=sheet["PlayerName"].replace(" ", "")
    race=sheet["Race"].replace(" ", "").replace("(","").replace(")","")
    dndclass=filter( lambda x: x.isalpha(), sheet["ClassLevel"].replace(" ", ""))
    background=sheet["Background"].replace(" ", "")

    fdf_name = name+'_'+race+'_'+dndclass+'_'+background
    fdf_name = fdf_name.replace("(","").replace(")","")

    #may need to expand to include buttons
    #may need to change checkbox value thing to 'On' instead of 'Yes'

    fdf = forge_fdf("", sheet,[],[],[])
    fdf_file = open(cwd+'/'+name+'/'+fdf_name+'.fdf', 'wb')
    fdf_file.write(fdf)
    fdf_file.close()

    form_loc = get_char_sheet_filename(name)
    fdf_loc = cwd+'/'+name+'/'+fdf_name

    command = "pdftk "+form_loc+" fill_form "+fdf_loc+".fdf"+" output "+fdf_loc+".pdf"
    command = command.replace("(","")
    command = command.replace(")","")
    os.system(command)

    #final thing: also save their race, class, and background pdfs to directory
    if os.path.isfile("phb.pdf"):
        save_race(race, name)
        save_class(dndclass, name)
        if background in background_pages.keys():
            save_background(background, name)



for response in all_responses:
    player_name = get_player(response_to_dict(response))
    init_player_dir(player_name)
    fill_out_char_sheet(response)
