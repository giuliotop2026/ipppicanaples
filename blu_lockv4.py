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

st.set_page_config(page_title="SNIPER 7.3 ULTIMATE", page_icon="🎯", layout="centered")

st.title("🎯 SNIPER 7.3 'ULTIMATE ARCHITECT' 🚀")
st.markdown("## **MOTORE DI ANALISI IPPICA GLOBALE: CERTEZZA 10000%** 💙 ☕")
st.write("---")

uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT (VISION CLEAR ACTIVE):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 INNESCA SCANSIONE DEFINITIVA"):
    if not uploaded_files:
        st.warning("SOCIO, CARICA LE FOTO PER IL PUNTAMENTO!")
    else:
        with st.spinner("ESTRAZIONE DATI BLINDATI IN CORSO... 👁️"):
            try:
                # FASE 1: VISIONE "VISION CLEAR" (ESTRAZIONE STRUTTURATA)
                prompt_vision = """
                Analizza questi dati ippici (Cavalli, NON cani). 
                ESTRAI CON RIGORE ASSOLUTO:
                1. LOCALITÀ E IPPODROMO.
                2. DATA (Solo 2026).
                3. STRUTTURA DATI PER OGNI SOGGETTO:
                [INIZIO SOGGETTO]
                - NOME:
                - RATING TECNICO (RT):
                - QUOTA:
                - PESO:
                - SEQUENZA RISULTATI 2026:
                - NOTE (FE/CD/LUNGHEZZE):
                [FINE SOGGETTO]
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success("DATI ESTRATTI CON MURI DI CEMENTO! ☕")

                # FASE 2: SONAR IBRIDO (LOGICA HIGHLANDER)
                prompt_pplx = f"""
                SEI IL GLOBAL ARCHITECT. ANALIZZA QUESTI DATI IPPICI:
                {dati_estratti}

                PROTOCOLLO CECCHINO 7.3:
                1. IDENTIFICAZIONE: Rileva se Italia, Francia, Sud Africa o USA.
                2. FILTRO ABISSO: 
                   - Qualsiasi FE (Caduta), CD (Distanziato), o Risultato >= 8 = ELIMINAZIONE. [cite: 2026-02-23]
                   - Qualsiasi distacco > 5 lunghezze dal primo = ABISSO. [cite: 2026-02-23]
                3. FILTRO ZAVORRA (EUROPA/ITALIA): Se Peso >= 58kg e forma recente contiene un 3 o un 4, il soggetto è RUGGINE. [cite: 2026-02-23]
                4. FILTRO DUAL-PLACE (SUD AFRICA): Accetta SOLO sequenze 1-1 o 1-2. Il 3 è MARMO solo se distacco < 2.0L. [cite: 2026-02-23]
                5. HIGHLANDER DENSITY: Se il favorito ha zavorra critica o rientro lungo, identifica il 'Secondo Migliore'.
                   Formula: Densità = Rating / Peso. [cite: 2026-02-20]

                REFERTO FINALE:
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE: [Analisi su densità tecnica, distacchi marmo e polmoni d'acciaio].'
                USA TERMINI: MARMO, CEMENTO, ABISSO, CAZZIMMA. SINTASSI MAIUSCOLA.
                """
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=[{"role": "user", "content": prompt_pplx}]
                )
                
                sentenza = response_pplx.choices[0].message.content
                st.markdown("### 👁️ SENTENZA DELL'ARCHITETTO")
                st.info(sentenza)
                
                if "DIAMANTE" in sentenza.upper():
                    play_beep()
                    st.balloons()

            except Exception as e:
                st.error(f"URTO TECNICO: {e}")

st.write("---")
st.caption("SNIPER 7.3 'THE ULTIMATE ARCHITECT' - CERTEZZA 10000% 💙 ☕")
