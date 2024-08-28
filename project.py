import streamlit as st

# Title for the Projects page
st.title("Projects 🚀")

# Define project details
projects = [
    # Data Analysis Projects
    {
        "title": "SuperStore Sales Analysis - PowerBI",
        "description": "A comprehensive sales analysis of SuperStore data, including dashboards for sales analysis and forecasting using time series analysis and various plots.",
        "tech": "PowerBI",
        "image": "assets/ssbi.png",  # Replace with the path to your project image
        "link": "https://github.com/Lakshay9296/SuperStore_Sales_Analysis_PowerBI"  # Replace with the URL to the project
    },
    {
        "title": "Coffee Sales Analysis Dashboard - Excel",
        "description": "An Excel-based project that includes a dashboard for analyzing coffee sales data, focusing on visualizations and insights.",
        "tech": "Excel",
        "image": "assets/excel.png",  # Replace with the path to your project image
        "link": "https://github.com/Lakshay9296/Coffee_Sales_Data_Analysis_Dashboard_Excel"  # Replace with the URL to the project
    },
    {
        "title": "Automotive EDA Project - Exploratory Data Analysis",
        "description": "Exploratory Data Analysis (EDA) on an automotive dataset, focusing on various aspects of data analysis and visualization techniques.",
        "tech": "Python, Pandas, Matplotlib, Seaborn",
        "image": "assets/auto.png",  # Replace with the path to your project image
        "link": "https://github.com/Lakshay9296/Automobile_Data_Analysis_EDA"  # Replace with the URL to the project
    },
    {
        "title": "Machine Learning Based Optimized Fraud Detection in Credit Card",
        "description": "A machine learning project focused on optimizing fraud detection in credit card transactions. Implemented using Python and Jupyter Notebook.",
        "tech": "Python, Jupyter Notebook, Scikit-learn",
        "image": "assets/credit.png",  # Replace with the path to your project image
        "link": "https://github.com/Lakshay9296/Credit-Card-Fraud-Detection"  # Replace with the URL to the project
    },
    {
        "title": "HR Analytics Report - PowerBI",
        "description": "An in-depth analysis of HR data to uncover insights related to employee performance, attrition, and other key HR metrics.",
        "tech": "PowerBI",
        "image": "assets/hrbi.png",  # Replace with the path to your project image
        "link": "https://github.com/Lakshay9296/HR_Analytics_Report_PowerBI"  # Replace with the URL to the project
    },
    {
        "title": "Music Store SQL Analysis - SQL",
        "description": "SQL-based project focused on analyzing data from a music store, including sales, customer behavior, and inventory management.",
        "tech": "SQL",
        "image": "assets/sql.png",  # Replace with the path to your project image
        "link": "https://github.com/Lakshay9296/Music_Store_SQL_Data_Analysis"  # Replace with the URL to the project
    },
    {
        "title": "Basic Data Analyser - Streamlit",
        "description": "A basic data analysis tool that performs essential data operations such as cleaning, visualization, and simple statistical analysis.",
        "tech": "Python, Streamlit",
        "image": "assets/bda.png",  # Replace with the path to your project image
        "link": "https://github.com/Lakshay9296/Basic_Data_Analyzer_App"  # Replace with the URL to the project
    },
    # Pygame Projects
    {
        "title": "Car Racing Game using Pygame - Python",
        "description": "A Python-based car racing game developed using the Pygame library, featuring game mechanics and interactive gameplay.",
        "tech": "Python, Pygame",
        "image": "assets/car.png",  # Replace with the path to your project image
        "link": "https://github.com/Lakshay9296/Car_Crash_Game_pygame"  # Replace with the URL to the project
    },
    {
        "title": "Tic-Tac-Toe Game using Pygame - Python",
        "description": "A classic Tic-Tac-Toe game implemented using Pygame, showcasing game development and interactive elements.",
        "tech": "Python, Pygame",
        "image": "assets/ttt.png",  # Replace with the path to your project image
        "link": "https://github.com/Lakshay9296/TicTacToe_pygame"  # Replace with the URL to the project
    },
    # Streamlit Projects
    {
        "title": "Portfolio Website - Streamlit",
        "description": "A personal portfolio website built using Streamlit, showcasing my projects, skills, and contact information.",
        "tech": "Python, Streamlit",
        "image": "assets/port.png",  # Replace with the path to your project image
        "link": "https://lakshaybda.streamlit.app/"  # Replace with the URL to the project
    },
    # Web Development Projects
    {
        "title": "Weather Website - Web Development",
        "description": "A weather website built using HTML, CSS, and JavaScript to fetch and display weather information using an API.",
        "tech": "HTML, CSS, JavaScript",
        "image": "assets/weather.png",  # Replace with the path to your project image
        "link": "https://github.com/Lakshay9296/Weather-App-Project"  # Replace with the URL to the project
    },
    {
        "title": "Gym Website - Web Development",
        "description": "A website for a gym, designed with HTML, CSS, and JavaScript, featuring member information, class schedules, and other gym-related features.",
        "tech": "HTML, CSS, JavaScript",
        "image": "assets/gym.png",  # Replace with the path to your project image
        "link": "https://github.com/Lakshay9296/Gym-Website-Project"  # Replace with the URL to the project
    }
]

# Display each project
for project in projects:
    st.subheader(project["title"])
    st.write(project["description"])
    st.write(f"**Technologies Used**: {project['tech']}")
    st.image(project["image"] ,width=600)  # Adjust width as needed
    st.markdown(f"[View Project]({project['link']})")
    st.write("\n")  # Add some space between projects
