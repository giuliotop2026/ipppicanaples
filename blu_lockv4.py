import streamlit as st
from google import genai
from PIL import Image

# 1. CASSAFORTE INVIOLABILE - BENZINA DALLE SETTINGS
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except KeyError:
    st.error("❌ BENZINA NON TROVATA! CONFIGURA I SECRETS CON 'GEMINI_API_KEY'.")
    st.stop()

# Innesco del Client GenAI
client = genai.Client(api_key=API_KEY)

# CONFIGURAZIONE PAGINA
st.set_page_config(page_title="BLUE LOCK SONAR - GIULIO", page_icon="🔵", layout="centered")

# --- INTERFACCIA NAPOLI POWER ---
st.title("👁️ BLUE LOCK SONAR 4.0 🛰️")
st.markdown("## **IL SONAR CHE SCANSIONA L'ABISSO E IL WEB IN TEMPO REALE!** 🐎")
st.write("---")

# AREA CREDITS
st.sidebar.markdown("### 🛠️ CANTIERE")
st.sidebar.write("**CREATA DA GIULIO SIMPATICO** 💙 ☕")
st.sidebar.write("---")
st.sidebar.info("MODALITÀ: LIVE SEARCH ATTIVA (METEO, TERRENO, NEWS).")

# 2. CARICAMENTO DELLE PARTICELLE
st.header("1. SGANCIATE I DATI 🕵️‍♂️")
st.info("CARICA LE FOTO. IL SONAR FARÀ IL RESTO CERCANDO ONLINE METEO E NEWS.")
uploaded_files = st.file_uploader("DOCUMENTI DEL CANTIERE", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = []
    for file in uploaded_files:
        image = Image.open(file)
        st.image(image, caption=f"ACQUISITO: {file.name}", use_container_width=True)
        images_to_process.append(image)
    
    if st.button("🚀 ATTIVA SONAR LIVE E SCANSIONA"):
        with st.spinner("CONNETTENDOSI AI SATELLITI E PREPARANDO IL CAFFÈ... ☕"):
            try:
                # PROTOCOLLO SONAR 4.0
                prompt_blue_lock = """
                SEI IL SISTEMA 'BLUE LOCK SONAR' DI GIULIO SIMPATICO. 
                
                MISSIONE:
                1. ANALIZZA LE FOTO CARICATE (PESI, QUOTE, CAVALLI).
                2. USA LO STRUMENTO DI RICERCA GOOGLE PER TROVARE:
                   - METEO ATTUALE SULLA LOCALITÀ DELLA GARA (Pisa, Hereford, ecc.).
                   - STATO DEL TERRENO (Erba, fango, sabbia, pesante/morbido).
                   - NEWS DELL'ULTIMA ORA SUI CAVALLI IDENTIFICATI (infortuni, ritiri, cambi guida).
                
                VALUTAZIONE (1-5):
                1. STABILITÀ CIRCUITO (IN BASE AL TERRENO TROVATO ONLINE).
                2. DENSITÀ TECNICA (MOTORE E PRESTAZIONI).
                3. ZAVORRA/PESO (SE IL PESO È UN'ANCORA RISPETTO AL FANGO TROVATO ONLINE, PENALIZZA).
                4. FORMA RECENTE.
                5. NEWS E CAZZIMMA (USA LE NOTIZIE TROVATE ONLINE).
                6. ABISSO QUOTA.
                
                REGOLE:
                - RISPONDI SEMPRE IN MAIUSCOLO.
                - USA: CEMENTO, MARMO, ABISSO, CAZZIMMA.
                - SE SCORE >= 24: '💎 DIAMANTE ASSOLUTO RILEVATO. POSARE IL CEMENTO. CERTEZZA 10000% 💙.'
                - MOSTRA TABELLA E FONTI DELLE NEWS TROVATE.
                """
                
                # INNESCO DEL MOTORE CON GOOGLE SEARCH ATTIVO
                response = client.models.generate_content(
                    model='gemini-2.0-flash',
                    contents=[prompt_blue_lock] + images_to_process,
                    config={
                        'tools': [{'google_search': {}}] 
                    }
                )
                
                st.markdown("### 2. LA SENTENZA DEL SONAR 💙")
                st.success(response.text)
                st.balloons()
                
            except Exception as e:
                st.error(f"URTO NEL SISTEMA: {e}")

# FOOTER GIULIO STYLE
st.write("---")
st.caption("BLUE LOCK SONAR - GIULIO SIMPATICO 💙 ☕ - LIVE EDITION 2026")
