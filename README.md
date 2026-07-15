# 🩺 AI-First CRM HCP Module

An AI-powered Customer Relationship Management (CRM) application designed for Pharmaceutical Sales Representatives to efficiently log and manage Healthcare Professional (HCP) interactions using both a structured form and an AI conversational interface.

This project was developed as part of the **AI-First CRM HCP Module Assignment**.

---

## 🚀 Features

### 📋 Structured Interaction Logging
- Log doctor interactions using a structured form.
- Capture:
  - Doctor Name
  - Hospital
  - Specialty
  - Interaction Type
  - Products Discussed
  - Discussion Notes
  - Follow-up Date
  - Summary

### 🤖 AI Chat Assistant
- Log doctor interactions through natural language.
- AI automatically extracts:
  - Doctor Name
  - Hospital
  - Specialty
  - Products
  - Interaction Summary
  - Follow-up Recommendation

### 🔍 Search Previous Interactions
Search interactions using:
- Doctor Name
- Hospital
- Specialty
- Product Name
- Summary

### ✏️ Edit Interaction
Modify previously saved interactions.

### 🗑 Delete Interaction
Remove unwanted interaction records.

### 📅 Follow-up Suggestions
Generate AI-based follow-up recommendations.

### 📌 Next Visit Recommendations
Receive suggested discussion points for the next doctor visit.

---

# 🧠 AI Architecture

The project uses **LangGraph** together with **Groq LLM** to process natural language interaction logs.

### Workflow

```
User Input
      │
      ▼
React Chat Interface
      │
      ▼
FastAPI Backend
      │
      ▼
LangGraph Agent
      │
      ▼
Groq LLM (Gemma / Llama)
      │
      ▼
Extract Entities
      │
      ▼
Generate Summary
      │
      ▼
Store in PostgreSQL
```

---

# 🛠 LangGraph Agent

The LangGraph ReAct Agent orchestrates the AI workflow and manages tool execution.

### Available Tools

### ✅ Log Interaction
Logs doctor interactions after AI extraction.

### ✅ Edit Interaction
Updates existing interaction details.

### ✅ Search Interaction
Searches previous interactions stored in the database.

### ✅ Generate Follow-up
Generates follow-up suggestions for doctors.

### ✅ Recommend Next Visit
Provides recommendations for the next doctor visit.

---

# 💻 Tech Stack

## Frontend
- React
- Redux Toolkit
- Axios
- Bootstrap
- Google Inter Font

## Backend
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL
- LangGraph
- LangChain
- Groq LLM

## AI
- LangGraph
- LangChain
- Groq API
- llama-3.3-70b-versatile (or gemma2-9b-it)

---

# 📂 Project Structure

```
crmaihcp
│
├── backend
│   ├── app
│   │   ├── agents
│   │   │     graph.py
│   │   ├── routes
│   │   │     chat.py
│   │   │     interaction.py
│   │   ├── services
│   │   │     ai_service.py
│   │   │     llm.py
│   │   │     tools.py
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   ├── redux
│   │   ├── services
│   │   ├── styles
│   │   └── App.jsx
│   │
│   └── package.json
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/sagar07999/crmaihcp.git

cd crmaihcp
```

---

# Backend Setup

Create virtual environment

```bash
cd backend

python -m venv venv
```

Activate environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```env
DATABASE_URL=postgresql://username:password@localhost/database_name

GROQ_API_KEY=your_groq_api_key
```

Run Backend

```bash
uvicorn app.main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

---

# Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

# API Endpoints

## AI Chat

```
POST /chat/
```

Logs interaction through AI.

---

## Create Interaction

```
POST /interactions/
```

---

## Get All Interactions

```
GET /interactions/
```

---

## Update Interaction

```
PUT /interactions/{id}
```

---

## Delete Interaction

```
DELETE /interactions/{id}
```

---

## Search Interaction

```
GET /interactions/search?query=apollo
```

---

# Example AI Input

```
Visited Dr. Rajesh Sharma at Apollo Hospital.

Discussed Glycomet XR for Type 2 Diabetes.

Doctor requested clinical trial data and patient education materials.

Follow-up planned next week.
```

### AI Output

```
Doctor:
Dr. Rajesh Sharma

Hospital:
Apollo Hospital

Specialty:
Endocrinology

Products:
Glycomet XR

Summary:
Discussed Glycomet XR for diabetes management.
Doctor requested clinical studies and patient education material.

Follow-up:
Next Week
```

---

# Assignment Requirements Covered

| Requirement | Status |
|------------|--------|
| React UI | ✅ |
| Redux | ✅ |
| FastAPI | ✅ |
| PostgreSQL | ✅ |
| LangGraph | ✅ |
| Groq LLM | ✅ |
| Structured Form | ✅ |
| AI Chat Interface | ✅ |
| Log Interaction Tool | ✅ |
| Edit Interaction Tool | ✅ |
| Search Interaction Tool | ✅ |
| Generate Follow-up Tool | ✅ |
| Recommend Next Visit Tool | ✅ |
| CRUD Operations | ✅ |
| AI Summarization | ✅ |

---

# Future Enhancements

- Voice-based interaction logging
- OCR prescription scanning
- Calendar integration
- Email follow-up generation
- Doctor visit analytics dashboard
- Authentication and user roles
- Multi-user CRM support

---

# Author

**Sagar Gaddi**

GitHub: https://github.com/sagar07999

LinkedIn: https://www.linkedin.com/in/sagar-gaddi-a42240246/

Portfolio: https://69808e1cf75478d9c756eb50--cosmic-alpaca-1d9e2a.netlify.app/

---

# License

This project was developed for educational and assessment purposes.
