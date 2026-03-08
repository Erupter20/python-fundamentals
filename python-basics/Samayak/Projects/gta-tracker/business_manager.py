import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


# ---------------------------
# FILE PATHS
# ---------------------------

def get_player_file(player):
    return os.path.join(DATA_DIR, f"transactions_{player}.txt")


def get_upgrade_file(player):
    return os.path.join(DATA_DIR, f"upgrades_{player}.txt")


# ---------------------------
# ADD PROPERTY
# ---------------------------

def add_property(player, name, category, subcategory, price):

    file = get_player_file(player)

    with open(file, "a") as f:
        f.write(f"{name}:{category}:{subcategory}:{price}\n")


# ---------------------------
# READ PROPERTIES
# ---------------------------

def get_properties(player):

    file = get_player_file(player)
    properties = []

    try:
        with open(file) as f:
            for line in f:

                line = line.strip()

                if not line:
                    continue

                parts = line.split(":")

                if len(parts) != 4:
                    continue

                name, category, subcategory, price = parts

                if name == "Cash":
                    continue

                try:
                    price = int(price)
                except:
                    continue

                properties.append((name, category, subcategory, price))

    except FileNotFoundError:
        pass

    return properties


# ---------------------------
# TOTAL SPENT
# ---------------------------

def total_spent(player):

    props = get_properties(player)

    return sum(p[3] for p in props)


# ---------------------------
# CASH
# ---------------------------

def get_cash(player):

    file = get_player_file(player)

    try:
        with open(file) as f:
            for line in f:

                parts = line.strip().split(":")

                if len(parts) != 4:
                    continue

                name, _, _, value = parts

                if name == "Cash":
                    return int(value)

    except FileNotFoundError:
        pass

    return 0


def update_cash(player, new_cash):

    file = get_player_file(player)

    lines = []
    found = False

    try:
        with open(file) as f:
            lines = f.readlines()
    except FileNotFoundError:
        pass

    with open(file, "w") as f:

        for line in lines:

            parts = line.strip().split(":")

            if len(parts) == 4 and parts[0] == "Cash":
                f.write(f"Cash:Finance:Cash:{new_cash}\n")
                found = True
            else:
                f.write(line)

        if not found:
            f.write(f"Cash:Finance:Cash:{new_cash}\n")


# ---------------------------
# UPGRADES
# ---------------------------

def add_upgrade(player, property_name, upgrade, price):

    file = get_upgrade_file(player)

    with open(file, "a") as f:
        f.write(f"{property_name}:{upgrade}:{price}\n")