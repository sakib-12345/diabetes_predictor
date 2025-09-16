import numpy as np
import pickle
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('Diabetes_prediction_model.sav', 'rb'))

#creating fuction for prediction

def test(user_input):
    user_input_array = np.asarray(user_input)
    user_input_reshaped = user_input_array.reshape(1,-1)

    prediction = loaded_model.predict(user_input_reshaped)[0]
    if prediction == 0:
        return "The person is not diabetic"
    else:
        return "The person is diabetic"
    


#creating the main function
def main():
    st.title("Diabetes Prediction Web App")

    #getting the input data from the user
    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("Blood Pressure value")
    SkinThickness = st.text_input("Skin Thickness value")
    Insulin = st.text_input("Insulin Level")
    Bmi = st.text_input("BMI value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    Age = st.text_input("Age of the Person")

    diagnosis = ""

    #creating a button for prediction
    if st.button("Diabetes Test Result"):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, Bmi, DiabetesPedigreeFunction, Age]
        diagnosis = test(user_input)

    st.success(diagnosis)

if __name__ == '__main__':
    main()

# command to run the app: python -m streamlit run Diabetes_prediction--WEBAPP.py
# to stop the app: ctrl + c
