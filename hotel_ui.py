import streamlit as st

# Import your menu and logic
from hotelmanagement import menu

st.title("🍽️ Python Restaurant")
st.write("Welcome! Here's our menu:")

for item, price in menu.items():
    st.write(f"**{item.capitalize()}** — Rs{price}")

# First item selection
item_1 = st.selectbox("Select your first item:", options=list(menu.keys()))
order_total = menu[item_1]
st.write(f"✅ {item_1.capitalize()} added to order. Price: Rs{menu[item_1]}")

# Ask if user wants to add another item
add_more = st.radio("Do you want to add another item?", ['No', 'Yes'])

if add_more == 'Yes':
    item_2 = st.selectbox("Select your second item:", options=list(menu.keys()), key="item2")
    order_total += menu[item_2]
    st.write(f"✅ {item_2.capitalize()} added to order. Price: Rs{menu[item_2]}")

# Show total
st.write("---")
st.write(f"### 💰 Total Amount to Pay: Rs{order_total}")
