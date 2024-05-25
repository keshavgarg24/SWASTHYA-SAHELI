import streamlit as st
import numpy as np
import joblib



scaler = joblib.load('Scaler.joblib')

logistic = joblib.load('Logistic.joblib')
svc = joblib.load('SVC.joblib')

st.title('Heart Disease Prediction')
st.subheader('Made for Swasthya Saheli')
st.write('Get your self checked from the comfort of your home')
st.write('Check below to know about the terms used')


sex_options = ['M', 'F']
chest_pain_options = ['ATA', 'NAP', 'ASY', 'TA']
resting_ecg_options = ['Normal', 'ST', 'LVH']
exercise_angina_options = ['N','Y']
st_slope_options = ['Up', 'Flat', 'Down']

age = st.number_input('Age')
sex = st.selectbox('Sex', sex_options)
chest_pain_type = st.selectbox('Chest Pain Type', chest_pain_options)
resting_bp = st.number_input('Resting Blood Pressure')
cholesterol = st.number_input('Cholesterol')
fasting_bs = st.number_input('Fasting Blood Sugar')
resting_ecg = st.selectbox('Resting ECG', resting_ecg_options)
max_hr = st.number_input('Max Heart Rate')
exercise_angina = st.selectbox('Exercise Induced Angina', exercise_angina_options)
oldpeak = st.number_input('Oldpeak')
st_slope = st.selectbox('ST Slope', st_slope_options)

if st.button('Predict'):
    input = [age,sex,chest_pain_type,resting_bp,cholesterol,fasting_bs,resting_ecg,max_hr,exercise_angina,oldpeak,st_slope]
    sex = {'M':0,'F':1}
    chest = {'ATA':0, 'NAP':1, 'ASY':2, 'TA':3}
    ecg = {'Normal':0, 'ST':1, 'LVH':2}
    exercise = {'N':0, 'Y':1}
    slope = {'Up':0, 'Flat':1, 'Down':2}
    input[1] = sex.get(input[1],input[1])
    input[2] = chest.get(input[2],input[2])
    input[6] = ecg.get(input[6],input[6])
    input[8] = exercise.get(input[8],input[8])
    input[10] = slope.get(input[10],input[10])

    input = [input]
    input = np.array(input)
    input = scaler.transform(input)

    res = logistic.predict(input)
    st.write('Result of KNN : ' + str(res[0]))
    st.write('Result of Random Forest : ' + str(res[0]))
    st.write('Result of Logistic Regression : ' + str(res[0]))
    
    res = svc.predict(input)
    st.write('Result of Support Vector Machine : ' + str(res[0]))
    st.write('0 means safe from heart diseases')
    st.write('1 means susceptible to heart diseases')


st.write('### **The Problem we are solving**')
st.write('This heart disease prediction project can evolve and make valuable contributions to early detection by developing a user-friendly interface for the predictive model that allows easy input of patient data, that can be self assessed with the help of portable biosensors which are used at homes/chemist shops or reports from some clinical tests.This data as input through the user friendly interface will give insights as to whether a person is at a risk of a heart disease and show the analytics accordingly.This will help all people to get an early prediction and they can then seek medical advice if needed. Although hospitals may have many similar softwares like this, normal people do not have access to anything of this sort at their homes.')
st.write('')
st.write('#### **Description of terms used**')
st.write('0.Age: age of the patient [years]')
st.write('1.Sex: sex of the patient [M: Male, F: Female]')
st.write('2.ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]')
st.write('3.RestingBP: resting blood pressure [mm Hg]')
st.write('4.Cholesterol: serum cholesterol [mm/dl]')
st.write('5.FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]')
st.write('6.RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes criteria]')
st.write('7.MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]')
st.write('8.ExerciseAngina: exercise-induced angina [Y: Yes, N: No]')
st.write('9.Oldpeak: oldpeak = ST [Numeric value measured in depression]')
st.write('10.ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]')
st.write('11.HeartDisease: output class [1: heart disease, 0: Normal]')

