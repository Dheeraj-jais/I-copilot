import streamlit as st
from PIL import Image
import google.generativeai as genai


GOOGLE_API_KEY = "AIzaSyBHL4RPc1ENg_8MFKsOVelhUncDQKZ2pYc"
genai.configure(api_key=GOOGLE_API_KEY)


model = genai.GenerativeModel('gemini-1.5-pro')

st.set_page_config(page_title="Welcome to I-Copilot")
st.title("Intelligent Copilot Multimodal")

tab1, tab2 = st.tabs(["🧠 Ask anything", "🖼️ Image Analyzer"])

with tab1:
    st.header("Content Generator")
    st.write("Ask I-Copilot for creative ideas")
    user_input = st.text_input("Enter your prompt:", value="")
    if st.button("Generate Idea"):
        if user_input.strip() == "":
            st.warning("Please enter a prompt.")
        else:
            with st.spinner("Thinking..."):
                try:
                    response = model.generate_content(user_input)
                    st.success("Response:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")

with tab2:
    st.header("Image Analyzer")
    st.write("Upload an image and I-copilot will describe or analyze it.")
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    prompt = st.text_input("Optional: Add a prompt for the image (e.g., 'Describe this image')", key="imgprompt")
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_container_width=True)
        if st.button("Analyze Image", key="image"):
            with st.spinner("Generating response..."):
                try:
                    
                    contents = []
                    if prompt.strip():
                        contents.append(prompt)
                    contents.append(img)
                    response = model.generate_content(contents)
                    st.markdown("### Generated Response")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error generating content: {e}")
    else:
        st.info("Please upload an image to get started.")



st.markdown("***Developed by-: Dheeraj jaiswal***")
