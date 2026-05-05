import streamlit as st


def footer_home():
    logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created with <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" width="110"> by Raja </p>  
        <img src='{logo_url}' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;"> Created with <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" width="110"> by Raja </p>  
        <img src='{logo_url}' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)
