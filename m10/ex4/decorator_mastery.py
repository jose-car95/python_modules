from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


@spell_timer
def fireball() -> str:
    time.sleep(0.101)
    return "Fireball cast!"


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
                    else:
                        return (
                            f"Spell casting failed after "
                            f"{max_attempts} attempts"
                        )
        return wrapper
    return decorator


def create_unstable_success_spell() -> Callable[[], str]:
    attempts: int = 0

    @retry_spell(3)
    def unstable() -> str:
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise ValueError("Spell exploded")
        return "Waaaaaaagh spelled !"
    return unstable


@retry_spell(3)
def unstable_spell() -> str:
    raise ValueError("Spell exploded")


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if "power" in kwargs:
                power = kwargs["power"]
            elif len(args) >= 1 and isinstance(args[0], int):
                power = args[0]
            elif len(args) >= 3 and isinstance(args[2], int):
                power = args[2]
            else:
                return "Insufficient power for this spell"
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


@power_validator(10)
def channel_spell(power: int, spell_name: str) -> str:
    return f"{spell_name} cast with {power} power"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name) >= 3 and all(
                char.isalpha() or char.isspace() for char in name
            )
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retrying spell failure...")
    unstable = unstable_spell()
    print(unstable)
    print("\nTesting retrying spell success...")
    unstable_success = create_unstable_success_spell()
    print(unstable_success())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("A1"))

    guild: MageGuild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))

    print("\nTesting power validator with standalone function...")
    print(channel_spell(12, "Lightning"))
    print(channel_spell(5, "Lightning"))
    print(channel_spell(power=20, spell_name="Frost Nova"))
    print(channel_spell(power=3, spell_name="Frost Nova"))


if __name__ == "__main__":
    main()
