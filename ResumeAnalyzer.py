import streamlit as st
from openai import OpenAI
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv

# -------------------------------
# Load environment variables
# -------------------------------
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OPENAI_API_KEY not found. Please check your .env file.")
    st.stop()

client = OpenAI(api_key=api_key)

# -------------------------------
# Function: Extract text from PDF
# -------------------------------
def extract_text_from_pdf(file):
    try:
        reader = PdfReader(file)
        text = ""

        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content

        return text if text else "No readable text found in PDF."

    except Exception as e:
        return f"Error reading PDF: {str(e)}"

# -------------------------------
# Function: Analyze Resume
# -------------------------------
def analyze_resume(resume_text, job_desc):
    try:
        prompt = f"""
You are a professional AI Resume Analyzer.

Analyze the resume based on the given job description.

Provide output in clear format:

1. Resume Score (out of 100)
2. Matching Percentage with Job Description
3. Key Strengths
4. Weaknesses
5. Missing Skills
6. Suggestions for Improvement

Job Description:
{job_desc}

Resume:
{resume_text}
"""

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error during AI analysis: {str(e)}"

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")

st.title("📄 Smart Resume Analyzer with AI")
st.markdown("Upload your resume and compare it with a job description 🚀")

# Upload Resume
uploaded_file = st.file_uploader("📂 Upload Resume (PDF only)", type=["pdf"])

# Job Description Input
job_description = st.text_area("📝 Paste Job Description")

# Analyze Button
if st.button("🔍 Analyze Resume"):

    if uploaded_file is None:
        st.warning("⚠️ Please upload a resume first.")
    
    elif job_description.strip() == "":
        st.warning("⚠️ Please enter a job description.")

    else:
        with st.spinner("⏳ Analyzing your resume..."):

            resume_text = extract_text_from_pdf(uploaded_file)

            if "Error" in resume_text:
                st.error(resume_text)
            else:
                result = analyze_resume(resume_text, job_description)

                st.subheader("📊 Analysis Result")
                st.write(result)

                st.success("✅ Analysis completed successfully!")
