import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


def get_player_file(player):
    return os.path.join(DATA_DIR, f"transactions_{player}.txt")


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

                parts = [p.strip() for p in line.split(":")]

                if len(parts) != 4:
                    continue

                name, category, subcategory, price = parts

                properties.append(
                    (name, category, subcategory, int(price))
                )

    except FileNotFoundError:
        pass

    return properties


# ---------------------------
# TOTAL SPENT
# ---------------------------

def total_spent(player):

    props = get_properties(player)

    return sum(p[3] for p in props)