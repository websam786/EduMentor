import streamlit as st
import requests

st.set_page_config(
    page_title="EduMentor AI",
    page_icon="🎓",
    layout="centered"
)


def feedback_card(title, icon, content, color):
    st.markdown(
        f"""
        <div style="
            background-color:#F8FAFC;
            padding:18px;
            border-radius:12px;
            border-left:6px solid {color};
            margin-top:15px;
        ">
            <h3>{icon} {title}</h3>
            <p>{content}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------- HEADER ----------

st.markdown(
    """
    <div style="
        background: linear-gradient(90deg, #2563EB, #7C3AED);
        padding:25px;
        border-radius:15px;
        text-align:center;
        color:white;
    ">
        <h1>🎓 EduMentor AI</h1>
        <h4>Your Personal AI-Powered Academic Mentor</h4>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("Welcome to your personal AI learning mentor")

# ---------- STUDENT INFORMATION ----------

st.header("Student Information")

name = st.text_input("Student Name")

math = st.number_input(
    "Math Marks",
    min_value=0,
    max_value=100
)

english = st.number_input(
    "English Marks",
    min_value=0,
    max_value=100
)

science = st.number_input(
    "Science Marks",
    min_value=0,
    max_value=100
)

social = st.number_input(
    "Social Studies Marks",
    min_value=0,
    max_value=100
)


# ---------- ANALYZE BUTTON ----------

if st.button("Analyze Performance"):

    with st.spinner("EduMentor AI is analyzing your performance"):

        student_data = {
            "name": name,
            "math": math,
            "english": english,
            "science": science,
            "social": social
        }

        response = requests.post(
            "https://edumentor-xfjp.onrender.com/analyze-student",
            json=student_data
        )

    # ---------- RESPONSE ----------

    if response.status_code == 200:

        result = response.json()

        feedback = result["feedback"]

        # ---------- STUDENT REPORT ----------

        st.markdown("## 👤 Student Report")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                f"""
                <div style="
                    background-color:#F8FAFC;
                    padding:18px;
                    border-radius:12px;
                    border-left:6px solid #2563EB;
                ">
                    <h3>👤 {name}</h3>
                    <p>Student Performance Report</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            st.metric(
                "Overall",
                f'{result["percentage"]:.2f}%'
            )


        # ---------- SUBJECT SCORES ----------

        st.markdown("### 📚 Subject Scores")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("📐 Math", math)

        with col2:
            st.metric("📖 English", english)

        col3, col4 = st.columns(2)

        with col3:
            st.metric("🔬 Science", science)

        with col4:
            st.metric("🌍 Social", social)


        # ---------- AI FEEDBACK ----------

        feedback_card(
            "Summary",
            "📋",
            feedback["summary"],
            "#2563EB"
        )

        feedback_card(
            "Strengths",
            "💪",
            feedback["strength"],
            "#16A34A"
        )

        feedback_card(
            "Areas to Improve",
            "📚",
            feedback["areas_to_improve"],
            "#EA580C"
        )

        feedback_card(
            "Tomorrow's Study Plan",
            "📅",
            feedback["study_plan"],
            "#7C3AED"
        )

    else:

        st.error(
            f"Something went wrong while analyzing the student. "
            f"Status code: {response.status_code}"
        )
