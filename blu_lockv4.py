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

st.set_page_config(page_title="SNIPER 7.7 SUPREME", page_icon="🎯", layout="centered")

st.title("🎯 SNIPER 7.7 'ARCHITECT SUPREME' 🚀")
st.markdown("## **MODELLAZIONE ANALITICA: QUALITÀ > OGNI OSTACOLO** 💙 ☕")

# 3. CARICAMENTO DATI (VERSIONE BLINDATA)
uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT (CLASSE E TERRENO):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 INNESCA ARCHITECT SUPREME 7.7"):
    if not uploaded_files:
        st.warning("SOCIO, IL REATTORE È VUOTO!")
    else:
        with st.spinner("ANALISI CINETICA DI ALTA QUALITÀ IN CORSO... 👁️"):
            try:
                # FASE 1: VISIONE "PURE QUALITY" (ESTRAZIONE DINAMICA)
                prompt_vision = """
                Converti questi dati in un report tecnico di 'Soggetti Atletici'.
                ESTRAI CON RIGORE ASSOLUTO:
                1. AMBIENTE: Località e Condizioni Terreno (Pesante, Morbido, PSF, Polytrack).
                2. CATEGORIA SESSIONE: Identifica se Listed, Group 1/2/3, Classe 1/2 o Handicap.
                3. ELENCO SOGGETTI:
                [INIZIO SOGGETTO]
                - NOME:
                - INDICE RILEVANZA (Rating):
                - CARICO (Peso):
                - CLASSE INDIVIDUALE (Listed, G1, Classe 2, ecc.):
                - SEQUENZA STORICA:
                - ANOMALIE (FE, CD, Squ, distacchi in lunghezze):
                [FINE SOGGETTO]
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success("DATI ESTRATTI: MURI DI CEMENTO E CLASSE IDENTIFICATA! ☕")

                # FASE 2: SONAR IBRIDO (LOGICA DI QUALITÀ SUPERIORE)
                prompt_pplx = f"""
                SIMULAZIONE PRESTAZIONALE 7.7 - ARCHITECT SUPREME.
                DATI DI INPUT: 
                {dati_estratti}

                PARAMETRI DI LABORATORIO DEFINITIVI:
                1. REGOLA D'ORO (CLASSE > FORMA): Se il soggetto è CLASSE LISTED o superiore (G1-2-3), un singolo FE (Caduta) o CD (Distanziato) NON è ABISSO. È un incidente di percorso.
                2. BIAS TERRENO PESANTE: Se l'Ambiente è 'PESANTE' o 'MORBIDO', ignora la regolarità (2-2-2) e cerca la Forza Bruta ($Rating / Peso$) dei soggetti di Classe Superiore.
                3. BIAS SUPERFICIE VELOCE (POLYTRACK/DIRT): Qui il CARICO è vitale. Se Peso < 55kg e Sequenza è pulita, assegna bonus 'CAZZIMMA CINETICA'.
                4. FILTRO RUGGINE: Risultati recenti 9, 0 o 10 restano ABISSO a meno che non siano in G1. 
                5. HIGHLANDER DENSITY: Calcola Efficienza = Rating / Peso. 

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE: [Perché la sua Classe o Densità schiaccerà il fango e il peso oggi].'
                USA: MARMO, CEMENTO, ABISSO, CAZZIMMA.
                """
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=[{"role": "user", "content": prompt_pplx}]
                )
                
                sentenza = response_pplx.choices[0].message.content
                st.markdown("### 🎯 SENTENZA DELL'ARCHITETTO SUPREMO")
                st.info(sentenza)
                
                if "DIAMANTE" in sentenza.upper():
                    play_beep()
                    st.balloons()

            except Exception as e:
                st.error(f"URTO TECNICO: {e}")

st.write("---")
st.caption("SNIPER 7.7 'ARCHITECT SUPREME' - CERTEZZA 10000% 💙 ☕")
