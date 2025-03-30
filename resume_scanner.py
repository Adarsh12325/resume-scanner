import PyPDF2
import re
import nltk

nltk.download('punkt')

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def load_keywords(file_path):
    with open(file_path, "r") as file:
        keywords = [line.strip() for line in file.readlines()]
    return keywords

def calculate_match_percentage(resume_text, keywords):
    found_keywords = [kw for kw in keywords if re.search(rf'\b{kw}\b', resume_text, re.IGNORECASE)]
    match_percentage = (len(found_keywords) / len(keywords)) * 100
    return found_keywords, match_percentage

resume_file = "sample_resume.pdf"
keywords_file = "job_keywords.txt"

resume_text = extract_text_from_pdf(resume_file)

job_keywords = load_keywords(keywords_file)

matched_keywords, match_percent = calculate_match_percentage(resume_text, job_keywords)

print(f"Matched Keywords: {matched_keywords}")
print(f"Resume Match Percentage: {match_percent:.2f}%")
