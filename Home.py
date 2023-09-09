import streamlit as st 
from streamlit_option_menu import option_menu
from transformers import pipeline, Conversation

pipe = pipeline(task="conversational", model="microsoft/DialoGPT-medium")


# def homepage():
#     st.write("Timeline")
#     # allmessages =[]
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     if usrmsg := st.chat_input("Share a thought"):
#         st.session_state.messages.append(usrmsg)
#         with st.chat_message("user"):
#             st.session_state.messages
    
    
def chat():
    if query := st.chat_input("Enter your message"):
        uquery = Conversation(query)
        response = pipe(uquery)
        with st.chat_message("assistant"):
            st.write(response.generated_responses[-1])
        
    
# def invoke_document():
#     st.write("Invoke Document")
#     st.write("Welcome to the invoke document page")
    
# def invoke_audio():
#     st.write("Invoke Audio")
#     st.write("Welcome to the invoke audio page")
    
# def invoke_video():
#     st.write("Invoke Video")
#     st.write("Welcome to the invoke video page")
    
# def invoke_image():
#     st.write("Invoke Image")
#     st.write("Welcome to the invoke image page")
    
# def invoke_text():
#     st.write("Invoke Text")
#     st.write("Welcome to the invoke text page")
    



def dashboard():
    
    with st.sidebar:
        selected = option_menu(None, ['Conversational', "Q&A", "Text Generation", "Text Classification", "Image Classification", "Summurization", "Visual Q&A" , "Logout"],
                               icons=['💬','❓', '📝', '🔤', '🖼️', '📑', '🔎', '🔓'])
    # if selected == 'Home':
    #     homepage()
    if selected == 'Conversational':
        chat()
    elif selected == 'Logout':
        st.session_state.user = None
        st.experimental_rerun()
    # elif selected == "Invoke Document":
    #     invoke_document()
    # elif selected == "Invoke Audio":
    #     invoke_audio()
    # elif selected == "Invoke Video":
    #     invoke_video()
    # elif selected == "Invoke Image":
    #     invoke_image()
    # elif selected == "Invoke Text":
    #     invoke_text()
        