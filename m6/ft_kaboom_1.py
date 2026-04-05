print("=== Kaboom 1 ===")
print("Access to dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

try:
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print(dark_spell_record("Nightmare", "bats and fog"))
except ImportError:
    raise
