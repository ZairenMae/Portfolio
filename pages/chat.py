import streamlit as st

# Streamlit app
st.title("Chat with me👋")

# Expanded predefined responses
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm a bot, so I don't have feelings, but thanks for asking!",
    "what's your name": "I'm a static chatbot created with Streamlit!",
    "who created you": "I was created by a developer using Python and Streamlit.",
    "what can you do": "I can chat with you and provide some basic information!",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "what's the weather like": "I can't check the weather, but I hope it's nice wherever you are!",
    "what's your favorite color": "I like all colors equally, but blue is quite calming.",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! I'm here to help.",
    "tell me a fun fact": "Did you know? The Eiffel Tower can be 15 cm taller during the summer due to the expansion of iron in the heat.",
    "do you like music": "I don't listen to music, but I've heard it's a great way to relax.",
    "what's the capital of France": "The capital of France is Paris.",
    "how old are you": "I'm timeless! I exist in the digital realm.",
    "can you help me with programming": "Sure! I can give you some basic advice. What do you need help with?",
    "what's the meaning of life": "42! Just kidding, that's a reference from 'The Hitchhiker's Guide to the Galaxy.' Everyone finds their own meaning.",
    "do you know any languages": "I can 'speak' in any language you program me to, but I'm currently set up to understand English.",
    "what's your favorite food": "I don't eat, but I've heard pizza is quite popular!",
    "can you dance": "I can't dance, but I can imagine you doing a great job!",
    "what's your purpose": "My purpose is to provide you with responses and help with any queries you might have!",
}

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask me anything!")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate a static response based on the prompt
    response = responses.get(prompt.lower(), "Sorry, I don't understand that. Try asking something else!")
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
