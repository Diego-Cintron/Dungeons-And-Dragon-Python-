from PlayerCharacter import PC


class Rogue(PC):

    def __init__(self, name, race, archetype, level, stats):
        super().__init__(name, race, archetype, level, stats)
        self.languages.append("Thieves\' Cant")  # Adds the Rogue language. Fix the "".
        self.features.append("Sneak Attack")

        temp_level = self.level
        self.level = 0
        while self.level < temp_level:  # Add all the things appropriate for their level.
            self.level += 1
            self.level_up(self.level)  # This is not the best way to do this...

    def level_up(self, lvl):  # Currently only applies to Arcane Trickster. Gotta add Thief and Assassin.
        self.level += 1

        if lvl == 2:
            self.features.append("Cunning Action")
        # elif lvl == 3:
        #     self.archetype = "Arcane Trickster"  # This needs stuff added, obviously.
