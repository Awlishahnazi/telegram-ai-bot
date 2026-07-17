# 🤖 Telegram AI Assistant Bot

An intelligent Telegram chatbot powered by LLMs with conversation memory and user personalization.

The goal of this project is to build a production-ready AI assistant that can understand users, remember important information about them, and provide personalized responses.

---

## ✨ Features

### ✅ AI Chat System

* Built with Telegram Bot API
* Uses `aiogram 3` for asynchronous bot handling
* Connected to LLM providers through OpenRouter API
* Supports natural language conversations

### ✅ Conversation Memory (Short-Term Memory)

The bot stores recent conversations and uses them as context for generating responses.

Implemented using:

* SQLite database
* SQLAlchemy ORM
* Message repository pattern

Stored information:

* User messages
* Assistant responses
* Conversation history

---

### ✅ User Personal Memory (Long-Term Memory)

The bot can extract and remember permanent user information.

Examples:

```
User:
سلام اسم من علی است

AI Memory:
name: Ali
```

Implementation:

* AI-based fact extraction
* JSON structured output
* User facts database
* Automatic context injection into AI prompts

---

## 🏗️ Project Architecture

```
telegram-ai-bot/

│
├── app/
│   │
│   ├── database/
│   │   ├── database.py
│   │   ├── models.py
│   │   └── repository.py
│   │
│   ├── handlers/
│   │   └── start.py
│   │
│   ├── repositories/
│   │   └── user_fact_repository.py
│   │
│   ├── services/
│   │   ├── ai.py
│   │   ├── memory.py
│   │   ├── memory_manager.py
│   │   └── fact_extractor.py
│   │
│   ├── prompts/
│   │   └── system_prompt.py
│   │
│   └── config.py
│
├── main.py
├── create_db.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies

| Technology     | Purpose                      |
| -------------- | ---------------------------- |
| Python         | Core programming language    |
| aiogram 3      | Telegram Bot framework       |
| OpenRouter API | LLM communication            |
| SQLAlchemy     | Database ORM                 |
| SQLite         | Local database               |
| AsyncIO        | Asynchronous operations      |
| Pydantic       | Configuration and validation |

---

## ⚙️ Installation

### 1. Clone repository

```bash
git clone <repository-url>
cd telegram-ai-bot
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate:

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file:

```env
BOT_TOKEN=your_telegram_bot_token

OPENROUTER_API_KEY=your_openrouter_api_key

OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

MODEL_NAME=your_model_name
```

---

### 5. Initialize database

```bash
python create_db.py
```

---

### 6. Run bot

```bash
python main.py
```

---

## 🧠 Memory Architecture

The bot currently uses two memory layers:

### 1. Conversation Memory

Stores recent messages:

```
User
 ↓
Message Repository
 ↓
SQLite Database
 ↓
AI Context
```

---

### 2. User Fact Memory

Pipeline:

```
User Message
      |
      v
Fact Extractor (LLM)
      |
      v
Structured JSON Facts
      |
      v
User Fact Database
      |
      v
Personalized AI Response
```

---

## 📌 Current Progress

Implemented:

* [x] Telegram bot connection
* [x] AI response generation
* [x] OpenRouter integration
* [x] SQLite database
* [x] Conversation history
* [x] Repository pattern
* [x] Automatic fact extraction
* [x] Long-term user memory
* [x] Personalized responses

---

## 🚀 Future Roadmap

Planned improvements:

* [ ] Better memory ranking system
* [ ] Vector database integration
* [ ] Semantic search over conversations
* [ ] User profile management
* [ ] Voice message support
* [ ] Image understanding
* [ ] Deployment on cloud server
* [ ] Web dashboard

---

## 👨‍💻 Author

Ali Shahnazi

Computer Engineering Student
Interested in Artificial Intelligence, Deep Learning and Software Engineering

