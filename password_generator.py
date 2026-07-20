import streamlit as st
import random
import string

st.set_page_config(page_title="Password Generator",  layout="centered")

st.sidebar.title("Password Generator")
st.sidebar.write("Create secure random passwords.")

st.title("Secure Password Generator")

length = st.slider("Select Password Length", 4, 30, 12)

options = st.multiselect(
    "Choose Character Types",
    ["Uppercase Letters", "Lowercase Letters", "Numbers", "Symbols"],
    default=["Uppercase Letters", "Lowercase Letters", "Numbers"]
)

generate = st.button("Generate Password", use_container_width=True)

if generate:

    characters = ""

    if "Uppercase Letters" in options:
        characters += string.ascii_uppercase

    if "Lowercase Letters" in options:
        characters += string.ascii_lowercase

    if "Numbers" in options:
        characters += string.digits

    if "Symbols" in options:
        characters += "!@#$%^&*()_-+=<>?"

    if characters == "":
        st.warning("Please select at least one character type.")

    else:
        password = ""

        for i in range(length):
            password += random.choice(characters)

        strength = "Weak"

        if length >= 8 and len(options) >= 2:
            strength = "Medium"

        if length >= 12 and len(options) == 4:
            strength = "Strong"

        st.success("Password Generated Successfully!")

        st.code(password, language=None)

        c1, c2 = st.columns(2)

        c1.metric("Length", len(password))
        c2.metric("Strength", strength)

        st.subheader("Password Details")

        st.write("Character Types Selected:", len(options))
        st.write("Contains Numbers:", "Numbers" in options)
        st.write("Contains Symbols:", "Symbols" in options)

st.divider()
st.caption("Developed using Python & Streamlit")
