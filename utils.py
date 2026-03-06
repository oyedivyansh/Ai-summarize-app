import os
import io
from PyPDF2 import PdfReader
from docx import Document
from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv

load_dotenv()


def get_client():
    api_key = os.getenv("CEREBRAS_API_KEY")

    if not api_key:
        raise ValueError("CEREBRAS_API_KEY not found in .env file")

    return Cerebras(api_key=api_key)


def extract_text_from_file(file):

    ext = os.path.splitext(file.name)[1].lower()

    if ext == ".txt":
        return file.read().decode("utf-8")

    elif ext == ".pdf":
        reader = PdfReader(io.BytesIO(file.read()))
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

        return text

    elif ext == ".docx":
        doc = Document(io.BytesIO(file.read()))
        text = ""

        for p in doc.paragraphs:
            text += p.text + "\n"

        return text

    else:
        raise ValueError("Unsupported file format. Use txt, pdf, or docx.")


def summarize_text(text):

    client = get_client()

    if len(text) > 8000:   # prevent huge prompts
        text = text[:8000]

    prompt = f"Summarize the following text concisely in English under 500 words and focus on the main points:\n{text}"

    response = client.chat.completions.create(
        model="gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400
    )

    return response.choices[0].message.content.strip()


def translate_to_hindi(text):

    client = get_client()

    prompt = f"Translate this English text into Hindi under 500 words and focus on the main points and clarity:\n{text}"

    response = client.chat.completions.create(
        model="gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=600
    )

    return response.choices[0].message.content.strip()


def generate_summaries(text):

    english_summary = summarize_text(text)

    hindi_summary = translate_to_hindi(english_summary)

    return english_summary, hindi_summary