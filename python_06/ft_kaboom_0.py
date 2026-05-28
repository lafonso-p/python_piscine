"""Module for testing light magic spells."""

import alchemy.grimoire

print("=== Kaboom 0 ===")
print("Using grimoire module directly")
print(
    "Testing record light spell: "
    f"{alchemy.grimoire.light_spell_record('Fantasy', 'Earth, wind and fire')}"
)
