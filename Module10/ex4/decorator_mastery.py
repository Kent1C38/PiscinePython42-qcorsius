from typing import Callable, Any
import functools
import time
import inspect


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")

        start = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - start

        print(f"Spell completed in {elapsed}s")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)

            power = bound.arguments.get("power", 0)
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            while attempt < max_attempts:
                attempt += 1
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying..." +
                          f"(attempt {attempt}/{max_attempts})")
                time.sleep(0.5)
            print(f"Spell cating failed after {max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    @spell_timer
    def fireball() -> str:
        time.sleep(1)
        return "FIREEEEEEEEEEEEEEEEEEEBAAAAAAALLL"
    print("="*5 + "Timer demo" + "="*5)
    print(fireball())

    @power_validator(15)
    def create_spell(name: str, power: int) -> str:
        return f"Spell {name} (power {power}) created!"

    print("\n" + "="*5 + "Power Validator demo" + "="*5)
    print(create_spell("Ice Spike", 20))
    print(create_spell("Shit Throwing", 0))

    @retry_spell(5)
    def spell_creation() -> None:
        raise Exception("Et pourquoi pas ?")

    print("\n" + "="*5 + "Retry demo")
    spell_creation()

    print("\n" + "="*5 + "Mage Guild class demo" + "="*5)
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Zeuby Le Magicien"))
    print(MageGuild.validate_mage_name("Ah48631"))
    print(guild.cast_spell("Fireball", 15))
    print(guild.cast_spell("Lightning Bolt", 5))
