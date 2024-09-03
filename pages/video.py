import streamlit as st

st.title('Youtube Stream')
st.write('Stream your favorite youtube video here!')

st.write('---')

videos = {
    "ITZY UNTOUCHABLE": "https://www.youtube.com/watch?v=5e3rKInegeU",
    "ENHYPEN (엔하이픈) 'Sacrifice (Eat Me Up)'": "https://www.youtube.com/watch?v=HROTJfbtcU4&list=RDV3Xpaadt-RA&index=30",
    "Bite Me - Enhypen": "https://www.youtube.com/watch?v=wXFLzODIdUI",
    "ITZY “Cheshire” ": "https://www.youtube.com/watch?v=zugAhfd2r0g&list=RDV3Xpaadt-RA&index=34",
}

selected_video = st.selectbox("Choose a video", list(videos.keys()))

if selected_video:
    st.video(videos[selected_video])

url = st.text_input('Enter video URL')

if url:
    st.video(url)
