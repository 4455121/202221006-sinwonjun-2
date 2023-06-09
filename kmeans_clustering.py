import numpy as np
import streamlit as st
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def initialize_centroids(data, k):
    centroids = data[np.random.choice(data.shape[0], k, replace=False)]
    return centroids

def kmeans_clustering():
    # 예시 데이터 생성
    data = np.random.randn(100, 2)

    # Streamlit 애플리케이션 설정
    st.title("k-means Clustering with Streamlit")

    # 클러스터 개수 입력
    k = st.slider("Select the number of clusters", min_value=1, max_value=10)

    # k-means 클러스터링 수행
    centroids = initialize_centroids(data, k)
    kmeans = KMeans(n_clusters=k, init=centroids, random_state=42)
    kmeans.fit(data)
    labels = kmeans.predict(data)

    # 클러스터 시각화
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=100)
    plt.title("k-means Clustering")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    st.pyplot()

    # 클러스터 중심 및 할당된 레이블 출력
    st.subheader("Cluster Centers:")
    st.write(centroids)

    st.subheader("Assigned Labels:")
    st.write(labels)

if __name__ == '__main__':
    kmeans_clustering()
