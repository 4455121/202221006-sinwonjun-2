# iris_app.py

import streamlit as st
import pandas as pd
import seaborn as sns

# Iris 데이터셋 로드
iris_df = sns.load_dataset('iris')

# 품종별 꽃잎 길이 분포 그래프
sns.set_style('whitegrid')
fig = sns.FacetGrid(data=iris_df, hue='species', height=5)
fig.map(sns.histplot, 'petal_length', bins=10, alpha=0.7)
fig.add_legend()

# 그래프를 이미지 파일로 저장
fig.savefig('iris_classification.png', format='png')

# 출력
st.image('iris_classification.png')
