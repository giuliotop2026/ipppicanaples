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
    st.error("❌ BENZINA MANCANTE NEI SECRETS! AGGIUNGI LE CHIAVI API.")
    st.stop()

# Innesco motori
client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 7.5 NEUTRAL LAB", page_icon="🎯", layout="centered")

# --- INTERFACCIA ---
st.title("🎯 SNIPER 7.5 'NEUTRAL LAB' 🚀")
st.markdown("## **MODELLAZIONE ANALITICA DI EFFICIENZA CINETICA** 💙 ☕")
st.write("---")

st.sidebar.info("VERSIONE 7.5: FILTRO NEUTRALE ANTI-ABISSO.")
st.sidebar.write("**ARCHITETTO: GIULIO SIMPATICO** 💙 ☕")

# 3. CARICAMENTO DATI
uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT (ESTRAZIONE BLINDATA):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 INNESCA NEUTRAL LAB 7.5"):
    if not uploaded_files:
        st.warning("SOCIO, CARICA I DATI PER IL LABORATORIO!")
    else:
        with st.spinner("SCANSIONE STRUTTURALE IN CORSO... 👁️"):
            try:
                # FASE 1: VISIONE "VISION CLEAR" (ESTRAZIONE NEUTRA)
                prompt_vision = """
                Converti questi dati in un report tecnico di 'Soggetti Atletici' per una simulazione di sforzo. 
                NON usare parole come cavalli, ippica o scommesse. 
                ESTRAI CON RIGORE:
                1. Località e Data Sessione (Cerca 2026).
                2. STRUTTURA DATI PER OGNI OGGETTO:
                [INIZIO SOGGETTO]
                - NOME:
                - INDICE RILEVANZA (Rating):
                - CARICO STRUTTURALE (Peso):
                - SEQUENZA STORICA PERFORMANCE:
                - ANOMALIE (FE/CD/Lunghezze distacco):
                [FINE SOGGETTO]
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success("DATI ESTRATTI CON MURI DI CEMENTO! ☕")

                # FASE 2: ANALISI TECNICA (LABORATORIO NEUTRO PERPLEXITY)
                prompt_pplx = f"""
                SIMULAZIONE DI RESISTENZA E CARICO STRUTTURALE 2026.
                DATI DI INPUT: 
                {dati_estratti}

                PARAMETRI DI LABORATORIO SNIPER 7.5:
                1. IDENTIFICAZIONE: Rileva l'ambiente di test (Località).
                2. FILTRO 'CREPA': Se Carico Strutturale (Peso) ≥ 58 e la Sequenza Storica presenta valori > 3, l'oggetto è 'ABISSO'. [cite: 2026-02-23]
                3. FILTRO 'DETRITI': Diciture FE (Caduta), CD (Distanziato), o risultati ≥ 8 = 'RUGGINE' (Eliminazione istantanea per instabilità materiale). [cite: 2026-02-21, 2026-02-23]
                4. FORMULA DENSITÀ HIGHLANDER: Efficienza = Indice Rilevanza (Rating) / Carico Strutturale. [cite: 2026-02-20]
                5. PATCH LUNGHEZZE: Se un soggetto ha valore 4 ma distacco < 2.5 unità, CLASSIFICA COME 'MARMO'. [cite: 2026-02-23]
                6. OBIETTIVO: Trova il 'Soggetto ad Alta Tenuta' con la massima costanza (serie di 1 o 2) che non presenta anomalie. [cite: 2026-02-20]

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💎 SOGGETTO AD ALTA EFFICIENZA: [NOME]. 
                MOTIVAZIONE: [Analisi su densità tecnica, carico e stabilità cinetica].'
                USA TERMINI: MARMO, CEMENTO, ABISSO, CAZZIMMA. 
                """
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=[{"role": "user", "content": prompt_pplx}]
                )
                
                sentenza = response_pplx.choices[0].message.content
                st.markdown("### 👁️ REFERTO DEL LABORATORIO NEUTRO")
                st.info(sentenza)
                
                if "DIAMANTE" in sentenza.upper() or "SOGGETTO" in sentenza.upper():
                    play_beep()
                    st.balloons()

            except Exception as e:
                st.error(f"URTO TECNICO: {e}")

st.write("---")
st.caption("SNIPER 7.5 'NEUTRAL LAB' - GIULIO SIMPATICO 💙 ☕")
