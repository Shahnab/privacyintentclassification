import streamlit as st
import streamlit.components.v1 as components

st. set_page_config(layout="wide")

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4104/4104799.png", width=100)
st.sidebar.subheader("About Privacy Intent Classifier")
st.sidebar.markdown("####### Understanding privacy policies is crucial for users as it empowers them to learn about the information that matters to them.")
st.sidebar.markdown("####### In this work, PolicyIE, an English corpus consisting of 5,250 intent and 11,788 slot annotations spanning 31 privacy policies of websites and mobile applications.")
st.sidebar.markdown("####### PolicyIE corpus is a challenging real-world benchmark with limited labeled examples reflecting the cost of collecting large-scale annotations from domain experts")


st.sidebar.subheader("Types of Intents Classified: ")
st.sidebar.markdown("###### 1. Data Collection/Usage: What, why and how user information is collected")
st.sidebar.markdown("###### 2. Data Sharing/Disclosure: What, why and how user information is shared with or collected by third parties")
st.sidebar.markdown("###### 3. Data Storage/Retention: How long and where user information will be stored")
st.sidebar.markdown("###### 4. Data Security/Protection: Protection measures for user information")
st.sidebar.markdown("###### 5. Other: Other privacy practices that do not fall into the above four categories")


st.sidebar.caption("Model is trained on PolicyIE dataset")
st.sidebar.caption("Read more- [link](https://aclanthology.org/2021.acl-long.340.pdf)")
st.sidebar.caption("App by </Shahnab>")

# embed streamlit docs in a streamlit app
st.components.v1.iframe("https://shad0ws-privacyintentclassifier.hf.space", width=1100, height=650, scrolling=True)
