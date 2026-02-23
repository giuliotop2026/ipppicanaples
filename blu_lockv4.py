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
    st.error("❌ MANCA BENZINA NEI SECRETS! IL CANTIERE È BLOCCATO.")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 8.0 OMNIVERSE", page_icon="🎯", layout="wide")

st.title("🎯 SNIPER 8.0 'OMNIVERSE ARCHITECT' 🚀")
st.markdown("## **MOTORE ANALITICO GLOBALE: ZERO ERRORI, SOLO GLORIA** 💙 ☕")

# 3. SELETTORE DI PROTOCOLLO NAZIONALE
nazione = st.selectbox("IDENTIFICA IL CAMPO DI BATTAGLIA:", [
    "ITALIA & SVEZIA (TROTTO/ARCOVEGGIO/NAPOLI)", 
    "FRANCIA & GERMANIA (OSTACOLI/MUD HUNTER)", 
    "USA, MESSICO, BRASILE, CILE (DIRT SPEED)", 
    "UK & AUSTRALIA (PURE CLASS/SECTIONALS)", 
    "SUD AFRICA (POLYTRACK/DUAL-PLACE)",
    "ARABIA SAUDITA (SAND FORCE)"
])

uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT (ESTRAZIONE BLINDATA):", type=["jpg", "png", "jpeg"], accept_multiple_files=Accept_True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 INNESCA OMNIVERSE 8.0"):
    if not uploaded_files:
        st.warning("CARICA I DATI, ARCHITETTO!")
    else:
        with st.spinner(f"CALIBRAZIONE PROTOCOLLO {nazione}... 👁️"):
            try:
                # FASE 1: VISIONE "PURE QUALITY" (ESTRAZIONE)
                prompt_vision = """
                Converti questi dati in un report tecnico di 'Soggetti Atletici' 2026. 
                ESTRAI CON RIGORE ASSOLUTO:
                1. LOCALITÀ E SUPERFICIE.
                2. CATEGORIA (Listed, G1/2/3, Classe 1/2, Handicap, Condizionata).
                [INIZIO SOGGETTO]
                - NOME:
                - RATING (RT):
                - CARICO (Peso/Distanza):
                - SEQUENZA STORICA:
                - NOTE CINETICHE (FE, CD, Squ, Distacchi in lunghezze o tempo):
                [FINE SOGGETTO]
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success("DATI ESTRATTI: MURI DI CEMENTO ATTIVI! ☕")

                # FASE 2: ANALISI TECNICA PER NAZIONE (PROTOCOLLI SPECIFICI)
                prompt_pplx = f"""
                SIMULAZIONE PRESTAZIONALE 8.0 - OMNIVERSE. 
                NAZIONE RILEVATA: {nazione}
                DATI DI INPUT: {dati_estratti}

                PARAMETRI DI PERFEZIONE PER {nazione}:
                - ITALIA/SVEZIA (TROTTO): Cerca 'Tempo al KM' (1:14 o migliore è MARMO). Ignora il favorito se ha RP o 0 recenti. La 'Cazzimma' è del guidatore e della regolarità.
                - FRANCIA/GERMANIA: 'PURE QUALITY'. Se G1/Listed, ignora un FE. Su fango, la densità tecnico-polmonare schiaccia la forma.
                - USA/AMERICHE: 'SPEED FIGURES'. Cerca incrementi di velocità (Beyer). Sequenza 1-2 obbligatoria per il marmo.
                - UK/AUSTRALIA: 'SECTIONALS'. Cerca chi ha spinto negli ultimi 400m. WFA (Weight-for-age) è la chiave.
                - ARABIA: 'SAND FORCE'. Forza bruta su sabbia. Peso secondario rispetto al Rating.

                PROTOCOLLO GENERALE:
                1. IGNORA LE QUOTE. [cite: 2026-02-20]
                2. TROVA IL SECONDO MIGLIORE per densità tecnica se il favorito è instabile. [cite: 2026-02-20]
                3. FILTRO ABISSO: Sequenza 8/9/0 = ELIMINAZIONE. [cite: 2026-02-23]
                4. HIGHLANDER: $Efficienza = \\frac{Rating}{Carico}$. [cite: 2026-02-20]

                REFERTO FINALE:
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE: [Perché la sua Cazzimma o Densità schiaccerà il cantiere oggi].'
                USA: MARMO, CEMENTO, ABISSO, CAZZIMMA.
                """
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=[{"role": "user", "content": prompt_pplx}]
                )
                
                sentenza = response_pplx.choices[0].message.content
                st.markdown("### 👁️ SENTENZA DELL'ARCHITETTO SUPREMO")
                st.info(sentenza)
                
                if "DIAMANTE" in sentenza.upper():
                    play_beep()
                    st.balloons()

            except Exception as e:
                st.error(f"URTO TECNICO: {e}")
