import streamlit as st
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def iris_classification():
    # Iris 데이터셋 로드
    iris = load_iris()
    X = iris.data
    y = iris.target

    # 데이터 분할
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # k-NN 분류기 초기화 및 학습
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)

    # 테스트 데이터에 대한 예측
    y_pred = knn.predict(X_test)

    # 정확도 평가
    accuracy = accuracy_score(y_test, y_pred)

    # 결과 출력
    st.subheader("Iris Classification")
    st.write("Accuracy:", accuracy)

if __name__ == '__main__':
    iris_classification()
