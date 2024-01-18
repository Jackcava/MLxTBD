import os
import streamlit as st
import pandas as pd
import numpy as np
import pickle


# streamlit run TBD.py

st.set_page_config(page_title="Telomeropathy Diagnosis", page_icon=":medical_symbol:",layout="wide")
st.markdown("<h1 style='text-align: center; color: black;'>This web app is for supporting the clinician in the telomeropathy diagnosis.</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Please fill the form below and click the predict button to see how likely variant is pathogenic.</h3>", unsafe_allow_html=True)

with open('style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

filename = 'rf_tbd_other_Dec12_23.sav'
with open(filename, 'rb') as file:
    model = pickle.load(file)

patient_df = pd.read_csv("x_mode.csv", sep="\t")

st.divider()

count = 0
_, col1, col2, _ = st.columns([1, 1, 1, 1])

with col1:
  #GENDER
  gender = st.radio(
      "Patient gender:",
      ("Not selected", "Not known", "Male", "Female"),key="gender")
  if gender != "Not selected":
    count += 1
    st.success('✓')
  if gender == "Male":
      patient_df["SEX"] = 1
  elif gender == "Female":
      patient_df["SEX"] = 0

  #L<1°p
  l1p = st.selectbox(
      'Does the patient have a telomere length shorter than the 1°p?',
      ('','Yes', 'No', 'Not known'),key="l1p")
  if l1p != "":
    st.success('✓')
    count += 1
  if l1p == "Yes":
    patient_df["L1°p"] = 1
  elif l1p == "No":
    patient_df["L1°p"] = 0

  #Familiarity
  fam = st.selectbox(
      'Does the patient have an affected family member?',
      ('','Yes', 'No', 'Not known'),key="fam")
  if fam != "":
    st.success('✓')
    count += 1
  if fam == "Yes":
    patient_df["Familiarity"] = 1
  elif fam == "No":
    patient_df["Familiarity"] = 0

  #ALL CYTOPENIA
  all_cyt = st.selectbox(
      'Does the patient have any kind of cytopenia?',
      ('','Yes', 'No', 'Not known'),key="all_cyt")
  if all_cyt != "":
    st.success('✓')
    count += 1
  if all_cyt == "Yes":
    patient_df["ALL CYTOPENIA"] = 1
  elif all_cyt == "No":
    patient_df["ALL CYTOPENIA"] = 0

  #Autoimmunity
  autoimm = st.selectbox(
      'Does the patient have any autoimmunities?',
      ('','Yes', 'No', 'Not known'),key="autoimm")
  if autoimm != "":
    st.success('✓')
    count += 1
  if autoimm == "Yes":
    patient_df["Any Autoimmunity"] = 1
  elif autoimm == "No":
    patient_df["Any Autoimmunity"] = 0

  #Mucocutaneous alterations
  mucoalt = st.selectbox(
      'Does the patient have any mucocutaneous alterations?',
      ('','Yes', 'No', 'Not known'),key="mucoalt")
  if mucoalt != "":
    st.success('✓')
    count += 1
  if mucoalt == "Yes":
    patient_df["Mucocutaneaous alterations"] = 1
  elif mucoalt == "No":
    patient_df["Mucocutaneaous alterations"] = 0

  # #Neuro-malformations
  # neuro = st.selectbox(
  #     'Does the patient have any neuro-malformations?',
  #     ('','Yes', 'No', 'Not known'),key="neuro")
  # if neuro != "":
  #   st.success('✓')
  #   count += 1
  # if neuro == "Yes":
  #   patient_df["Neuro-malformations"] = 1
  # elif neuro == "No":
  #   patient_df["Neuro-malformations"] = 0

  #Other malformations
  malf = st.selectbox(
      'Does the patient have any other malformations?',
      ('','Yes', 'No', 'Not known'),key="malf")
  if malf != "":
    st.success('✓')
    count += 1
  if malf == "Yes":
    patient_df["Other malformations"] = 1
  elif malf == "No":
    patient_df["Other malformations"] = 0

with col2:

  #AGE
  age = st.radio("Enter the patient's age at the time of sampling:",
                 ("Not selected", "Not known", "younger than 18 y.o.", "older than 18 y.o."),key="age")
  if age != "Not selected":
    st.success('✓')
    count += 1
  if age == "younger than 18 y.o.":
    patient_df["AgeSampleGroup"] = 0
  elif age == "older than 18 y.o.":
    patient_df["AgeSampleGroup"] = 1

  #L<10°p
  l10p = st.selectbox(
      'Does the patient have a telomere length shorter than the 10°p?',
      ('','Yes', 'No', 'Not known'),key="l10p")
  if l10p != "":
    st.success('✓')
    count += 1
  if l10p == "Yes":
    patient_df["L10°p"] = 1
  elif l10p == "No":
    patient_df["L10°p"] = 0

  #BMF
  bmf = st.selectbox(
      'Does the patient have a Bone Marrow Failure (BMF)?',
      ('','Yes', 'No', 'Not known'),key="bmf")
  if bmf != "":
    st.success('✓')
    count += 1
  if bmf == "Yes":
    patient_df["BMF"] = 1
  elif bmf == "No":
    patient_df["BMF"] = 0

  #PERIPHERAL CYTOPENIA
  per_cyt = st.selectbox(
      'Does the patient have any peripheral cytopenia?',
      ('','Yes', 'No', 'Not known'),key="per_cyt")
  if per_cyt != "":
    st.success('✓')
    count += 1
  if per_cyt == "Yes":
    patient_df["Peripheral Cytopenia"] = 1
  elif per_cyt == "No":
    patient_df["Peripheral Cytopenia"] = 0

  #Immunodeficiency
  immunodef = st.selectbox(
      'Does the patient have any immunodeficiency?',
      ('','Yes', 'No', 'Not known'),key="immunodef")
  if immunodef != "":
    st.success('✓')
    count += 1
  if immunodef == "Yes":
    patient_df["Any immunodeficiency"] = 1
  elif immunodef == "No":
    patient_df["Any immunodeficiency"] = 0

  # #Pulmonary disease
  # puldef = st.selectbox(
  #     'Does the patient have any pulmonary diseases?',
  #     ('','Yes', 'No', 'Not known'),key="puldef")
  # if puldef != "":
  #   st.success('✓')
  #   count += 1
  # if puldef == "Yes":
  #   patient_df["Pulmonary disease"] = 1
  # elif puldef == "No":
  #   patient_df["Pulmonary disease"] = 0

  #Hepatopathy
  hepa = st.selectbox(
      'Does the patient have hepatopathy?',
      ('','Yes', 'No', 'Not known'),key="hepa")
  if hepa != "":
    st.success('✓')
    count += 1
  if hepa == "Yes":
    patient_df["Hepathopathy"] = 1
  elif hepa == "No":
    patient_df["Hepathopathy"] = 0

  # #Ophthalmopathy
  # opht = st.selectbox(
  #     'Does the patient have ophthalmopathy?',
  #     ('','Yes', 'No', 'Not known'),key="opht")
  # if opht != "":
  #   st.success('✓')
  #   count += 1
  # if opht == "Yes":
  #   patient_df["Ophtalmopathy"] = 1
  # elif opht == "No":
  #   patient_df["Ophtalmopathy"] = 0

st.divider()
#st.write(count)
_, col1, col2, _ = st.columns([1, 1, 1, 1])

# for debugging uncomment the following lines:
# if st.checkbox('Show patient'):
#     st.subheader('Patient')
#     st.write(patient_df)

with col1:
  if st.button('Predict'):
    #patient_df = pd.DataFrame(patient, index=[0])
    pred = model.predict_proba(patient_df)
    st.write(pred)
    if count > 12:
      if pred[0][0] > 0.50:
        st.write("The patient has **:red[TBD]** with a probability of:", round(pred[0][0]*100,2), "%")
      else:
        st.write("The patient has a diagnosis **:red[other]** than TBD with a probability of:", round(pred[0][1]*100,2), "%")
    else:
      st.error("All the fields must be filled.")

l_variables = ["gender","l1p","fam","all_cyt","autoimm","mucoalt","malf","age","l10p","bmf","per_cyt","immunodef","hepa"]

with col2:
  if st.button('Clear all'):
    for el in l_variables:
      del st.session_state[el]
      if el == "gender" or el == "age":
        st.session_state[el] = "Not selected"
      else:
        st.session_state[el] = ""
    st.experimental_rerun()