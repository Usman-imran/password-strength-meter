import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Strength Meter By Usman Imran", page_icon="✅", layout="centered")

#page title
st.title("🔐 Password Strength Meter")
st.write("Enter your Password Below to Check its Security Level 🔍")

#Function to check password strength

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increase score by 1
    else:
        feedback.append("❌ Password Should be ***atleast 8 Character Long***.")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password Should contain both ***UpperCase(A-Z) and LowerCase(a-z) letter***.")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password Should Contain atleast ***One Number(0-9)***.")

    #Special Characters
    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append("❌ Password Should Contain atleast ***One Special Character(!@#$%&*)***.")

  #Display Password Strength Result
    if score == 4:
        st.success("✔ **Strong Password** - Your Password is Secured.")
    elif score == 3:
        st.info("⚠ **Moderate Password** - Consider Improving Security by Adding more Feature.")
    else: 
        st.error("❌ **Weak Password** - Follow the Suggestion Below to Strengthen it.")

  #Feedback
    if feedback:
        with st.expander("⚠ **Improve Your Password** "):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter Your Password: ", type="password", help="Ensure Your Password is Strong 🔏") 
        
#Button Working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please Enter a Password First! ") #Show Warning if Password is Empty   