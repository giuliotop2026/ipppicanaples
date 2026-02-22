import streamlit as st
from google import genai
from PIL import Image

# 1. CASSAFORTE E BENZINA
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except KeyError:
    st.error("❌ BENZINA NON TROVATA! CONFIGURA I SECRETS.")
    st.stop()

client = genai.Client(api_key=API_KEY)

st.set_page_config(page_title="BLUE LOCK FORTEZZA - GIULIO", page_icon="🏰", layout="centered")

# --- INTERFACCIA ---
st.title("🏰 BLUE LOCK FORTEZZA 4.5 👁️")
st.markdown("## **IL DIAMANTE DIPENDE DAL FANGO: SCANSIONE RELATIVA ATTIVA!** 💙 ☕")

st.sidebar.markdown("### 🛠️ CREATORE: GIULIO SIMPATICO")
st.sidebar.info("MODELLO STABILE: 1.5 FLASH - SONAR LIVE ATTIVO.")

# 2. CARICAMENTO PARTICELLE
st.header("1. SGANCIATE I DATI DEL GIORNO 🕵️‍♂️")
uploaded_files = st.file_uploader("FOTO QUOTE, PESI E PRESTAZIONI", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)
    
    if st.button("🔥 AVVIA SCANSIONE RELATIVA"):
        with st.spinner("SCANSIONANDO METEO, TERRENO E CAZZIMMA... ☕"):
            try:
                # PROTOCOLLO FORTEZZA RELATIVA
                prompt_fortezza = """
                SEI IL SISTEMA 'BLUE LOCK FORTEZZA' DI GIULIO SIMPATICO.
                
                MISSIONE: IDENTIFICA IL 'SECONDO MIGLIORE' IN BASE ALLE CONDIZIONI SPECIFICHE DI OGGI.
                1. USA GOOGLE SEARCH PER TROVARE METEO E STATO DEL TERRENO (FANGO, ERBA, SABBIA).
                2. ANALIZZA LE FOTO: PESI, QUOTE E PRESTAZIONI.
                
                PROTOCOLLO RIGIDO (1-5):
                - STABILITÀ CIRCUITO: Affinità reale al terreno di oggi (se piove, chi tiene?).
                - DENSITÀ TECNICA: Potenza del motore relativa al campo partenti.
                - POLMONI D'ACCIAIO: Resistenza sulla distanza specifica con la zavorra odierna.
                - ZAVORRA/PESO: Chi è avvantaggiato dal peso in queste condizioni di terreno?
                - FORMA RECENTE: Deve essere solida. Se non è nei primi 3 recentemente, penalizza.
                - CAZZIMMA: News online su cambi guida o voglia di vincere.

                SENTENZA:
                - SCORE >= 26: '💎 DIAMANTE ASSOLUTO. CERTEZZA 10000% 💙.'
                - SCORE 23-25: '⚙️ BULLONE SOLIDO. SOLO PIAZZATO. IL CEMENTO REGGE.'
                - SCORE < 23: '❌ CANTIERE PERICOLOSO. ABISSO TROPPO PROFONDO.'

                RICORDA: IL VINCENTE È QUELLO CHE TIEN' 'A CAZZIMMA NELLE CONDIZIONI DI OGGI.
                """
                
                response = client.models.generate_content(
                    model='gemini-1.5-flash',
                    contents=[prompt_fortezza] + images_to_process,
                    config={'tools': [{'google_search': {}}]}
                )
                
                st.markdown("### 2. VERDETTO DI GIULIO 💙")
                st.success(response.text)
                st.balloons()
                
            except Exception as e:
                st.error(f"URTO: {e}. ASPETTA 30 SECONDI.")
