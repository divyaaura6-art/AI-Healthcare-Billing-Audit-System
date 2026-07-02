


# ---------------------------------------
# Generate Checklist
# ---------------------------------------

def generate_checklist(referral_data, bill_data):

    checklist = []

    # ---------------------------------------
    # Patient Name
    # ---------------------------------------

    if referral_data["patient_name"] == bill_data["patient_name"]:

        checklist.append({
            "check": "Patient Name",
            "status": "PASS",
            "reason": "Patient names match.",
            "type": "python"
        })

    else:

        checklist.append({
            "check": "Patient Name",
            "status": "FAIL",
            "reason": "Patient names do not match.",
            "type": "python"
        })

    # ---------------------------------------
    # Hospital Name
    # ---------------------------------------

    if referral_data["hospital_name"] == bill_data["hospital_name"]:

        checklist.append({
            "check": "Hospital Name",
            "status": "PASS",
            "reason": "Hospital names match.",
            "type": "python"
        })

    else:

        checklist.append({
            "check": "Hospital Name",
            "status": "FAIL",
            "reason": "Hospital names do not match.",
            "type": "python"
        })

    # ---------------------------------------
    # Test Type
    # ---------------------------------------

    if referral_data["test_type"] == bill_data["test_type"]:

        checklist.append({
            "check": "Test Type",
            "status": "PASS",
            "reason": "Test types match.",
            "type": "python"
        })

    else:

        checklist.append({
            "check": "Test Type",
            "status": "FAIL",
            "reason": "Test type mismatch.",
            "type": "python"
        })

    # ---------------------------------------
    # Insurance
    # ---------------------------------------

    if referral_data["insurance_info"] == bill_data["insurance_coverage_applied"]:

        checklist.append({
            "check": "Insurance",
            "status": "PASS",
            "reason": "Insurance information matches.",
            "type": "python"
        })

    else:

        checklist.append({
            "check": "Insurance",
            "status": "FAIL",
            "reason": "Insurance information mismatch.",
            "type": "python"
        })

    # ---------------------------------------
    # Agreement Checks
    # ---------------------------------------

    checklist.append({
        "check": "Maximum Test Cost",
        "status": "PENDING",
        "reason": "",
        "type": "agreement",
        "query":"Maximum allowed cost for " + bill_data["test_type"]
    })

    checklist.append({
        "check": "Extra Fees",
        "status": "PENDING",
        "reason": "",
        "type": "agreement",
        "query":"Extra fees allowed for " + bill_data["test_type"]
    })

    checklist.append({
        "check": "Insurance Coverage Rules",
        "status": "PENDING",
        "reason": "",
        "type": "agreement",
        "query":"Insurance coverage for " + bill_data["test_type"],

    })

    return checklist