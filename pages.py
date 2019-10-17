#!/usr/bin/env python

from PyPDF2 import PdfFileWriter, PdfFileReader

#This file is for automatically separating out race, class, and background pages
#to be emailed to players.

race_pages={"DwarfHill":(18,20),
           "DwarfMountain":(18,20),
           "ElfHigh":(21,25),
           "ElfWood":(21,25),
           "Drow":(21,25),
           "HalflingLightfoot":(26,28),
           "HalflingStout":(26,28),
           "Human":(29,31),
           "DragonbornMetallic":(32, 34 ),
           "DragonbornChromatic":(32,34),
           "GnomeRock":(35, 37 ),
           "GnomeForest":(35, 37),
           "Half-Elf":(38,39),
           "Half-Orc":(40,41),
           "Tiefling":(42,44),
           "Aasimar":(42,44)}

class_pages={"Barbarian":(46,50),
             "Bard":(51,55),
             "Cleric":(56,63),
             "Druid":(64,69),
             "Fighter":(70,75),
             "Monk":(76,81),
             "Paladin":(82,88),
             "Ranger":(89,93),
             "Rogue":(94,98),
             "Sorcerer":(99,104),
             "Warlock":(105,111),
             "Wizard":(112,119)}

background_pages={
                 "Acolyte":(127,127),
                 "Charlatan":(128,128),
                 "Criminal":(129,130),
                 "Entertainer":(130,131),
                 "FolkHero": (131,132),
                 "GuildArtisan": (132, 133),
                 "Hermit": (134, 135),
                 "Noble": (135, 136),
                 "Outlander": (136, 137),
                 "Sage": (137, 138),
                 "Sailor": (139,139),
                 "Soldier": (140,141),
                 "Urchin": (141, 141)
                 }

def save_pages(a, b, playername, filename):
    #save a slice of pdf from page a through b to filename.pdf in the playername
    #directory
    output = PdfFileWriter()
    input1 = PdfFileReader(open("phb.pdf", "rb"))
    for i in range(a, b+1):
        output.addPage(input1.getPage(i))

    outputStream = open(playername +"/"+filename + ".pdf", "wb")
    output.write(outputStream)


def save_race(race, playername):
    race_tuple= race_pages[race]
    save_pages(race_tuple[0], race_tuple[1], playername, race)

def save_class(dndclass, playername):
    class_tuple= class_pages[dndclass]
    save_pages(class_tuple[0], class_tuple[1], playername, dndclass)

def save_background(background, playername):
    back_tuple = background_pages[background]
    save_pages(back_tuple[0], back_tuple[1], playername, background)
