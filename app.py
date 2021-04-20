import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

model = pickle.load(open('model.pkl', 'rb'))

def predict_immo(MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude):
    input=np.array([[MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude]])
    pred=model.predict(input)
    return(pred)

#StandardScaler().fit_transform()

def main():
    st.title("California Housing Prices Prediction")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">California Housing Prices Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    MedInc = st.text_input("MedInc","Type Here")
    HouseAge = st.text_input("HouseAge","Type Here")
    AveRooms = st.text_input("AveRooms","Type Here")
    AveBedrms = st.text_input("AveBedrms","Type Here")
    Population = st.text_input("Population","Type Here")
    AveOccup = st.text_input("AveOccup","Type Here")
    Latitude = st.text_input("Latitude","Type Here")
    Longitude = st.text_input("Longitude","Type Here")

    if st.button("Predict"):
        output=predict_immo(MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude)
        st.success(output)

if __name__=='__main__':
    main()

