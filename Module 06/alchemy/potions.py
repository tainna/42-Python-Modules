from .elements import create_fire, create_water, create_earth, create_air


def healing_potion():
    """Brews a healing potion using fire and water."""
    fire = create_fire()
    water = create_water()
    return f"Healing potion brewed with {fire} and {water}"


def strength_potion():
    """Brews a strength potion using earth and fire."""
    earth = create_earth()
    fire = create_fire()
    return f"Strength potion brewed with {earth} and {fire}"


def invisibility_potion():
    """Brews an invisibility potion using air and water."""
    air = create_air()
    water = create_water()
    return f"Invisibility potion brewed with {air} and {water}"


def wisdom_potion():
    """Brews a wisdom potion using all four elements."""
    fire = create_fire()
    water = create_water()
    earth = create_earth()
    air = create_air()
    return (f"Wisdom potion brewed with all elements: "
            f"{fire}, {water}, {earth}, {air}")
