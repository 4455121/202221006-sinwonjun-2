import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Iris 데이터셋 로드
iris = load_iris()
X = iris.data
y = iris.target

# 학습 데이터와 테스트 데이터로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# k-NN 분류기 생성 및 학습
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

# 테스트 데이터 예측
y_pred = knn.predict(X_test)

# 예측 결과 시각화
fig, ax = plt.subplots()
ax.scatter(X_test[:, 0], X_test[:, 1], c=y_pred)
ax.set_xlabel('Sepal length')
ax.set_ylabel('Sepal width')
plt.show()
