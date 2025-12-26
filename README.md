# 🍽️ Restaurant Name & Menu Generator

A beginner-friendly GenAI project that generates a fancy restaurant name and
suggests menu items based on cuisine using **LangChain** and a **local Ollama model (phi3)**.
The app is built with **Streamlit** and runs completely offline.

---

## ✨ Features
- Generate a fancy restaurant name by cuisine
- Suggest menu items for the generated restaurant
- Runs locally (no API keys required)
- Uses lightweight `phi3` model via Ollama
- Simple Streamlit UI

---

## 🛠 Tech Stack
- Python
- LangChain
- Ollama (`phi3`)
- Streamlit

---

## ⚙️ Prerequisites
- Python 3.10+
- Ollama installed  
  👉 https://ollama.com

---

## 🚀 Setup & Run

```bash
# Clone the repository
git clone https://github.com/pratham-jdn/restaurant-name-generator.git
cd restaurant-name-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Pull Ollama model
ollama pull phi3

# Start Ollama server
ollama serve

# Run the app
streamlit run main.py
