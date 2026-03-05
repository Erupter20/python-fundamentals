import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRANSACTIONS_FILE = os.path.join(BASE_DIR, "transactions.txt")
UPGRADES_FILE = os.path.join(BASE_DIR, "upgrades.txt")


# Record property purchase
def record_transaction():
    property_name = input("Enter property name:\n")
    amount_spent = int(input("Enter amount spent:\n"))

    with open(TRANSACTIONS_FILE, "a") as file:
        file.write(f"{property_name}:{amount_spent}\n")

    print("Transaction recorded.")


# View properties
def view_properties():
    try:
        with open(TRANSACTIONS_FILE, "r") as file:
            lines = file.readlines()

            if not lines:
                print("No properties recorded yet.")
                return

            print("\n=== PROPERTY LEDGER ===")
            for line in lines:
                print(line.strip())

    except FileNotFoundError:
        print("No transactions file found.")


# Calculate total spending
def total_spending():
    total = 0

    try:
        with open(TRANSACTIONS_FILE, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(":")

                if len(parts) < 2:
                    continue

                amount = int(parts[1])
                total += amount

        print(f"\nTotal investment: {total}")

    except FileNotFoundError:
        print("No transactions recorded yet.")


# Add upgrade
def add_upgrade():
    upgrade_name = input("Enter upgrade name:\n")
    purchased = input("Purchased? (yes/no): ").lower()

    if purchased == "yes":
        price = int(input("Enter upgrade price:\n"))
    else:
        price = 0

    with open(UPGRADES_FILE, "a") as file:
        file.write(f"{upgrade_name}:{purchased}:{price}\n")

    print("Upgrade recorded.")


# View upgrades
def view_upgrades():
    try:
        with open(UPGRADES_FILE, "r") as file:
            lines = file.readlines()

            if not lines:
                print("No upgrades recorded yet.")
                return

            print("\n=== UPGRADES ===")
            for line in lines:
                print(line.strip())

    except FileNotFoundError:
        print("No upgrade file found.")


def delete_property():
    try:
        with open(TRANSACTIONS_FILE, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No properties to delete.")
            return

        print("\n=== SELECT PROPERTY TO DELETE ===")

        for i, line in enumerate(lines, start=1):
            print(f"{i}. {line.strip()}")

        choice = int(input("Enter number to delete: "))

        if 1 <= choice <= len(lines):
            removed = lines.pop(choice - 1)

            with open(TRANSACTIONS_FILE, "w") as file:
                file.writelines(lines)

            print(f"Removed: {removed.strip()}")

        else:
            print("Invalid selection.")

    except FileNotFoundError:
        print("No transactions found.")

# ================================
# WEB DASHBOARD FUNCTIONS
# ================================

DATA_DIR = os.path.join(BASE_DIR, "data")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


def get_player_file(player):
    return os.path.join(DATA_DIR, f"transactions_{player}.txt")


def add_property(player, name, price):
    file = get_player_file(player)

    with open(file, "a") as f:
        f.write(f"{name}:{price}\n")


def get_properties(player):
    file = get_player_file(player)

    properties = []

    try:
        with open(file) as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                name, price = line.split(":")
                properties.append((name, int(price)))
    except:
        pass

    return properties


def total_spent(player):
    props = get_properties(player)
    return sum(p[1] for p in props)