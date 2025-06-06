import streamlit as st
from PIL import Image
import os

def home_page():
    # 创建两列布局，调整比例
    left_col, right_col = st.columns([3, 2])  # 调整比例为3:2
    
    # 左侧介绍
    left_col.markdown(
        """
        <div style='padding: 20px;'>
            <h2 style='margin-bottom: 20px;'>LEI LEI</h2>
            <p style='font-size: 16px; line-height: 1.6;'>
                Status: Recent Master's Graduate in Marketing<br>
                Graduate: Chinese University of Hong Kong<br>
                Address: 8 Shan Tong Road, Mid-Levels, Tai Po, New Territories, Hong Kong<br>
                Email: <a href="mailto:lleirosalie@163.com">lleirosalie@163.com</a>
            </p>
        </div>
        """,unsafe_allow_html=True
    )

    # 右侧照片
    image_path = os.path.join("static", "images", "image.png")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.markdown("<div style='padding: 20px;'>", unsafe_allow_html=True)
        right_col.image(image, width=250)  # 调整图片大小
        right_col.markdown("</div>", unsafe_allow_html=True)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        <div style='background-color: #FFE4C4; padding: 10px; border-radius: 5px;'>
            <h3 style='margin: 0; color: #212529;'>About Me</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

        
    st.markdown(
        """
        - Master of Marketing from The Chinese University of Hong Kong (ranked 36th in QS), Bachelor of Economics from East China Normal University (985 and Double First-Class). 
        - I am passionate about the Internet industry, familiar with the commercialization logic of Internet products and the logic of optimizing advertising placement effects. I have internship experience in the operation of commercial seeding advertising products on Xiaohongshu. I possess strong logical thinking ability, problem-solving skills and document writing skills 
        - Understand the gameplay and rules of various social media community platforms, have a marketing talent certification from Xiaohongshu and a student certificate of product operation experience Officer from NetEase 
        - Sensitive to data, proficient in using office, Python, SQL and other tools for data analysis, with strong learning ability 
        - Fluent in English, with a CET-6 score of 524 and a TOEFL score of 95. Has overseas exchange experience at the University of California, Berkeley (ranked among the top 20 by QS) 
        - Outgoing in personality, good at cooperation, patient, meticulous and responsible in work"""
    )

    st.markdown(
        """
        <div style='background-color: #FFE4C4; padding: 10px; border-radius: 5px;'>
            <h3 style='margin: 0; color: #212529;'>Skills</h3>
        </div>
        """,
        unsafe_allow_html=True)
    st.markdown(
        """
        - **Marketing**: Proficient in Advertising, SEO, SEM, Data Analysis, etc.
        - **Coding**: Proficient in Offices, Python, Stata, R, Web Crawling, etc.
        - **Language**: Chinese(native), English (TOEFL 95), GRE (315+) 
        - **Certification**: Xiaohongshu Marketing Competence Certification: Primary
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 