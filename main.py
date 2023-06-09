# main.py

import streamlit as st
import subprocess

# GitHub 리포지토리 주소
github_repo = 'https://github.com/your_username/your_repository'

# Streamlit 앱 설정
st.set_page_config(layout="wide")

# 사이드바에 GitHub 리포지토리 주소 입력
repo_address = st.sidebar.text_input('GitHub Repository Address', github_repo)

if st.sidebar.button('Run App'):
    # GitHub 리포지토리 클론
    clone_command = f"git clone {repo_address}"
    subprocess.call(clone_command, shell=True)
    
    # 필요한 라이브러리 설치
    install_command = "pip install -r requirements.txt"
    subprocess.call(install_command, shell=True)
    
    # Streamlit 앱 실행
    run_command = "streamlit run app.py"
    subprocess.call(run_command, shell=True)
