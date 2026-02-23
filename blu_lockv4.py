import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# 1. NOTIFICA SONORA
def play_beep():
    beep_html = '<audio autoplay><source src="https://www.soundjay.com/buttons/beep-01a.mp3" type="audio/mpeg"></audio>'
    components.html(beep_html, height=0, width=0)

# 2. CASSAFORTE API
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("❌ CHIAVI API MANCANTI!")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 7.6.1 STABLE", page_icon="🎯", layout="centered")

st.title("🎯 SNIPER 7.6.1 'STABLE GHOST' 🚀")
st.markdown("## **MOTORE RICALIBRATO: ZERO ERRORI DI CODICE** 💙 ☕")

uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 RIAVVIA REATTORE 7.6.1"):
    if not uploaded_files:
        st.warning("CARICA I DATI!")
    else:
        with st.spinner("PUNTAMENTO LASER... 👁️"):
            try:
                # FASE 1: VISIONE ESTRAZIONE (GEMINI)
                prompt_vision = """
                Converti questi dati in un report tecnico di 'Soggetti Atletici'.
                ESTRAI:
                [INIZIO SOGGETTO]
                - NOME:
                - QUALITÀ (Listed, Classe 1/2/3, Rating):
                - CARICO (Peso):
                - SEQUENZA STORICA:
                - NOTE (FE, CD, Distacchi):
                [FINE SOGGETTO]
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text

                # FASE 2: ANALISI (PERPLEXITY GHOST) - FIX DELLE GRAFFE
                prompt_pplx = f"""
                SIMULAZIONE PRESTAZIONALE 7.6.1.
                DATI DI INPUT: 
                {dati_estratti}

                PARAMETRI DI LABORATORIO:
                1. MUD HUNTER: Se terreno è PESANTE, la Classe vale doppio.
                2. ECCEZIONE FE: Se Classe >= 2, un solo FE è incidente statistico.
                3. FORMULA HIGHLANDER: Efficienza = Rating diviso Peso.
                4. OBIETTIVO: Trova il soggetto con massima stabilità e polmoni d'acciaio.

                REFERTO FINALE:
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE: [Analisi tecnica strutturale].'
                USA: MARMO, CEMENTO, ABISSO, CAZZIMMA. SINTASSI MAIUSCOLA.
                """
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=[{"role": "user", "content": prompt_pplx}]
                )
                
                sentenza = response_pplx.choices[0].message.content
                st.info(sentenza)
                if "DIAMANTE" in sentenza.upper():
                    play_beep()
                    st.balloons()

            except Exception as e:
                st.error(f"URTO TECNICO: {e}")
