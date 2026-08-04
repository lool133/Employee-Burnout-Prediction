import streamlit as st
import pandas as pd
import joblib
from groq import Groq


# ================= Page Setup =================

st.set_page_config(
    page_title="Employee Burnout AI",
    page_icon="🧠",
    layout="wide"
)


# ================= Load Model =================

model = joblib.load("burnout_model.pkl")


# ================= LLM =================

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)



# ================= Title =================

st.title("🧠 Employee Burnout Prediction System")

st.caption(
    "Machine Learning + Large Language Model (LLM)"
)



# ================= Inputs =================
st.subheader("👤 Employee Information")

col1,col2 = st.columns(2)


with col1:

    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )


    company = st.selectbox(
        "Company Type",
        ["Service","Product"]
    )


    wfh = st.selectbox(
        "WFH Setup Available",
        ["Yes","No"]
    )


    designation = st.slider(
        "Designation",
        0,5,2
    )


    resource = st.slider(
        "Resource Allocation",
        0,10,5
    )



with col2:

    fatigue = st.slider(
        "Mental Fatigue Score",
        0.0,10.0,5.0
    )


    year = st.number_input(
        "Joining Year",
        2000,
        2030,
        2008
    )


    month = st.slider(
        "Joining Month",
        1,12,1
    )


    day = st.slider(
        "Joining Day",
        1,31,1
    )



# ================= Prediction =================
st.divider()

st.subheader("📊 Prediction Result")

if st.button("🚀 Predict Burnout", use_container_width=True):

    input_data = pd.DataFrame({

        "Gender":[gender],
        "Company Type":[company],
        "WFH Setup Available":[wfh],
        "Designation":[designation],
        "Resource Allocation":[resource],
        "Mental Fatigue Score":[fatigue],
        "Joining_Year":[year],
        "Joining_Month":[month],
        "Joining_Day":[day]

    })

    prediction = model.predict(input_data)[0]

    if prediction < 0.33:
        level = "🟢 LOW"

    elif prediction < 0.66:
        level = "🟡 MEDIUM"

    else:
        level = "🔴 HIGH"

    st.success("Prediction Completed Successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Burn Rate",
            value=f"{prediction:.3f}"
        )

    with col2:
        st.metric(
            label="Risk Level",
            value=level
        )

    st.progress(min(float(prediction),1.0))

    st.caption(f"Burnout Probability : {prediction*100:.1f}%")

    st.divider()

    st.subheader("🤖 AI Recommendation")

    prompt = f"""
You are an HR expert.

Employee Data

Gender: {gender}

Company Type: {company}

WFH Setup: {wfh}

Designation: {designation}

Resource Allocation: {resource}

Mental Fatigue Score: {fatigue}

Joining Year: {year}

Joining Month: {month}

Joining Day: {day}

Predicted Burn Rate: {prediction:.3f}

Risk Level: {level}

Explain WHY the employee reached this burnout level based on the employee data.

Then provide ONLY 3 practical recommendations.

Keep the answer under 80 words.


Give only:

📌 Reason:
(one long sentence).

💡 Solutions:
- Solution 1
- Solution 2
- Solution 3

Maximum 70 words.
"""

    with st.spinner("AI is analyzing..."):

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[

                {
                    "role":"system",
                    "content":"You are an HR assistant. Keep the answer short."
                },

                {
                    "role":"user",
                    "content":prompt
                }

            ]

        )

        result = response.choices[0].message.content

    with st.expander("📌 AI Analysis", expanded=True):

        st.write(result)