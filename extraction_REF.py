import fitz
import json



from Database_11.search import search_patient, search_hospital
from Database_11.create_ticket import create_ticket

from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def extract_pdf_text(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text() + "\n"

    doc.close()

    return text


# -------------------------------------------------
# Read Referral PDF
# -------------------------------------------------



# -------------------------------------------------
# Extract Referral Information
# -------------------------------------------------

# -------------------------------------------------
# Extract Referral Information
# -------------------------------------------------

def extract_referral(pdf_path):

    text = extract_pdf_text(pdf_path)

    prompt = f"""
You are an expert healthcare document extraction assistant.

Extract ONLY the following entities.

Return ONLY valid JSON.

{{
    "hospital_name": null,
    "patient_name": null,
    "gender": null,
    "dob": null,
    "address": null,
    "phone": null,
    "test_type": null,
    "allergies": null,
    "insurance_info": null
}}

Instructions:
- Return ONLY JSON.
- If a value is missing, return null.
- Do not guess values.
- Do not add explanations.

Document:

{text}
"""
    response = client.models.generate_content(

        model="gemini-2.5-flash",

        contents=prompt,

        config=types.GenerateContentConfig(
            response_mime_type="application/json"
        )

    )

    response_text = response.text.strip()

    if response_text.startswith("```"):

        response_text = (
            response_text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

    extracted_data = json.loads(response_text)

    return extracted_data
    

# -------------------------------------------------
# Main
# -------------------------------------------------

if __name__ == "__main__":

    try:

        pdf_path = "docs/SD1.pdf"

        extracted_data = extract_referral(pdf_path)

        print("\n========== Extracted Entities ==========\n")
        print(json.dumps(extracted_data, indent=4))

        # -------------------------------------------------
        # STEP 1 : Patient Validation
        # -------------------------------------------------

        patient = search_patient(extracted_data)

        if patient:

            print("\n✅ Patient Exists")

            # -------------------------------------------------
            # STEP 2 : Hospital Validation
            # -------------------------------------------------

            hospital = search_hospital(extracted_data)

            if hospital:

                print("✅ Hospital Tie-up Found")

                discount_status = "YES"

            else:

                print("❌ Hospital Not in Tie-up Database")

                discount_status = "NO"

            print("Discount Applied :", discount_status)

            # -------------------------------------------------
            # STEP 3 : Ticket Creation
            # -------------------------------------------------

            ticket_id = create_ticket(

                patient,

                hospital,

                extracted_data

            )

            print("\n===================================")
            print("🎉 Ticket Created Successfully")
            print("Ticket ID :", ticket_id)
            print("===================================")

        else:

            print("\n❌ Patient Not Found")
            print("Ticket NOT Created")

    except json.JSONDecodeError:

        print("Gemini did not return valid JSON.")

    except Exception as e:

        print("\nError :", e)