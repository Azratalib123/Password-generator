
import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special, use_uppercase, use_lowercase):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        return "Please select at least one character type!"
    
    return ''.join(random.choice(characters) for _ in range(length))

def check_strength(length, use_digits, use_special):
    if length >= 16 and use_digits and use_special:
        return "🟢 Very Strong"
    elif length >= 12 and (use_digits or use_special):
        return "🟡 Medium"
    else:
        return "🔴 Weak"

st.set_page_config(page_title="Advanced Password Generator", page_icon="🔑", layout="wide")

st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>🔐 Password Generator</h1>
    <p style='text-align: center;'>Generate strong, customizable passwords easily with enhanced security options.</p>
""", unsafe_allow_html=True)

st.sidebar.markdown("### ⚙️ Customize Your Password")
length = st.sidebar.slider("🔢 Select password length", min_value=6, max_value=64, value=16)
use_uppercase = st.sidebar.checkbox("🔠 Include Uppercase Letters", value=True)
use_lowercase = st.sidebar.checkbox("🔡 Include Lowercase Letters", value=True)
use_digits = st.sidebar.checkbox("🔢 Include Digits")
use_special = st.sidebar.checkbox("🔣 Include Special Characters")

if "password" not in st.session_state:
    st.session_state.password = ""

generate_clicked = st.sidebar.button("🚀 Generate Password")
refresh_clicked = st.sidebar.button("🔄 Refresh")

if generate_clicked:
    st.session_state.password = generate_password(length, use_digits, use_special, use_uppercase, use_lowercase)
    st.session_state.strength = check_strength(length, use_digits, use_special)

if refresh_clicked:
    st.session_state.password = ""
    st.session_state.strength = ""

st.markdown("### 🔑 Your Generated Password")
if st.session_state.password:
    st.text_input("", st.session_state.password, key="password_display")
    st.markdown(f"**Strength:** {st.session_state.strength}")
    st.code(st.session_state.password, language="text")
    st.button("📋 Copy to Clipboard", on_click=st.write, args=("Copied to clipboard!",))

st.write("---")
st.markdown("""
    <div style='text-align: center;'>
        👨‍💻 <strong>Built with ❤️ by Azra</strong> <br>
        <a href='https://github.com/Azratalib123' target='_blank' style='color: #4A90E2;'>GitHub Profile</a>
    </div>
""", unsafe_allow_html=True)