import streamlit as st

def calculate_prehospital_heart_score(age, mi_history, hf_history, ecg_findings, troponin_level):
    score = 0
    if age >= 65:
        score += 2
    elif age >= 45:
        score += 1

    if mi_history:
        score += 2

    if hf_history:
        score += 1

    if ecg_findings == "ST depression":
        score += 2
    elif ecg_findings == "T-wave inversion":
        score += 1

    if troponin_level > 3:
        score += 2
    elif troponin_level > 0.03:
        score += 1

    return score

def main():
    st.title("Prehospital Heart Score Calculator")
    st.write("This app calculates the prehospital heart score.")

    age = st.number_input("Age", min_value=0, max_value=120)
    mi_history = st.checkbox("History of Myocardial Infarction")
    hf_history = st.checkbox("History of Heart Failure")
    ecg_findings = st.selectbox("Initial ECG Findings", ["Normal", "ST depression", "T-wave inversion"])
    troponin_level = st.number_input("Initial Troponin Level", min_value=0.0)

    if st.button("Calculate"):
        score = calculate_prehospital_heart_score(age, mi_history, hf_history, ecg_findings, troponin_level)
        st.write(f"Prehospital heart score: {score}")

if __name__ == "__main__":
    main()
