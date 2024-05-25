import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings

st.write("""
    # Diabetes Prediction App
    
    ##### This app predicts the diabetes in pregnant women!
    ### Made for Swasthya Saheli
""")
warnings.filterwarnings('ignore')

df = pd.read_csv('diabetes.csv')

st.sidebar.header('User Input Parameters')

def user_input_features():
    Glucose = st.sidebar.slider('Glucose', 0.0, 199.0, 18.0)
    BloodPressure = st.sidebar.slider('Blood Pressure', 0.0, 122.0, 10.0)
    Insulin = st.sidebar.slider('Insulin', 0.0, 846.0, 80.3)
    Age = st.sidebar.slider('Age', 21.0, 81.0, 21.0)
    data = {'Glucose': Glucose,
            'BloodPressure': BloodPressure,
            'Insulin': Insulin,
            'Age': Age 
    }

    features = pd.DataFrame(data, index=[0])
    return features

f = user_input_features()

st.subheader('User Input Parameters')
st.write(f)

st.subheader('Column names')
st.write(df.columns)



X = df.drop(['Pregnancies','SkinThickness','BMI','DiabetesPedigreeFunction','Outcome'], axis=1)#df.drop('Outcome', axis=1)
y = df['Outcome']

# Train a logistic regression model
clf = LogisticRegression(random_state=42)
clf.fit(X, y)

# Use the model to predict the outcomes for the test set
test_preds = clf.predict(f)

#
# Save the predicted outcomes to a CSV file
#pred_df = pd.DataFrame({'Actual': y_test, 'Predicted': test_preds})
#pred_df.to_csv('predictions.csv', index=False)

st.subheader('The Predicted results are: ')
st.write(test_preds)

if test_preds==0:
    st.header(' You are Non Diabetic')
elif test_preds==1:
    st.header('You are most probably a Diabetic')