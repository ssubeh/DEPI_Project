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
    country = st.radio('Banck Country', ['France', 'Germany','Spain'], horizontal=True)
    age = st.slider('Your Age', 15, 95, 25, step=1)
    Sex = st.selectbox('Gender', ['Male', 'Female'])
    
    BP = st.selectbox('Blood Pressure Status', ['HIGH', 'LOW', 'NORMAL'])
    Cholesterol = st.radio('Cholesterol Status', ['HIGH', 'NORMAL'], horizontal=True)
    Na_to_K = st.number_input('Insert Value', min_value=6.269, max_value=38.247)

    if st.button('Predict'):
        results = prediction(Age, Sex, BP, Cholesterol, Na_to_K)
        label = ['DrugY', 'drugX', 'drugC', 'drugA', 'drugB']
        st.text(f'The Recommended Drug is {label[results]}')

# تشغيل التطبيق
if __name__ == '__main__':
    main()
