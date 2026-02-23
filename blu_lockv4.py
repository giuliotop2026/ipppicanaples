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
    PPL_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("❌ BENZINA MANCANTE NEI SECRETS! IL CANTIERE È BLOCCATO.")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPL_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 8.0 OMNIVERSE", page_icon="🎯", layout="wide")

st.title("🎯 SNIPER 8.0 'OMNIVERSE ARCHITECT' 🚀")
st.markdown("## **MOTORE ANALITICO GLOBALE: ZERO ERRORI, SOLO GLORIA** 💙 ☕")

# 3. CARICAMENTO DATI
uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT (ESTRAZIONE BLINDATA):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 INNESCA OMNIVERSE 8.0"):
    if not uploaded_files:
        st.warning("SOCIO, CARICA I DATI PER IL LABORATORIO!")
    else:
        with st.spinner("SCANSIONE GEOPOLITICA E CINETICA IN CORSO... 👁️"):
            try:
                # FASE 1: VISIONE "PURE QUALITY" (ESTRAZIONE STRUTTURATA)
                prompt_vision = """
                Converti questi dati in un report tecnico di 'Soggetti Atletici' 2026. 
                ESTRAI CON RIGORE ASSOLUTO:
                1. LOCALITÀ E SUPERFICIE (Esempio: Australia/Turf, USA/Dirt, Italia/Trotto, Francia/Ostacoli, Arabia/Sand).
                2. CATEGORIA (Listed, G1/2/3, Classe 1/2, Handicap, Condizionata).
                3. STRUTTURA PER SOGGETTO:
                [INIZIO SOGGETTO]
                - NOME:
                - RATING (RT):
                - CARICO (Peso):
                - SEQUENZA STORICA:
                - NOTE CINETICHE (FE, CD, Squ, Distacchi in lunghezze):
                [FINE SOGGETTO]
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success("TARGET AGGANCIATO: MURI DI CEMENTO ATTIVI! ☕")

                # FASE 2: ANALISI TECNICA (PROTOCOLLI MONDIALI)
                prompt_pplx = f"""
                SIMULAZIONE PRESTAZIONALE 8.0 - OMNIVERSE.
                DATI DI INPUT: {dati_estratti}

                PROTOCOLLI DI SETTAGGIO (ATTIVA SOLO QUELLO RILEVATO):

                A) EUROPA (ITALIA, FRANCIA, UK, GERMANIA, SVEZIA):
                - REGOLA 'PURE QUALITY': Se Listed/G1/G2/G3, ignora un singolo FE/CD. La Classe domina il fango. [cite: 2026-02-23]
                - TROTTO (ITALIA/SVEZIA): Focus su tempi al KM e regolarità. Sequenza 8/0/RP = ABISSO. [cite: 2026-02-11]
                - HIGHLANDER: Efficienza = Rating / Peso. [cite: 2026-02-20]

                B) SUD AFRICA (GREYVILLE/KENILWORTH):
                - DUAL-PLACE: Accetta solo 1-1 o 1-2. Il 3 è MARMO solo se distacco < 2.0 unità. [cite: 2026-02-23]
                - POLYTRACK: Peso < 58kg è vitale. Peso > 60kg = RUGGINE. [cite: 2026-02-23]

                C) AMERICHE (USA, BRASILE, CILE, MESSICO):
                - BEYER BIAS: Ignora il peso. Cerca Speed Figures crescenti. Sequenza 1-2 obbligatoria. [cite: 2026-02-23]
                - DIRT/SAND: Forza bruta e posizione interna (Steccato).

                D) AUSTRALIA & ARABIA SAUDITA:
                - WEIGHT-FOR-AGE: Cerca il miglior rapporto Rating/Peso in base alla classe. [cite: 2026-02-20]
                - DISTANZA: Se > 2000m, cerca polmoni d'acciaio con sequenza senza ABISSO (8/9/0). [cite: 2026-02-23]

                REFERTO FINALE:
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE: [Analisi su nazione, classe e densità tecnica].'
                USA TERMINI: MARMO, CEMENTO, ABISSO, CAZZIMMA. SINTASSI MAIUSCOLA.
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
