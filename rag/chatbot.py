import json

from .retrieve import retrieve_clause


from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ---------------------------------------
# Chatbot Function
# ---------------------------------------

def ask_chatbot(question, referral_data, bill_data, checklist):

    results = retrieve_clause(question)

    agreement_clause = "\n\n".join(
        results["documents"][0]
    )

    prompt = f"""
You are an AI Healthcare Billing Audit Assistant.

You are helping a billing auditor answer questions about a patient's case.

=========================
REFERRAL INFORMATION
=========================

{json.dumps(referral_data, indent=4)}

=========================
BILL INFORMATION
=========================

{json.dumps(bill_data, indent=4)}

=========================
AUDIT CHECKLIST
=========================

{json.dumps(checklist, indent=4)}

=========================
RELEVANT AGREEMENT CLAUSES
=========================

{agreement_clause}

=========================
USER QUESTION
=========================

{question}

Instructions

1. Answer ONLY using the Referral, Bill, Checklist and Agreement.

2. If the question is about the agreement, explain using the retrieved clauses.

3. If the question is about the audit, explain using the checklist.

4. If the answer cannot be found, reply:

"I couldn't find this information in the uploaded documents."

5. Keep answers professional and concise.
"""

    try:

        response = client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt

        )

        return response.text

    except Exception as e:

        return f"Error: {e}"