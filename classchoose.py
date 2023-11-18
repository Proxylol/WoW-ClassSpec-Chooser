import tkinter as tk
import random


class CharacterGenerator:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="dark gray")

        self.label_class = tk.Label(root, bg="dark gray", text="Class")
        self.label_class.grid(row=0, column=0, pady=2)

        self.label_spec = tk.Label(root, bg="dark gray", text="Spec")
        self.label_spec.grid(row=2, column=0, pady=2)

        self.button_generate = tk.Button(
            root, text="Choose Class / Spec", command=self.generate_character)
        self.button_generate.grid(row=3, column=0, pady=20)

    def choose_class(self):
        classes = ["Warrior", "Paladin", "Hunter", "Rogue", "Priest", "Death Knight",
                   "Shaman", "Mage", "Warlock", "Monk", "Druid", "Demon Hunter", "Evoker"]
        return random.choice(classes)

    def choose_spec(self, class_choice):
        specs_by_class = {
            "Warrior": ["Protection", "Arms", "Fury"],
            "Paladin": ["Protection", "Holy", "Retribution"],
            "Hunter": ["Marksman", "Beast Mastery", "Survival"],
            "Rogue": ["Assassination", "Subtlety", "Outlaw"],
            "Priest": ["Holy", "Discipline", "Shadow"],
            "Death Knight": ["Unholy", "Frost", "Blood"],
            "Shaman": ["Elemental", "Enhancement", "Restoration"],
            "Mage": ["Fire", "Frost", "Arcane"],
            "Warlock": ["Demonology", "Destruction", "Affliction"],
            "Monk": ["Mistweaver", "Brewmaster", "Windwalker"],
            "Druid": ["Feral", "Balance", "Guardian", "Restoration"],
            "Demon Hunter": ["Havoc", "Vengeance"],
            "Evoker": ["Preservation", "Augmentation", "Destruction"]
        }
        return random.choice(specs_by_class.get(class_choice, []))

    def update_labels(self, class_choice, spec_choice):
        class_color_map = {
            "Warrior": "brown", "Paladin": "pink", "Hunter": "green", "Rogue": "yellow",
            "Priest": "white", "Death Knight": "red", "Shaman": "blue", "Mage": "light blue",
            "Warlock": "purple", "Monk": "light green", "Demon Hunter": "purple", "Evoker": "dark green"
        }

        self.label_class.config(fg=class_color_map.get(
            class_choice, "white"), text=class_choice)
        self.label_spec.config(text=spec_choice)

    def generate_character(self):
        class_choice = self.choose_class()
        spec_choice = self.choose_spec(class_choice)
        self.update_labels(class_choice, spec_choice)


if __name__ == "__main__":
    root = tk.Tk()
    generator = CharacterGenerator(root)
    root.mainloop()
