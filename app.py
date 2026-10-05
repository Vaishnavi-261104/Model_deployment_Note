
import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(
    page_title="🚢 Titanic Survival Prediction",
    page_icon="🚢",
    layout="centered"
)

# CUSTOM CSS
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.title-box {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
}

.title-box h1 {
    font-size: 38px;
    margin-bottom: 8px;
}

.title-box p {
    font-size: 17px;
    margin: 0;
}

.input-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #ff512f, #dd2476);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0px 6px 15px rgba(221,36,118,0.3);
}

.success-box {
    background-color: #d4edda;
    color: #155724;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    margin-top: 20px;
}

.error-box {
    background-color: #f8d7da;
    color: #721c24;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    margin-top: 20px;
}

.footer {
    text-align: center;
    color: #777;
    margin-top: 30px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ----------------

st.markdown("""
<div class="title-box">
    <h1>🚢 Titanic Survival Prediction</h1>
    <p>🔮 Enter passenger details and predict survival</p>
</div>
""", unsafe_allow_html=True)


# ---------------- INPUT CARD ----------------

st.markdown('<div class="input-card">', unsafe_allow_html=True)

st.subheader("👤 Passenger Information")

# User inputs
pclass = st.selectbox(
    "🎫 Passenger Class",
    [1, 2, 3]
)

sex = st.selectbox(
    "⚧️ Gender",
    ["male", "female"]
)

age = st.number_input(
    "🎂 Age",
    min_value=0.0,
    max_value=100.0,
    value=25.0
)

sibsp = st.number_input(
    "👨‍👩‍👧‍👦 Number of Siblings/Spouses Aboard",
    min_value=0,
    max_value=10,
    value=0
)

parch = st.number_input(
    "👪 Number of Parents/Children Aboard",
    min_value=0,
    max_value=10,
    value=0
)

fare = st.number_input(
    "💰 Ticket Fare",
    min_value=0.0,
    value=32.0
)

embarked = st.selectbox(
    "⚓ Port of Embarkation",
    ["S", "C", "Q"]
)

st.markdown('</div>', unsafe_allow_html=True)


# Pridict

if st.button("🔮 Predict Survival"):

    input_data = pd.DataFrame([{
        "Pclass": pclass,
        "Sex": sex,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "Embarked": embarked
    }])

    prediction = model.predict(input_data)[0]


    if prediction == 1:
        st.success("🎉Prediction: Passenger Survived! 🚢")
    else:
        st.error("😔Prediction: Passenger Did Not Survive")


