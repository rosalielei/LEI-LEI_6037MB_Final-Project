import streamlit as st

def contact_page():
    st.markdown("""
        <div style='background-color: #FFE4C4; padding: 10px; border-radius: 5px;'>
            <h2 style='margin: 0; color: #212529;'>Contact Me</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("Feel free to reach out to me through any of the following channels:")
    
    st.markdown("""
    ### Direct Contact
    - **Email**: [sarah.lleirosalie@163.com](mailto:lleirosalie@163.com)
    - **Phone**: +852 4662 8851
    - **LinkedIn**: [linkedin.com/in/lei-lei](https://www.linkedin.com/in/lei-lei-7b0200346/)
    - **GitHub**: [github.com/rosalielei](https://github.com/rosalielei)
    """)
    
    st.markdown("""
        <div style='background-color: #FFE4C4; padding: 10px; border-radius: 5px; margin-top: 20px;'>
            <h3 style='margin: 0; color: #212529;'>Send Me a Message</h3>
        </div>
        """, unsafe_allow_html=True)
    
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Name")
            email = st.text_input("Email")
            
        with col2:
            subject = st.text_input("Subject")
            
        message = st.text_area("Message", height=150)
        
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            st.success("Thanks for your message! I'll get back to you soon.")
            # In a real application, you would process the form data here
            # For example, send an email or store in a database
    
    st.markdown("---")