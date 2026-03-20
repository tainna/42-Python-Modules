
__version__ = "1.0.0"
__author__ = "Master Pythonicus"

# Importa e expõe APENAS fire e water para o nível do pacote
from .elements import create_fire, create_water, create_air, create_earth
__all__ = ["create_fire", "create_water", "create_air", "create_earth"]
# create_earth e create_air NÃO são importados aqui, portanto ficam "ocultos"
