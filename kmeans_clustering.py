# kmeans_app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# 데이터 생성
X, y = make_blobs(n_samples=200, centers=3, random_state=42)

# K-Means 클러스터링
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# 클러스터 할당 및 중심 좌표
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# 데이터프레임 생성
data = pd.DataFrame({'X1': X[:, 0], 'X2': X[:, 1], 'Label': labels})

# 그래프 그리기
fig, ax = plt.subplots(figsize=(8, 6))
colors = ['r', 'g', 'b']
for label, color in zip(range(3), colors):
    subset = data[data['Label'] == label]
    ax.scatter(subset['X1'], subset['X2'], c=color, label=f'Cluster {label+1}')

ax.scatter(centers[:, 0], centers[:, 1], c='black', marker='x', s=200, label='Centroids')
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_title('K-Means Clustering')
ax.legend()
plt.tight_layout()

# 그래프를 이미지 파일로 저장
plt.savefig('kmeans_clustering.png', format='png')

# 출력
st.image('kmeans_clustering.png')
