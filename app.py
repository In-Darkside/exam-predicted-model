import streamlit as st
import numpy as np
import pickle

# ====== 加载模型 ======

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# ====== 页面 ======
st.title("🎓 Exam Score Predictor")
st.write("input relevant information and get the predicted score")

education_map = {
    "High School": 0,
    "College": 1,
    "Postgraduate":2

}

involvement_map = {
    'Low': 0,
    'Medium': 1,
    'High': 2
}

# ====== 用户输入 ======
Attendance = st.slider("Attendance", 60, 100, 75)
Hours_Studied = st.slider("Hours_Studied", 1, 44, 5)
Previous_Scores = st.slider("Previous_Scores", 50, 100, 75)
Tutoring_Sessions = st.slider("Tutoring_Sessions", 0, 8, 0)

# 用户输入（显示文字）
Parental_Education_Level = st.selectbox(
    "Parental_Education_Level",
    ["High School", "College", "Postgraduate"]
)
education_value = education_map[Parental_Education_Level]

# 用户输入（显示文字）
Parental_Involvement = st.selectbox(
    "Parental_Involvement_level",
    ["Low", "Medium", "High"]
)
involvement_value = involvement_map[Parental_Involvement]

# ====== 构建输入 ======

import numpy as np
input_data = np.array([[Attendance, Hours_Studied, Previous_Scores, 
                        Tutoring_Sessions,education_value,involvement_value]])

# ====== 预测 ======

if st.button("predict score"):
    prediction = model.predict(input_data)

    st.success(f"📊 predicted score: {prediction[0]:.2f}")
