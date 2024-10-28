# Create a dummy streamlit page
import streamlit as st
from streamlit_scroll_navigation import scroll_navbar

# Anchor IDs and icons
anchor_ids = ["About", "Features", "Settings", "Pricing", "Contact"]
anchor_icons = ["info-circle", "lightbulb", "gear", "tag", "envelope"]

# 1. as sidebar menu
with st.sidebar:
    st.subheader("Example 1")
    scroll_navbar(
        anchor_ids,
        anchor_labels=None, # Use anchor_ids as labels
        anchor_icons=anchor_icons)

# 2. horizontal menu
st.subheader("Example 2")
scroll_navbar(
        anchor_ids,
        key = "navbar2",
        anchor_icons=anchor_icons,
        orientation="horizontal")

# Dummy page setup
for anchor_id in anchor_ids:
    st.subheader(anchor_id,anchor=anchor_id)
    st.write("content " * 100)