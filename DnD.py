# D&D Classes and stuff
# from Archetypes import Rogue

# TODO:
#   Make it so you cant repeat skills/skillProficiencies

# TODO:
#   Make it so you can't have stats over 20.
#   Saving Throws & Death Saves
#   Passive Perception
#   Armor Class
#   Alignment
#   Background
#   Race Features
#   Prompt the user for Cantrips/Spells
#   -- Rogue

# DONE:
#   Currently have no way for the Races to affect stats
#   Fix the set_modifiers to apply only after leveling up so as not to have redundant code.
#   Finish the Rogue

#   -- I noticed that when I call the PlayerCharacter and it's child classes, I specify an Archetype but when I make
#   -- the character, I already call the Archetype directly. It's redundant. I would remove it if I'm to later make the
#   -- entire PC creation via asking for inputs, it might be more useful to keep it as is.
#   ^^ To fix this, I suggest making a new method that asks the user for their class and base it off that.
#####################################################################
import Archetypes

Diego = Archetypes.Rogue("Indigo", "Elf (Eladrin, High)", 2, [14, 15, 13, 10, 8, 12])
Diego.introduce_self()
