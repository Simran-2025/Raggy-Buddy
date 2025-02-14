# import streamlit as st
# from google import genai
# # import google.generativeai as genai

# # Streamlit title
# st.title("Chatbot using Gemini API")

# # Initialize the API client with your key
# try:
#     client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
# except Exception as e:
#     st.error(f"Error initializing Gemini API: {e}")

# # Set a default model
# if "genai_model" not in st.session_state:
#     st.session_state["genai_model"] = "gemini-2.0-flash"

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Accept user input
# if prompt := st.chat_input("What do you want to ask?"):
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     # Display user message in chat message container
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Generate response using Gemini API
#     try:
#         with st.chat_message("assistant"):
#             with st.spinner("Generating response..."):
#                 response = client.models.generate_content(
#                     model=st.session_state["genai_model"],
#                     contents=prompt
#                 )
#                 assistant_reply = response.text
#                 st.markdown(assistant_reply)

#         # Add assistant response to chat history
#         st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

#     except Exception as e:
#         st.error(f"Error generating response: {e}")












import streamlit as st
import google.generativeai as genai

# Streamlit title
st.title("Chatbot using Gemini API")

# Initialize the API client with your key
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error(f"Error initializing Gemini API: {e}")

# Set a default model
if "genai_model" not in st.session_state:
    st.session_state["genai_model"] = "gemini-1.5-flash"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What do you want to ask?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response using Gemini API
    try:
        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                # Initialize the model
                model = genai.GenerativeModel(st.session_state["genai_model"])
                
                # Generate response using the model
                response = model.generate_content(prompt)
                assistant_reply = response.text  # Accessing the response text
                
                st.markdown(assistant_reply)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

    except Exception as e:
        st.error(f"Error generating response: {e}")
