import streamlit as st
import spacy
from collections import Counter
import random
import PyPDF2

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# ------------------ MCQ Generation Logic ------------------ #
def generate_mcqs(text, num_questions=5):
    if not text:
        return []

    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    num_questions = min(num_questions, len(sentences))
    selected_sentences = random.sample(sentences, num_questions)
    mcqs = []

    for sentence in selected_sentences:
        sent_doc = nlp(sentence)
        nouns = [token.text for token in sent_doc if token.pos_ == "NOUN"]

        if len(nouns) < 2:
            continue

        noun_counts = Counter(nouns)
        if noun_counts:
            subject = noun_counts.most_common(1)[0][0]
            question_stem = sentence.replace(subject, "______")
            answer_choices = [subject]

            distractors = list(set(nouns) - {subject})
            while len(distractors) < 3:
                distractors.append("[Distractor]")

            random.shuffle(distractors)
            for distractor in distractors[:3]:
                answer_choices.append(distractor)

            random.shuffle(answer_choices)
            correct_answer = chr(64 + answer_choices.index(subject) + 1)
            mcqs.append((question_stem, answer_choices, correct_answer))

    return mcqs

# ------------------ PDF Processing ------------------ #
def process_pdf(file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(file)
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text

# ------------------ Streamlit Frontend ------------------ #
def main():
    st.title("🧠 MCQ Generator using NLP")
    st.write("Paste your text or upload a file to generate multiple-choice questions.")

    text_input = st.text_area("📄 Paste your text here:")

    uploaded_file = st.file_uploader("Or upload a text file", type=["txt", "pdf"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".txt"):
            text_input = uploaded_file.read().decode("utf-8")
        elif uploaded_file.name.endswith(".pdf"):
            text_input = process_pdf(uploaded_file)

    num_questions = st.slider("Number of MCQs to generate:", 1, 10, 5)

    if st.button("🚀 Generate MCQs"):
        if text_input:
            mcqs = generate_mcqs(text_input, num_questions)
            if mcqs:
                for i, mcq in enumerate(mcqs):
                    st.write(f"**Question {i+1}:** {mcq[0]}")
                    st.write("Options:")
                    for j, option in enumerate(mcq[1]):
                        st.write(f"{chr(65+j)}. {option}")
                    st.write(f"✅ **Correct Answer:** {mcq[2]}")
                    st.write("---")
            else:
                st.warning("⚠️ No MCQs generated. Try with a longer text.")
        else:
            st.error("Please paste text or upload a file first!")

if __name__ == "__main__":
    main()
