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
    st.error("❌ BENZINA MANCANTE NEI SECRETS!")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 10.0 SUPREME", page_icon="🎯", layout="wide")

st.title("🎯 SNIPER 10.0 'ARCHITECT SUPREME' 🚀")
st.markdown("## **MODELLAZIONE OMNIVERSE: PERFEZIONE GLOBALE** 💙 ☕")

# 3. SELETTORE DI CAMPO (PARAMETRI SPECIFICI)
nazione = st.selectbox("IDENTIFICA IL CAMPO DI BATTAGLIA:", [
    "ITALIA & SVEZIA (TROTTO - RAGGUAGLIO KM)", 
    "FRANCIA & GERMANIA (OSTACOLI - MUD HUNTER)", 
    "USA, MESSICO, BRASILE, CILE (DIRT - SPEED BIAS)", 
    "UK, AUSTRALIA, ARABIA SAUDITA (CLASS & POWER)"
])

uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT (ESTRAZIONE BLINDATA):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 INNESCA ARCHITECT SUPREME 10.0"):
    if not uploaded_files:
        st.warning("CARICA I DATI, ARCHITETTO!")
    else:
        with st.spinner(f"CALIBRAZIONE PROTOCOLLO {nazione}... 👁️"):
            try:
                # FASE 1: VISIONE "PURE QUALITY" (ESTRAZIONE NEUTRALE)
                prompt_vision = """
                Converti questi dati in un report tecnico di 'Soggetti Atletici' 2026.
                ESTRAI CON RIGORE ASSOLUTO:
                [INIZIO SOGGETTO]
                - NOME:
                - RATING (RT):
                - CARICO (Peso/Distanza):
                - QUALITÀ (Listed, G1/2/3, Classe):
                - SEQUENZA STORICA:
                - NOTE (FE, CD, RP, Distacchi):
                [FINE SOGGETTO]
                IDENTIFICA: Superficie e Condizione Terreno.
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success("TARGET AGGANCIATO! ☕")

                # FASE 2: ANALISI PERFEZIONATA PER NAZIONE
                regole = {
                    "ITALIA & SVEZIA (TROTTO - RAGGUAGLIO KM)": "FOCUS TROTTO: Cerca il ragguaglio al KM (es. 1:13.2). <1:14 = MARMO. Ignora il favorito se ha RP o 0 recenti. La cazzimma è del driver.",
                    "FRANCIA & GERMANIA (OSTACOLI - MUD HUNTER)": "PURE QUALITY: Se Listed/G1/G2, ignora un FE. Su pesante, la Classe > Forma. Highlander: Rating diviso Peso.",
                    "USA, MESSICO, BRASILE, CILE (DIRT - SPEED BIAS)": "SPEED FIGURES: Cerca Beyer crescenti. Sequenza 1-2 obbligatoria. Posizione interna è cemento.",
                    "UK, AUSTRALIA, ARABIA SAUDITA (CLASS & POWER)": "WFA & POWER: Cerca miglior Rating/Peso. Se Arabia (Sabbia), forza bruta > forma."
                }

                prompt_pplx = f"""
                SIMULAZIONE OMNIVERSE 10.0. NAZIONE: {nazione}.
                PARAMETRI: {regole[nazione]}
                DATI DI INPUT: {dati_estratti}

                PROTOCOLLO 'PERFEZIONE BLUE LOCK':
                1. IGNORA LE QUOTE: Il favorito di carta è instabile. [cite: 2026-02-20]
                2. FILTRO ABISSO: Sequenza con 8, 9, 0 o RP = ELIMINAZIONE ISTANTANEA. [cite: 2026-02-23]
                3. HIGHLANDER DENSITY: Cerca il secondo migliore per Rating / Carico se il favorito ha crepe. [cite: 2026-02-20]
                4. OBIETTIVO: Trova il Diamante con polmoni d'acciaio che schiaccia il cantiere. [cite: 2026-02-20]

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE: [Perché la sua Classe o Densità schiaccerà il cantiere oggi].'
                USA: MARMO, CEMENTO, ABISSO, CAZZIMMA.
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

st.write("---")
st.caption("SNIPER 10.0 'ARCHITECT SUPREME' - CERTEZZA 10000% 💙 ☕")
