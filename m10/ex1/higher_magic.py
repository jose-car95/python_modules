from collections.abc import Callable


Spell = Callable[[str, int], str]
Condition = Callable[[str, int], bool]
CombinedSpell = Callable[[str, int], tuple[str, str]]
SequenceSpell = Callable[[str, int], list[str]]


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def enough_power(target: str, power: int) -> bool:
    return power >= 20


def spell_combiner(
    spell1: Spell,
    spell2: Spell
) -> CombinedSpell:
    def combined(target: str, power: int) -> tuple[str, str]:
        result1: str = spell1(target, power)
        result2: str = spell2(target, power)
        return (result1, result2)
    return combined


def power_amplifier(
    base_spell: Spell,
    multiplier: int
) -> Spell:
    def amplified(target: str, power: int) -> str:
        new_power: int = power * multiplier
        return base_spell(target, new_power)
    return amplified


def conditional_caster(
    condition: Condition,
    spell: Spell
) -> Spell:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(
    spells: list[Spell]
) -> SequenceSpell:
    def sequence(target: str, power: int) -> list[str]:
        result: list[str] = []
        for spell in spells:
            result.append(spell(target, power))
        return result
    return sequence


def main() -> None:
    print("\nTesting spell combiner...")
    combined_spell: CombinedSpell = spell_combiner(fireball, heal)
    result1: str
    result2: str
    result1, result2 = combined_spell('Dragon', 10)
    print(f"Combined spell result: {result1}, {result2}")

    print("\nTesting power amplifier...")
    mega_fireball: Spell = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 10)}")
    print(f"Amplified: {mega_fireball('Dragon', 10)}")

    print("\nTesting conditional caster...")
    safe_fireball: Spell = conditional_caster(enough_power, fireball)
    print(safe_fireball('Dragon', 10))
    print(safe_fireball('Dragon', 30))

    print("\nTesting spell sequence...")
    spell_combo: SequenceSpell = spell_sequence([fireball, heal])
    results: list[str] = spell_combo('Dragon', 10)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
