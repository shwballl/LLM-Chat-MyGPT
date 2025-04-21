# LLM-Chat-MyGPT
![image](https://github.com/user-attachments/assets/83a26bad-d65b-4b37-bcf7-76fefacf5c68)

**LLM-Chat-MyGPT** is a personal project designed to explore and understand the integration of Large Language Models (LLMs) using Python. It serves as a learning platform to experiment with LLM capabilities, including backend and frontend interactions.

## 🧠 Project Overview

- **Purpose**: Educational exploration of LLMs with Python
- **Components**:
  - `backend/`: Contains server-side code for handling LLM interactions
  - `frontend/`: Houses the client-side interface for user interactions
- **Technologies Used**:Python, FastAPI for the backend, and Astro, JavaScript and TailwindCSS for the frontend

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js and npm (for frontend development)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shwballl/LLM-Chat-MyGPT.git
   cd LLM-Chat-MyGPT
   ```


2. **Set Up Backend**:
   - Navigate to the backend directory:
     ```bash
     cd backend
     ```
   - Create a virtual environment and activate it:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up Frontend**:
   - Navigate to the frontend directory:
     ```bash
     cd ../frontend
     ```
    Install dependencies:
     ```bash
     npm install
     ```

4. **Run the Application**:
    Start the backend server:
     ```bash
     cd ../backend
     uvicorn src.main:app --reload
     ```
    Start the frontend development server:
     ```bash
     cd ../frontend
     npm run dev
     ```

## 🛠️ Usage

Once both servers are running, navigate to `http://localhost:4321/` in your browser to interact with the applicatin. You can input queries, and the backend will process them using the integrated LLM.

## ⚠️ Disclaimr

This project is intended for educational and research purposes ol. The author is not responsible for any misuse of this softwr. Ensure compliance with all applicable laws and regulations when using this softwre.
