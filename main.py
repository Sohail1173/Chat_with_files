import streamlit as st
from chat import comp_process
def frontend():
    page=st.set_page_config(page_title="chat with multiple pdf files",layout="wide")
    st.title("chat with multiple :red[PDF Files]!")
    question=st.text_input("Ask Question Below:")

    with st.sidebar:
        api_key=st.text_input("Enter apikey",placeholder="Enter OpenAI Key",type="password")
        st.subheader("upload PDFS here")
        pdfs=st.file_uploader("Upload PDF files",type="pdf",accept_multiple_files=True)
        st.button('process')
    if pdfs and api_key is not None:
        if question:
            ans=comp_process(apikey=api_key,pdfs=pdfs,question=question)

if __name__ == "__main__":
    frontend()
