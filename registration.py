import streamlit as st
st.markdown('''<h1 style='text-align:center;'>USER REGISTRATION</h1>''',unsafe_allow_html=True)
with st.form("Form2"):
    col1,col2=st.columns(2)
    f_name=col1.text_input("First Name")
    l_name=col2.text_input("Last Name")
    email=st.text_input("Enter email address")
    password=st.text_input("Enter password")
    s_state=st.form_submit_button("Submit")
    if s_state:
        if f_name=="" or l_name=="" or email=="" or password=="":
            st.warning("Recheck all fields")
        else:
            st.success("Form submitted sucessfully")
