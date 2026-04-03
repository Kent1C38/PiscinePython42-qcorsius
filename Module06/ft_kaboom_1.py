
if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Testing import - THIS WILL RAISE AN UNCAUGHT ERROR INTENTIONNALLY")

    import alchemy.grimoire.dark_spellbook
    alchemy.grimoire.dark_spellbook.dark_spell_record('avdakedavra', 'bats')
