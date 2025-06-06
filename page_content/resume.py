import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import os
def resume_page():
    st.title("LEI LEI")

    # 所有现有的内容保持不变
    st.markdown("""
        <div style='background-color: #FFE4C4; padding: 10px; border-radius: 5px;'>
            <h2 style='margin: 0; color: #212529;'>Contact Information</h2>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("""
    - **Email:** lleirosalie@163.com
    - **Phone:** (+852) 4662 8851
    - **LinkedIn:** [linkedin.com/in/janedoe](https://www.linkedin.com/in/lei-lei-7b0200346/)
    - **GitHub:** [github.com/janedoe](https://github.com/rosalielei)
    - **Address:** 8 Shan Tong Road, Mid-Levels, Tai Po, New Territories, Hong Kong
    """)

    st.markdown("""
        <div style='background-color: #FFE4C4; padding: 10px; border-radius: 5px; margin-top: 20px;'>
            <h2 style='margin: 0; color: #212529;'>Professional Summary</h2>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("""
    Highly analytical Master's candidate in Marketing (CUHK) with a strong foundation in Economics (ECNU) and international experience (UC Berkeley). Proven ability to drive marketing growth and optimize performance using data analytics, market research, and digital strategies. Seeking a challenging marketing or data-driven role to apply advanced analytical and cross-cultural communication skills.
    """)

    st.markdown("---")

    # 添加PDF预览部分
    st.markdown("""
        <div style='background-color: #FFE4C4; padding: 10px; border-radius: 5px;'>
            <h2 style='margin: 0; color: #212529;'>Resume Preview</h2>
        </div>
        """, unsafe_allow_html=True)
    
    pdf_path = "static/docs/resume.pdf"
    if os.path.exists(pdf_path):
        # 使用 streamlit_pdf_viewer 显示 PDF
        pdf_viewer(pdf_path, width=700, height=800)
        
        # 添加下载按钮
        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label=" 📄 Resume Download",
                data=pdf_file,
                file_name="resume_LEI_LEI.pdf",
                mime="application/pdf"
            )
    else:
        st.error("The PDF file was not found. Please ensure that 'resume.pdf' exists in the static/docs directory.")