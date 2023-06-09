# main.py

import streamlit as st
import subprocess

# GitHub 리포지토리 주소
github_repo = 'https://github.com/your_username/your_repository'

# Streamlit 앱 설정
st.set_page_config(layout="wide")

# 사이드바에 GitHub 리포지토리 주소 입력
repo_address = st.sidebar.text_input('GitHub Repository Address', github_repo)

if st.sidebar.button
