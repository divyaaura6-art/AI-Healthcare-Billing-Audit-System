import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from extraction_REF import extract_referral
from extraction_BIL import extract_bill

from rag.checklist import generate_checklist

from rag.retrieve import retrieve_clause


# ---------------------------------------
# Run Audit
# ---------------------------------------

def run_audit(referral_pdf, bill_pdf):

    print("\n========== REFERRAL EXTRACTION ==========\n")

    referral_data = extract_referral(referral_pdf)

    print(referral_data)

    print("\n========== BILL EXTRACTION ==========\n")

    bill_data = extract_bill(bill_pdf)

    print(bill_data)

    print("\n========== GENERATING CHECKLIST ==========\n")

    checklist = generate_checklist(

        referral_data,

        bill_data

    )

    for item in checklist:

        print(f"\nCheck : {item['check']}")

        print("Status :", item["status"])

        # ---------------------------------
        # Agreement Checks
        # ---------------------------------

        if item["type"] == "agreement":

            print("\nSearching Agreement...")

            results = retrieve_clause(item["query"])

            documents = results["documents"][0]

            print("\nRelevant Clauses:\n")

            for i, clause in enumerate(documents):

                print(f"Clause {i+1}")

                print(clause)

                print("-" * 50)

    return checklist


# ---------------------------------------
# Main
# ---------------------------------------

if __name__ == "__main__":

    run_audit(

        "docs/SD1.pdf",

        "docs/BD1.pdf"

    )