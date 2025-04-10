import streamlit as st
import pandas as pd
import joblib as jb
import sklearn
import sklearn.ensemble
# إعداد عنوان الصفحة
st.set_page_config(page_title='Bank Customer Churn Prediction')
from PIL import Image

# Load and show the logo
logo = Image.open("logo.png")
st.image(logo, width=70)  # Adjust width as needed
st.write('<h1 style="text-align:center;color:  blue;">Bank Customer Churn Prediction</h1>', unsafe_allow_html=True)
st.write("*" * 100)

# دالة التنبؤ
def prediction(Age, Sex, BP, Cholesterol, Na_to_K):
    test_df = pd.DataFrame(columns=['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K'])
    test_df.loc[0, 'Age'] = Age
    test_df.loc[0, 'Sex'] = Sex
    test_df.loc[0, 'BP'] = BP
    test_df.loc[0, 'Cholesterol'] = Cholesterol
    test_df.loc[0, 'Na_to_K'] = Na_to_K
    result = Model.predict(test_df)
    return int(result[0])  # نحول الناتج إلى رقم صحيح لو كان مصفوفة أو سلسلة

# الدالة الرئيسية
def main():
    Age = st.slider('Age', 15, 74, 25, step=1)
    Sex = st.selectbox('Gender', ['M', 'F'])
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
