from elements import create_fire, create_water
from .elements import create_earth, create_air


def healing_potion() -> str:
    return (
        f"Healing potion brewed "
        f"with '{create_earth()}' and '{create_air()}'"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed "
        f"with '{create_fire()}' and '{create_water()}'"
    )
