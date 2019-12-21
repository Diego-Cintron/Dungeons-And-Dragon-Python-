from PlayerCharacter import PC


class Rogue(PC):

    def __init__(self, name, race, archetype, level, stats):
        super().__init__(name, race, archetype, level, stats)
        self.add_language("Thieves\' Cant")  # Adds the Rogue language. Fix the "".
        self.features.append("Sneak Attack (1d6)")

        # Skill Proficiencies for Rogue
        self.setSkillProficiencies(4)

        # Add all the things appropriate for their level.
        temp_level = self.level
        self.level = 0
        while self.level < temp_level:
            self.level_up()  # This is not the best way to do this...

        # At the end, gotta prompt the user to add their spells/cantrips

    def increaseSneakAttackBonus(self):
        if self.level == 3:
            bonus = "(1d6)"
            new_bonus = "(2d6)"
        elif self.level == 5:
            bonus = "(2d6)"
            new_bonus = "(3d6)"
        elif self.level == 7:
            bonus = "(3d6)"
            new_bonus = "(4d6)"
        elif self.level == 9:
            bonus = "(4d6)"
            new_bonus = "(5d6)"
        elif self.level == 11:
            bonus = "(5d6)"
            new_bonus = "(6d6)"
        elif self.level == 13:
            bonus = "(6d6)"
            new_bonus = "(7d6)"
        elif self.level == 15:
            bonus = "(7d6)"
            new_bonus = "(8d6)"
        elif self.level == 17:
            bonus = "(8d6)"
            new_bonus = "(9d6)"
        else:
            bonus = "(9d6)"
            new_bonus = "(10d6)"
        pos = 0
        while self.features[pos] != ("Sneak Attack " + bonus):
            pos += 1
        self.features[pos] = "Sneak Attack " + new_bonus

    # Adds Features and stuff based on their level
    def level_up(self):  # Missing "Expertise" and Third level archetype stuff
        self.level += 1

        if self.level == 2:
            self.features.append("Cunning Action")
        elif self.level == 3:  # Chooses their Archetype at Third level and adds their stuff.
            self.increaseSneakAttackBonus()

            arch = ''
            while arch not in ('A', 'a', 'B', 'b', 'C', 'c'):
                arch = input("Choose an Archetype:\n(A) Thief\t(B) Assassin\t(C) Arcane Trickster\n")
            if arch in ('A', 'a'):
                self.archetype = "Thief"
                self.features.append("Fast Hands")
                self.features.append("Second-Story Work")
            elif arch in ('B', 'b'):
                self.archetype = "Assassin"
                self.features.append("Bonus Proficiencies")  # Should maybe add to the proficiencies
                self.features.append("Assassinate")
            else:
                self.archetype = "Arcane Trickster"
                self.canCast = True
                self.spellcastingAbility = "Intelligence"
                self.spellLevel = 1
                self.spellSlots[1] = 2
                self.knownCantrips = 3
                self.knownSpells = 3
                self.cantrips.append("Mage Hand Legerdemain")
        elif self.level == 4:
            self.ability_score_improvement()
            if self.archetype == "Arcane Trickster":
                self.spellSlots[1] = 3
                self.knownSpells = 4
        elif self.level == 5:
            self.increaseSneakAttackBonus()
            self.features.append("Uncanny Dodge")
        # elif self.level == 6:
            #  Add another "Expertise"... But I never added the first level one
        elif self.level == 7:
            self.increaseSneakAttackBonus()
            self.features.append("Evasion")
            if self.archetype == "Arcane Trickster":
                self.spellLevel = 2
                self.spellSlots[1] = 4
                self.spellSlots[2] = 2
                self.knownSpells = 5
        elif self.level == 8:
            self.ability_score_improvement()
            if self.archetype == "Arcane Trickster":
                self.knownSpells = 6
        elif self.level == 9:
            self.increaseSneakAttackBonus()
            if self.archetype == "Thief":
                self.features.append("Supreme Sneak")
            elif self.archetype == "Assassin":
                self.features.append("Infiltration Expertise")
            else:
                self.features.append("Magical Ambush")
        elif self.level == 10:
            self.ability_score_improvement()
            if self.archetype == "Arcane Trickster":
                self.knownCantrips = 4
                self.knownSpells = 7
                self.spellSlots[2] = 3
        elif self.level == 11:
            self.increaseSneakAttackBonus()
            self.features.append("Reliable Talent")
            if self.archetype == "Arcane Trickster":
                self.knownSpells = 8
        elif self.level == 12:
            self.ability_score_improvement()
        elif self.level == 13:
            self.increaseSneakAttackBonus()
            if self.archetype == "Thief":
                self.features.append("Use Magic Devise")
            elif self.archetype == "Assassin":
                self.features.append("Impostor")
            else:
                self.features.append("Versatile Trickster")
                self.spellLevel = 3
                self.knownSpells = 9
                self.spellSlots[3] = 2
        elif self.level == 14:
            self.features.append("Blindsense")
            if self.archetype == "Arcane Trickster":
                self.knownSpells = 10
        elif self.level == 15:
            self.increaseSneakAttackBonus()
            self.features.append("Slippery Mind")
        elif self.level == 16:
            self.ability_score_improvement()
            if self.archetype == "Arcane Trickster":
                self.knownSpells = 11
                self.spellSlots[3] = 3
        elif self.level == 17:
            self.increaseSneakAttackBonus()
            if self.archetype == "Thief":
                self.features.append("Thief\'s Reflexes")
            elif self.archetype == "Assassin":
                self.features.append("Death Strike")
            else:
                self.features.append("Spell Thief")
        elif self.level == 18:
            self.features.append("Elusive")
        elif self.level == 19:
            self.increaseSneakAttackBonus()
            self.ability_score_improvement()
            if self.archetype == "Arcane Trickster":
                self.knownSpells = 12
                self.spellLevel = 4
                self.spellSlots[4] = 1
        elif self.level == 20:
            self.features.append("Stroke of Luck")
            if self.archetype == "Arcane Trickster":
                self.knownSpells = 13
        # This needs stuff added, obviously.
