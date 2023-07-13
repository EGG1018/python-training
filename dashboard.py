pip install matplotlib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 載入碳排放數據
emissions_data = pd.read_csv('碳排放數據.csv')

# 在側邊欄添加選項
st.sidebar.title('碳排放 Dashboard')
visualization = st.sidebar.selectbox('個人分析', ('數據表格', '折線圖'))

if visualization == '數據表格':
    # 顯示碳排放數據表格
    st.header('碳排放數據表格')
    st.dataframe(emissions_data)
else:
    # 顯示碳排放折線圖
    st.header('碳排放趨勢折線圖')
    plt.plot(emissions_data['年份'], emissions_data['碳排放量'])
    plt.xlabel('年份')
    plt.ylabel('碳排放量')
    plt.title('碳排放趨勢')
    st.pyplot(plt)




