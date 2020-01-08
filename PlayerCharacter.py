class PC:

    # Constructor
    def __init__(self, name, race, archetype, level, stats):
        self.name = name
        self.level = level
        self.race = race
        self.stats = stats
        self.languages = []
        self.mods = []
        self.set_raceDetails()  # Adds the race modifiers and languages.
        self.archetype = archetype
        self.proficiencyBonus = self.set_proficiencyBonus()
        self.skills = []
        self.skillProficiencies = {}
        self.features = []
        self.speed = 30  # Most common speed. Any class that changes this will simply change it during initialization.
        self.maxHealth = 3

        # Default Magic
        self.canCast = False
        self.spellcastingAbility = ''
        self.spellLevel = 0  # Max spell level
        self.spellSlots = {}  # Dictionary cuz different levels have different amount of slots
        self.knownCantrips = 0
        self.knownSpells = 0
        self.cantrips = []
        self.spells = []

    # Sets the mods for the PC. To be used after the Ability Score Improvements.
    def set_modifiers(self):
        modifiers = [0, 0, 0, 0, 0, 0]
        stat_index = -1
        for stat in self.stats:
            stat_index += 1
            if stat == 0 or stat == 1:
                modifiers[stat_index] = -5
            elif stat == 2 or stat == 3:
                modifiers[stat_index] = -4
            elif stat == 4 or stat == 5:
                modifiers[stat_index] = -3
            elif stat == 6 or stat == 7:
                modifiers[stat_index] = -2
            elif stat == 8 or stat == 9:
                modifiers[stat_index] = -1
            elif stat == 10 or stat == 11:
                modifiers[stat_index] = 0
            elif stat == 12 or stat == 13:
                modifiers[stat_index] = 1
            elif stat == 14 or stat == 15:
                modifiers[stat_index] = 2
            elif stat == 16 or stat == 17:
                modifiers[stat_index] = 3
            elif stat == 18 or stat == 19:
                modifiers[stat_index] = 4
            elif stat == 20 or stat == 21:
                modifiers[stat_index] = 5
            elif stat == 22 or stat == 23:
                modifiers[stat_index] = 6
            elif stat == 24 or stat == 25:
                modifiers[stat_index] = 7
            elif stat == 26 or stat == 27:
                modifiers[stat_index] = 8
            elif stat == 28 or stat == 29:
                modifiers[stat_index] = 9
            else:
                modifiers[stat_index] = 10
        self.mods = modifiers

    # Sets the proficiency when the PC is created.
    def set_proficiencyBonus(self):
        if self.level < 5:
            return 2
        elif self.level < 9:
            return 3
        elif self.level < 13:
            return 4
        elif self.level < 17:
            return 5
        else:
            return 6

    # Sets the PC's languages and race bonuses (Not counting features). Used for when the PC is created.
    def set_raceDetails(self):
        for x in range(6):  # Sets all the mods to 0 by default so I only have to add the ones that actually change.
            self.mods.append(0)

        if self.race == "Dwarf (Hill)":
            self.languages = ['Common', 'Dwarvish']
            self.stats[2] += 2
            self.stats[4] += 1
        elif self.race == "Dwarf (Mountain)":
            self.languages = ['Common', 'Dwarvish']
            self.stats[0] += 2
            self.stats[2] += 2
        elif self.race == "Dragonborn":
            self.languages = ['Common', 'Draconic']
            self.stats[0] += 2
            self.stats[5] += 1
        elif self.race == "Elf (Drow)":
            self.languages = ['Common', 'Elvish']
            self.stats[1] += 2
            self.stats[5] += 1
        elif self.race == "Elf (Eladrin, High)":
            lang = input("Choose an extra language: ")
            self.languages = ['Common', 'Elvish', lang]
            self.stats[1] += 2
            self.stats[3] += 1
        elif self.race == "Elf (Wood)":
            self.languages = ['Common', 'Elvish']
            self.stats[1] += 2
            self.stats[4] += 1
        elif self.race == "Gnome (Deep, Forest)":
            self.languages = ['Common', 'Gnomish']
            self.stats[1] += 1
            self.stats[3] += 2
        elif self.race == "Gnome (Rock)":
            self.languages = ['Common', 'Gnomish']
            self.stats[2] += 1
            self.stats[3] += 2
        elif self.race == "Halfling (Lightfoot)":
            self.languages = ['Common', 'Halfling']
            self.stats[1] += 2
            self.stats[5] += 1
        elif self.race == "Halfling (Stout)":
            self.languages = ['Common', 'Halfling']
            self.stats[1] += 2
            self.stats[2] += 1
        elif self.race == "Half-Elf":
            lang = input("Choose an extra language: ")
            self.languages = ['Common', 'Elvish', lang]
            self.stats[5] += 2
            # Also something else I don't understand :P
        elif self.race == "Half-Orc":
            self.languages = ['Common', 'Orc']
            self.stats[0] += 2
            self.stats[2] += 1
        elif self.race == "Human":
            lang = input("Choose an extra language: ")
            self.languages = ['Common', lang]
            for x in range(6):
                self.stats[x] += 1
        elif self.race == "Tiefling":
            self.languages = ['Common', 'Infernal']
            self.stats[3] += 1
            self.stats[5] += 2
        else:
            return ['Common']

    # Adds a known language to the PC. Not the most useful method since it doesn't really save any lines.
    def add_language(self, language):
        self.languages.append(language)

    # Chooses the skills during the Archetype initialization since it depends on the class.
    def chooseSkills(self, profs):
        for x in range(0, profs):
            while True:
                skill = input("Choose four from (A) Acrobatics, (B) Athletics, (C) Deception, (D) Insight, "
                              "(E) Intimidation, (F) Investigation, (G) Perception, (H) Performance, (I) Persuasion, "
                              "(J) Sleight of Hand, and (K) Stealth\n")
                if skill in ('A', 'a'):
                    self.skills.append("Acrobatics")
                    break
                elif skill in ('B', 'b'):
                    self.skills.append("Athletics")
                    break
                elif skill in ('C', 'c'):
                    self.skills.append("Deception")
                    break
                elif skill in ('D', 'd'):
                    self.skills.append("Insight")
                    break
                elif skill in ('E', 'e'):
                    self.skills.append("Intimidation")
                    break
                elif skill in ('F', 'f'):
                    self.skills.append("Investigation")
                    break
                elif skill in ('G', 'g'):
                    self.skills.append("Perception")
                    break
                elif skill in ('H', 'h'):
                    self.skills.append("Performance")
                    break
                elif skill in ('I', 'i'):
                    self.skills.append("Persuasion")
                    break
                elif skill in ('J', 'j'):
                    self.skills.append("Sleight of Hand")
                    break
                elif skill in ('K', 'k'):
                    self.skills.append("Stealth")
                    break
                else:
                    print("Invalid Answer.")

    # After the skills are chosen, this edits the self.skillProficiencies to be a dict of the Skills' Modifier
    def set_skillProficiencies(self):
        for skill in self.skills:
            if skill == 'Athletics':
                self.skillProficiencies[skill] = self.mods[0] + self.proficiencyBonus
            elif skill in ('Acrobatics', 'Sleight of Hand', 'Stealth'):
                self.skillProficiencies[skill] = self.mods[1] + self.proficiencyBonus
            elif skill in ('Arcana', 'History', 'Investigation', 'Nature', 'Religion'):
                self.skillProficiencies[skill] = self.mods[3] + self.proficiencyBonus
            elif skill in ('Animal Handling', 'Insight', 'Medicine', 'Perception', 'Survival'):
                self.skillProficiencies[skill] = self.mods[4] + self.proficiencyBonus
            elif skill in ('Deception', 'Intimidation', 'Performance', 'Persuasion'):
                self.skillProficiencies[skill] = self.mods[5] + self.proficiencyBonus

    # To be used in specific levels to increase stats.
    def ability_score_improvement(self):
        decision = ''
        while decision not in ('A', 'a', 'B', 'b'):
            decision = input(
                "Ability Score Improvement!\n(A) Increase one stat by 2\t(B) Increase two stats by 1\n")
        if decision in ('A', 'a'):
            stat = -1
            while stat not in (0, 1, 2, 3, 4, 5):
                stat = int(input("Choose a stat to upgrade! (Choose a number)\n(0)Strength\n(1)Dexterity\n"
                                 "(2)Constitution\n(3)Wisdom\n(4)Intelligence\n(5)Charisma\n"))
            self.stats[stat] += 2
        else:
            stat = -1
            while stat not in (0, 1, 2, 3, 4, 5):
                stat = int(input("Choose the first stat to upgrade! (Choose a number)\n(0)Strength\n(1)Dexterity\n"
                                 "(2)Constitution\n(3)Wisdom\n(4)Intelligence\n(5)Charisma\n"))
            self.stats[stat] += 1
            stat = -1
            while stat not in (0, 1, 2, 3, 4, 5):
                stat = int(input("Choose the second stat to upgrade! (Choose a number)\n(0)Strength\n(1)Dexterity\n"
                                 "(2)Constitution\n(3)Wisdom\n(4)Intelligence\n(5)Charisma\n"))
            self.stats[stat] += 1

    def set_maxHealth(self):
        self.maxHealth += 5 + self.mods[2]

    # Test method
    def introduce_self(self):
        print("My name is " + self.name + ", I am a " + self.race, self.archetype + '.', "I'm level", self.level)
        print("My stats are:", self.stats)
        print("My mods are:", self.mods)
        print("My Health is:", self.maxHealth, "| My initiative is:", self.initiative)
        print("My languages are:", self.languages)
        print("My skills are:", self.skills)
        print("My skill proficiencies are:", self.skillProficiencies)
        print("My features are:", self.features)
        if self.canCast:
            print("\nMy spellcasting ability is:", self.spellcastingAbility)
            print("I can know", self.knownCantrips, "cantrips.")
            print("I can know", self.knownSpells, "spells.")
            print("Spell slots:", self.spellSlots)
