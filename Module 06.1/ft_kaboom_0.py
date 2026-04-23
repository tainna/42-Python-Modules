from alchemy import grimoire

print("=== Kaboom 0 ===")
print("Using grimoire module directly")

# Testa a magia da luz (não vai dar erro!)
result = grimoire.light_spell_record('Fantasy', 'Earth, wind and fire')
print(f"Testing record light spell: {result}")
