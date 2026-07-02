import fitz
import json
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ---------------------------------------
# Function to Extract Text from PDF
# ---------------------------------------

def extract_pdf_text(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text() + "\n"

    doc.close()

    return text

# ---------------------------------------
# Extract Bill Information
# ---------------------------------------

def extract_bill(pdf_path):

    text = extract_pdf_text(pdf_path)

    prompt = f"""
You are an expert medical invoice extraction assistant.

Extract ONLY the following information.

Return ONLY valid JSON.

Use this exact JSON format:

{{
    "test_type": null,
    "patient_name": null,
    "hospital_name": null,

    "drawn_by": null,

    "drawn_at": {{
        "date": null,
        "time": null
    }},

    "bill_info": {{
        "base_cost": null,
        "extra_fees": null,
        "net_total": null
    }},

    "performed_by": null,

    "insurance_coverage_applied": null
}}

Instructions:
- Return ONLY valid JSON.
- If a field is missing return null.
- Do not guess values.

Invoice:

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

    bill_data = json.loads(response_text)

    return bill_data


# ---------------------------------------
# Main
# ---------------------------------------

if __name__ == "__main__":

    try:

        pdf_path = "docs/BD1.pdf"

        bill_data = extract_bill(pdf_path)

        print("\n========== Bill Entities ==========\n")
        print(json.dumps(bill_data, indent=4))

        print("\n========== Extracted Fields ==========\n")

        print("Test Type                :", bill_data["test_type"])
        print("Patient Name             :", bill_data["patient_name"])
        print("Hospital Name            :", bill_data["hospital_name"])
        print("Doctor (Drawn By)        :", bill_data["drawn_by"])

        print("\nDrawn At")
        print("Date                     :", bill_data["drawn_at"]["date"])
        print("Time                     :", bill_data["drawn_at"]["time"])

        print("\nPerformed By             :", bill_data["performed_by"])
        print("Insurance Applied        :", bill_data["insurance_coverage_applied"])

        print("\n========== Bill Information ==========\n")

        print("Base Cost                :", bill_data["bill_info"]["base_cost"])
        print("Extra Fees               :", bill_data["bill_info"]["extra_fees"])
        print("Net Total                :", bill_data["bill_info"]["net_total"])

    except json.JSONDecodeError:

        print("Gemini returned invalid JSON.")

    except Exception as e:

        print("Error :", e)
