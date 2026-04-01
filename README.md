# 🧠 Smart Resume Analyzer with AI  

<p align="center">
  🚀 OpenAI + Streamlit + Python  
</p>

<p align="center">
  👨‍💻 <b>Developed by Yadnesh Patil</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/OpenAI-AI-green?style=for-the-badge&logo=openai">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">
</p>

---

## 📌 About the Project
An AI-powered web application that analyzes resumes and provides smart feedback, skill insights, resume scoring, and improvement suggestions using OpenAI.

---

## ✨ Features
- 📄 Upload Resume (PDF/DOCX/Text)  
- 🤖 AI Resume Analysis  
- 🎯 Skill Extraction  
- 📊 Resume Score (ATS-like)  
- 💡 Improvement Suggestions  
- 🔍 Missing Skills Detection  
- ⚡ Interactive UI with Streamlit  

---

## 🛠️ Tech Stack
| Category | Technology |
|----------|-----------|
| Frontend | Streamlit |
| Backend | Python |
| AI | OpenAI API |
| Libraries | PyPDF2, python-docx, pandas, re |

---

## 📂 Project Structure
```bash
Smart-Resume-Analyzer/
│── app.py
│── requirements.txt
│── README.md
│── utils/
│   ├── parser.py
│   ├── analyzer.py
│── sample_resumes/
```

---

## ⚙️ Installation
```bash
git clone https://github.com/your-username/smart-resume-analyzer.git
cd smart-resume-analyzer
python -m venv venv
venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🔐 Setup API Key
```python
OPENAI_API_KEY = "your_api_key_here"
```

---

## ▶️ Run App
```bash
streamlit run app.py
```

👉 Open: http://localhost:8501  

---

## 🧠 How It Works
1. Upload resume  
2. Extract text (PDF/DOCX)  
3. AI analyzes content  
4. Generates score, skills, and suggestions  

---

## 📊 Example Output
```
Resume Score: 78/100
Missing Skills: Docker, Kubernetes
Suggestions:
- Add measurable achievements
- Improve summary section
- Add technical keywords
```

---

## 📸 Screenshots
Add your Streamlit UI screenshots here

---

## 🚀 Future Scope
- 🔗 LinkedIn Analysis  
- 📈 ATS Checker  
- 🌐 Multi-language Support  
- 🧑‍💼 Job Recommendations  

---

## 🤝 Contributing
Feel free to fork this repo and submit pull requests!

---

## 🙌 Acknowledgements
- OpenAI  
- Streamlit  

---

## ⭐ Support
If you like this project, give it a ⭐ on GitHub!
