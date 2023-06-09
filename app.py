import streamlit as st
from iris_classification import iris_classification
from kmeans_clustering import kmeans_clustering

# Streamlit 애플리케이션 설정
def main():
    st.title("Machine Learning Examples")

    # 사이드바 메뉴 선택
    menu = st.sidebar.selectbox("Select Example", ["Iris Classification", "K-means Clustering"])

    # 예제 실행
    if menu == "Iris Classification":
        iris_classification()
    elif menu == "K-means Clustering":
        kmeans_clustering()

if __name__ == '__main__':
    main()
