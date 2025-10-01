
import streamlit as st

# Parametre
stred_x = st.number_input("Stred x", value=0)
stred_y = st.number_input("Stred y", value=0)
polomer = st.number_input("Polomer", value=100)
pocet_bodov = st.number_input("Počet bodov", value=10)
farba_bodov = st.color_picker("Vyberte farbu bodov", "#FF0000")
