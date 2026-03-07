import sys
from typing import Dict, List


def ft_inventory_system() -> None:
    """
    Parses command-line arguments to build a game inventory system.
    Uses dictionaries to store items and their quantities, calculates
    statistics (total and unique items), sorts the inventory by
    abundance, and categorizes items to provide restock suggestions.
    """
    if len(sys.argv) < 2:
        return

    """ Dictionary to store the parsed items and their quantities """
    inventory: Dict[str, int] = dict()

    """ Parses arguments character by character to avoid using split() """
    for arg in sys.argv[1:]:
        name: str = ""
        quantity_str: str = ""
        is_parsing_quantity: bool = False

        for char in arg:
            if char == ':':
                is_parsing_quantity = True
                continue

            if not is_parsing_quantity:
                name += char
            else:
                quantity_str += char

        """ Ensures both name and quantity were found before updating """
        if len(name) > 0 and len(quantity_str) > 0:
            quantity: int = int(quantity_str)
            inventory.update({name: quantity})

    """ Calculates fundamental inventory statistics """
    total_items: int = 0
    for val in inventory.values():
        total_items += val

    unique_types: int = len(inventory.keys())

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")

    """
    Custom Selection Sort algorithm to order the inventory by quantity
    from highest to lowest, built manually since sorted() is forbidden.
    """
    sorted_keys: List[str] = []
    processed_keys: Dict[str, bool] = dict()

    while len(sorted_keys) < len(inventory):
        max_key: str = ""
        max_val: int = -1

        for k, v in inventory.items():
            if processed_keys.get(k) is None:
                if v > max_val:
                    max_val = v
                    max_key = k

        sorted_keys.append(max_key)
        processed_keys.update({max_key: True})

    print("\n=== Current Inventory ===")
    for k in sorted_keys:
        v = inventory.get(k)

        if v is not None:
            pct: float = (v / total_items) * 100
            unit_str: str = "unit" if v == 1 else "units"
            print(f"{k}: {v} {unit_str} ({pct:.1f}%)")

    """ Identifies the extremes in the sorted inventory """
    most_k: str = sorted_keys[0]
    least_k: str = sorted_keys[-1]

    unit_most: str = "unit" if inventory.get(most_k) == 1 else "units"
    unit_least: str = "unit" if inventory.get(least_k) == 1 else "units"

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most_k} ({inventory.get(most_k)} {unit_most})")
    print(f"Least abundant: {least_k} ({inventory.get(least_k)} {unit_least})")

    """ Groups items into categories based on their abundance """
    moderate: Dict[str, int] = dict()
    scarce: Dict[str, int] = dict()
    restock: List[str] = []

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

    """ Formats restock suggestions manually without using join() """
    print("\n=== Management Suggestions ===")
    restock_str: str = ""
    for i in range(len(restock)):
        restock_str += restock[i]
        if i < len(restock) - 1:
            restock_str += ", "
    print(f"Restock needed: {restock_str}")

    """ Demonstrates Dictionary properties and manual string formatting """
    print("\n=== Dictionary Properties Demo ===")

    keys_list: List[str] = list(inventory.keys())
    keys_str: str = ""
    for i in range(len(keys_list)):
        keys_str += keys_list[i]
        if i < len(keys_list) - 1:
            keys_str += ", "

    vals_list: List[int] = list(inventory.values())
    vals_str: str = ""
    for i in range(len(vals_list)):
        vals_str += str(vals_list[i])
        if i < len(vals_list) - 1:
            vals_str += ", "

    print(f"Dictionary keys: {keys_str}")
    print(f"Dictionary values: {vals_str}")

    sample: str = keys_list[0] if len(keys_list) > 0 else ""
    is_in_inv: bool = inventory.get(sample) is not None
    print(f"Sample lookup - '{sample}' in inventory: {is_in_inv}")


if __name__ == "__main__":
    ft_inventory_system()
