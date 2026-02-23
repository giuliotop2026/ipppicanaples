import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

def play_beep():
    beep_html = '<audio autoplay><source src="https://www.soundjay.com/buttons/beep-01a.mp3" type="audio/mpeg"></audio>'
    components.html(beep_html, height=0, width=0)

try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("❌ BENZINA MANCANTE!")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 7.4 GHOST", page_icon="🎯", layout="centered")

st.title("🎯 SNIPER 7.4 'GHOST PROTOCOL' 🚀")
st.markdown("## **MODELLAZIONE ANALITICA DI EFFICIENZA CINETICA** 💙 ☕")

uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 INNESCA GHOST PROTOCOL"):
    if not uploaded_files:
        st.warning("SOCIO, CARICA I DATI!")
    else:
        with st.spinner("SCANSIONE INVISIBILE IN CORSO... 👁️"):
            try:
                # FASE 1: ESTRAZIONE NEUTRA (GEMINI)
                prompt_vision = """
                Converti questi dati in un report tecnico di 'Soggetti Atletici'.
                NON usare parole come cavalli o scommesse. 
                ESTRAI: Località Sessione, Carico (Peso), Indice di Rilevanza (Rating), Sequenza Storica Performance. 
                Usa i tag [INIZIO SOGGETTO] e [FINE SOGGETTO] per separare i dati.
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text

                # FASE 2: ANALISI TECNICA (PERPLEXITY GHOST)
                prompt_pplx = f"""
                ANALISI TECNICA DI STABILITÀ E MODELLAZIONE PRESTAZIONALE 2026.
                DATI DI INPUT: {dati_estratti}

                PROTOCOLLO 7.4 (GHOST):
                1. IDENTIFICAZIONE: Rileva il contesto geografico della sessione sportiva.
                2. FILTRO STABILITÀ: Se Carico ≥ 58 e Sequenza contiene valori > 3, CLASSIFICA COME 'ABISSO'. 
                3. FILTRO ANOMALIE: Diciture FE/CD/Squ o risultati ≥ 8 = 'RUGGINE' (Eliminazione istantanea).
                4. FORMULA HIGHLANDER: Densità = Indice Rilevanza / Carico. 
                5. CERCA IL MARMO: Identifica il soggetto con la massima regolarità storica (es. serie di 2) che non presenta 'ABISSO'.

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💎 SOGGETTO AD ALTA EFFICIENZA: [NOME]. 
                MOTIVAZIONE: [Analisi su densità tecnica, carico e costanza cinetica].'
                USA: MARMO, CEMENTO, ABISSO, CAZZIMMA.
                """
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=[{"role": "user", "content": prompt_pplx}]
                )
                
                sentenza = response_pplx.choices[0].message.content
                st.markdown("### 🎯 SENTENZA DEL GHOST PROTOCOL")
                st.info(sentenza)
                
                if "DIAMANTE" in sentenza.upper() or "SOGGETTO" in sentenza.upper():
                    play_beep()
                    st.balloons()

            except Exception as e:
                st.error(f"URTO TECNICO: {e}")
