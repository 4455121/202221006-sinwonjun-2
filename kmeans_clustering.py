# kmeans_clustering.py

import streamlit as st
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 데이터 생성
X, _ = make_blobs(n_samples=300, centers=4, random_state=0, cluster_std=0.60)

# Streamlit 앱 생성
st.title('k-means Clustering')
st.sidebar.header('Parameters')

# 클러스터 개수 선택
n_clusters = st.sidebar.slider('Number of Clusters', min_value=2, max_value=10, value=4, step=1)

# k-means 클러스터링
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# 클러스터 할당 결과 시각화
fig, ax = plt.subplots()
ax.scatter(X[:, 0], X[:, 1], c=labels)
ax.scatter(centroids[:, 0], centroids[:, 1], marker='*', c='red', s=150)
ax.set_xlabel('X')
ax.set_ylabel('Y')
st.pyplot(fig)
