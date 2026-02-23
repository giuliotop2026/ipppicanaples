import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# 1. NOTIFICA SONORA (PROTOCOLLO SONIC)
def play_beep():
    beep_html = '<audio autoplay><source src="https://www.soundjay.com/buttons/beep-01a.mp3" type="audio/mpeg"></audio>'
    components.html(beep_html, height=0, width=0)

# 2. CASSAFORTE API
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("❌ BENZINA MANCANTE NEI SECRETS!")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="CHAMELEON 7.1", page_icon="🦎", layout="centered")

st.title("🦎 SNIPER 7.1 'CHAMELEON' 🚀")
st.markdown("## **AUTOPILOTA ANALITICO: ZERO INPUT, SOLO GLORIA** 💙 ☕")
st.write("---")

uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT (QUALUNQUE NAZIONE):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 ATTIVA PUNTAMENTO AUTOMATICO"):
    if not uploaded_files:
        st.warning("SOCIO, IL REATTORE È VUOTO. CARICA LE FOTO!")
    else:
        with st.spinner("SCANSIONE GEOLOCALIZZATA IN CORSO... 👁️"):
            try:
                # FASE 1: VISIONE UNIVERSALE (GEMINI 2.5 FLASH)
                prompt_vision = """
                Analizza questi dati e identifica AUTOMATICAMENTE l'ippodromo e la nazione.
                ESTRAI: 
                - Pista, Distanza, Superficie.
                - Elenco completo partecipanti con Quota, Peso, Sequenza Risultati 2026.
                - Identifica note critiche (FE, CD, distacchi in lunghezze).
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success("TARGET IDENTIFICATO! INNESCAMENTO SONAR DINAMICO... ☕")

                # FASE 2: SONAR IBRIDO (PERPLEXITY SONAR PRO)
                prompt_pplx = f"""
                SEI IL 'GLOBAL ARCHITECT'. ANALIZZA QUESTI DATI:
                {dati_estratti}

                1. RICERCA LIVE: Cerca le condizioni meteo odierne e il 'bias' della pista per questo ippodromo specifico.
                2. ADATTAMENTO PROTOCOLLO: 
                   - SE OSTACOLI/TURF FRANCIA: Peso ≥58kg + forma 3/4 = ABISSO. Cerca polmoni d'acciaio. [cite: 2026-02-23]
                   - SE SUD AFRICA: Applica Patch 6.8 (Lunghezze < 2.5L = MARMO). Dual-Place rigoroso 1-1/1-2. [cite: 2026-02-23]
                   - SE USA DIRT: Ignora peso, cerca Beyer record crescenti 2026. [cite: 2026-02-23]
                   - SE ITALIA: Blocco rimosso. Applica Highlander (Rating/Peso). [cite: 2026-02-11, 2026-02-20]
                
                3. FILTRO CRITICO: Qualsiasi piazzamento ≥ 8 recente o caduta (FE/CD) = ELIMINAZIONE ISTANTANEA. [cite: 2026-02-23]

                REFERTO FINALE:
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE TECNICA: [Analisi profonda del momentum e del terreno per schiacciare il favorito].'
                
                TERMINI: MARMO, CEMENTO, ABISSO, CAZZIMMA. SINTASSI MAIUSCOLA.
                """
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=[{"role": "user", "content": prompt_pplx}]
                )
                
                sentenza = response_pplx.choices[0].message.content
                st.markdown("### 🎯 SENTENZA DEL REATTORE 7.1")
                st.info(sentenza)
                
                if "DIAMANTE" in sentenza.upper():
                    play_beep()
                    st.balloons()

            except Exception as e:
                st.error(f"URTO TECNICO: {e}")

st.write("---")
st.caption("SNIPER 7.1 'CHAMELEON' - THE ULTIMATE ARCHITECT 💙 ☕")
