import streamlit as st
from google import genai
from PIL import Image

# 1. CASSAFORTE INVIOLABILE - BENZINA DALLE SETTINGS
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except KeyError:
    st.error("❌ BENZINA NON TROVATA! CONFIGURA I SECRETS CON 'GEMINI_API_KEY'.")
    st.stop()

# Innesco del Client GenAI (Modello 2.0 Flash)
client = genai.Client(api_key=API_KEY)

# CONFIGURAZIONE PAGINA
st.set_page_config(page_title="BLUE LOCK SONAR 2.5 - GIULIO", page_icon="🔵", layout="centered")

# --- INTERFACCIA NAPOLI POWER ---
st.title("👁️ BLUE LOCK SONAR 2.5 🛰️")
st.markdown("## **IL DIAMANTE DIPENDE DALLA GARA: SCANSIONE RELATIVA ATTIVA!** 🏇")
st.write("---")

# AREA CREDITS
st.sidebar.markdown("### 🛠️ CANTIERE")
st.sidebar.write("**CREATA DA GIULIO SIMPATICO** 💙 ☕")
st.sidebar.write("---")
st.sidebar.info("MODELLO: GEMINI 2.0 FLASH (SONAR 2.5) - LIVE SEARCH ATTIVO.")

# 2. CARICAMENTO DELLE PARTICELLE
st.header("1. SGANCIATE I DATI 🕵️‍♂️")
st.info("CARICA LE FOTO. IL SONAR ANALIZZERÀ IL FANGO E IL METEO IN TEMPO REALE.")
uploaded_files = st.file_uploader("DOCUMENTI DEL CANTIERE", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)
    
    if st.button("🚀 ATTIVA SONAR 2.5 E SCANSIONA"):
        with st.spinner("CONNETTENDOSI AI SATELLITI E PREPARANDO IL CAFFÈ... ☕"):
            try:
                # PROTOCOLLO DI RELATIVITÀ 2.5
                prompt_blue_lock = """
                SEI IL SISTEMA 'BLUE LOCK SONAR 2.5' DI GIULIO SIMPATICO. 
                
                MISSIONE: IDENTIFICA IL 'SECONDO MIGLIORE' CHE PUÒ VINCERE IN QUESTE CONDIZIONI SPECIFICHE.
                - IL DIAMANTE NON È FISSO: DIPENDE DALLA GARA, DAL FANGO E DALLA CAZZIMMA.
                - USA GOOGLE SEARCH PER TROVARE: METEO, STATO DEL TERRENO E NEWS ULTIMO MINUTO.
                
                PROTOCOLLO RIGIDO (1-5):
                1. STABILITÀ CIRCUITO (AFFINITÀ AL TERRENO DI OGGI: SE C'È FANGO, CHI TIENE?).
                2. DENSITÀ TECNICA (IL MOTORE RELATIVO AL CAMPO PARTENTI).
                3. POLMONI D'ACCIAIO (RESISTENZA SULLA DISTANZA CON LA ZAVORRA ODIERNA).
                4. ZAVORRA/PESO (CHI È AVVANTAGGIATO DAL PESO IN QUESTO MOMENTO?).
                5. FORMA RECENTE (RIGORE: SE NON È NEI PRIMI 3 RECENTEMENTE, IL VOTO È BASSO).
                6. CAZZIMMA (NEWS ONLINE, CAMBI GUIDA, VOGLIA DI VINCERE).
                
                SENTENZA FINALE (IN MAIUSCOLO):
                - SCORE >= 26: '💎 DIAMANTE ASSOLUTO RILEVATO. CERTEZZA 10000% 💙.'
                - SCORE 23-25: '⚙️ BULLONE SOLIDO. SOLO PIAZZATO. IL CEMENTO REGGE.'
                - SCORE < 23: '❌ CANTIERE PERICOLOSO. ABISSO TROPPO PROFONDO.'

                NOTE DI GIULIO: IL VINCENTE NON È IL PIÙ VELOCE, MA QUELLO CHE TIEN' 'A CAZZIMMA OGGI.
                """
                
                # CHIAMATA AL MODELLO 2.0 FLASH (IL 2.5 DI GIULIO)
                response = client.models.generate_content(
                    model='gemini-2.0-flash', 
                    contents=[prompt_blue_lock] + images_to_process,
                    config={'tools': [{'google_search': {}}]}
                )
                
                st.markdown("### 2. LA SENTENZA DEL SONAR 💙")
                st.success(response.text)
                st.balloons()
                
            except Exception as e:
                st.error(f"URTO NEL SISTEMA: {e}. ASPETTA 60 SECONDI E RIPROVA.")

# FOOTER GIULIO STYLE
st.write("---")
st.caption("BLUE LOCK SONAR - GIULIO SIMPATICO 💙 ☕ - VERSION 2.5")
