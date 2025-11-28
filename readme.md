# ED Mental Health Screening Demo (Somatic Complaints)

## 1. Project Overview

This project is a **GenAI prototype** designed to simulate a mental health risk screening process for patients presenting with **somatic complaints** (e.g., headache, fatigue, chest pain) in an Emergency Department (ED) setting.

**Use Case:**
ED doctors often encounter patients with physical symptoms that may have underlying psychological root causes (stress, depression, anxiety). Due to time constraints, performing a comprehensive mental health assessment is difficult. This tool assists by conducting a quick, conversational screening.

**Goal:**

* Ask **5 standardized screening questions**.
* Use **LangChain** and a local LLM (**Ollama / qwen2.5:7b**) to analyze the patient's responses.
* Generate a structured **Risk Summary** for the physician, highlighting risk flags and suggested next steps.

---

## 2. Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io/) (for rapid web UI development)
* **Orchestration**: [LangChain](https://python.langchain.com/)
  * `PromptTemplate`: To structure the AI instruction.
  * `LLMChain`: To connect user inputs with the LLM.
* **LLM**: [Ollama](https://ollama.com/) (Running `qwen2.5:7b` locally)

---

## 3. Prerequisites

Before running the project, ensure you have the following installed:

1. **Python 3.9+**
2. **Ollama**: Download and install from [ollama.com](https://ollama.com/).
3. **LLM Model**: You must have the `qwen2.5:7b` model pulled locally.
   ```bash
   ollama pull qwen2.5:7b
   ```

---

## 4. Setup & Installation

1. **Create a Virtual Environment** (Recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
2. **Install Dependencies**:
   Ensure `requirements.txt` is present, then run:

   ```bash
   pip install -r requirements.txt
   ```

   *Dependencies included in `requirements.txt`:*

   * `streamlit`
   * `langchain`
   * `langchain-community`

---

## 5. How to Run

1. **Start Ollama**:
   Make sure the Ollama app is running in the background.
2. **Run the Streamlit App**:

   ```bash
   source venv/bin/activate  streamlit run app.py

   ```

---

## 6. User Flow

1. **Start**: Click the **"Start Screening"** button on the home page.
2. **Interview**: The patient (user) answers 5 fixed questions regarding their mood, interest, stress, sleep, and symptom correlation.
3. **Generate**: After filling out the form, click **"Generate AI Summary"**.
4. **Result**: The LLM processes the inputs and displays:
   * **Clinical Summary**
   * **Risk Flags** (Bullet points)
   * **Overall Risk Level** (None / Mild / Urgent)
   * **Suggested Next Steps**

---

## 7. Project Structure

```
.
├── app.py                # Main application logic (UI + LangChain integration)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── venv/                 # Virtual environment (excluded from git)
```

## 8. Customization

* **Questions**: To modify the screening questions, edit the `QUESTIONS` list in `app.py`.
* **Prompt**: To change how the AI summarizes the data, modify the `template` string in the `generate_summary` function in `app.py`.
* **Model**: To use a different local model (e.g., `llama3`), change the `LLM_MODEL` variable in `app.py` and ensure the model is pulled via Ollama.
