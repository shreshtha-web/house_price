import streamlit as st

st.set_page_config(page_title="Test", page_icon="🏠")

st.title("🏠 TEST PAGE")
st.success("Streamlit is rendering correctly!")
st.write("If you can see this, the problem is with the previous app.py.")

name = st.text_input("Enter your name")

if st.button("Test Button"):
    st.write("Hello", name)
