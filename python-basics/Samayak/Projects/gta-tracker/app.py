import streamlit as st
import pandas as pd

from database import (
    init_db,
    add_asset,
    get_assets,
    total_assets,
    add_upgrade,
    get_upgrades,
    total_upgrades,
    get_cash,
    update_cash
)

from parser import extract_stats


# Initialize database
init_db()

st.set_page_config(
    page_title="GTA Business Terminal",
    layout="wide"
)

st.title("💼 GTA Business Terminal")

players = [
    "bingchillingsuki",
    "darthmadansh",
    "erupter"
]

tabs = st.tabs(players)


def dashboard(player):

    st.subheader(player)

    assets = get_assets(player)

    col1, col2, col3 = st.columns(3)

    cash = get_cash(player)
    asset_total = total_assets(player)
    upgrade_total = total_upgrades(player)

    net = cash + asset_total + upgrade_total

    col1.metric("Cash", f"${cash:,}")
    col2.metric("Assets", f"${asset_total:,}")
    col3.metric("Net Worth", f"${net:,}")

    st.divider()

    # ------------------------
    # ADD ASSET
    # ------------------------

    st.markdown("### Add Asset")

    name = st.text_input("Asset Name", key=f"name{player}")

    category = st.selectbox(
        "Category",
        ["Property", "Business", "Vehicle", "Utility"],
        key=f"cat{player}"
    )

    sub = st.text_input("Subcategory", key=f"sub{player}")

    price = st.number_input(
        "Price",
        min_value=0,
        step=10000,
        key=f"price{player}"
    )

    if st.button("Add Asset", key=f"add{player}"):

        if name:
            add_asset(player, name, category, sub, price)
            st.rerun()

    st.divider()

    # ------------------------
    # SHOW ASSETS
    # ------------------------

    if assets:

        df = pd.DataFrame(
            assets,
            columns=["Name", "Category", "Type", "Price"]
        )

        st.table(df)

    else:
        st.info("No assets yet")

    st.divider()

    # ------------------------
    # ADD UPGRADE
    # ------------------------

    st.markdown("### Add Upgrade")

    if assets:

        prop = st.selectbox(
            "Property",
            [a[0] for a in assets],
            key=f"prop{player}"
        )

        upgrade = st.text_input(
            "Upgrade Name",
            key=f"upgrade{player}"
        )

        upgrade_price = st.number_input(
            "Upgrade Price",
            min_value=0,
            step=10000,
            key=f"upprice{player}"
        )

        if st.button("Add Upgrade", key=f"addUp{player}"):

            add_upgrade(player, prop, upgrade, upgrade_price)
            st.rerun()

    else:
        st.info("Add a property first to attach upgrades")

    st.divider()

    # ------------------------
    # IMPORT ROCKSTAR STATS
    # ------------------------

    st.markdown("### Import Rockstar Stats")

    html = st.text_area(
        "Paste Rockstar Stats HTML",
        height=150,
        key=f"html{player}"
    )

    if st.button("Extract", key=f"extract{player}"):

        stats = extract_stats(html)

        if stats:

            for k, v in stats.items():

                if "cash" in k.lower():
                    update_cash(player, v)

            st.success("Stats Imported")

            df = pd.DataFrame(
                [{"Stat": k, "Value": v} for k, v in stats.items()]
            )

            st.table(df)

            st.rerun()

        else:
            st.error("Parser failed")

    st.divider()

    # ------------------------
    # GOAL TRACKER
    # ------------------------

    st.markdown("### Goal Tracker")

    goal = st.number_input(
        "Goal Amount",
        value=6500000,
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


# ------------------------
# PLAYER TABS
# ------------------------

for i, p in enumerate(players):

    with tabs[i]:

        dashboard(p)