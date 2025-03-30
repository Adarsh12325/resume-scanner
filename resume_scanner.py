import PyPDF2
import re
import nltk

nltk.download('punkt')

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def load_keywords(file_path):
    """Loads keywords from a text file."""
    with open(file_path, "r") as file:
        keywords = [line.strip() for line in file.readlines()]
    return keywords

def calculate_match_percentage(resume_text, keywords):
    """Calculates how many job keywords appear in the resume."""
    found_keywords = [kw for kw in keywords if re.search(rf'\b{kw}\b', resume_text, re.IGNORECASE)]
    match_percentage = (len(found_keywords) / len(keywords)) * 100
    return found_keywords, match_percentage

# File paths
resume_file = "sample_resume.pdf"
keywords_file = "job_keywords.txt"

# Extract text from resume
resume_text = extract_text_from_pdf(resume_file)

# Load job keywords
job_keywords = load_keywords(keywords_file)

# Calculate match percentage
matched_keywords, match_percent = calculate_match_percentage(resume_text, job_keywords)

# Display results
print(f"Matched Keywords: {matched_keywords}")
print(f"Resume Match Percentage: {match_percent:.2f}%")
