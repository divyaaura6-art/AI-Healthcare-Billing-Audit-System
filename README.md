# AI Healthcare Billing Audit System

An AI-powered healthcare billing audit application that uses
**Retrieval-Augmented Generation (RAG)** and **Google's Gemini API** to
automate document validation, patient verification, and billing audits.

------------------------------------------------------------------------

## About the Project

Healthcare billing audits often require auditors to manually compare
referral documents, patient records, hospital agreements, and billing
invoices before approving payments. This process is repetitive,
time-consuming, and susceptible to human error.

This project was developed to explore how Artificial Intelligence can
simplify and automate this workflow. By combining document
understanding, database validation, and Retrieval-Augmented Generation
(RAG), the application assists auditors in verifying billing
information, identifying inconsistencies, and generating explainable
audit reports.

The project demonstrates the practical application of AI in healthcare
document processing through an end-to-end billing audit solution
developed using **Python**, **Streamlit**, **SQLite**, **Google
Gemini**, and a custom **RAG pipeline**.

------------------------------------------------------------------------

## Motivation

The objective of this project is to build an intelligent healthcare
billing audit system capable of:

-   Extracting structured information from referral documents.
-   Extracting billing information from invoices.
-   Validating patient records using a healthcare database.
-   Verifying hospital partnership information.
-   Generating audit tickets for every patient visit.
-   Retrieving agreement information using Retrieval-Augmented
    Generation.
-   Comparing referral and billing information.
-   Detecting billing discrepancies.
-   Producing transparent AI-assisted audit reports.

------------------------------------------------------------------------

## Features

-   Referral document upload
-   Billing invoice upload
-   AI-powered document understanding using Google Gemini
-   Structured JSON extraction
-   Patient validation using SQLite
-   Hospital partnership validation
-   Active audit ticket generation
-   Retrieval-Augmented Generation (RAG) based billing audit
-   Agreement-aware validation
-   Interactive audit chatbot
-   Explainable audit reports
-   Modular project architecture

------------------------------------------------------------------------

## Tech Stack

  Layer            Technology
  ---------------- ---------------------------------------------
  Frontend         Streamlit
  Backend          Python
  Database         SQLite
  AI               Google Gemini API
  Retrieval        Custom Retrieval-Augmented Generation (RAG)
  PDF Processing   PyMuPDF
  Environment      python-dotenv

------------------------------------------------------------------------

## Backend Architecture

``` text
                           Streamlit Frontend
                                   │
      ┌────────────────────────────┼────────────────────────────┐
      │                            │                            │
      ▼                            ▼                            ▼
 Referral Processing        Billing Processing          Audit Chatbot
      │                            │                            │
      ▼                            ▼                            ▼
 Gemini Extraction         Gemini Extraction             RAG Chat
      │                            │
      └───────────────┬────────────┘
                      ▼
              Validation Layer
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
 Patient DB      Hospital DB     Ticket Manager
      │               │                │
      └───────────────┴────────────────┘
                      ▼
               RAG Audit Engine
                      │
                      ▼
          Explainable Audit Report
```

------------------------------------------------------------------------

## What the Application Provides

-   Extracts information from referral documents.
-   Extracts structured billing information from invoices.
-   Validates patient records against a database.
-   Verifies hospital partnership information.
-   Creates audit tickets.
-   Retrieves agreement information using RAG.
-   Performs AI-assisted billing verification.
-   Detects billing inconsistencies and agreement violations.
-   Generates explainable audit reports.
-   Supports audit-related queries through an interactive chatbot.

------------------------------------------------------------------------

## Project Structure

``` text
AI-Healthcare-Billing-Audit-System/
│
├── app.py
├── config.py
├── extraction_REF.py
├── extraction_BIL.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── rag/
│   ├── audit.py
│   ├── chatbot.py
│   └── knowledge_base/
│
├── Database_11/
│   ├── create_DB.py
│   ├── create_ticket.py
│   ├── search.py
│   └── healthcare.db
│
├── uploads/
├── extracted_documents/
└── assets/
```

------------------------------------------------------------------------

## AI Components

The application uses Google's Gemini API to extract structured
information from healthcare documents. The extracted information is
converted into JSON format before being validated against the healthcare
database.

The custom Retrieval-Augmented Generation (RAG) pipeline retrieves
relevant hospital agreement information and combines it with extracted
document data to generate context-aware billing audit decisions and
explainable reports.

------------------------------------------------------------------------

## Database Design

The application currently maintains three primary entities:

-   Patients
-   Hospitals
-   Audit Tickets

These entities support patient validation, hospital verification, and
complete audit workflow management.

------------------------------------------------------------------------

## Libraries Used

### Core

-   os
-   json
-   sqlite3
-   pathlib
-   datetime

### AI

-   google-genai

## Embedding Model

- `sentence-transformers` (`all-MiniLM-L6-v2`)

## Vector Database

- `chromadb`

### Frontend

-   streamlit

### Document Processing

-   PyMuPDF (fitz)

### Environment

-   python-dotenv

------------------------------------------------------------------------

## Future Scope

-   User authentication
-   Role-based access control
-   OCR support for scanned documents
-   Multi-hospital support
-   Cloud database integration
-   Dashboard analytics
-   Audit history management
-   PDF audit report generation
-   API integration with Hospital Management Systems
-   Automated compliance reporting

------------------------------------------------------------------------

## Installation

Clone the repository.

``` bash
git clone https://github.com/<your-username>/AI-Healthcare-Billing-Audit-System.git
```

Navigate to the project directory.

``` bash
cd AI-Healthcare-Billing-Audit-System
```

Install dependencies.

``` bash
pip install -r requirements.txt
```

Create a `.env` file.

``` text
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application.

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

## Author

**Divyadarshini Palanipandian**

B.Tech Computer Science and Engineering

Vellore Institute of Technology, Chennai

------------------------------------------------------------------------

## Acknowledgement

This project was developed during my **Summer Internship at KANINI
Software Solutions**. It demonstrates the application of Artificial
Intelligence, Retrieval-Augmented Generation (RAG), and intelligent
document processing to automate healthcare billing audits through a
scalable and modular workflow.
