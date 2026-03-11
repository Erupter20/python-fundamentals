from database import add_asset, add_upgrade, update_cash, init_db

player = "erupter"

init_db()

transactions = """
Cash:Finance:Cash:5229000

Kosatka:Utility:Submarine:2200000
Agency Hawick:Property:Agency:2830000
Maze Bank West Office:Business:CEO Office:1000000
Nightclub Downtown Vinewood:Business:Nightclub:1670000
Fort Zancudo Hangar A2:Property:Hangar:3250000
Paleto Forest Bunker:Business:Bunker:1165000
Great Chaparral Clubhouse:Business:MC Clubhouse:200000
Alamo Sea Cocaine Lockup:Business:MC Cocaine:975000
Grand Senora Meth Lab:Business:MC Meth:910000
Counterfeit Cash Factory:Business:MC Cash:845000
San Chianski Weed Farm:Business:MC Weed:715000
Grapeseed Document Forgery:Business:MC Documents:650000
Terrorbyte:Utility:Operations Truck:1375000
"""

upgrades = """
Kosatka:Sparrow:1815000
Agency Hawick:Armory:720000
Agency Hawick:Vehicle Workshop:800000
Nightclub Downtown Vinewood:Equipment Upgrade:1410000
Nightclub Downtown Vinewood:Security Upgrade:695000
"""


# -------------------------
# IMPORT TRANSACTIONS
# -------------------------

for line in transactions.strip().split("\n"):

    if not line.strip():
        continue

    parts = line.split(":")

    if parts[0] == "Cash":
        update_cash(player, int(parts[3]))
    else:
        name, category, subcategory, price = parts
        add_asset(player, name, category, subcategory, int(price))


# -------------------------
# IMPORT UPGRADES
# -------------------------

for line in upgrades.strip().split("\n"):

    if not line.strip():
        continue

    property_name, upgrade, price = line.split(":")

    add_upgrade(player, property_name, upgrade, int(price))


print("Erupter data imported successfully.")