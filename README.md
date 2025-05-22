# ProtekTalk 👁️🛡️  
**AI-Powered Child Protection in Online Games**

ProtekTalk is a real-time safety system designed to protect children from online abuse, grooming, and cyberbullying inside the games they love to play. Using NLP and AI, it monitors game conversations and alerts guardians the moment suspicious behavior is detected.

---

## 🧩 Features

- 🧠 **AI-Driven Chat Monitoring** – Detects grooming, threats, and bullying in real-time  
- 🚨 **Red/Yellow Alert System** – Flags severity and sends alerts via SMS  
- 👨‍👩‍👧‍👦 **Parent Dashboard** – Review flagged conversations and file reports  
- 📑 **Incident Reporting Tool** – Generate and send reports to authorities (DSWD, NBI, PNP Cybercrime)  
- 🕹️ **Game Simulation Layer** – For demo and prototyping environments  
- 🔐 **Privacy-First** – Designed with compliance to RA 11930 and RA 10173 (Philippines)

---

## 🛠️ Tech Stack

| Component              | Stack / Service                  |
|------------------------|----------------------------------|
| Backend Framework      | Django (Python)                  |
| Frontend (Dashboard)   | Django Templates + Bootstrap     |
| NLP/AI Layer           | OpenAI GPT (Free-tier via API)   |
| Alerts/Communication   | SMS Gateway (TBD - Free Tier)    |
| Database               | PostgreSQL (Supabase/Heroku dev) |
| Hosting (MVP Phase)    | Railway / Render (free tier)     |
| Logging                | SQLite (Dev) / PostgreSQL (Prod) |
| Demo Game Sim          | Browser-based chat emulator      |

---

## 📦 Installation (Dev)

```bash
git clone https://github.com/your-org/protektalk.git
cd protektalk
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# ProtekTalk