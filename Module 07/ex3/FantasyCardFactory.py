from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power="Dragon") -> CreatureCard:
        return CreatureCard(str(name_or_power), 5, "Rare", 7, 5)

    def create_spell(self, name_or_power="Fireball") -> SpellCard:
        return SpellCard(str(name_or_power), 3, "Common", "damage")

    def create_artifact(self, name_or_power="Mana Ring") -> ArtifactCard:
        return ArtifactCard(str(name_or_power), 2, "Epic", 3, "Add mana")

    def create_themed_deck(self, size: int) -> dict:
        return {"deck_size": size, "theme": "Fantasy"}

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
