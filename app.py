import streamlit as st
import os

from extraction_REF import extract_referral
from extraction_BIL import extract_bill

from rag.audit import run_audit
from rag.chatbot import ask_chatbot

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="AI Healthcare Billing Auditor",
    page_icon="🏥",
    layout="wide"
)

# -------------------------------------------------
# Save Uploaded File
# -------------------------------------------------

def save_uploaded_file(uploaded_file):

    os.makedirs("docs", exist_ok=True)

    save_path = os.path.join("docs", uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return save_path


# -------------------------------------------------
# Initialize Session State
# -------------------------------------------------

if "referral_data" not in st.session_state:
    st.session_state.referral_data = None

if "bill_data" not in st.session_state:
    st.session_state.bill_data = None

if "checklist" not in st.session_state:
    st.session_state.checklist = None


# -------------------------------------------------
# Title
# -------------------------------------------------

st.title("🏥 AI Healthcare Billing Auditor")

st.write(
    "Upload the Referral, Lab Report and Bill. Generate the audit and ask questions about the case."
)


st.divider()

# -------------------------------------------------
# Upload Panel
# -------------------------------------------------

st.header("📂 Upload Documents")

col1, col2, col3 = st.columns(3)

with col1:

    referral_file = st.file_uploader(
        "Referral (PDF)",
        type=["pdf"]
    )

with col2:

    lab_report = st.file_uploader(
        "Lab Report (PDF)",
        type=["pdf"]
    )

with col3:

    bill_file = st.file_uploader(
        "Invoice Bill (PDF)",
        type=["pdf"]
    )

# -------------------------------------------------
# Extract Referral Immediately After Upload
# -------------------------------------------------

if referral_file is not None and st.session_state.referral_data is None:

    referral_path = save_uploaded_file(referral_file)

    with st.spinner("Extracting Referral..."):

        st.session_state.referral_data = extract_referral(referral_path)


# -------------------------------------------------
# Generate Audit
# -------------------------------------------------

st.write("")

generate = st.button(
    "🚀 Generate Audit",
    use_container_width=True
)

if generate:

    if referral_file is None or bill_file is None:

        st.error("Please upload both Referral and Invoice Bill.")

    else:

        referral_path = save_uploaded_file(referral_file)

        bill_path = save_uploaded_file(bill_file)

        if lab_report is not None:

            lab_path = save_uploaded_file(lab_report)

        st.success("Files Uploaded Successfully")

        with st.spinner("Running Audit..."):

            referral_data = st.session_state.referral_data

            bill_data = extract_bill(bill_path)

            checklist = run_audit(
                referral_path,
                bill_path
            )
            st.session_state.bill_data = bill_data
            st.session_state.checklist = checklist

    


        st.success("Audit Completed Successfully!")

        st.divider()

st.divider()

st.header("👤 Patient Details")


if st.session_state.referral_data:

    data = st.session_state.referral_data

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):

            st.markdown("### Patient Information")

            st.write(f"**Name:** {data['patient_name']}")
            st.write(f"**Gender:** {data['gender']}")
            st.write(f"**Date of Birth:** {data['dob']}")
            st.write(f"**Phone:** {data['phone']}")

    with c2:
        with st.container(border=True):

            st.markdown("### Referral Information")

            st.write(f"**Hospital:** {data['hospital_name']}")
            st.write(f"**Test:** {data['test_type']}")
            st.write(f"**Insurance:** {data['insurance_info']}")
            st.write(f"**Allergies:** {data['allergies']}")

# -------------------------------------------------
# Checklist
# -------------------------------------------------

st.divider()

st.header("📋 Audit Checklist")

if st.session_state.checklist:

    for item in st.session_state.checklist:

        col1, col2 = st.columns([4,1])

        with col1:

            st.write(f"**{item['check']}**")

        with col2:

            if item["status"] == "PASS":

                st.success("PASS")

            else:

                st.error("FAIL")

else:

    st.info("Generate an audit to view the checklist.")

# -------------------------------------------------
# Chatbot
# -------------------------------------------------

st.divider()

st.header("💬 AI Auditor Chatbot")

question = st.text_input(
    "Ask a question about the uploaded documents"
)

send = st.button("Send")

if send:

    if st.session_state.checklist is None:

        st.warning("Please generate the audit first.")

    elif question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            answer = ask_chatbot(

                question,

                st.session_state.referral_data,

                st.session_state.bill_data,

                st.session_state.checklist

            )

        st.success(answer)