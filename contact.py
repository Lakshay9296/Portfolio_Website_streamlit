import streamlit as st

st.title("Contact Me ✉",anchor=False)
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

col1,col2,col3 = st.columns(3,gap="large",vertical_alignment="center")

with col1:
    st.image("assets/gmail.png",width=150) 
    st.subheader("Email",anchor=False)
    st.write("lakshay.kumar9911@gmail.com")

with col2:
    st.image("assets/linkedin.png",width=150) 
    st.subheader("LinkedIn",anchor=False)
    st.write("[Connect with me on LinkedIn](https://www.linkedin.com/in/lakshay9911)")
 
with col3:
    st.image("assets/github.png",width=150) 
    st.subheader("GitHub",anchor=False)
    st.write("[Check out my GitHub profile](https://github.com/Lakshay9296)")
