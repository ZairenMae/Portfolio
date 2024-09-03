import streamlit as st
from PIL import Image
import base64
import smtplib
from email.message import EmailMessage

def encode_image(image_path):
    """ Convert image file to base64 string. """
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load the background image
background_image_path = "views/images/Enchanted Workshop At Night With Glowing Crystal Cube.png"
b64_background = encode_image(background_image_path)

# Load the profile image
profile_image_path = "views/images/zairen.jpg"
profile_b64_string = encode_image(profile_image_path)

# Icons
icons_paths = [
    "views/icons/android.png",
    "views/icons/artificial-intelligence.png",
    "views/icons/css.png",
    "views/icons/html-5.png",
    "views/icons/java.png",
    "views/icons/js.png",
    "views/icons/nextjs.png",
    "views/icons/nodejs.png",
    "views/icons/python.png",
    "views/icons/react2.png",
    "views/icons/springboot2.png",
    "views/icons/streamlit.png",
    "views/icons/typescript.png",
    "views/icons/vite-js2.png"
]

icons_b64 = [encode_image(path) for path in icons_paths]

# Hide Streamlit default elements
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {opacity: 0.5;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Display the background image and profile image with enhanced styling
st.markdown(
f"""
<style>
.stApp {{
    background-image: url(data:image/png;base64,{b64_background});
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
    padding: 20px;
    box-sizing: border-box;
}}
.content {{
    background-color: rgba(0, 0, 0, 0.6);
    padding: 20px;
    border-radius: 10px;
    color: white;
    max-width: 800px;
    margin: auto;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    position: relative;
    text-align: center;
    transition: box-shadow 0.3s ease;
    margin-bottom: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
}}
.content:hover {{
    box-shadow: 0 0 20px 5px lightblue;
}}
.title {{ 
    font-size: 3em;
    font-weight: bold;
    text-align: center;
    color: white;
}}
.subtitle {{
    font-size: 1.5em;
    font-weight: bold;
    margin-bottom: 10px;
    color: white;
}}
.text {{
    font-size: 1.2em;
    margin-bottom: 20px;
    line-height: 1.6;
    color: white;
}}
.profile-image {{
    width: 250px; /* Increase the size */
    height: 250px; /* Increase the size */
    border-radius: 50%;
    object-fit: cover;
}}
.transparent-container {{
    background-color: rgba(0, 0, 0, 0.4); /* Lightly dark transparent background */
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 20px;
    border: 1px solid lightblue; /* Thin blue border */
    transition: box-shadow 0.3s ease;
}}
.transparent-container:hover {{
    box-shadow: 0 0 10px 2px lightblue; /* Glow effect on hover */
}}
.icon-container {{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    max-width: 600px; /* Adjust to fit icons */
    margin: 20px auto; /* Center the container */
}}
.icon {{
    width: 50px; /* Icon size */
    height: 50px; /* Icon size */
    margin: 5px; /* Space between icons */
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    background-color: rgba(255, 255, 255, 0.2); /* Transparent background */
    transition: box-shadow 0.3s ease;
}}
.icon img {{
    width: 30px; /* Adjust the icon size */
    height: 30px; /* Adjust the icon size */
}}
.icon:hover {{
    box-shadow: 0 0 10px 2px lightblue; /* Glow effect on hover */
}}
.contact-button {{
    display: inline-block;
    padding: 10px 20px;
    margin-top: 20px;
    font-size: 1.2em;
    font-weight: bold;
    color: #fff;
    background-color: #007BFF;
    border: none;
    border-radius: 5px;
    text-align: center;
    text-decoration: none;
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
}}
.contact-button:hover {{
    background-color: #0056b3;
    box-shadow: 0 0 10px 2px lightblue;
}}
</style>
""",
unsafe_allow_html=True
)

# Page content
st.markdown(
    f"""
    <div class="content">
        <img src="data:image/jpeg;base64,{profile_b64_string}" class="profile-image"/>
        <div>
            <h1 class="title">Zairen Mae A. Niñofranco</h1>
            <h2 class="subtitle">BSIT Student | Aspiring Full-Stack Developer</h2>
        </div>
    </div>
    """, 
    unsafe_allow_html=True
)

def send_email(name, email, message):
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = f"New Contact Form Submission from {name} Email: {email}"
    user = "smsalertprac@gmail.com"
    msg['To'] = "zairenninofranco@gmail.com"
    msg["From"] = user
    password = "nuescnvuiwlhhlqi"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(user, password)
            server.send_message(msg)
        return True
    except smtplib.SMTPAuthenticationError:
        st.error("Authentication failed. Check your email and password.")
    except smtplib.SMTPRecipientsRefused:
        st.error("Recipient address refused. Check the recipient email address.")
    except Exception as e:
        st.error(f"Failed to send email: {e}")

@st.dialog("Contact Me", width="large")
def contact_form():
    st.write("### Contact Form")
    name = st.text_input('Name')
    email = st.text_input('Email')
    message = st.text_area('Message')
    if st.button('Send'):
        if send_email(name, email, message):
            st.session_state.message_sent = True
            st.session_state.contact_info = {
                'Name': name,
                'Email': email,
                'Message': message
            }
            st.rerun()
        else:
            st.error("There was an error sending your message. Please try again later.")

if 'message_sent' in st.session_state and st.session_state.message_sent:
    contact_info = st.session_state.contact_info
    st.write("Thank you for contacting me!")

else:
    if st.button('Contact Me'):
        contact_form()

st.markdown("<div class='transparent-container'><p class='text'>I specialize in UI/UX design for both frontend and backend, with expertise in various frameworks including HTML, CSS, JavaScript, React, Next.js, Flask, Three.js, Vite, and more. Although I have no industry experience yet, I have honed my skills in key areas and am committed to continuous learning to stay updated with the latest trends in the tech world.</p></div>", unsafe_allow_html=True)

st.markdown("<h2 class='subtitle'>Skills</h2></div>", unsafe_allow_html=True)
st.markdown("<div class='transparent-container'><p class='text'>HTML, CSS, JavaScript, React, Next.js, Flask, Three.js, Vite, Mobile Development, Android Studio, Springboot, Streamlit, Machine Learning, AI, Java, Python, Node.js</p></div>", unsafe_allow_html=True)

st.markdown("<h2 class='subtitle'>Personal Interests</h2></div>", unsafe_allow_html=True)
st.markdown("<div class='transparent-container'><p class='text'>Outside of work, I enjoy watching anime, K-drama, movies, TikTok, YouTube, and listening to music. I also love drawing and reading manhwa and anime, which helps me stay balanced and inspired.</p></div>", unsafe_allow_html=True)

st.markdown("<h2 class='subtitle'>Explore My Portfolio</h2></div>", unsafe_allow_html=True)
st.markdown("<div class='transparent-container'><p class='text'>Feel free to explore my portfolio to see some of the projects I've worked on.</p></div>", unsafe_allow_html=True)

# Icons below the text
st.markdown("<div class='icon-container'>", unsafe_allow_html=True)
for icon_b64 in icons_b64:
    st.markdown(f"<div class='icon'><img src='data:image/png;base64,{icon_b64}' /></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
