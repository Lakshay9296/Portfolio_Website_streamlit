import streamlit as st

col1,col2 = st.columns(2,gap='medium',vertical_alignment='center')

with col1:
    st.image("assets/profile.png")
    
with col2:
    st.title("Lakshay Kumar",anchor=False)
    st.write("Data Analyst")
    st.write("I'm Lakshay Kumar, a BE graduate in Computer Science and Engineering from Chandigarh University. I'm passionate about data science, Python programming, and building practical applications.")

st.write("\n")
st.subheader("Technical Skills",anchor=False)
st.write(
    """
    - Programing Languages: Python, SQL, Java, R 
    - Database Management: MySQL, MongoDB, SQLite 
    - Developer Tools: Jupyter Notebook, R Studio, Visual Studio Code, Arduino IDE, MySQL Workbench
    - Data Analysis & Visualization: NumPy, Pandas, Power BI, Matplotlib, Seaborn 
    - IoT Platforms: Tinkercad, Arduino 
    - Other Tools: MS Excel, Power BI
    """
)

st.write("\n")
st.subheader("Education",anchor=False)
st.write(
    """
    - **Bachelor of Engineering in Computer Science and Engineering**  
      **Chandigarh University** *(Oct. 2020 – May 2024)*  
      **CGPA:**  7.3
    
    - **Senior Secondary Education (Class 12th)**  
      **Lions Public School** *(2019 – 2020)*  
      **Percentage:** 83%
    
    - **Secondary Education (Class 10th)**  
      **Lord Jesus Public School** *(2017 – 2018)*  
      **Percentage:** 83.5%
    """
)


