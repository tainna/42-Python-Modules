import time
from typing import Generator


def generator(total_events: int) -> Generator[dict, None, None]:
    """
    This function
    """
    players = ["alice", "bob", "charlie"]
    actions = ["killed_monster", "found_treasure", "leveled_up"]
    for i in range(total_events):
        (event) = {
            "player": players[i % len(players)],
            "level": (i % 20) + 1,
            "action": actions[i % len(actions)]
        }
        yield (event)


def Analyses_processor() -> None:
    print("=== Game Data Stream Processor ===")
    print("\nProcessing 1000 game events...\n")

    stream = generator(1000)

    total_events = 0
    high_level = 0
    level_up = 0
    treasure = 0

    start_time = time.time()

    for event in stream:
        total_events += 1

        if total_events <= 3:
            print(
                f"Event {total_events}: Player {event['player']} (level "
                f"{event['level']}) {event['action']}"
            )
        elif total_events == 4:
            print("...")

        if event['level'] >= 10:
            high_level += 1
        if event['action'] == "found_treasure":
            treasure += 1
        if event['action'] >= "leveled_up":
            level_up += 1

    end_time = time.time()
    processing_time = end_time - start_time

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")

    print("\nMemory Usage: Constant (streaming)")
    print(f"Processing time: {processing_time:.3f} seconds")


def fibonacci(limit: int) -> Generator[int, None, None]:
    a = 0
    b = 1

    for _ in range(limit):
        yield (a)
        a, b = b, a + b
        """
        explica ou refaz
        """


def prime_gen(limit: int) -> Generator[int, None, None]:
    count = 0
    numero_atual = 2

    while count < limit:
        is_prime = True
        for divisor in range(2, numero_atual):
            if numero_atual % divisor == 0:
                is_prime = False
                break

        if is_prime:
            yield numero_atual
            count += 1

        numero_atual += 1


if __name__ == "__main__":
    Analyses_processor()

    print("\n=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10): ", end="")
    fib = fibonacci(10)

    for i in range(10):
        numero = next(fib)

        if i == 9:
            print(numero)
        else:
            print(f"{numero}, ", end="")

    print("Prime numbers (first 5): ", end="")
    primos = prime_gen(5)

    for i in range(5):
        numero = next(primos)
        if i == 4:
            print(numero)
        else:
            print(f"{numero}, ", end="")
