# Restaurant Name Generator 🍽️

A Streamlit app that generates a restaurant name and menu items using
LangChain and a local Ollama model (phi3).

## Features
- Local LLM (no API key)
- Restaurant name generation
- Menu item suggestion
- Built with Streamlit + LangChain

## Requirements
- Python 3.10+
- Ollama installed

## Setup
```bash
ollama pull phi3
ollama serve
pip install -r requirements.txt
streamlit run main.py
