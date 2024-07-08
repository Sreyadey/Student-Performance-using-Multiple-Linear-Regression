import streamlit as st


import pickle


scaler = pickle.load(open('scaler.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))


st.title('Student Performance Predictor')


study_hrs = st.number_input("Study Hours ")


prev_score = st.number_input("Previous Score :")


ec = st.multiselect("Extracurricular Activities",['Yes','No'])


sh = st.number_input("Sleep Hours :")


sqpp = st.number_input("Sample Question Papers Practiced :")


def prediction(study_hrs,prev_score,ec,sh,sqpp):
    print(study_hrs,prev_score,ec,sh,sqpp)
    if ec[0]=='No':
        ec=0
    else:
        ec=1
    updated_data = scaler.fit_transform([[study_hrs,prev_score,ec,sh,sqpp]])
    pred = model.predict(updated_data)
    st.write(f"Performance Index = {pred[0]}")
   
   


if st.button("Predict"):
    prediction(study_hrs,prev_score,ec,sh,sqpp)
