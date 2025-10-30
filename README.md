# MCQ Generator using NLP

The MCQ Generator using NLP is an intelligent application designed to automatically create Multiple Choice Questions (MCQs) from any given text or PDF document.  
It combines the power of Natural Language Processing (NLP) and Machine Learning to generate high-quality, contextually relevant questions that can be used for educational, training, and evaluation purposes.

This project leverages libraries such as spaCy, NLTK, and Streamlit to process input text, extract key entities and concepts, and then generate meaningful questions with multiple options (including correct and distractor answers).  
The web-based interface allows users to easily paste text or upload files, and instantly view generated MCQs — making the entire process simple, efficient, and fully automated.

---

## Project Overview

### Objective
The primary objective of this project is to automate the creation of MCQs from text-based materials such as chapters, research articles, notes, or e-learning content.  
By doing so, it significantly reduces the manual effort educators and content creators spend on designing assessments, while maintaining quality and coherence.

This system can be used by:
- Teachers and educators to generate quizzes from study material  
- Students and learners for self-assessment and revision  
- Training professionals to prepare competency tests  
- E-learning platforms for automated evaluation content creation  

In a world where education is increasingly digital, the project aims to provide a smart, scalable, and AI-driven solution for question generation that enhances learning and teaching efficiency.

---

## Features

1. **Flexible Input Options**
   - Users can paste text directly or upload `.txt` or `.pdf` files.
   - Extracts text automatically from PDFs using PyPDF2.

2. **Intelligent Text Analysis**
   - Uses spaCy for tokenization, POS tagging, and entity recognition.
   - Identifies meaningful nouns and entities for question formation.

3. **MCQ Generation Logic**
   - Creates fill-in-the-blank style questions.
   - Automatically generates one correct and three distractor options.

4. **Automatic Distractor Creation**
   - Uses NLP and text context to create realistic incorrect answers.

5. **Interactive Web Interface**
   - Built with Streamlit, allowing real-time question generation.

6. **Dynamic MCQ Display**
   - Displays each question with clear formatting and correct answers.

7. **Extensible Architecture**
   - Can easily be extended to support multiple languages or deep learning models.

---

## Tech Stack and Tools

| Category | Tools / Libraries Used | Purpose and Description |
|-----------|------------------------|--------------------------|
| Programming Language | Python 3.13 | Core development language used for implementing NLP logic, backend processing, and integration with libraries. |
| Frontend / User Interface | Streamlit | Framework for building the web-based interface that allows users to interact with the MCQ generator easily. |
| Natural Language Processing Libraries | spaCy, NLTK | Used for tokenization, POS tagging, entity recognition, and sentence segmentation to identify meaningful question patterns. |
| Machine Learning Frameworks | PyTorch, Transformers | Potentially used for advanced question generation and contextual understanding; supports integration with pre-trained language models. |
| PDF Processing | PyPDF2 | Extracts readable text from uploaded PDF documents for analysis and MCQ creation. |
| Data Handling and Processing | Pandas, NumPy | Handles text data manipulation, array processing, and efficient data management throughout the pipeline. |
| Development Environment | VS Code with Python Virtual Environment (venv) | Provides an isolated and controlled workspace to manage dependencies and maintain code reproducibility. |

---

## How the System Works

### 1. Input Phase
The user provides input by pasting text or uploading a file. The system reads and converts it into raw text for processing.

### 2. Preprocessing Phase
The text undergoes cleaning, tokenization, and part-of-speech tagging using spaCy and NLTK.  
Unnecessary symbols, punctuation, and stopwords are removed to retain meaningful words.

### 3. Question Generation Phase
From the preprocessed text, the system identifies sentences with high informational value.  
Key nouns or entities are replaced with blanks to form questions, and distractors are generated automatically.

### 4. Output Phase
The final MCQs are displayed through the Streamlit interface, with clearly formatted questions, options, and correct answers.

---

## Importance of the Project

- Automation of manual effort: Reduces hours of question-writing into seconds.  
- Scalability: Can handle small paragraphs or large documents effortlessly.  
- Adaptability: Easily adaptable for different subjects and domains.  
- Integration: Can be integrated with LMS or e-learning platforms.  
- Future scope: Expandable to support semantic question generation using deep learning models like T5 or GPT.  

---

## System Architecture (Overview)
<img width="866" height="833" alt="Screenshot 2025-10-30 at 10 55 23 AM" src="https://github.com/user-attachments/assets/93610ec6-ee87-4ea7-b983-1c627ff13d94" />

