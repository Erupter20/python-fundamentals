import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

from business_manager import (
    add_property,
    get_properties,
    total_spent,
    get_cash,
    update_cash,
    add_upgrade,
)

st.set_page_config(page_title="GTA Business Terminal", layout="wide")

st.title("💼 GTA Business Terminal")

players = [
    "bingchillingsuki",
    "darthmadansh",
    "erupter"
]

tabs = st.tabs(players)


# ---------------------------
# HTML PARSER
# ---------------------------

def extract_cash_stats(html):

    soup = BeautifulSoup(html, "html.parser")

    stats = {}

    rows = soup.select("#cash tr")

    for row in rows:
        cols = row.find_all("td")

        if len(cols) == 2:
            name = cols[0].text.strip()
            value = cols[1].text.strip()
            stats[name] = value

    return stats


# ---------------------------
# DASHBOARD
# ---------------------------

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
            "Subcategory",
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
            "Property",
            property_names,
            key=f"prop_{player}"
        )

        upgrade = st.text_input(
            "Upgrade Name",
            key=f"upgrade_{player}"
        )

        upgrade_price = st.number_input(
            "Upgrade Price",
            min_value=0,
            key=f"upgrade_price_{player}"
        )

        if st.button("Add Upgrade", key=f"upgrade_btn_{player}"):

            add_upgrade(player, selected_property, upgrade, upgrade_price)
            st.success("Upgrade added")

    # -------------------
    # IMPORT ROCKSTAR STATS
    # -------------------

    st.divider()
    st.markdown("### Import Rockstar Stats")

    with st.expander("How to get the stats HTML"):

        st.markdown("""
1. Open GTA Online stats on Rockstar Social Club  
2. Press **F12**  
3. Go to **Network**  
4. Select **Fetch/XHR**  
5. Reload the page  
6. Click **StatsAjax**  
7. Copy **Response**  
8. Paste it below
""")

    stats_html = st.text_area(
        "Paste Stats HTML",
        height=120,
        key=f"stats_{player}"
    )

    if st.button("Extract Stats", key=f"import_{player}"):

        if not stats_html.strip():
            st.warning("Paste the HTML response first")

        else:

            stats = extract_cash_stats(stats_html)

            if stats:

                st.success("Stats extracted")

                df = pd.DataFrame(
                    [{"Stat": k, "Value": v} for k, v in stats.items()]
                )

                st.table(df)

            else:
                st.error("Could not parse stats")

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

    cash = get_cash(player)

    remaining = max(goal - cash, 0)
    progress = min(cash / goal, 1)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Current Cash", f"${cash:,}")

    with col2:
        st.metric("Remaining", f"${remaining:,}")

    st.progress(progress)


# ---------------------------
# PLAYER TABS
# ---------------------------

for i, player in enumerate(players):
    with tabs[i]:
        player_dashboard(player)