import streamlit as st
import base64

# Function to load and encode the image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load your image and encode it
image_path = 'E:/4th yr/CSIT342/Basic Streamlit App/project_background.png'
image_base64 = get_base64_of_bin_file(image_path)

# Hide Streamlit default elements and apply custom styles
hide_streamlit_style = f"""
<style>
#MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}
header {{opacity: 0.5;}}
.stApp {{
    background-image: url("data:image/png;base64,{image_base64}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
.title {{
    color: #FFD700;
    font-size: 3em;
    font-weight: bold;
    text-shadow: 2px 2px 5px #000000;
    text-align: center;
}}
.project-list {{
    color: #FFFFFF;
    background: rgba(0, 0, 0, 0.5);
    padding: 20px;
    border-radius: 10px;
    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
    margin: 10px auto;
    width: 80%;
    max-width: 600px;
}}
.card {{
    background: rgba(0, 0, 0, 0.7);
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 15px;
    box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.3);
    transition: background 0.3s ease, box-shadow 0.3s ease;
}}
.card:hover {{
    background: rgba(0, 0, 0, 0.8);
    box-shadow: 0 0 15px rgba(0, 255, 0, 0.7); /* Green glow effect */
}}
.card-title {{
    font-size: 1.5em;
    color: #FFD700;
    margin-bottom: 10px;
}}
.card-description {{
    font-size: 1.2em;
    color: #FFFFFF;
}}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Title with bright color
st.markdown('<div class="title">Welcome to My Project</div>', unsafe_allow_html=True)

# Display a simple text without a container
st.markdown('<p style="color: #FFFFFF; font-size: 1.2em; text-align: center;">This is a list of my projects that I\'ve worked on:</p>', unsafe_allow_html=True)

# Project cards with clickable links
projects = [
    {
        "title": "BloodcountProject",
        "description": "Our Bloodcount app provides Instant notifications on blood availability. Ensuring the safety of user data. Providing a platform for donors and recipients to create and manage profiles. ",
        "link": "https://github.com/ZaiTakaki/BloodcountProject"
    },
    {
        "title": "DeliverYey",
        "description": "DeliverYey is a user-friendly mobile app that revolutionizes the school canteen experience. It allows students to easily browse and order their favorite meals directly from their smartphones. With DeliverYey, students can skip the long queues and enjoy their food conveniently delivered to their classrooms.",
        "link": "https://github.com/ZairenMae/DeliverYey"
    },
    {
        "title": "DeliverYey-backend",
        "description": "Backend",
        "link": "https://github.com/ZairenMae/DeliverYey-backend"
    },
    {
        "title": "Stock-Management-System",
        "description": "Stock Management System with Python Tkinter GUI and MySQL Workbench Database Introduction The Stock Management System is a Python application with a graphical user interface (GUI) built using Tkinter. It allows users to efficiently manage and track inventory. This system utilizes a MySQL database to store and retrieve information about items, their quantities, and other relevant data.",
        "link": "https://github.com/ZairenMae/Stock-Management-System"
    }
]

# Create project cards with links
for project in projects:
    st.markdown(f'''
        <a href="{project["link"]}" target="_blank" style="text-decoration: none;">
            <div class="card">
                <div class="card-title">{project["title"]}</div>
                <div class="card-description">{project["description"]}</div>
            </div>
        </a>
    ''', unsafe_allow_html=True)
