# RFP Analyzer AI Agent

A Streamlit-based AI tool that extracts structured information from RFP documents (PDF, DOCX, or text). It uses OpenAI's GPT to analyze content, and will soon support RAG-based Q&A using LangChain.

## Features
- Upload and parse RFP files (.pdf, .docx, or paste text)
- Extract and display structured fields like deadlines, contacts, evaluation criteria, etc.
- Export results to `.json`, `.txt`, `.docx`
- Future: Ask questions about the document using LangChain + FAISS

## Tech Stack
- Python 3.x
- Streamlit
- OpenAI GPT (via API)
- PyMuPDF, docx2txt
- LangChain (coming soon)

## Setup
```bash
pip install -r requirements.txt
streamlit run app.py
