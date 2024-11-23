import streamlit as st
import src

# Use Google Fonts via a <style> tag
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400;1,700&display=swap');
        * {
            font-family: 'Courier Prime', sans-serif !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; text-transform: uppercase;'>Whow Scraper</h1>", unsafe_allow_html=True)
url = st.text_input("Enter a Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website")
    
    result = src.scrape_website(url)
    body_content = src.extract_body_content(result)
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