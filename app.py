import streamlit as st
import pandas as pd
import joblib as jb
import sklearn
import sklearn.ensemble
# Custom CSS to make sliders green
st.markdown("""
    <style>
    /* Change color of slider track and handle */
    .stSlider > div[data-baseweb="slider"] > div {
        background: linear-gradient(to right, green 0%, green 100%) !important;
    }
    .stSlider > div[data-baseweb="slider"] span {
        background-color: green !important;
        border-color: green !important;
    }
    </style>
""", unsafe_allow_html=True)
# إعداد عنوان الصفحة
st.set_page_config(page_title='Bank Customer Churn Prediction')
from PIL import Image

# Load and show the logo
logo = Image.open("logo.png")

col1, col2 = st.columns([1, 5])
with col1:
    st.image("logo.png", width=80)
with col2:
    st.markdown("<h2 style='color:blue;'>Bank Customer Churn Prediction</h2>", unsafe_allow_html=True)


# دالة التنبؤ
def prediction(credit_score,country, gender, age,tenure, balance, products_number,credit_card,active_member,estimated_salary):
    test_df = pd.DataFrame(columns=['credit_score', 'country', 'gender', 'age', 'tenure',
       'balance', 'products_number', 'credit_card', 'active_member',
       'estimated_salary'])
    test_df.loc[0, 'credit_score'] = credit_score
    test_df.loc[0, 'country'] = country
    test_df.loc[0, 'gender'] = gender
    test_df.loc[0, 'age'] = age
    test_df.loc[0, 'tenure'] = tenure
    test_df.loc[0, 'balance'] = balance
    test_df.loc[0, 'products_number'] = products_number
    test_df.loc[0, 'credit_card'] = credit_card
    test_df.loc[0, 'active_member'] = active_member
    test_df.loc[0, 'estimated_salary'] = estimated_salary
    result = Model.predict(test_df)
    return int(result[0])  # نحول الناتج إلى رقم صحيح لو كان مصفوفة أو سلسلة

# الدالة الرئيسية

def main():
    country = st.radio('Banck Country', ['France','Germany','Spain'], horizontal=True)
    age = st.slider('Your Age', 15, 95, 25, step=1)
    gender = st.selectbox('Gender', ['Male', 'Female'])
    credit_score = st.number_input('Credit Score', min_value=300, max_value=900)
    tenure = st.slider("Tenure (years)", 0, 10)
    balance = st.number_input("Account Balance", min_value=0.0, step=100.0)
    products_number = st.slider("Number of Products", 1, 4)
    credit_card = st.selectbox("Has Credit Card?", ["Yes", "No"])
    active_member = st.selectbox("Is Active Member?", ["Yes", "No"])
    estimated_salary = st.number_input("Estimated Salary", min_value=0.0, step=100.0)
    # Convert Yes/No to 1/0
    credit_card = 1 if has_cr_card == "Yes" else 0
    active_member = 1 if is_active_member == "Yes" else 0

    if st.button('Predict'):
        results = prediction(credit_score,country, gender, age,tenure, balance, products_number,credit_card,active_member,estimated_salary)
        label = prediction['prediction_label'].iloc[0]
        score = prediction['prediction_score'].iloc[0]
        st.subheader("🔍 Prediction Result")
        st.write(f"The customer is **{'likely' if label == 1 else 'not likely'}** to churn.")
        st.write(f"Prediction Confidence: **{score:.2f}**")

# تشغيل التطبيق
if __name__ == '__main__':
    main()
