# AI-Powered Meeting Notes Summarizer and Sharer

## Project Overview
This project is a **full-stack application** that allows users to summarize meeting transcripts and share them via email. The application leverages AI to generate concise, structured summaries based on user prompts.

---

## How it Works

1. **Upload Transcript**  
   - Users can upload or paste a text transcript (e.g., meeting notes, call transcript).  

2. **Custom Instructions / Prompts**  
   - Users can provide a custom instruction such as:  
     - “Summarize in bullet points for executives”  
     - “Highlight only action items”  

3. **Generate Summary**  
   - Clicking **Generate Summary** triggers the AI to produce a structured summary based on the transcript and custom prompt.  

4. **Edit Summary**  
   - The generated summary is editable, allowing users to make final adjustments.  

5. **Share via Email**  
   - Users can enter recipient email addresses to send the final summary directly via Gmail SMTP.

---

## Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript (basic interface for functionality)  
- **AI Summarization:** Hugging Face `facebook/bart-large-cnn`  
- **Email Service:** Gmail SMTP with App Password  
- **Environment Management:** `.env` file for API keys and email credentials  
- **CORS:** Enabled to allow frontend-backend communication

---

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/Nazeya86/Lumio-transcript-app.git
cd Lumio-transcript-app

```
2. **Install backend dependencies**
```bash
pip install -r backend/requirements.txt

```
3. **Create a .env file in the backend folder**
```bash
HF_API_KEY=your_huggingface_api_key
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_16_char_app_password

```
4. **Run the backend**
```bash
python backend/app.py

```

## Rules & Resources Followed
```bash
AI services used: Hugging Face summarization API

Frontend is intentionally basic to prioritize functionality

The project uses free and open resources for AI summarization

```

## Deployed Link
```bash

```

## License
```bash
This project is for educational purposes.
