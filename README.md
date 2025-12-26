# 🍽️ Local LLM-Powered Restaurant Name & Menu Generator

An **applied Generative AI project** that uses a **locally hosted Large Language Model (Phi-3)** via **Ollama** to generate **context-aware restaurant names and menu suggestions** based on cuisine type.

This project is designed to demonstrate **local LLM inference, prompt engineering, and AI system design**, without relying on any cloud APIs or paid services.

---

## 🎯 Problem Statement

Naming and branding a restaurant is a **creative yet constrained problem** influenced by factors such as cuisine, style, and customer perception.  
This project explores how **Generative AI can assist early-stage business ideation** by producing relevant and creative restaurant names along with matching menu suggestions.

Unlike typical AI applications that depend on cloud APIs, this system runs **entirely offline**, giving full control over inference, cost, and privacy.

---

## 🧠 Key Highlights

- Runs a **local Large Language Model (LLM)** using Ollama
- Uses **Phi-3**, a lightweight and efficient LLM suitable for on-device inference
- No API keys or cloud services required
- Prompt-driven generation with business constraints
- Generates:
  - Restaurant name
  - Cuisine-specific menu items
- Simple and interactive **Streamlit UI**
- Fully offline and cost-efficient

---

## 🏗️ System Design Overview

1. User selects a cuisine type
2. Application constructs a structured prompt with branding constraints
3. Prompt is sent to a **locally running Phi-3 model via Ollama**
4. The model generates:
   - A restaurant name
   - Relevant menu suggestions
5. Results are displayed in the Streamlit interface

This architecture emphasizes **privacy, low cost, and control over inference**, making it suitable for environments where cloud access is limited or undesirable.

---

## 🛠️ Tech Stack

- **Python**
- **Ollama** – Local LLM runtime
- **Phi-3** – Lightweight language model
- **LangChain** – Prompt orchestration
- **Streamlit** – Web interface

---

## ⚙️ Prerequisites

- Python 3.10 or higher
- Ollama installed locally  
  👉 https://ollama.com

---


⚖️ Design Choices & Trade-offs

Why Local LLM Instead of Cloud APIs?

No dependency on external services
Zero API usage cost
Better data privacy and control
Greater control over latency and inference behavior
Deeper understanding of real-world AI system constraints

Why Phi-3?

Lightweight and resource-efficient
Designed for constrained hardware environments
Provides a good balance between creativity and performance
Suitable for local experimentation and rapid prototyping

---

Limitations

Output quality depends heavily on prompt design
Performance is constrained by local hardware resources
No long-term memory or user personalization
Not intended for direct commercial deployment without additional safeguards

## 🚀 Setup & Run Locally

---

Future Improvements

Add brand tone selection (luxury, casual, street-style)
Introduce ranking or feedback for generated names
Support batch generation and filtering
Containerize the inference service for scalability
Add logging and performance monitoring

---

Interview & Engineering Perspective

This project demonstrates:
Understanding of LLM inference beyond simple API usage
Experience with local AI system deployment
Prompt engineering and constraint-based generation
Cost-aware and privacy-focused AI design
Practical application of Generative AI in a business context

---

```bash
# Clone the repository
git clone https://github.com/pratham-jdn/restaurant-name-generator.git
cd restaurant-name-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
(streamlit,
langchain
langchain-core
langchain-ollama)

Install Ollama from https://ollama.com

# Pull the Phi-3 model
ollama pull phi3

# Start Ollama server
ollama serve

# Run the Streamlit application
streamlit run main.py


👤 Author

Pratham
GitHub: https://github.com/pratham-jdn