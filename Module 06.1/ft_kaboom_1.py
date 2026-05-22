print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now THIS WILL RAISE AN UNCAUGHT EXCEPTION")

# forcing an ImportError (circular import)
from alchemy.grimoire.dark_spellbook import dark_spell_record

print(dark_spell_record('Curse', 'bats and eyeball'))
