import streamlit as st
from modules.load_config import watsonx_conf
from modules.simple_auth import authenticate_user
from modules.watsonx import WatsonxAI

###################
# Variables
system_prompt = """
## System Instructions
You are a knowledgeable and friendly AI assistant named Thomas. 
Your role is to help users by answering their questions, providing information, and offering guidance to the best of your abilities. When responding, use a warm and professional tone, and break down complex topics into easy-to-understand explanations. If you are unsure about an answer, it's okay to say you don't know rather than guessing.
"""

###################
# Functions

def response_generator( model_id ):
    apikey = watsonx_conf()["WATSONX_APIKEY"]
    region = watsonx_conf()["WATSONX_REGION"]
    project_id = watsonx_conf()["WATSONX_PROJECT_ID"]
    watsonx_ai = WatsonxAI( apikey, region, project_id)
    
    response = watsonx_ai.getLLMresponse( generate_message_prompt(), model_id)
    return response

def response_stream_generator( model_id):
    apikey = watsonx_conf()["WATSONX_APIKEY"]
    region = watsonx_conf()["WATSONX_REGION"]
    project_id = watsonx_conf()["WATSONX_PROJECT_ID"]
    watsonx_ai = WatsonxAI( apikey, region, project_id)

    stream_response = watsonx_ai.getLLMStreamResponse( generate_message_prompt(), model_id)
    return stream_response

def generate_message_prompt ():
    result_prompt = "" 
    for m in st.session_state.messages:
        result_prompt = result_prompt + '\n' + f'"role": {m["role"]}, "content": {m["content"]}'
    return result_prompt

def setSystemPrompt ( in_system_prompt):
     system_prompt = in_system_prompt

def getSystemPrompt ( ):   
     return system_prompt

def model_select_box():
     
     label = "Select an available model in watsonx.ai for the Chat."
     options = ['mistralai/mistral-large']
     model_id = st.selectbox(label, options, index=1, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder="Choose an option", disabled=False, label_visibility="visible")
     return model_id 

def chat_type_select_box():
     
     label = "Select how you want to interact with the model in the Chat."
     options = ['streaming', 'non-streaming']
     chat_type = st.selectbox(label, options, index=1, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder="Choose an option", disabled=False, label_visibility="visible")
     return chat_type 

def execution():

    # Init configuration
    model_id = model_select_box()
    chat_type = chat_type_select_box()
    reset_button= st.button("Reset Chat", icon="🔄", type="primary")
    
    prompt = st.chat_input("Say something")

    # Initialize chat history and set system prompt
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({"role": "system", "content": getSystemPrompt()})
    
    # Reset history and reset system prompt
    if reset_button:
        st.session_state.messages = []
        st.session_state.messages.append({"role": "system", "content": getSystemPrompt()})

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
         
        if chat_type == "non-streaming":
            # Display assistant response
            with st.chat_message("assistant"):
                print(f"\n***LOG messages:\n\n{st.session_state.messages}\n\n")
                with st.sidebar:
                    st.markdown(f"# Your chat prompt: :sunglasses:\n```text{generate_message_prompt()}```", unsafe_allow_html=False, help=None)
                response = response_generator( model_id=model_id  )
                st.markdown(response)
                # Add assistant response to chat history
                message = {"role": "assistant", "content": response}
                st.session_state.messages.append(message) 

        if chat_type == "streaming":
            # Display assistant response
            with st.chat_message("assistant"):
                with st.sidebar:
                    st.markdown(f"# Your chat prompt: :sunglasses:\n```text{generate_message_prompt()}```", unsafe_allow_html=False, help=None)

                stream_response = response_stream_generator( model_id=model_id )
            
                response = st.write_stream(stream_response)
                # Add assistant response to chat history
                message = {"role": "assistant", "content": response}       
                st.session_state.messages.append(message)

###################
# Execution
st.set_page_config(page_title="Simple Chat with watsonx.ai", layout="wide")
logo_url = './app_imgs/chat_image.png'
st.sidebar.image(logo_url)

st.markdown("""
        <style>
            .reportview-container {
                margin-top: -2em;
            }
            #MainMenu {visibility: hidden;}
            .stDeployButton {display:none;}
            footer {visibility: hidden;}
            #stDecoration {display:none;}
        </style>
    """, unsafe_allow_html=True)

if authenticate_user():
    execution()



      
