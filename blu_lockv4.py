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
st.set_page_config(page_title="BLUE LOCK VISION - GIULIO", page_icon="🔵", layout="centered")

# --- INTERFACCIA NAPOLI POWER ---
st.title("👁️ BLUE LOCK VISION 4.6 🏰")
st.markdown("## **MOTORE INTERNO ATTIVO: ANALISI PURA DELLE PARTICELLE!** 🏇")
st.write("---")

# AREA CREDITS
st.sidebar.markdown("### 🛠️ CANTIERE")
st.sidebar.write("**CREATA DA GIULIO SIMPATICO** 💙 ☕")
st.sidebar.write("---")
st.sidebar.info("MODELLO: GEMINI 2.0 FLASH - FOCUS SCREENSHOT (NO LIVE).")

# 2. CARICAMENTO DELLE PARTICELLE
st.header("1. CARICA LE TUE FOTO 🕵️‍♂️")
st.info("CARICA SCREENSHOT DI QUOTE, PESI, METEO E NEWS. IL RADAR LEGGERÀ TUTTO.")
uploaded_files = st.file_uploader("DOCUMENTI DEL CANTIERE", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)
    
    if st.button("🔥 AVVIA SCANSIONE MOLECOLARE"):
        with st.spinner("PREPARANDO IL CAFFÈ E SCANSIONANDO IL MARMO... ☕"):
            try:
                # PROTOCOLLO DI RELATIVITÀ 4.6 (SOLO DATI FORNITI)
                prompt_blue_lock = """
                SEI IL SISTEMA 'BLUE LOCK VISION 4.6' DI GIULIO SIMPATICO. 
                
                MISSIONE: IDENTIFICA IL 'SECONDO MIGLIORE' ANALIZZANDO ESCLUSIVAMENTE GLI SCREENSHOT FORNITI.
                - IL DIAMANTE DIPENDE DALLA GARA, DAL FANGO E DALLA CAZZIMMA SCRITTA NELLE FOTO.
                - LEGGI OGNI DETTAGLIO: PESI, TERRENO (SOFT, GOOD, HEAVY), NEWS E PRESTAZIONI.
                
                PROTOCOLLO RIGIDO (1-5):
                1. STABILITÀ CIRCUITO (AFFINITÀ AL TERRENO INDICATO NELLE FOTO).
                2. DENSITÀ TECNICA (MOTORE RELATIVO AL CAMPO PARTENTI).
                3. POLMONI D'ACCIAIO (RESISTENZA SULLA DISTANZA CON LA ZAVORRA ODIERNA).
                4. ZAVORRA/PESO (CHI È AVVANTAGGIATO DAL PESO IN QUESTE CONDIZIONI?).
                5. FORMA RECENTE (RIGORE: SE NON È NEI PRIMI 3 RECENTEMENTE, IL VOTO È BASSO).
                6. CAZZIMMA (TESTO DELLE NEWS, CAMBI GUIDA, VOGLIA DI VINCERE).
                
                SENTENZA FINALE (IN MAIUSCOLO):
                - SCORE >= 26: '💎 DIAMANTE ASSOLUTO RILEVATO. CERTEZZA 10000% 💙.'
                - SCORE 23-25: '⚙️ BULLONE SOLIDO. SOLO PIAZZATO. IL CEMENTO REGGE.'
                - SCORE < 23: '❌ CANTIERE PERICOLOSO. ABISSO TROPPO PROFONDO.'

                NOTE DI GIULIO: IL VINCENTE NON È IL PIÙ VELOCE, MA QUELLO CHE TIEN' 'A CAZZIMMA NELLE CONDIZIONI DI OGGI.
                """
                
                # CHIAMATA SENZA GOOGLE SEARCH PER EVITARE ERRORE 429
                response = client.models.generate_content(
                    model='gemini-2.0-flash', 
                    contents=[prompt_blue_lock] + images_to_process
                )
                
                st.markdown("### 2. LA SENTENZA DI GIULIO 💙")
                st.success(response.text)
                st.balloons()
                
            except Exception as e:
                st.error(f"URTO NEL SISTEMA: {e}. ASPETTA 30 SECONDI.")

# FOOTER GIULIO STYLE
st.write("---")
st.caption("BLUE LOCK VISION - GIULIO SIMPATICO 💙 ☕ - VERSION 4.6")
