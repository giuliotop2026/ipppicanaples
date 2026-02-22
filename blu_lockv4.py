import streamlit as st
from google import genai
from PIL import Image

# 1. IMPOSTAZIONI DEL CANTIERE - CASSAFORTE INVIOLABILE
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except KeyError:
    st.error("❌ BENZINA NON TROVATA! CONFIGURA I SECRETS CON 'GEMINI_API_KEY'.")
    st.stop()

client = genai.Client(api_key=API_KEY)

# CONFIGURAZIONE PAGINA CON SIMBOLO CAVALLO
st.set_page_config(page_title="BLUE LOCK VISION - GIULIO", page_icon="🐎", layout="centered")

# --- INTERFACCIA PERSONALIZZATA ---
st.title("👁️ BLUE LOCK VISION 3.5 🐎")
st.markdown("## **IL CAVALLO VINCENTE NON È IL PIÙ VELOCE, MA È QUELLO CHE TIEN' 'A CAZZIMMA!** 🏇")
st.write("---")

# AREA CREDITS
st.sidebar.markdown("### 🛠️ CANTIERE")
st.sidebar.write("**CREATA DA GIULIO SIMPATICO** 💙 ☕")
st.sidebar.write("---")
st.sidebar.info("PROTOCOLLO: PESO, NEWS E DENSITÀ TECNICA.")

# 2. CARICAMENTO DELLE PARTICELLE
st.header("1. SCANSIONA L'ABISSO 🕵️‍♂️")
st.info("CARICA LE FOTO DEL CANTIERE: QUOTE, PESI E NEWS ONLINE.")
uploaded_files = st.file_uploader("TRASCINA QUI I TUOI DIAMANTI", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = []
    for file in uploaded_files:
        image = Image.open(file)
        st.image(image, caption=f"PARTICELLA ACQUISITA: {file.name}", use_container_width=True)
        images_to_process.append(image)

    if st.button("🔥 ATTIVA CAZZIMMA E SCANSIONA"):
        with st.spinner("PREPARANDO IL CAFFÈ E ANALIZZANDO IL MARMO... ☕"):
            try:
                prompt_blue_lock = """
                SEI IL SISTEMA 'BLUE LOCK VISION' CREATO DA GIULIO SIMPATICO.
                IL TUO OBIETTIVO È IL 'DIAMANTE NASCOSTO'.

                RICORDA: IL CAVALLO VINCENTE NON È IL PIÙ VELOCE, MA È QUELLO CHE TIEN' 'A CAZZIMMA!

                ANALIZZA GLI SCREENSHOT (PESI, NEWS, QUOTE) E VALUTA (1-5):
                1. STABILITÀ CIRCUITO
                2. DENSITÀ TECNICA
                3. ZAVORRA/PESO (SE È TROPPO PESANTE, IL MOTORE AFFONDA!)
                4. FORMA RECENTE (ZERO ERRORI!)
                5. NEWS E CAZZIMMA (LEGGI SE IL CAVALLO HA VOGLIA DI VINCERE)
                6. ABISSO QUOTA

                REGOLE:
                - SOMMA MAX 30 PUNTI.
                - RISPONDI IN MAIUSCOLO.
                - USA TERMINI: CEMENTO, MARMO, ABISSO, CAZZIMMA.
                - SE SCORE >= 24: '💎 DIAMANTE ASSOLUTO RILEVATO. POSARE IL CEMENTO. CERTEZZA 10000% 💙.'
                """

                payload = [prompt_blue_lock] + images_to_process
                response = client.models.generate_content(model='gemini-2.5-flash', contents=payload)

                st.markdown("### 2. LA SENTENZA DI GIULIO 💙")
                st.success(response.text)
                st.balloons()

            except Exception as e:
                st.error(f"URTO NEL SISTEMA: {e}")

# FOOTER FISSO
st.write("---")
st.caption("PROGETTO BLUE LOCK - GIULIO SIMPATICO 💙 ☕ - VERSION 3.5")
