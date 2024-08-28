import streamlit as st

about_page= st.Page(
    page="about.py",
    title="About Me",
    icon=":material/person:",
    default=True,
)
project_page= st.Page(
    page="project.py",
    title="Projects",
    icon=":material/task:"
)
contact_page=st.Page(
    page="contact.py",
    title="Contact Me",
    icon=":material/mail:"
)

pages=st.navigation(pages=[about_page,project_page,contact_page])
pages.run()

st.logo("assets/logo.png")
st.sidebar.text("Made by Lakshay")
