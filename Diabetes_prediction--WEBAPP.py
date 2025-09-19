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

    home, about = st.tabs(["Home", "About Me"])
    with home:
        st.title("Diabetes Prediction Web App BY SAKIB")
        st.warning("*Warning: This prediction is not 100% accurate. Please consult a medical professional for a definitive diagnosis.*")
        col1, col2 = st.columns(2)
        #getting the input data from the user
        with col1:
            Pregnancies = st.number_input("Number of Pregnancies")
            Glucose = st.number_input("Glucose Level")
            BloodPressure = st.number_input("Blood Pressure value")
            SkinThickness = st.number_input("Skin Thickness value")
        with col2:    
            Insulin = st.number_input("Insulin Level")
            Bmi = st.number_input("BMI value")
            DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function value")
            Age = st.number_input("Age of the Person")

        diagnosis = ""

        #creating a button for prediction
        if st.button("Diabetes Test Result"):
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, Bmi, DiabetesPedigreeFunction, Age]
            diagnosis = test(user_input)

        st.success(diagnosis)
        
    with about:
        st.header("About Me")
        col4, col5 = st.columns(2, gap="small")
        with col4:
            st.image("image.png", width=150,)
        with col5:    
            st.write("**Sakib Hossain Tahmid**")
            st.write("Class: 12")
            st.write("Dhaka College")
        st.write("---")
        st.text("I am a passionate data scientist and machine learning enthusiast with a strong foundation in Python programming. I love exploring new technologies and applying them to solve real-world problems. My goal is to leverage data to drive informed decision-making and create impactful solutions.")
        st.write("Connect with me:")
        st.markdown("[Facebook](https://www.facebook.com/sakibhossain.tahmid)")
    st.markdown(
        f'<div style="text-align: center; color: grey;">&copy; 2025 Sakib Hossain Tahmid. All Rights Reserved.</div>',
        unsafe_allow_html=True
        )    

if __name__ == '__main__':
    main()

# command to run the app: python -m streamlit run Diabetes_prediction--WEBAPP.py
# to stop the app: ctrl + c


