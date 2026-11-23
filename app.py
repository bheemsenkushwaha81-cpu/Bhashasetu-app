import streamlit as st

st.set_page_config(
    page_title="BhashaSetu",
    page_icon="🌉",
    layout="wide",
)

# ------------------------------
# Translations
# ------------------------------
TEXT = {
    "English": {
        "title": "Welcome to BhashaSetu",
        "tagline": "Science becomes easy in your language!",
        "intro": "Learn Science in the language you understand.",
        "language": "Choose your language",
        "selected": "Your selected language is",
        "class": "Class 8 Science",
        "chapter": "Choose your chapter",
        "story": "Learn through stories",
        "story_text": "Welcome to the world of Science! Explore amazing concepts through simple, friendly stories.",
        "lesson": "Today’s lesson",
        "key": "Key ideas",
        "experiment": "Science Experiment",
        "notes": "Make your notes",
        "notes_placeholder": "Write your chapter notes here...",
        "save": "Save my notes",
        "saved": "Your notes are ready!",
        "download": "Download notes",
        "quiz": "Science Quiz",
        "check": "Check answer",
        "correct": "Excellent! Correct answer 🎉",
        "wrong": "Not quite. Read the explanation below.",
        "explanation": "Explanation",
        "footer": "Made with love for students",
        "brand": "BHASHASETU — Learn, Explore and Grow",
        "progress": "Your progress",
        "complete": "Chapters completed",
        "score": "Quiz score",
        "reset": "Reset progress",
    },
    "Hindi": {
        "title": "BhashaSetu में आपका स्वागत है",
        "tagline": "विज्ञान अब अपनी भाषा में आसान!",
        "intro": "अपनी समझ की भाषा में विज्ञान सीखें।",
        "language": "अपनी भाषा चुनें",
        "selected": "आपकी चुनी हुई भाषा है",
        "class": "कक्षा 8 विज्ञान",
        "chapter": "अपना अध्याय चुनें",
        "story": "कहानियों के साथ सीखें",
        "story_text": "विज्ञान की दुनिया में आपका स्वागत है! सरल और प्यारी कहानियों के साथ नए विषय सीखें।",
        "lesson": "आज का पाठ",
        "key": "मुख्य बातें",
        "experiment": "विज्ञान प्रयोग",
        "notes": "अपने नोट्स बनाएँ",
        "notes_placeholder": "यहाँ अध्याय के नोट्स लिखें...",
        "save": "नोट्स सेव करें",
        "saved": "आपके नोट्स तैयार हैं!",
        "download": "नोट्स डाउनलोड करें",
        "quiz": "विज्ञान प्रश्नोत्तरी",
        "check": "उत्तर जाँचें",
        "correct": "बहुत बढ़िया! सही उत्तर 🎉",
        "wrong": "लगभग सही। नीचे दिया व्याख्या पढ़ें।",
        "explanation": "व्याख्या",
        "footer": "छात्रों के लिए प्यार से बनाया गया",
        "brand": "भाषासेतु — सीखें, खोजें और आगे बढ़ें",
        "progress": "आपकी प्रगति",
        "complete": "पूर्ण अध्याय",
        "score": "क्विज़ स्कोर",
        "reset": "प्रगति रीसेट करें",
    },
}

CHAPTERS = {
    "Microorganisms: Friend and Foe": {
        "title": "Microorganisms: Friend and Foe",
        "story_en": "Tiny organisms called microorganisms live everywhere—in soil, air, water, and even inside our bodies. Some help us make curd and medicines, while some can cause diseases.",
        "lesson_en": "Microorganisms are too small to be seen with the naked eye. Bacteria, fungi, protozoa, and some algae are microorganisms. Useful microorganisms make curd, bread, medicines, and help clean the environment.",
        "points_en": ["Microorganisms are found in almost every environment.", "Some microorganisms cause diseases and food spoilage.", "Vaccination helps protect us from many diseases.", "Microorganisms recycle nutrients in nature."],
        "experiment_en": "Place a slice of bread in a dry paper bag and another in a moist bag. Observe after two days. Do not open or eat mouldy bread.",
        "question_en": "Which microorganism is used to make curd?",
        "options_en": ["Virus", "Bacteria", "Algae", "Protozoa"],
        "answer_en": "Bacteria",
        "explanation_en": "Lactic acid bacteria convert milk into curd.",
        "icon": "🦠",
    },
    "Force and Pressure": {
        "title": "Force and Pressure",
        "story_en": "A cart moves when pushed and stops when pulled. Push and pull are forces. Pressure tells us how force is spread over a surface.",
        "lesson_en": "A force can move, stop, or change the shape or direction of an object. Pressure is force per unit area. Smaller area can create greater pressure.",
        "points_en": ["Force can change motion or shape.", "Pressure = Force ÷ Area.", "Broad straps reduce pressure on a shoulder.", "Liquids and gases exert pressure in all directions."],
        "experiment_en": "Press the blunt end of a pencil and then its sharpened point into clay. Observe the impressions safely.",
        "question_en": "Pressure is equal to force divided by which quantity?",
        "options_en": ["Speed", "Area", "Mass", "Time"],
        "answer_en": "Area",
        "explanation_en": "Pressure = Force/Area. Pressure decreases when the area increases.",
        "icon": "🧲",
    },
    "Sound": {
        "title": "Sound",
        "story_en": "A vibrating guitar string produces sound. In every sound, vibrations carry energy from a source to our ears.",
        "lesson_en": "Sound is produced by vibrations. It travels through solids, liquids, and gases, but not through vacuum. Loudness and pitch describe sound.",
        "points_en": ["Sound requires a vibrating source.", "Sound needs a medium to travel.", "Amplitude affects loudness.", "Frequency mainly affects pitch."],
        "experiment_en": "Stretch a rubber band around a box. Pluck it gently and touch it to feel the vibrations.",
        "question_en": "What property of a sound mainly affects its pitch?",
        "options_en": ["Frequency", "Temperature", "Colour", "Weight"],
        "answer_en": "Frequency",
        "explanation_en": "Higher frequency usually means a higher pitch.",
        "icon": "🔊",
    },
    "Light": {
        "title": "Light",
        "story_en": "Light travels in straight lines and helps us see objects. Mirrors reflect light, while lenses can bend it.",
        "lesson_en": "Light enables vision and travels in straight lines in a uniform medium. Mirrors reflect light, and the law of reflection compares angles.",
        "points_en": ["Light travels in straight lines.", "A mirror reflects light.", "The angle of incidence equals the angle of reflection.", "The moon is visible because it reflects sunlight."],
        "experiment_en": "Shine a torch through a narrow cardboard hole and observe how light travels to a wall.",
        "question_en": "Which object is visible because it reflects sunlight?",
        "options_en": ["Torch", "Bulb", "Moon", "Fire"],
        "answer_en": "Moon",
        "explanation_en": "The Moon does not produce its own visible light; it reflects sunlight.",
        "icon": "💡",
    },
    "Coal and Petroleum": {
        "title": "Coal and Petroleum",
        "story_en": "Coal and petroleum were formed slowly from ancient plants and organisms under heat and pressure over millions of years.",
        "lesson_en": "Coal and petroleum are fossil fuels. They are exhaustible natural resources, so we must use them carefully and develop alternatives.",
        "points_en": ["Fossil fuels take millions of years to form.", "Coal, petroleum, and natural gas are exhaustible resources.", "Burning fuels can cause air pollution.", "Conservation and renewable energy reduce dependence on fossil fuels."],
        "experiment_en": "Compare how much material a bicycle, bus, and scooter consume in an imaginary one-week journey. Discuss alternatives.",
        "question_en": "Coal and petroleum are examples of what type of resource?",
        "options_en": ["Renewable", "Exhaustible", "Unlimited", "Artificial"],
        "answer_en": "Exhaustible",
        "explanation_en": "They are exhaustible because they take millions of years to form and may run out.",
        "icon": "⛽",
    },
}

LANGUAGES = ["English", "Hindi", "Gujarati", "Marathi", "Marwari"]

for key, default in {
    "completed_chapters": [],
    "quiz_scores": {},
    "saved_notes": {},
}.items():
    if key not in st.session_state:
        st.session_state[key] = default.copy() if isinstance(default, list) else default.copy()

# ------------------------------
# Header and navigation
# ------------------------------
st.markdown("""
<style>
.block-container {padding-top: 2rem; padding-bottom: 2rem;}
.hero {padding: 1.2rem 1.5rem; border-radius: 18px; background: linear-gradient(135deg, #eef7ff, #f2fff5); border: 1px solid #dceee2;}
.lesson-card {padding: 1.2rem; border-radius: 14px; border: 1px solid #e4e7ec; background: white;}
[data-testid="stMetric"] {background: #f7fafc; padding: 12px; border-radius: 12px;}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    st.title("🌉 BhashaSetu")
    st.subheader("Science becomes easy in your language!")
    st.write("Learn Science in the language you understand.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    language = st.selectbox("Choose your language", LANGUAGES)
    st.info("Interface translation available in English and Hindi.")

ui = TEXT[language] if language in TEXT else TEXT["English"]

st.success(f"{ui['selected']} {language}")

chapter_name = st.selectbox("Choose your chapter", list(CHAPTERS.keys()))
chapter = CHAPTERS[chapter_name]

# ------------------------------
# Progress summary
# ------------------------------
st.subheader(ui["progress"])
c1, c2 = st.columns(2)
with c1:
    st.metric(ui["complete"], len(st.session_state.completed_chapters))
with c2:
    total_score = sum(st.session_state.quiz_scores.values())
    st.metric(ui["score"], f"{total_score}/{len(CHAPTERS)}")

st.divider()

# ------------------------------
# Lesson
# ------------------------------
st.header(f"{chapter['icon']} {ui['class']} — {chapter_name}")
st.subheader(ui["story"])
st.write(chapter["story_en"])

lesson_col, key_col = st.columns([2, 1])
with lesson_col:
    st.markdown(f"### {ui['lesson']}")
    st.write(chapter["lesson_en"])
with key_col:
    st.markdown(f"### {ui['key']}")
    for point in chapter["points_en"]:
        st.write(f"• {point}")

st.markdown(f"### 🧪 {ui['experiment']}")
st.info(chapter["experiment_en"])

# ------------------------------
# Notes
# ------------------------------
st.header(f"📝 {ui['notes']}")
existing_note = st.session_state.saved_notes.get(chapter_name, "")
notes = st.text_area(
    ui["notes_placeholder"],
    value=existing_note,
    height=180,
)

save_col, download_col = st.columns(2)
with save_col:
    if st.button(ui["save"]):
        st.session_state.saved_notes[chapter_name] = notes
        st.success(ui["saved"])
with download_col:
    st.download_button(
        ui["download"],
        data=notes or "",
        file_name=f"BhashaSetu-{chapter_name.replace(':', '').replace(' ', '-')}-notes.txt",
        mime="text/plain",
    )

# ------------------------------
# Quiz
# ------------------------------
st.header(f"🧠 {ui['quiz']}")
answer = st.radio(chapter["question_en"], chapter["options_en"])

if st.button(ui["check"]):
    if answer == chapter["answer_en"]:
        st.success(ui["correct"])
        st.session_state.quiz_scores[chapter_name] = 1
        if chapter_name not in st.session_state.completed_chapters:
            st.session_state.completed_chapters.append(chapter_name)
    else:
        st.error(ui["wrong"])
        st.session_state.quiz_scores[chapter_name] = 0

    st.markdown(f"**{ui['explanation']}:** {chapter['explanation_en']}")

st.divider()

col_footer, reset_col = st.columns([3, 1])
with col_footer:
    st.write(f"❤️ {ui['footer']}")
    st.write(ui["brand"])
with reset_col:
    if st.button(ui["reset"]):
        st.session_state.completed_chapters = []
        st.session_state.quiz_scores = {}
        st.rerun()

