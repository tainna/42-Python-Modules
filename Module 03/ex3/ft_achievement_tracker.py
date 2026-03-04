

def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}
    """
    alice = set(['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'])
    bob = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
    """
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    all_total = alice.union(bob, charlie)
    total = len(all_total)
    print(f"All unique achievements: {all_total}")
    print(f"Total unique achievements: {total}")

    common = bob.intersection(alice, charlie)
    print(f"\nCommon to all players: {common}")

    alice_bob = alice.intersection(bob)
    bob_charlie = bob.intersection(charlie)
    charlie_alice = charlie.intersection(alice)

    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)

    all_shared = alice_bob.union(bob_charlie, charlie_alice)

    rare = all_total.difference(all_shared)
    print(f"Rare achievemen (1 player) : {rare}")

    print(f"Alice vs Bob common: {alice_bob}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    ft_achievement_tracker()
