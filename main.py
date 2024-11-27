import streamlit as st
import src

st.set_page_config(page_title="Whow Scraper", page_icon=":robot_face:")

with open("assets/styles/custom.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
st.markdown("<h1 style='text-align: center; text-transform: uppercase;'>Whow Scraper</h1>", unsafe_allow_html=True)
url = st.text_input("Enter a Website URL: ")

if st.button("Scrape Site"):
    if url:
        st.write("Scraping the website")
    
        dom_content = src.scrape_website(url)
        body_content = src.extract_body_content(dom_content)
        cleaned_content = src.clean_body_content(body_content)
        
        st.session_state.dom_content = cleaned_content
        
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Descrive what you want to parse?")
    
    if st.button("Parse Content"):
        if  parse_description:
            st.write("Parsing the content")
            
            dom_chunks = src.split_dom_content(st.session_state.dom_content)
            parsed_result = src.parse_with_ollama(dom_chunks, parse_description)
            print(f"Dữ liệu nè: {parsed_result}")
            st.write(parsed_result)