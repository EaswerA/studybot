import streamlit as st
from engine.roadmap import create_study_plan
from models.question_generator import generate_template_question, generate_t5_question
from engine.tracker import log_score, get_scores

st.title("StudyBot - NLP Learning Assistant")

name = st.text_input("Your name")
subject = st.text_input("Subject (e.g., neet_biology)")
days = st.number_input("Days left to study", min_value=1, step=1)

if st.button("Create Plan"):
    plan = create_study_plan(subject, days)
    for i, topics in enumerate(plan):
        st.write(f"**Day {i+1}**: {', '.join(topics)}")

if st.button("Start Quiz"):
    concept = st.text_input("Enter a concept to quiz on (e.g., photosynthesis)")
    if st.checkbox("Use T5 model?"):
        question = generate_t5_question(f"{concept} is ...")  # write a mini para
    else:
        question = generate_template_question(concept)

    st.write("Question:", question)
    answer = st.text_input("Your Answer")
    if st.button("Submit Answer"):
        score = st.slider("How well did you recall? (0-5)", 0, 5)
        log_score(name, concept, score)
        st.success("Score logged!")

