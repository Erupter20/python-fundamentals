import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from business_manager import add_property, get_properties, total_spent

st.set_page_config(page_title="GTA Business Terminal", layout="wide")

st.title("💼 GTA Business Terminal")

players = [
    "bingchillingsuki",
    "darthmadansh",
    "erupter"
]

UPGRADES = {
    "Kosatka": ["Sparrow"],
    "Terrorbyte": ["Oppressor Mk2"],
    "Nightclub": ["Security Upgrade", "Equipment Upgrade"],
    "Agency": ["Armory", "Vehicle Workshop"]
}

tabs = st.tabs(players)

PLAYER_CASH = {
    "bingchillingsuki": 0,
    "darthmadansh": 0,
    "erupter": 1047176
}


def player_dashboard(player):

    st.subheader(f"{player}'s Business")

    properties = get_properties(player)

    # -------------------
    # ADD ASSET
    # -------------------

    st.markdown("### Add Asset")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Asset Name", key=f"name_{player}")

        category = st.selectbox(
            "Category",
            ["Property", "Business", "Vehicle", "Utility"],
            key=f"cat_{player}"
        )

    with col2:
        subcategory = st.text_input(
            "Subcategory (Car, Bunker, Apartment...)",
            key=f"sub_{player}"
        )

        price = st.number_input(
            "Price",
            min_value=0,
            step=10000,
            key=f"price_{player}"
        )

    if st.button("Add Asset", key=f"btn_{player}"):

        if name:
            add_property(player, name, category, subcategory, price)
            st.success("Asset added")
            st.rerun()

    # -------------------
    # ASSET TABLE
    # -------------------

    st.divider()

    if properties:

        table_data = [
            {
                "Name": p[0],
                "Category": p[1],
                "Type": p[2],
                "Price": p[3]
            }
            for p in properties
        ]

        st.table(table_data)

        total = total_spent(player)

        st.metric("Total Investment", f"${total:,}")

    else:
        st.info("No assets yet")

    # -------------------
    # UPGRADES
    # -------------------

    st.divider()
    st.markdown("### Upgrades")

    property_names = [p[0] for p in properties]

    if property_names:

        selected_property = st.selectbox(
            "Select Property",
            property_names,
            key=f"prop_{player}"
        )

        available_upgrades = UPGRADES.get(selected_property, [])

        if available_upgrades:

            upgrade = st.selectbox(
                "Upgrade",
                available_upgrades,
                key=f"upgrade_{player}"
            )

            upgrade_price = st.number_input(
                "Upgrade Price",
                min_value=0,
                key=f"upgrade_price_{player}"
            )

            if st.button("Add Upgrade", key=f"upgrade_btn_{player}"):

                with open(f"data/upgrades_{player}.txt", "a") as f:
                    f.write(
                        f"{selected_property}:{upgrade}:{upgrade_price}\n"
                    )

                st.success("Upgrade added")

        else:
            st.info("No upgrades available for this property")

    else:
        st.warning("Add a property first to unlock upgrades")

    # -------------------
    # GOAL TRACKER
    # -------------------

    st.divider()
    st.markdown("### Goal Tracker")

    goal = st.number_input(
        "Goal Amount",
        value=6000000,
        step=100000,
        key=f"goal_{player}"
    )

    cash = PLAYER_CASH.get(player, 0)

    remaining = max(goal - cash, 0)

    progress = min(cash / goal, 1) if goal else 0

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Current Cash", f"${cash:,}")

    with col2:
        st.metric("Remaining", f"${remaining:,}")

    st.progress(progress)

    # -------------------
    # PROFIT ANALYSIS
    # -------------------

    st.divider()
    st.markdown("### Profit Analysis")

    if properties:

        spent = sum(p[3] for p in properties)

        recovered = spent * 0.5

        data = pd.DataFrame({
            "Category": ["Spent", "Recovered"],
            "Amount": [spent, recovered]
        })

        st.bar_chart(data.set_index("Category"))

    else:
        st.info("No assets yet")

    # -------------------
    # CATEGORY DISTRIBUTION
    # -------------------

    st.divider()
    st.markdown("### Asset Categories")

    if properties:

        category_totals = {}

        for p in properties:
            category = p[1]
            price = p[3]

            if category not in category_totals:
                category_totals[category] = 0

            category_totals[category] += price

        data = pd.DataFrame({
            "Category": list(category_totals.keys()),
            "Value": list(category_totals.values())
        })

        st.bar_chart(data.set_index("Category"))

    else:
        st.info("No assets yet")


# ---------------------------
# PLAYER TABS
# ---------------------------

for i, player in enumerate(players):
    with tabs[i]:
        player_dashboard(player)