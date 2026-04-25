import requests
import json

API_URL = 'http://127.0.0.1:5002/predict'

# Complete payload based on your CSV screenshot
sample_data = {
    "Claim_Am": 5086294,
    "Patient_Ag": 24,
    "Patient_G": "Female",
    "Patient_Ci": "New York",
    "Patient_St": "FL",
    "Hospital_Il": 827,
    "Provider_1": "Specialist",
    "Provider_S": "Specialist",
    "Provider_C": "San Diego",
    "Provider_E": "PA",
    "Diagnosis_": "H25.9",
    "Procedure": 93571,
    "Number_o": 5,
    "Admission": "Trauma",
    "Discharge": "Deceased",
    "Length_of": 0,
    "Service_Ty": "Emergenc",
    "Deductibk": 3047.55,
    "CoPay_An": 847.4,
    "Number_c": 0, # Number_of_Previous_Claims
    "Number_o_1": 15, # Number_of_Procedures
    "Provider_f": "TRUE", # Claim_Submitted_Late
    "Claim_Sui": "FALSE"  # Is_Fraudulent (exclude this if your model dropped it)
}
# sample_data = {
#     "Claim_Amount": 897322.71,
#     "Patient_Age": 89,
#     "Patient_Gender": "Other",
#     "Patient_City": "Austin",
#     "Patient_State": "AZ",
#     "Hospital_ID": 490,
#     "Provider_Type": "Specialist Office",
#     "Provider_Specialty": "Cardiology",
#     "Provider_City": "San Francisco",
#     "Provider_State": "MN",
#     "Diagnosis_Code": "I10",
#     "Procedure_Code": 93040,
#     "Number_of_Procedures": 9,
#     "Admission_Type": "Emergency",
#     "Discharge_Type": "Rehab/Skilled Nursing",
#     "Length_of_Stay_Days": 0,
#     "Service_Type": "Laboratory",
#     "Deductible_Amount": 4332.3,
#     "CoPay_Amount": 674.51,
#     "Number_of_Previous_Claims_Patient": 0,
#     "Number_of_Previous_Claims_Provider": 17,
#     "Provider_Patient_Distance_Miles": 408.98,
#     "Claim_Submitted_Late": 1  # Changed True to 1 for API safety
# }

def run_test():
    try:
        response = requests.post(API_URL, json=sample_data)
        if response.status_code == 200:
            print(f"Response: {response.json()}")
        else:
            print(f"Failed with status code: {response.status_code}")
            print(f"Error detail: {response.text}")
    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    run_test()