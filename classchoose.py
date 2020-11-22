from tkinter import *
import random

def classPick():
    classRNG = random.randint(1,12)
    if classRNG == 1:
        choice = "Warrior"
    elif classRNG == 2:
        choice = "Paladin"
    elif classRNG == 3:
        choice = "Hunter"
    elif classRNG == 4:
        choice = "Rogue"
    elif classRNG == 5:
        choice = "Priest"
    elif classRNG == 6:
        choice = "Death Knight"
    elif classRNG == 7:
        choice = "Shaman"
    elif classRNG == 8:
        choice = "Mage"
    elif classRNG == 9:
        choice = "Warlock"
    elif classRNG == 10:
        choice = "Monk"
    elif classRNG == 11:
        choice = "Druid"
    elif classRNG == 12:
        choice = "Demon Hunter"
    return choice

def spec(choice):

    classChoice = choice

    if classChoice == "Warrior":
        specRNG = random.randint(1,3)
        if specRNG == 1:
            specChoice = "Protection"
        elif specRNG == 2:
            specChoice = "Arms"
        elif specRNG == 3:
            specChoice = "Fury"
    elif classChoice == "Paladin":
        specRNG = random.randint(1,3)
        if specRNG == 1:
            specChoice = "Protection"
        elif specRNG == 2:
            specChoice = "Holy"
        elif specRNG ==3:
            specChoice = "Retribution"
    elif classChoice == "Hunter":
        specRNG = random.randint(1,3)
        if specRNG == 1:
            specChoice = "Marksman"
        if specRNG == 2:
            specChoice = "Beast Mastery"
        if specRNG == 3:
            specChoice = "Survival"
    elif classChoice == "Rogue":
        specRNG = random.randint(1,3)
        if specRNG == 1:
            specChoice = "Assassination"
        if specRNG == 2:
            specChoice = "Subtlety"
        if specRNG == 3:
            specChoice = "Outlaw"
    elif classChoice == "Priest":
        specRNG = random.randint(1,3)
        if specRNG == 1:
            specChoice = "Holy"
        if specRNG == 2:
            specChoice = "Discipline"
        if specRNG == 3:
            specChoice = "Shadow"
    elif classChoice == "Death Knight":
        specRNG = random.randint(1,3)
        if specRNG == 1:
            specChoice = "Unholy"
        if specRNG == 2:
            specChoice = "Frost"
        if specRNG == 3:
            specChoice = "Blood"
    elif classChoice == "Shaman":
        specRNG = random.randint(1,3)
        if specRNG == 1:
            specChoice = "Elemental"
        if specRNG == 2:
            specChoice = "Enhancement"
        if specRNG == 3:
            specChoice = "Restoration"
    elif classChoice == "Mage":
        specRNG = random.randint(1,3)
        if specRNG == 1:
            specChoice = "Fire"
        if specRNG == 2:
            specChoice = "Frost"
        if specRNG == 3:
            specChoice = "Arcane"
    elif classChoice == "Warlock":
        specRNG = random.randint(1,3)
        if specRNG == 1:
            specChoice = "Demonology"
        if specRNG == 2:
            specChoice = "Destruction"
        if specRNG == 3:
            specChoice = "Affliction"
    elif classChoice == "Monk":
        specRNG = random.randint(1,3)
        if specRNG == 1:
            specChoice = "Mistweaver"
        if specRNG == 2:
            specChoice = "Brewmaster"
        if specRNG == 3:
            specChoice = "Windwalker"
    elif classChoice == "Druid":
        specRNG = random.randint(1,4)
        if specRNG == 1:
            specChoice = "Feral"
        if specRNG == 2:
            specChoice = "Balance"
        if specRNG == 3:
            specChoice = "Guardian"
        if specRNG == 4:
            specChoice = "Restoration"
    elif classChoice == "Demon Hunter":
        specRNG = random.randint(1,2)
        if specRNG == 1:
            specChoice = "Havoc"
        if specRNG == 2:
            specChoice = "Vengeance"
    return specChoice
      

def specandclass():
    classChoice = classPick()
    if classChoice == "Warrior":
        labelClass.config(fg="brown", bg="dark gray", text=classChoice)
    elif classChoice == "Paladin":
        labelClass.config(fg="pink", bg="dark gray", text=classChoice)
    elif classChoice == "Hunter":
        labelClass.config(fg="green", bg="dark gray", text=classChoice)
    elif classChoice == "Rogue":
        labelClass.config(fg="yellow", bg="dark gray", text=classChoice)
    elif classChoice == "Priest":
        labelClass.config(fg="white", bg="dark gray", text=classChoice)
    elif classChoice == "Death Knight":
        labelClass.config(fg="red", bg="dark gray", text=classChoice)
    elif classChoice == "Shaman":
        labelClass.config(fg="blue", bg="dark gray", text=classChoice)
    elif classChoice == "Mage":
        labelClass.config(fg="light blue", bg="dark gray", text=classChoice)
    elif classChoice == "Warlock":
        labelClass.config(fg="purple", bg="dark gray", text=classChoice)
    elif classChoice == "Monk":
        labelClass.config(fg="light green", bg="dark gray", text=classChoice)
    elif classChoice == "Demon Hunter":
        labelClass.config(fg="purple", bg="dark gray", text=classChoice)
    labelClass.config(text=classChoice)
    specChoice = spec(classChoice)
    labelSpec.config(text=specChoice)


root = Tk()

root.configure(bg="dark gray")
labelClass = Label(root, bg="dark gray", text="Class")
labelClass.grid(row = 0, column = 0, pady = 2)
labelSpec = Label(root, bg="dark gray", text="Spec")
labelSpec.grid(row = 2, column = 0, pady = 2)
b = Button(root, text="Choose Class / Spec", command=specandclass)
b.grid(row = 3, column = 0, pady = 20)

mainloop()
