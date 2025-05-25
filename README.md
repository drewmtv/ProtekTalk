# **🛡️ ProtekTalk**

**Real-time AI-powered child protection simulation and incident reporting system**

ProtekTalk is a Django-based project designed to simulate risky online gaming chats, powered by **Gemini 1.5 Flash** for AI-driven conversation analysis. It allows children to experience simulated online interactions and enables guardians to review flagged incidents and file reports.

---

## **⚙️ Tech Stack**

| Layer | Technology |
| ----- | ----- |
| **Backend** | Python 3.8+, Django, Django Environ |
| **Frontend** | HTML5, CSS3, JavaScript (AJAX), Bootstrap |
| **AI/ML** | Gemini 1.5 Flash via `google-generativeai` |
| **Environment** | `.env` config with `django-environ` |
| **Templating** | Django Templates |
| **Deployment** | (Local for now – ready for Heroku, Render, or Docker-based deployment) |

---

## **📁 Project Structure**

bash  
CopyEdit  
`protek_talk/`  
`│`  
`├── protektalk_app/           # Game simulation and AI monitoring logic`  
`│   ├── templates/`  
`│   ├── static/`  
`│   ├── fake_responds.py      # Randomized demo replies (Safe, Yellow, Red)`  
`│   ├── gemini_client.py      # Gemini 1.5 Flash integration`  
`│   ├── prompt_templates.py   # Templates and AI prompt logic`  
`│   ├── urls.py               # Routes: /chat/, /chat/process/`  
`│   └── views.py              # Chat handling views (AJAX-powered)`  
`│`  
`├── parent_dashboard/         # Reporting interface for parents/guardians`  
`│   ├── templates/`  
`│   ├── views.py              # Incident reporting + confirmation logic`  
`│   ├── urls.py               # Routes for report viewer and form`  
`│`  
`├── protek_talk/              # Project-level configuration`  
`│   ├── settings.py`  
`│   ├── urls.py`  
`│`  
`├── .env                      # Your environment variables`  
`├── manage.py`  
`└── README.md`

---

## **🚀 Getting Started**

### **1\. Clone the Repository**

bash  
CopyEdit  
`git clone https://github.com/your-username/protektalk.git`  
`cd protektalk`

### **2\. Install Dependencies**

bash  
CopyEdit  
`pip install -r requirements.txt`

If not using `requirements.txt`, install manually:

bash  
CopyEdit  
`pip install django`  
`pip install django-environ`  
`pip install google-generativeai`

### **3\. Add a `.env` File**

env  
CopyEdit  
`SECRET_KEY=your-django-secret-key`  
`DEBUG=True`  
`GEMINI_API_KEY=your-google-generativeai-key`

### **4\. Apply Migrations**

bash  
CopyEdit  
`python manage.py migrate`

### **5\. Run the Server**

bash  
CopyEdit  
`python manage.py runserver`

Visit: [http://127.0.0.1:8000/API/chat/](http://127.0.0.1:8000/API/chat/) to test the chat simulation.

---

## **🧩 Features Overview**

### **🎮 Game Simulation (`protektalk_app`)**

* Looping in-game video background \+ simulated chat

* AI-generated response categories:

  * **Safe** – casual, harmless

  * **Yellow** – concerning, potentially manipulative

  * **Red** – highly inappropriate or predatory

* Uses `fake_responds.py` for preloaded replies

* Uses Gemini AI (via `gemini_client.py`) to analyze interactions

### **🧑‍💼 Parent Dashboard (`parent_dashboard`)**

* Report incidents using incident number

* View full chat thread \+ Gemini-generated summary

* See involved player nicknames and game title

* Submit incident with name/contact to authorities

---

## **🔐 Gemini AI Configuration**

Gemini API is accessed via the `google-generativeai` package.

* Model: `gemini-1.5-flash`

* Prompts stored in `prompt_templates.py`

* Handles slang translation, threat detection, and summary generation

---

## **📌 Routing Summary**

| Route | Purpose |
| ----- | ----- |
| `/API/chat/` | Frontend game simulation chat |
| `/API/chat/process/` | Backend AI analysis (AJAX endpoint) |
| `/report/<incident_id>/` | View incident report (demo) |
| `/report/submit/` | Submit report form |

---

## **🧠 Vision**

ProtekTalk was designed to:

* Educate children on digital safety through simulated experience

* Detect signs of online grooming or threats using AI

* Empower guardians to understand and act quickly
