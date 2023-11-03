import streamlit as st
from st_keyup import st_keyup

from rates import load_rates
from cfg import CURRENCY


exchange_rates = load_rates()

st.header("GEL Exchange Rate Calculator")
amount_base = st_keyup("Enter the amount in GEL", type="number")

try:
    amount_base = float(amount_base) if amount_base else 0.0
except ValueError:
    amount_base = 0.0

conversion_rates = exchange_rates[CURRENCY]
for currency, conversion_rate in conversion_rates.items():
    amount_target = float(amount_base) * conversion_rate
    st.write("#### " + f"{currency}: {amount_target:,.2f}")
