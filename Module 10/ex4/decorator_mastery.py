import time
from typing import Callable
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    """Decorator that measures and prints a function's execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator factory to validate power levels before casting."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Attempt to extract 'power' from kwargs
            # otherwise assume it's the last positional argument
            power = kwargs.get('power')
            if power is None and args:
                power = args[-1]

            # Validate the extracted power
            if isinstance(power, (int, float)) and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator factory that retries a failed spell up to max_attempts."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying...\
                              (attempt {attempt}/{max_attempts})")
                    else:
                        return f"Spell casting failed\
                            after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Checks if a name is at least 3
        characters and contains only letters/spaces."""
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Casts a spell if the power validator allows it."""
        return f"Successfully cast {spell_name} with {power} power"


# Testing Block (Matches Expected Output)

if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.101)
        return "Fireball cast!"

    print(f"Result: {fireball()}\n")

    print("Testing retrying spell...")

    @retry_spell(max_attempts=3)
    def fail_spell():
        raise ValueError("Oops")

    # Simulating a spell that succeeds on the 3rd try
    waagh_attempts = 0

    @retry_spell(max_attempts=3)
    def waagh_spell():
        global waagh_attempts
        waagh_attempts += 1
        if waagh_attempts < 3:
            raise ValueError("Fizzle")
        return "Waaaaaaagh spelled !"

    print(fail_spell())
    print(waagh_spell(), "\n")

    print("Testing MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Merlin"))  # True
    print(MageGuild.validate_mage_name("M1"))      # False
    print(guild.cast_spell("Lightning", 15))       # Valid
    print(guild.cast_spell("Lightning", 5))        # Invalid
