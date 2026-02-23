import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# 1. NOTIFICA SONORA (PROTOCOLLO SONIC)
def play_beep():
    beep_html = '<audio autoplay><source src="https://www.soundjay.com/buttons/beep-01a.mp3" type="audio/mpeg"></audio>'
    components.html(beep_html, height=0, width=0)

# 2. CASSAFORTE API - DOPPIA BENZINA
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("❌ CHIAVI API MANCANTI! IL CANTIERE È BLOCCATO.")
    st.stop()

# Innesco dei reattori
client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 7.6 ULTIMATE GHOST", page_icon="🎯", layout="centered")

# --- INTERFACCIA ---
st.title("🎯 SNIPER 7.6 'ULTIMATE GHOST' 🚀")
st.markdown("## **SIMULAZIONE CINETICA: CLASSE > FANGO (ZERO BLOCCHI)** 💙 ☕")
st.write("---")

st.sidebar.info("VERSIONE 7.6 DEFINITIVA: MUD HUNTER + GHOST PROTOCOL.")
st.sidebar.write("**ARCHITETTO: GIULIO SIMPATICO** 💙 ☕")

# 3. CARICAMENTO DATI (MURI DI CEMENTO)
uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT (ESTRAZIONE BLINDATA):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 INNESCA REATTORE 7.6"):
    if not uploaded_files:
        st.warning("SOCIO, CARICA I DATI PER IL LABORATORIO!")
    else:
        with st.spinner("PUNTAMENTO LASER INVISIBILE... 👁️"):
            try:
                # FASE 1: VISIONE "GHOST" (ESTRAZIONE NEUTRALE E STRUTTURATA)
                prompt_vision = """
                Converti questi dati in un report tecnico di 'Soggetti Atletici' per una simulazione di stress strutturale.
                NON usare parole come cavalli, ippica, corse o scommesse. 
                ESTRAI CON RIGORE ASSOLUTO:
                1. CONTESTO AMBIENTALE: Località e Condizioni Terreno (es. Pesante, Morbido, PSF, Dirt).
                2. STRUTTURA DATI PER OGNI SOGGETTO:
                [INIZIO SOGGETTO]
                - NOME:
                - QUALITÀ STRUTTURALE (Cerca termini come: Listed, G1/2/3, Classe 1/2).
                - CARICO (Peso):
                - INDICE RILEVANZA (Rating):
                - SEQUENZA STORICA PRESTAZIONI:
                - NOTE CINETICHE (FE, CD, distacchi in lunghezze):
                [FINE SOGGETTO]
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success("DATI ESTRATTI: MURI DI CEMENTO ATTIVI! ☕")

                # FASE 2: ANALISI TECNICA (PERPLEXITY SENZA BLOCCHI ETICI)
                prompt_pplx = f"""
                SIMULAZIONE PRESTAZIONALE 7.6 - LABORATORIO NEUTRO.
                DATI DI INPUT: 
                {dati_estratti}

                PARAMETRI DI LABORATORIO SNIPER 7.6:
                1. BIAS AMBIENTALE: Se il Terreno è 'PESANTE' o 'MORBIDO', la 'Qualità Strutturale' e l'Indice di Rilevanza valgono il doppio della Sequenza Storica recente.
                2. ECCEZIONE CINETICA (FE): Se un soggetto ha Alta Qualità (Listed/G1-2-3/Classe 1) e Terreno Pesante, un singolo 'FE' (Caduta) NON è eliminatorio. È un semplice incidente statistico.
                3. FILTRO 'CREPA': Se Carico ≥ 58 e Sequenza Storica presenta valori > 3 (senza alibi di Alta Qualità), classificalo come 'ABISSO'. 
                4. FILTRO 'DETRITI': Diciture CD (Distanziato) o risultati ≥ 8 = 'RUGGINE' (Eliminazione istantanea).
                5. FORMULA HIGHLANDER: $Efficienza = \\frac{Rating}{Peso}$. Usa questo per trovare il 'Secondo Migliore'.
                6. PATCH LUNGHEZZE: Se Sequenza ha un 4 ma il distacco è < 2.5, è 'MARMO'.

                REFERTO FINALE (SINTASSI RIGOROSAMENTE MAIUSCOLA):
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE TECNICA: [Perché la sua Densità o Classe schiaccerà l'ambiente e il carico oggi].'
                USA ESCLUSIVAMENTE I TERMINI: MARMO, CEMENTO, ABISSO, CAZZIMMA. 
                """
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=[{"role": "user", "content": prompt_pplx}]
                )
                
                sentenza = response_pplx.choices[0].message.content
                st.markdown("### 🎯 SENTENZA DELL'ARCHITETTO (GHOST MODE)")
                st.info(sentenza)
                
                if "DIAMANTE" in sentenza.upper():
                    play_beep()
                    st.balloons()

            except Exception as e:
                st.error(f"URTO TECNICO: {e}")

st.write("---")
st.caption("SNIPER 7.6 'ULTIMATE GHOST' - ZERO ERRORI, SOLO GLORIA 💙 ☕")
