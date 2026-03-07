from typing import Set


def ft_achievement_tracker() -> None:
    """
    Analyzes player achievements using set operations.
    Demonstrates data deduplication and the use of union,
    intersection, and difference to find common and unique items.
    """
    print("=== Achievement Tracker System ===\n")

    """ Initializes player profiles using the set() function """
    alice: Set[str] = set(['first_kill', 'level_10', 'treasure_hunter',
                           'speed_demon'])
    bob: Set[str] = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
    charlie: Set[str] = set([
        'level_10', 'treasure_hunter', 'boss_slayer',
        'speed_demon', 'perfectionist'
    ])

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    """ Combines all sets to find the total unique achievements in the game """
    all_total: Set[str] = alice.union(bob, charlie)
    total: int = len(all_total)

    print(f"All unique achievements: {all_total}")
    print(f"Total unique achievements: {total}")

    """ Finds the specific achievements that every single player unlocked """
    common: Set[str] = bob.intersection(alice, charlie)
    print(f"\nCommon to all players: {common}")

    """ Calculates pairwise intersections to find any shared achievements """
    alice_bob: Set[str] = alice.intersection(bob)
    bob_charlie: Set[str] = bob.intersection(charlie)
    charlie_alice: Set[str] = charlie.intersection(alice)

    """ Determines what Alice has that Bob lacks, and vice versa """
    alice_unique: Set[str] = alice.difference(bob)
    bob_unique: Set[str] = bob.difference(alice)

    """
    Isolates achievements held by exactly one player by subtracting
    the pool of all shared achievements from the total game pool.
    """
    all_shared: Set[str] = alice_bob.union(bob_charlie, charlie_alice)
    rare: Set[str] = all_total.difference(all_shared)

    print(f"Rare achievements (1 player): {rare}")

    print(f"\nAlice vs Bob common: {alice_bob}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    ft_achievement_tracker()
