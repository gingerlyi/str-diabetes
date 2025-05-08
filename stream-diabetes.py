import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#judul web
st.title('Data Mining Prediksi Diabtes')

#Membagi kolom
col1, col2 = st.columns(2)

with col1:
     Pregnancies = st.number_input("Input Nilai Pregnancies")
     with col2:
          Glucose = st.text_input("Input Nilai Glucose")
          
BloodPressure = st.text_input("BloodPressure")
SkinThickness = st.text_input("SkinThickness")
Insulin = st.text_input("Insulin")
BMI = st.text_input("BMI")
DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")
Age = st.text_input("Age")

#Code Untuk Prediksi
diabetes_diagnosis = ''

#Membuat tombol prediksi
if st.button('Test Prediksi') :
     diab_prediction = diabetes_model.predict([[Pregnancies, Glucose ,BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

     if (diab_prediction[0] == 1):
          diab_diagnosis = 'Pasien Terdiagnosa Diabetes'
     else :
          diab_diagnosis = 'Pasien Tidak Terdiagnosa Diabetes'

st.success(diab_diagnosis)



