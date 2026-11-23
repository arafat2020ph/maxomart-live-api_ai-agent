# 🤖 Maxomart AI Agent

An advanced, AI-powered E-commerce Assistant built with **Django**, **LangChain**, and **LangGraph**. This agent connects directly to a **live E-commerce REST API** to provide real-time product discovery, intelligent customer support, and seamless backend operations through a conversational interface.

## 🚀 About The Project
The goal of this project was to build a production-ready AI agent that can interact with real-world data. Instead of using mock data, this agent is integrated with a live e-commerce platform's API. To handle complex decision-making and multi-step reasoning, **LangGraph** is used to create a stateful, cyclical agent workflow, while **LangChain** manages the LLM interactions and tool bindings.

### ✨ Key Features
* **Live API Integration:** Fetches real-time data (products, categories, orders, etc.) directly from a live e-commerce API.
* **Stateful Agent Workflow (LangGraph):** Uses graph-based architecture to handle complex, multi-step user queries (e.g., checking stock -> adding to cart -> verifying order status).
* **Tool Calling:** The agent is equipped with custom tools to interact with the E-commerce API dynamically.
* **Conversational Memory:** Remembers context within the session for a natural chat experience.
* **Django Backend:** Robust server-side logic, session management, and template rendering.
* **Secure Environment:** Uses `.env` for secret management, keeping API keys safe from public exposure.

## 🛠️ Tech Stack
* **Backend Framework:** Python, Django
* **AI Orchestration:** LangChain, LangGraph
* **LLM Integration:** [এখানে আপনার LLM-এর নাম দিন, যেমন: OpenAI GPT-4, Google Gemini, Groq (Llama 3)]
* **External API:** Live E-commerce REST API
* **Frontend:** HTML, CSS, JavaScript (Django Templates)
* **Database:** SQLite (Development)

## 🧠 Architecture (How it Works)
1. **User Input:** User sends a query via the Django chat interface.
2. **LangGraph State:** The input is passed to the LangGraph agent, which maintains the conversation state.
3. **Tool Selection:** The LLM analyzes the query and decides whether to call a specific tool (e.g., `fetch_products`, `check_order_status`).
4. **API Call:** The selected tool makes an HTTP request to the live E-commerce API.
5. **Response Generation:** The API data is returned to the LLM, which generates a natural language response and sends it back to the user.

## ⚙️ Getting Started

Follow these steps to set up the project locally.

### Prerequisites
* Python 3.10+
* Git
* API Keys for your LLM provider (e.g., OpenAI, Gemini)
* Access to the Live E-commerce API

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/maxomart_agent.git
   cd maxomart_agent
