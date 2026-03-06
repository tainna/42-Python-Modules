import sys
"""
nao pode usar split
"""

def ft_inventory_system() -> None:
    # Check if have arguments
    if len(sys.argv) < 2:
        return

    inventory = dict()

    # giving information fr the dic
    for arg in sys.argv[1:]:
        # split the arguments in format item:quantity
        parts = arg.split(':')
        if len(parts) == 2:
            name = parts[0]
            quantity = int(parts[1])
            inventory.update({name: quantity})

    # Base analyses
    total_items = 0
    for val in inventory.values():
        total_items += val

    unique_types = len(inventory.keys())

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")

    # Manual Ordenation (big to small)

    sorted_keys = []
    processed_keys = dict()
    # To know what already ordenate

    while len(sorted_keys) < len(inventory):
        max_key = None
        max_val = -1

        for k, v in inventory.items():
            if inventory.get(k) is not None and processed_keys.get(k) is None:
                if v > max_val:
                    max_val = v
                    max_key = k

        sorted_keys.append(max_key)
        processed_keys.update({max_key: True})

    print("\n=== Current Inventory ===")
    for k in sorted_keys:
        v = inventory.get(k)
        pct = (v / total_items) * 100
        unit_str = "unit" if v == 1 else "units"
        print(f"{k}: {v} {unit_str} ({pct:.1f}%)")

    # 4. Statistcs
    most_k = sorted_keys[0]
    least_k = sorted_keys[-1]

    unit_most = "unit" if inventory.get(most_k) == 1 else "units"
    unit_least = "unit" if inventory.get(least_k) == 1 else "units"

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most_k} ({inventory.get(most_k)} {unit_most})")
    print(f"Least abundant: {least_k} ({inventory.get(least_k)} {unit_least})")
    # Categories and suggestions
    moderate = dict()
    scarce = dict()
    restock = []

    for k, v in inventory.items():
        if v >= 5:
            moderate.update({k: v})
        else:
            scarce.update({k: v})

        if v == 1:
            restock.append(k)

    print("\n=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    restock_str = ""
    for i in range(len(restock)):
        restock_str += restock[i]
        if i < len(restock) - 1:
            restock_str += ", "
    print(f"Restock needed: {restock_str}")

    # Demonstração de Propriedades do Dicionário
    print("\n=== Dictionary Properties Demo ===")

    # Formating keys
    keys_list = list(inventory.keys())
    keys_str = ""
    for i in range(len(keys_list)):
        keys_str += keys_list[i]
        if i < len(keys_list) - 1:
            keys_str += ", "

    # Formating values
    vals_list = list(inventory.values())
    vals_str = ""
    for i in range(len(vals_list)):
        vals_str += str(vals_list[i])
        if i < len(vals_list) - 1:
            vals_str += ", "

    print(f"Dictionary keys: {keys_str}")
    print(f"Dictionary values: {vals_str}")

    sample = keys_list[0] if len(keys_list) > 0 else ""
    is_in_inv = inventory.get(sample) is not None
    print(f"Sample lookup - '{sample}' in inventory: {is_in_inv}")


if __name__ == "__main__":
    ft_inventory_system()
