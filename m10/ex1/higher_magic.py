from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def enough_power(target: str, power: int) -> bool:
    return power >= 20


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """fabrica un función -> Crear la herramienta"""
    def combined(target: str, power: int) -> tuple[str, str]:
        """ejecuta la lógica real -> Usar la herramienta"""
        result1: str = spell1(target, power)
        result2: str = spell2(target, power)
        return (result1, result2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        new_power: int = power * multiplier
        return base_spell(target, new_power)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable: ...


def main() -> None:
    combined_spell = spell_combiner(fireball, heal)
    print(combined_spell("Dragon", 10))

    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball("Dragon", 10))


if __name__ == "__main__":
    main()
