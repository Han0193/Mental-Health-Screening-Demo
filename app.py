import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Ollama

# --- Configuration ---
QUESTIONS = [
    "1. Over the last 2 weeks, how often have you been bothered by feeling down, depressed, or hopeless?",
    "2. Over the last 2 weeks, how often have you been bothered by little interest or pleasure in doing things?",
    "3. How would you rate your current stress level on a scale of 1 to 10?",
    "4. Have you been having trouble sleeping recently? If so, please describe.",
    "5. Do you feel that your physical symptoms (like headache, pain) are related to your current stress or emotions?"
]

LLM_MODEL = "qwen2.5:7b"

# --- App Layout ---
st.set_page_config(page_title="ED Mental Health Screening Demo", page_icon="🏥")

st.title("🏥 ED Mental Health Screening Demo")
st.subheader("Somatic Complaints & Risk Assessment")

# --- Session State Management ---
if "started" not in st.session_state:
    st.session_state.started = False
if "answers" not in st.session_state:
    st.session_state.answers = [""] * len(QUESTIONS)
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# --- Logic ---

def handle_start():
    st.session_state.started = True

def generate_summary():
    # Construct the input text
    interview_text = ""
    for i, q in enumerate(QUESTIONS):
        interview_text += f"Question: {q}\nAnswer: {st.session_state.answers[i]}\n\n"
    
    # LangChain Setup
    template = """
    You are an AI assistant helping an Emergency Department doctor assess a patient with somatic complaints for potential mental health risks.
    
    Below is a screening interview with the patient:
    
    {interview_text}
    
    Based on the above, please provide a summary in the following format:
    
    **Clinical Summary:**
    (A brief paragraph summarizing the patient's mental state and reported symptoms)
    
    **Risk Flags:**
    (A bulleted list of specific risk factors identified, e.g., depressive symptoms, high stress, sleep issues)
    
    **Overall Risk Level:** 
    (Choose one: None / Mild Concern / Needs Urgent Formal Assessment)
    
    **Suggested Next Steps:**
    (High-level recommendations for the doctor, e.g., "Refer to social worker", "Prescribe anxiety medication", "Discharge with follow-up")
    
    Note: Do NOT provide a medical diagnosis. This is a screening tool only.
    """
    
    prompt = PromptTemplate(
        input_variables=["interview_text"],
        template=template,
    )
    
    try:
        llm = Ollama(model=LLM_MODEL)
        chain = LLMChain(llm=llm, prompt=prompt)
        
        with st.spinner("Generating AI Summary..."):
            summary = chain.run(interview_text)
            st.success("Summary Generated")
            st.markdown("---")
            st.markdown(summary)
            
    except Exception as e:
        st.error(f"Error communicating with Ollama: {e}")
        st.info("Please make sure Ollama is running and the model 'qwen2.5:7b' is pulled.")

# --- UI Flow ---

if not st.session_state.started:
    st.write("Welcome. This tool assists in screening patients with somatic complaints for underlying mental health risks.")
    st.button("Start Screening", on_click=handle_start)

else:
    with st.form("screening_form"):
        for i, q in enumerate(QUESTIONS):
            st.session_state.answers[i] = st.text_input(q, value=st.session_state.answers[i], key=f"q{i}")
        
        submitted = st.form_submit_button("Generate AI Summary")
        
        if submitted:
            # Check if all questions are answered (optional validation)
            if all(st.session_state.answers):
                generate_summary()
            else:
                st.warning("Please answer all questions before generating the summary.")

