import streamlit as st
import textPreprocessing
# Set page title and icon
st.set_page_config(page_title="DiagnoSmart", page_icon="🩺")

header = """
# Welcome to the DiagnoSmart
"""

st.markdown(header)
paragraph = """
This is an AI-powered diagnostic application trained on an extensive dataset of disease symptoms. The model achieves an accuracy level of approximately 70% in effectively identifying various diseases. It serves as a tool for informational purposes and complements the expertise of healthcare professionals. However, for accurate medical diagnoses, it is crucial to consult with qualified healthcare professionals who can conduct personalized assessments based on individual circumstances.
"""
st.markdown(paragraph)
# Add a medical background image
st.image("/workspaces/DiagnoSmart/Code/1684888960420.png")

# Add a bold input box label with a specific size
st.markdown("<h2 style='color: green;'>Enter your symptoms:</h2>", unsafe_allow_html=True)

# Get input from the user in a multiline text area
user_input = st.text_area("", "", height=200)

# Add a button to trigger data extraction
if st.button("Submit"):
    # Save the extracted data to a variable
    extracted_data = user_input
    # st.write(f"Extracted Data: **{extracted_data}**")
text_obj = textPreprocessing()
text_obj.clean_duplicate(extracted_data)