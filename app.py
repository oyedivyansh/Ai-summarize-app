import streamlit as st
from utils import extract_text_from_file, generate_summaries

st.set_page_config(page_title="AI Summarizer")

st.title("AI Document Summarizer")
st.write("Upload a file (.txt, .pdf, .docx) to generate summaries in English and Hindi.")

uploaded_file = st.file_uploader(
    "Choose a file",
    type=["txt", "pdf", "docx"]
)
    
if uploaded_file is not None:

    st.success("File uploaded successfully!")

    if st.button("Generate Summary"):

        with st.spinner("Extracting text and generating summaries..."):

            try:
                # Extract text
                text = extract_text_from_file(uploaded_file)

                if not text.strip():
                    st.error("No readable text found in the file.")
                else:
                    english_summary, hindi_summary = generate_summaries(text)

                    st.subheader("English Summary")
                    st.write(english_summary)

                    st.subheader("Hindi Summary")
                    st.write(hindi_summary)

                    # Download buttons
                    st.download_button(
                        label="Download English Summary",
                        data=english_summary,
                        file_name="english_summary.txt",
                        mime="text/plain"
                    )

                    st.download_button(
                        label="Download Hindi Summary",
                        data=hindi_summary,
                        file_name="hindi_summary.txt",
                        mime="text/plain"
                    )

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

else:
    st.info("Please upload a file to proceed.")
