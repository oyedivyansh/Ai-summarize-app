# 🧠 AI Document Summarizer

An AI-powered document summarization application that allows users to upload documents and generate concise summaries in **English and Hindi**.  
The system uses **Cerebras LLM (GPT-OSS-120B)** for fast inference and accurate summarization.

---

# 🚀 Project Overview

The AI Document Summarizer enables users to upload documents such as **PDF, DOCX, or TXT files** and automatically generate a concise summary limited to **500 words**.

The application is built with a **simple and user-friendly interface using Streamlit**, allowing users to upload files, generate summaries, and download the results easily.

---

# 🎯 Objectives

The main objectives of this project are:

- Generate **concise summaries limited to 500 words**
- Support **multiple document formats (PDF, DOCX, TXT)**
- Provide **English summary and Hindi translation**
- Offer a **simple and intuitive user interface**
- Enable **easy deployment and public access**

---

# 📂 Project Structure
AI-Document-Summarizer
│
├── app.py # Streamlit frontend application

├── utils.py # Backend processing logic

├── requirements.txt # Python dependencies

├── README.md # Project documentation

├── instruction.txt # Provided instructions

├── Sample_1.pdf # Sample test file

├── Sample_2.pdf # Sample test file

└── .gitignore




---

# 🧰 Technology Stack

| Technology | Purpose |
|--------|--------|
| Python | Core programming language |
| Streamlit | Web application interface |
| Cerebras Cloud SDK | Large Language Model inference |
| PyPDF2 | PDF text extraction |
| python-docx | DOCX text extraction |
| python-dotenv | Environment variable management |

---

# 🧠 Summarization Approach

The system uses an **Abstractive Summarization approach** powered by a **Large Language Model (LLM)**.

### Model Used
**GPT-OSS-120B (Cerebras)**

This model generates human-like summaries by understanding the context of the document rather than simply extracting sentences.

### Process

1. Extract text from uploaded document
2. Send text to Cerebras LLM
3. Generate concise summary (max 500 words)
4. Translate summary to Hindi
5. Display results to the user

---

# ⚙️ System Workflow

### Step 1 — Upload File
User uploads a supported document:
- PDF
- DOCX
- TXT

### Step 2 — Text Extraction
The system extracts raw text from the document using:

- **PyPDF2** for PDFs
- **python-docx** for DOCX
- Standard Python file reading for TXT

### Step 3 — Summarization
Extracted text is sent to the **Cerebras GPT-OSS-120B model** with instructions to generate a summary limited to **500 words**.

### Step 4 — Translation
The generated English summary is translated into **Hindi** using the same model.

### Step 5 — Output Display
The application displays:

- English summary
- Hindi summary
- Download options for both summaries

---

# 🖥️ User Interface Features

The application provides an intuitive interface where users can:

- Upload files easily
- Generate summaries with one click
- View results instantly
- Download summaries as text files

---

# 📄 Sample Files

The repository contains two sample files for testing:
Sample_1.pdf
Sample_2.pdf  


These files can be used to verify the functionality of the summarizer.

---

# 🚀 Deployment

The application is deployed using **Streamlit Cloud**.

### Deployment Steps

1. Push project to GitHub
2. Connect repository to Streamlit Cloud
3. Select `app.py` as the main application file
4. Add API key to **Streamlit Secrets**
5. Deploy application

---

# 🌐 Live Application

Live URL: https://ai-summarize-app.streamlit.app/



---

# ⚠️ Limitations & Assumptions

- The system truncates very large documents to avoid model context limits.
- Summaries are limited to **500 words** as required.
- Accuracy depends on the quality of extracted text.
- Some scanned PDFs without selectable text may not be processed correctly.

---

# 🔑 Environment Variables

The application requires a Cerebras API key.

Create a `.env` file:


CEREBRAS_API_KEY=your_api_key_here


---

# ▶️ Running the Project Locally

Install dependencies:
pip install -r requirements.txt


Run the application:
streamlit run app.py


Then open:
http://localhost:8501


---

# 📬 Author
Divyansh Sharma

AI / Machine Learning Enthusiast 
