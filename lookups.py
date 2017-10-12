






race_dicts={'Dwarf (Hill)':
            {"Abilities":{"Constitution": 2, 'Wisdom': 1}, 'Height':3.6,
            'Weight':110, 'Speed':25, "Languages":["Common", "Dwarvish"],
            "HP":1, "Heightmod": 4, "Weightmod": [6,6]},

            'Dwarf (Mountain)':
            {"Abilities":{"Constitution": 2, 'Strength': 2}, 'Height':4.0,
            'Weight':130, 'Speed':25, "Languages":["Common", "Dwarvish"],
            "Heightmod": 4, "Weightmod": [6,6]},

            'Elf (High)':
            {"Abilities":{"Dexterity": 2, "Intelligence": 1}, 'Height':4.5,
            'Weight':90, 'Speed':30, "Languages":["Common", "Elvish"],
            'Proficiencies':["Perception"], "Heightmod": 10, "Weightmod": [4]},

            'Elf (Wood)':
            {"Abilities":{"Dexterity": 2, "Wisdom": 1}, 'Height':4.5,
            'Weight':100, 'Speed':35, "Languages":["Common", "Elvish"],
            'Proficiencies':["Perception"], "Heightmod": 10, "Weightmod": [4]},

            'Drow':
            {"Abilities":{"Dexterity": 2, "Charisma": 1}, 'Height':4.5,
            'Weight':75, 'Speed':30, "Languages":[],
            'Proficiencies':["Perception"], "Heightmod": 6, "Weightmod": [6]},

            'Halfling (Lightfoot)':
            {"Abilities":{"Dexterity": 2, "Charisma": 1}, 'Height':2.5,
            'Weight':35, 'Speed':25, "Languages":["Common", "Halfling"],
            "Heightmod": 4, "Weightmod": [1]},

            'Halfling (Stout)':
            {"Abilities":{"Dexterity": 2, "Constitution": 1}, 'Height':2.5,
            'Weight':35, 'Speed':25, "Languages":["Common", "Halfling"],
            "Heightmod": 4, "Weightmod": [1]},

            'Human':
            {"Abilities":{"Strength":1, "Dexterity":1, "Constitution":1,
            "Intelligence":1, "Wisdom":1, "Charisma":1}, 'Height':4.7,
            'Weight':110, 'Speed':30, "Languages":["Common"],
             "Heightmod": 10, "Weightmod": [4,4]},

            'Dragonborn (Chromatic)':
            {"Abilities":{"Strength": 2, "Charisma":1}, 'Height':5.5,
            'Weight':175, 'Speed':30, "Languages":["Common", "Draconic"],
             "Heightmod": 8, "Weightmod": [6,6]},

            'Dragonborn (Metallic)':
            {"Abilities":{"Strength": 2, "Charisma":1}, 'Height':5.5,
            'Weight':175, 'Speed':30, "Languages":["Common", "Draconic"],
             "Heightmod": 8, "Weightmod": [6,6]},

            'Gnome (Forest)':
            {"Abilities":{"Intelligence": 2, "Dexterity":1}, 'Height':3,
            'Weight':35, 'Speed':25, "Languages":["Common", "Gnomish"],
             "Heightmod": 4, "Weightmod": [1]},

            'Gnome (Rock)':
            {"Abilities":{"Intelligence": 2, "Constitution":1}, 'Height':3,
            'Weight':35, 'Speed':25, "Languages":["Common", "Gnomish"],
             "Heightmod": 4, "Weightmod": [1]},

            'Half-Elf':
            {"Abilities":{"Charisma": 2,}, 'Height':4.75,
            'Weight':110, 'Speed':30, "Languages":["Common", "Elvish"],
             "Heightmod": 8, "Weightmod": [4,4]},

            'Half-Orc':
            {"Abilities":{"Strength": 2, "Constitution":1}, 'Height':4.75,
            'Weight':140, 'Speed':30, "Languages":["Common", "Orc"],
            'Proficiencies':["Intimidation"],
             "Heightmod": 10, "Weightmod": [6,6]},

            'Tiefling':
            {"Abilities":{"Intelligence": 1, "Charisma": 2}, 'Height':4.75,
            'Weight':110, 'Speed':30, "Languages":["Common", "Infernal"],
             "Heightmod": 8, "Weightmod": [4,4]},

            'Aasimar':
            {"Abilities":{"Charisma": 2,"Wisdom": 1}, 'Height':4.75,
            'Weight': 110, 'Speed':30, "Languages":["Common", "Celestial"],
             "Heightmod": 8, "Weightmod": [4,4]},

            }



class_dicts={"Barbarian":{"Hit Dice": 12, "ST": ["Strength", "Constitution"], "Languages":[],},
             "Bard":{"Hit Dice": 8, "ST": ["Dexterity", "Charisma"], "Languages":[],},
             "Cleric":{"Hit Dice": 8, "ST": ["Wisdom", "Charisma"], "Languages":[],},
             "Druid":{"Hit Dice": 8, "ST": ["Intelligence", "Wisdom"], "Languages":["Druidic"],},
             "Fighter":{"Hit Dice": 10, "ST": ["Strength", "Constitution"], "Languages":[],},
             "Monk":{"Hit Dice": 8, "ST": ["Strength", "Dexterity"], "Languages":[],},
             "Paladin":{"Hit Dice": 10, "ST": ["Wisdom", "Charisma"], "Languages":[],},
             "Ranger":{"Hit Dice": 10, "ST": ["Strength", "Dexterity"], "Languages":[],},
             "Rogue":{"Hit Dice": 8, "ST": ["Dexterity", "Intelligence"], "Languages":["Thieves' Cant"],},
             "Sorcerer":{"Hit Dice": 6, "ST": ["Constitution", "Charisma"], "Languages":[],},
             "Warlock":{"Hit Dice": 8, "ST": ["Wisdom", "Charisma"], "Languages":[],},
             "Wizard":{"Hit Dice": 6, "ST": ["Intelligence", "Wisdom"], "Languages":[],},
            }

background_dicts={
                 "Acolyte":{"Proficiencies":["Insight", "Religion"], },
                 "Charlatan":{"Proficiencies":["Deception", "SleightofHand"],},
                 "Criminal":{"Proficiencies":["Deception", "Stealth"],},
                 "Entertainer":{"Proficiencies":["Acrobatics", "Performance"],},
                 "Folk Hero": {"Proficiencies":["Animal", "Survival"],},
                 "Guild Artisan": {"Proficiencies":["Insight", "Persuasion"],},
                 "Hermit": {"Proficiencies":["Medicine", "Religion"],},
                 "Noble": {"Proficiencies":["History", "Persuasion"],},
                 "Outlander": {"Proficiencies":["Athletics", "Survival"],},
                 "Sage": {"Proficiencies":["Arcana", "History"],},
                 "Sailor": {"Proficiencies":["Athletics", "Perception"],},
                 "Soldier": {"Proficiencies":["Athletics", "Intimidation"],},
                 "Urchin": {"Proficiencies":["SleightofHand", "Stealth"],},
                 }

keys_plus = ["STRmod", "DEXmod",
         "CONmod", "INTmod", "WISmod", "CHamod", 'ST Strength',
         'ST Dexterity', 'ST Constitution', 'ST Intelligence', 'ST Wisdom',
         'ST Charisma', "Initiative",
         "ProfBonus", "Initiative", "Acrobatics", "Animal", "Arcana",
         "Athletics", "Deception", "History", "Insight", "Intimidation",
         "Investigation", "Medicine", "Nature", "Perception", "Performance",
         "Persuasion", "Religion", "SleightofHand", "Stealth", "Survival",]

allfields = ['ClassLevel', 'Background', 'PlayerName', 'CharacterName', 'Race ',
 'Alignment', 'XP', 'Inspiration', 'STR', 'ProfBonus', 'AC', 'Initiative', 'Speed',
  'PersonalityTraits ', 'STRmod', 'HPMax', 'ST Strength', 'DEX', 'HPCurrent',
   'Ideals', 'DEXmod ', 'HPTemp', 'Bonds', 'CON', 'HDTotal', 'Check Box 12',
    'Check Box 13', 'Check Box 14', 'CONmod', 'Check Box 15', 'Check Box 16',
     'Check Box 17', 'HD', 'Flaws', 'INT', 'ST Dexterity', 'ST Constitution',
      'ST Intelligence', 'ST Wisdom', 'ST Charisma', 'Acrobatics', 'Animal',
       'Athletics', 'Deception ', 'History ', 'Insight', 'Intimidation',
        'Check Box 11', 'Check Box 18', 'Check Box 19', 'Check Box 20',
         'Check Box 21', 'Check Box 22', 'Wpn Name', 'Wpn1 AtkBonus',
          'Wpn1 Damage', 'INTmod', 'Wpn Name 2', 'Wpn2 AtkBonus ', 'Wpn2 Damage ',
           'Investigation ', 'WIS', 'Wpn Name 3', 'Wpn3 AtkBonus  ', 'Arcana', 'Wpn3 Damage ',
            'Perception ', 'WISmod', 'CHA', 'Nature', 'Performance', 'Medicine', 'Religion',
             'Stealth ', 'Check Box 23', 'Check Box 24', 'Check Box 25',
             'Check Box 26', 'Check Box 27', 'Check Box 28', 'Check Box 29',
             'Check Box 30', 'Check Box 31', 'Check Box 32', 'Check Box 33',
             'Check Box 34', 'Check Box 35', 'Check Box 36', 'Check Box 37',
             'Check Box 38', 'Check Box 39', 'Check Box 40', 'Persuasion',
             'SleightofHand', 'CHamod', 'Survival', 'AttacksSpellcasting', 'Passive',
              'CP', 'ProficienciesLang', 'SP', 'EP', 'GP', 'PP', 'Equipment',
               'Features and Traits', 'CharacterName 2', 'Age', 'Height', 'Weight',
                'Eyes', 'Skin', 'Hair', 'Faction Symbol Image', 'Allies',
                'FactionName', 'Backstory', 'Feat+Traits', 'Treasure',
                'CHARACTER IMAGE', 'Spellcasting Class 2', 'SpellcastingAbility 2',
                 'SpellSaveDC  2', 'SpellAtkBonus 2', 'SlotsTotal 19',
                 'SlotsRemaining 19', 'Spells 1014', 'Spells 1015', 'Spells 1016',
                  'Spells 1017', 'Spells 1018', 'Spells 1019', 'Spells 1020',
                  'Spells 1021', 'Spells 1022', 'Check Box 314', 'Check Box 3031',
                   'Check Box 3032', 'Check Box 3033', 'Check Box 3034',
                   'Check Box 3035', 'Check Box 3036', 'Check Box 3037',
                   'Check Box 3038', 'Check Box 3039', 'Check Box 3040',
                   'Check Box 321', 'Check Box 320', 'Check Box 3060',
                   'Check Box 3061', 'Check Box 3062', 'Check Box 3063',
                   'Check Box 3064', 'Check Box 3065', 'Check Box 3066',
                   'Check Box 315', 'Check Box 3041', 'Spells 1023',
                   'Check Box 251', 'Check Box 309', 'Check Box 3010',
                   'Check Box 3011', 'Check Box 3012', 'Check Box 3013',
                   'Check Box 3014', 'Check Box 3015', 'Check Box 3016',
                   'Check Box 3017', 'Check Box 3018', 'Check Box 3019',
                   'Spells 1024', 'Spells 1025', 'Spells 1026', 'Spells 1027',
                   'Spells 1028', 'Spells 1029', 'Spells 1030', 'Spells 1031',
                   'Spells 1032', 'Spells 1033', 'SlotsTotal 20', 'SlotsRemaining 20',
                    'Spells 1034', 'Spells 1035', 'Spells 1036', 'Spells 1037',
                    'Spells 1038', 'Spells 1039', 'Spells 1040', 'Spells 1041',
                    'Spells 1042', 'Spells 1043', 'Spells 1044', 'Spells 1045',
                    'Spells 1046', 'SlotsTotal 21', 'SlotsRemaining 21', 'Spells 1047',
                     'Spells 1048', 'Spells 1049', 'Spells 1050', 'Spells 1051',
                     'Spells 1052', 'Spells 1053', 'Spells 1054', 'Spells 1055',
                     'Spells 1056', 'Spells 1057', 'Spells 1058', 'Spells 1059',
                     'SlotsTotal 22', 'SlotsRemaining 22', 'Spells 1060', 'Spells 1061',
                     'Spells 1062', 'Spells 1063', 'Spells 1064', 'Check Box 323',
                     'Check Box 322', 'Check Box 3067', 'Check Box 3068', 'Check Box 3069',
                     'Check Box 3070', 'Check Box 3071', 'Check Box 3072', 'Check Box 3073',
                     'Spells 1065', 'Spells 1066', 'Spells 1067', 'Spells 1068', 'Spells 1069',
                     'Spells 1070', 'Spells 1071', 'Check Box 317', 'Spells 1072',
                     'SlotsTotal 23', 'SlotsRemaining 23', 'Spells 1073', 'Spells 1074',
                     'Spells 1075', 'Spells 1076', 'Spells 1077', 'Spells 1078', 'Spells 1079',
                     'Spells 1080', 'Spells 1081', 'SlotsTotal 24', 'SlotsRemaining 24',
                     'Spells 1082', 'Spells 1083', 'Spells 1084', 'Spells 1085', 'Spells 1086',
                     'Spells 1087', 'Spells 1088', 'Spells 1089', 'Spells 1090', 'SlotsTotal 25',
                     'SlotsRemaining 25', 'Spells 1091', 'Spells 1092', 'Spells 1093',
                     'Spells 1094', 'Spells 1095', 'Spells 1096', 'Spells 1097', 'Spells 1098',
                     'Spells 1099', 'SlotsTotal 26', 'SlotsRemaining 26', 'Spells 10100',
                     'Spells 10101', 'Spells 10102', 'Spells 10103', 'Check Box 316',
                     'Check Box 3042', 'Check Box 3043', 'Check Box 3044', 'Check Box 3045',
                     'Check Box 3046', 'Check Box 3047', 'Check Box 3048', 'Check Box 3049',
                     'Check Box 3050', 'Check Box 3051', 'Check Box 3052', 'Spells 10104',
                     'Check Box 325', 'Check Box 324', 'Check Box 3074', 'Check Box 3075',
                     'Check Box 3076', 'Check Box 3077', 'Spells 10105', 'Spells 10106',
                     'Check Box 3078', 'SlotsTotal 27', 'SlotsRemaining 27', 'Check Box 313',
                     'Check Box 310', 'Check Box 3020', 'Check Box 3021', 'Check Box 3022',
                     'Check Box 3023', 'Check Box 3024', 'Check Box 3025', 'Check Box 3026',
                     'Check Box 3027', 'Check Box 3028', 'Check Box 3029', 'Check Box 3030',
                     'Spells 10107', 'Spells 10108', 'Spells 10109', 'Spells 101010',
                     'Spells 101011', 'Spells 101012', 'Check Box 319', 'Check Box 318',
                     'Check Box 3053', 'Check Box 3054', 'Check Box 3055', 'Check Box 3056',
                     'Check Box 3057', 'Check Box 3058', 'Check Box 3059', 'Check Box 327',
                     'Check Box 326', 'Check Box 3079', 'Check Box 3080', 'Check Box 3081',
                     'Check Box 3082', 'Spells 101013', 'Check Box 3083']
