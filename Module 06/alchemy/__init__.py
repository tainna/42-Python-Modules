__version__ = "1.0.0"
__author__ = "Master Pythonicus"

"""Import and expose fire, water, and air to the package level.
create_air must be exposed for ft_alembic_4.py to work."""
from .elements import create_fire, create_water, create_air

__all__ = ["create_fire", "create_water", "create_air"]

"""
create_earth is intentionally NOT imported here.
Therefore, it remains "hidden" at the package level
and will raise an AttributeError if accessed directly
via alchemy.create_earth
"""
