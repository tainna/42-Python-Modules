def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x['power'])['power']
    min_power = min(mages, key=lambda x: x['power'])['power']

    todos_poderes = map(lambda x: x['power'], mages)
    avg_power = round(sum(todos_poderes) / len(mages), 2)
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


def main():
    print("\nTesting artifact sorter...")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'}
    ]
    sorted_arts = artifact_sorter(artifacts)
    print(f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power) comes"
          f"before {sorted_arts[1]['name']} ({sorted_arts[1]['power']} power)")

    print("\nTesting spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    transformed = spell_transformer(spells)
    print(" ".join(transformed))


if __name__ == "__main__":
    main()
