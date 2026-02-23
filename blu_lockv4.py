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
    st.error("❌ CHIAVI API MANCANTI! IL CANTIERE È BLOCCATO.")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 7.6 MUD HUNTER", page_icon="🎯", layout="centered")

st.title("🎯 SNIPER 7.6 'MUD HUNTER' 🚀")
st.markdown("## **ARCHITETTURA DINAMICA: CLASSE > FANGO** 💙 ☕")

# 3. CARICAMENTO DATI
uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT (OSTACOLI/TURF):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 INNESCA MUD HUNTER 7.6"):
    if not uploaded_files:
        st.warning("CARICA I DATI PER IL LABORATORIO!")
    else:
        with st.spinner("PUNTAMENTO LASER NEL FANGO... 👁️"):
            try:
                # FASE 1: VISIONE "MUD HUNTER" (ESTRAZIONE DI QUALITÀ)
                prompt_vision = """
                Report tecnico per simulazione di resistenza idraulica 2026.
                ESTRAI CON RIGORE PER OGNI SOGGETTO:
                [INIZIO SOGGETTO]
                - NOME:
                - QUALITÀ SESSIONE (Cerca: Listed, G1/2/3, Classe 1/2, Condizionata).
                - CARICO (Peso):
                - INDICE RILEVANZA (Rating):
                - SEQUENZA STORICA:
                - NOTE (FE, CD, distacchi):
                [FINE SOGGETTO]
                IDENTIFICA: Località e Condizioni Terreno (es. Pesante, Morbido, PSF).
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success("DATI ESTRATTI: OCCHIO ALLA CLASSE! ☕")

                # FASE 2: ANALISI TECNICA (PATCH 7.6 MUD HUNTER)
                prompt_pplx = f"""
                SIMULAZIONE PRESTAZIONALE 7.6 - MUD HUNTER.
                DATI DI INPUT: {dati_estratti}

                PARAMETRI DI LABORATORIO SNIPER 7.6:
                1. BIAS TERRENO: Se terreno è 'PESANTE' o 'MORBIDO', la Classe e il Rating valgono il doppio della forma recente.
                2. ECCEZIONE FE (CADUTA): Se un soggetto ha 'Qualità Listed/G1-2-3/Classe 1' e Terreno Pesante, un solo 'FE' (Caduta) NON è eliminatorio. È un incidente cinetico.
                3. FILTRO 'CREPA': Se Carico ≥ 58 e Sequenza ha risultati > 3 (senza alibi di Classe), è 'ABISSO'. 
                4. FORMULA DENSITÀ: $Efficienza = \\frac{Rating}{Peso}$.
                5. OBIETTIVO: Trova il 'Diamante di Fango' (Alta Qualità + Carico sostenibile) che gli altri scartano per un FE.

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE: [Perché la sua Classe schiaccerà il fango e il peso oggi].'
                USA TERMINI: MARMO, CEMENTO, ABISSO, CAZZIMMA.
                """
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=[{"role": "user", "content": prompt_pplx}]
                )
                
                sentenza = response_pplx.choices[0].message.content
                st.markdown("### 🎯 SENTENZA DEL MUD HUNTER")
                st.info(sentenza)
                
                if "DIAMANTE" in sentenza.upper():
                    play_beep()
                    st.balloons()

            except Exception as e:
                st.error(f"URTO TECNICO: {e}")
