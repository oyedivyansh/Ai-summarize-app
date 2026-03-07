#  AI Document Summarizer

Reading long documents can take a lot of time, especially when you only need the main ideas. I built this project to solve that problem.

The AI Document Summarizer allows users to upload documents and instantly generate a short summary in English along with a Hindi translation. The goal is to make information easier and faster to understand without reading the entire document.

The system uses Cerebras LLM (GPT-OSS-120B) to analyze the content and generate meaningful summaries while keeping them within a 500-word limit.

#  Project Overview

This application automatically summarizes documents such as PDF, DOCX, and TXT files.

Once a file is uploaded, the system extracts the text, sends it to a language model for summarization, and then produces a concise summary in English. The same model is also used to generate a Hindi translation of the summary.

The interface is built using Streamlit, which keeps the application simple and easy to use. Users can upload documents, generate summaries, and download the results directly from the browser.

#  Objectives

While working with reports, research papers, and documentation, I realized that reading everything from start to finish is often unnecessary when you only need the key points.

This project was created as a simple tool that can quickly extract the important information from a document and present it in a short, readable format.

Key Features

Generates concise summaries limited to 500 words

Supports multiple document formats (PDF, DOCX, TXT)

Provides summaries in English and Hindi

Simple Streamlit-based user interface

Allows users to download the generated summaries

Can be easily deployed online

#  Project Structure
AI-Document-Summarizer

├── app.py            # Streamlit frontend application
├── utils.py          # Backend logic for text extraction and summarization
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
├── Sample_1.pdf      # Sample file for testing
├── Sample_2.pdf      # Sample file for testing
└── .gitignore
Technology Stack

The project uses a small set of tools to keep the system lightweight and easy to maintain.

#  Technology Stack
Python	Core programming language
Streamlit	Web interface for the application
Cerebras Cloud SDK	Access to the GPT-OSS-120B model
PyPDF2	Extract text from PDF files
python-docx	Extract text from DOCX files
python-dotenv	Manage environment variables
How the Summarization Works

The application uses an abstractive summarization approach powered by a large language model.

Instead of simply selecting sentences from the document, the model reads the text, understands its meaning, and generates a new summary that captures the most important ideas.

Model Used

GPT-OSS-120B (Cerebras)

This model is capable of processing large amounts of text and producing summaries that are natural and easy to read.


# System Workflow
1. Upload a Document

Users can upload a document in one of the following formats:

PDF

DOCX

TXT

2. Text Extraction

Once the file is uploaded, the system extracts text using:

PyPDF2 for PDF files

python-docx for DOCX files

Standard Python file reading for TXT files

3. Generate Summary

The extracted text is sent to the Cerebras GPT-OSS-120B model, which generates a summary while ensuring that the output stays within 500 words.

4. Hindi Translation

After the English summary is created, the model generates a Hindi translation so the information can be understood by a wider audience.

5. Display Results

The application shows:

English Summary

Hindi Summary

Users can also download the summaries for later use.

User Interface

The application is built with Streamlit, which allows the entire tool to run directly in a browser.

The interface is intentionally kept simple so that users can:

Upload a document quickly

Generate summaries with one click

View results immediately

Download summaries if needed

Sample Files

Two sample documents are included in the repository:

Sample_1.pdf
Sample_2.pdf

These files can be used to test the summarizer and see how it works.

Deployment

The application is deployed using Streamlit Cloud, which makes it accessible without installing anything locally.

#  Deployment

Push the project to GitHub

Connect the repository to Streamlit Cloud

Select app.py as the main application file

Add the Cerebras API key in Streamlit Secrets

Deploy the application

Live Application

You can try the application here:

https://ai-summarize-app.streamlit.app/

#  Limitations & Assumptions


Very large documents may be shortened before processing due to model limits.

The summary length is restricted to 500 words.

The accuracy of results depends on how well text can be extracted from the document.

Some scanned PDFs without selectable text may not work properly.

#  Environment Variables

To run the project, you need a Cerebras API key.

Create a .env file in the project directory:

CEREBRAS_API_KEY=your_api_key_here

# Running the Project Locally

Install the required dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

Then open the browser and go to:

http://localhost:8501


# Author

Divyansh Sharma

AI / Machine Learning Enthusiast
