# D&D Classes and stuff
# from Archetypes import Rogue

# TODO:
#   Currently have no way for the Races to affect stats
#   Finish the Rogue
#   -- Expertise
#   Spell Saves
#   HP
#   Speed
#   Saving Throws & Death Saves
#   Passive Perception
#   Armor Class
#   Alignment
#   Background

#   -- I noticed that when I call the PlayerCharacter and it's child classes, I specify an Archetype but when I make
#   -- the character, I already call the Archetype directly. It's redundant. I would remove it if I'm to later make the
#   -- entire PC creation via asking for inputs, it might be more useful to keep it as is.
#####################################################################
import Archetypes

Diego = Archetypes.Rogue("Indigo", "Human", "Rogue", 2, [14, 16, 9, 11, 13, 15])
Diego.introduce_self()
