import streamlit as st
import base64

def get_base64_image(img_path):
    with open(img_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Paths to images
bg_img_path = 'E:/4th yr/CSIT342/Basic Streamlit App/Abandoned Mansion With Grand Staircase And Ethereal Lighting.png'
center_img_path = 'E:/4th yr/CSIT342/Basic Streamlit App/2b.png'

icon_paths = [
    'E:/4th yr/CSIT342/Basic Streamlit App/about.png',
    'E:/4th yr/CSIT342/Basic Streamlit App/facebook.png',
    'E:/4th yr/CSIT342/Basic Streamlit App/github.png',
    'E:/4th yr/CSIT342/Basic Streamlit App/instagram.png',
    'E:/4th yr/CSIT342/Basic Streamlit App/linkedin.png',
    'E:/4th yr/CSIT342/Basic Streamlit App/projects.png',
]
 
# Corresponding URLs to open when each icon is clicked
icon_urls = [ 
    'About_Me',  # URL for the 'about' icon
    'https://www.facebook.com/danderexzai?mibextid=ZbWKwL',  # URL for Facebook
    'https://github.com/ZairenMae',  # URL for GitHub
    'https://www.instagram.com/zairen._.00/',  # URL for Instagram
    'https://www.linkedin.com/in/zairen-mae-a-ni%C3%B1ofranco-930699305/',  # URL for LinkedIn
    'https://your-website-projects.com'  # URL for Projects
]
 
# Convert images to base64
bg_img_base64 = get_base64_image(bg_img_path)
center_img_base64 = get_base64_image(center_img_path)
icon_base64 = [get_base64_image(path) for path in icon_paths]

# Hide Streamlit default elements
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {opacity: 0.5;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Set CSS for the background image, centered image, and animated icons
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('data:image/png;base64,{bg_img_base64}');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: bottom;
        min-width: 100%;
        min-height: 100%;
    }}
    #centered-image {{
        position: fixed;
        top: 50%; 
        left: 50%; 
        transform: translate(-50%, -50%);
        z-index: 1;
        width: 900px; 
        height: auto;
        animation: moveUpDown 3s ease-in-out infinite;
    }}
    @keyframes moveUpDown {{
        0% {{ transform: translate(-50%, -50%) translateY(0); }}
        50% {{ transform: translate(-50%, -50%) translateY(-20px); }}
        100% {{ transform: translate(-50%, -50%) translateY(0); }}
    }}

    .icons-wrapper {{
        position: fixed;
        top: 50%;  
        left: 50%; 
        transform: translate(-50%, -50%);
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        width: 500px;  
        height: 500px; 
        z-index: 2; 
    }}

    .orbit-icon {{
        position: absolute;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.1);
        transition: transform 0.3s, box-shadow 0.3s;
        display: flex;
        align-items: center;
        justify-content: center;
        animation: iconMoveUpDown 2s ease-in-out infinite;
    }}

    @keyframes iconMoveUpDown {{
        0% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-20px); }}
        100% {{ transform: translateY(0); }}
    }}

    .orbit-icon:hover {{
        box-shadow: 0 0 15px 10px rgba(255, 255, 0, 0.75);
        transform: scale(1.2);
        animation: none; /* Stop animation on hover */
    }}

    #icon1 {{ top: 20%; left: -20%; z-index: 100; transform: translate(-50%, -50%); }}
    #icon2 {{ top: 30%; left: 10%; z-index: 100; transform: translate(-50%, -50%); }}
    #icon3 {{ top: 10%; left: 30%; z-index: 100; transform: translate(-50%, -50%); }}
    #icon4 {{ top: 50%; left: 70%; z-index: 100; transform: translate(-50%, -50%); }}
    #icon5 {{ top: 30%; left: 120%; z-index: 100; transform: translate(-50%, -50%); }}
    #icon6 {{ top: 40%; left: 90%; z-index: 100; transform: translate(-50%, -50%); }}
    </style>
    """,
    unsafe_allow_html=True
)

# Display the centered image
st.markdown(f'<img id="centered-image" src="data:image/png;base64,{center_img_base64}" />', unsafe_allow_html=True)

# Display the icons in a dynamically positioned layout
st.markdown('<div class="icons-wrapper">', unsafe_allow_html=True)
for i, (icon_base64, url) in enumerate(zip(icon_base64, icon_urls)):
    st.markdown(f'<a href="{url}" target="_blank"><img id="icon{i+1}" class="orbit-icon" src="data:image/png;base64,{icon_base64}" /></a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
