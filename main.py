import streamlit as st

pages = {
    "About Me": [
        st.Page("views/pages/dashboard.py", title="Dashboard", icon=":material/stadia_controller:"),
        st.Page("views/pages/profile.py", title="Profile", icon=":material/person:"),
        st.Page("views/pages/projects.py", title="Projects", icon=":material/home_storage:"),
    ],
    "Streamlit": [
        st.Page("views/pages/video.py", title="Video", icon=":material/video_library:"),
        st.Page("views/pages/chat.py", title="Chat", icon=":material/chat:"),
        st.Page("views/pages/maps.py", title="Maps", icon=":material/map:"),
        st.Page("views/pages/color.py", title="Color", icon=":material/format_color_fill:"),
    ],
}

st.sidebar.image("views/images/Logo&Name.png")

pg = st.navigation(pages)
pg.run()