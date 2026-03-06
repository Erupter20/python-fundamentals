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


def player_dashboard(player):

    st.subheader(f"{player}'s Business")

    # -------------------
    # ADD PROPERTY
    # -------------------

    st.markdown("### Add Property")

    col1, col2 = st.columns(2)

    with col1:
        property_name = st.text_input("Property Name", key=f"name_{player}")

    with col2:
        price = st.number_input(
            "Price",
            min_value=0,
            step=10000,
            key=f"price_{player}"
        )

    if st.button("Add Property", key=f"btn_{player}"):

        if property_name:
            add_property(player, property_name, price)
            st.success("Property added")
            st.rerun()

    st.divider()

    properties = get_properties(player)

    if properties:

        table_data = [
            {"Property": p[0], "Price": p[1]}
            for p in properties
        ]

        st.table(table_data)

        total = total_spent(player)

        st.metric("Total Investment", f"${total:,}")

    else:
        st.info("No properties yet")

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
        value=5000000,
        step=100000,
        key=f"goal_{player}"
    )

    total = total_spent(player)

    remaining = max(goal - total, 0)

    progress = min(total / goal, 1) if goal else 0

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Current", f"${total:,}")

    with col2:
        st.metric("Remaining", f"${remaining:,}")

    st.progress(progress)

    # -------------------
    # PROFIT ANALYSIS
    # -------------------

    st.divider()
    st.markdown("### Profit Analysis")

    if properties:

        spent = sum(p[1] for p in properties)

        recovered = spent * 0.5  # placeholder

        data = pd.DataFrame({
            "Category": ["Spent", "Recovered"],
            "Amount": [spent, recovered]
        })

        st.bar_chart(data.set_index("Category"))

    else:
        st.info("No properties yet")

    # -------------------
    # SPENDING PIE CHART
    # -------------------

    # -------------------
# SPENDING PIE CHART
# -------------------

    st.divider()
    st.markdown("### Spending Distribution")

    if properties:

        labels = [p[0].replace("_", " ") for p in properties]
        values = [p[1] for p in properties]

        fig, ax = plt.subplots(figsize=(4,4))   # smaller chart

        ax.pie(values, autopct="%1.1f%%", startangle=90)

        ax.axis("equal")

        st.pyplot(fig, use_container_width=False)

    else:
        st.info("No properties yet")

# ---------------------------
# PLAYER TABS
# ---------------------------

for i, player in enumerate(players):
    with tabs[i]:
        player_dashboard(player)