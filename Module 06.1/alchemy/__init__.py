__version__ = "1.0.0"
__author__ = "Eu oii"

"""Import and expose fire, water, and air to the package level.
create_air must be exposed for ft_alembic_4.py to work."""
from .elements import create_air
from .potions import strength_potion, healing_potion as heal
from . import transmutation
from . import grimoire

__all__ = ["create_air", "strength_potion", "heal",
           "transmutation", "grimoire"]

"""
create_earth is intentionally NOT imported here.
Therefore, it remains "hidden" at the package level
and will raise an AttributeError if accessed directly
via alchemy.create_earth
"""
