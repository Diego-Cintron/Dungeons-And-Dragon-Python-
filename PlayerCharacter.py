class PC:

    # Constructor
    def __init__(self, name, race, archetype, level, stats):
        self.name = name
        self.race = race
        self.archetype = archetype
        self.level = level
        self.stats = stats
        self.mods = self.set_modifiers(stats)
        self.proficiency = self.set_proficiency()
        self.languages = self.set_languages(race)
        self.features = []
        self.initiative = self.mods[1]

    # Sets the mods when the PC is created.
    @staticmethod
    def set_modifiers(stats):
        modifiers = [0, 0, 0, 0, 0, 0]
        stat_index = -1
        for stat in stats:
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
        return modifiers

    # Sets the proficiency when the PC is created.
    def set_proficiency(self):
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

    # Sets the stats when the PC is created.
    def set_stats(self, stats):
        self.stats = stats

    # Used for when the PC is created.
    @staticmethod
    def set_languages(race):  # Gotta add the rest of the races
        if race == "Dwarf":
            languages = ['Common', 'Dwarfish']
        elif race == "Elf":
            languages = ['Common', 'Elvish']
        elif race == "Hafling":
            languages = ['Common', 'Goblin']
        # elif race == "Human":
        #     lang = input("Choose a language: ")
        #     languages = ['Common', lang]
        else:
            return ['Common']

        return languages

    # Adds a known language to the PC.
    def add_language(self, language):
        self.languages.append(language)

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

    # Test method
    def introduce_self(self):
        print("My name is " + self.name + ", I am a " + self.race, self.archetype + '.', "I'm level", self.level)
        print("My stats are:", self.stats)
        print("My mods are:", self.mods)
        print("My initiative is:", self.initiative)
        print("My languages are:", self.languages)
        print("My features are:", self.features)
