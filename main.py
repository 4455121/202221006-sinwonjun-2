# main.py

import streamlit as st
import subprocess

# Streamlit 앱 설정
st.set_page_config(layout="wide")

# 예제 선택
example = st.sidebar.selectbox('Select an Example', ('iris classification', 'k-means clustering'))

if example == 'iris classification':
    # GitHub 리포지토리 주소
    github_repo = 'https://github.com/your_username/your_repository_iris'

    # 사이드바에 GitHub 리포지토리 주소 입력
    repo_address = st.sidebar.text_input('GitHub Repository Address', github_repo)

    if st.sidebar.button('Run App'):
        # GitHub 리포지토리 클론
        clone_command = f"git clone {repo_address}"
        subprocess.call(clone_command, shell=True)

        # 필요한 라이브러리 설치
        install_command = "pip install -r requirements.txt"
        subprocess.call(install_command, shell=True)

        # iris 분류 앱 실행
        run_command = "streamlit run iris_app.py"
        subprocess.call(run_command, shell=True)

        # 출력 파일 표시
        st.image('iris_classification.png')

elif example == 'k-means clustering':
    # GitHub 리포지토리 주소
    github_repo = 'https://github.com/your_username/your_repository_kmeans'

    # 사이드바에 GitHub 리포지토리 주소 입력
    repo_address = st.sidebar.text_input('GitHub Repository Address', github_repo)

    if st.sidebar.button('Run App'):
        # GitHub 리포지토리 클론
        clone_command = f"git clone {repo_address}"
        subprocess.call(clone_command, shell=True)

        # 필요한 라이브러리 설치
        install_command = "pip install -r requirements.txt"
        subprocess.call(install_command, shell=True)

        # k-means 클러스터링 앱 실행
        run_command = "streamlit run kmeans_app.py"
        subprocess.call(run_command, shell=True)

        # 출력 파일 표시
        st.image('kmeans_clustering.png')
