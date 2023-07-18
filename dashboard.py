import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 載入碳排放數據
emissions_data = pd.read_csv('碳排放數據.csv')

# 定義更新時間函數
def update_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_time

# 在側邊欄上方新增即時時間
time_placeholder = st.sidebar.empty()

# 在側邊欄添加選項
st.sidebar.title('碳排放 Dashboard')
visualization = st.sidebar.selectbox('可視化方式', ('數據表格', '趨勢圖'))

# 使用JavaScript來定期更新時間
time_interval_script = """
setInterval(function() {
    const placeholder = document.querySelector("#time-placeholder");
    const currentTime = new Date().toLocaleString();
    placeholder.textContent = "當前時間：" + currentTime;
}, 1000);
"""
st.sidebar.markdown(f'<div id="time-placeholder">當前時間：{update_time()}</div>', unsafe_allow_html=True)
st.sidebar.markdown(f'<script>{time_interval_script}</script>', unsafe_allow_html=True)

if visualization == '數據表格':
    # 顯示碳排放數據表格
    st.header('碳排放數據表格')
    st.dataframe(emissions_data)
else:
    # 顯示碳排放趨勢圖
    st.header('碳排放趨勢圖')
    plt.plot(emissions_data['年份'], emissions_data['碳排放量'])
    plt.xlabel('年份')
    plt.ylabel('碳排放量')
    plt.title('碳排放趨勢')
    st.pyplot(plt)

# 添加其他需要的統計信息或圖表
# ...
