import alchemy.elements
import alchemy


def ft_sacred_scroll():
    print("=== Sacred Scroll Mastery ===")

    # Testando acesso direto ao módulo (tudo deve funcionar)
    print("\nTesting direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water(): {alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

    # Testando acesso ao nível do pacote (controlado pelo __init__.py)
    print("\nTesting package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")

    # Estas devem falhar e gerar AttributeError
    try:
        alchemy.create_earth()
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        alchemy.create_air()
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    # Metadados do pacote
    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    ft_sacred_scroll()
