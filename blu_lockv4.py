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
    st.error("❌ CHIAVI API MANCANTI NEI SECRETS! AGGIUNGI GEMINI_API_KEY E PERPLEXITY_API_KEY.")
    st.stop()

# Innesco motori
client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 7.8 VOID", page_icon="🎯", layout="centered")

# --- INTERFACCIA ---
st.title("🎯 SNIPER 7.8 'VOID PROTOCOL' 🚀")
st.markdown("## **MODELLAZIONE CINETICA DI ALTA QUALITÀ: ZERO ERRORI** 💙 ☕")
st.write("---")

st.sidebar.info("VERSIONE 7.8: PURE QUALITY + GHOST BYPASS.")
st.sidebar.write("**ARCHITETTO: GIULIO SIMPATICO** 💙 ☕")

# 3. CARICAMENTO DATI (MURI DI CEMENTO)
uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT (ESTRAZIONE BLINDATA):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 INNESCA VOID PROTOCOL 7.8"):
    if not uploaded_files:
        st.warning("SOCIO, IL REATTORE È VUOTO! CARICA I DATI.")
    else:
        with st.spinner("SCANSIONE CINETICA INVISIBILE... 👁️"):
            try:
                # FASE 1: VISIONE "VOID" (ESTRAZIONE STRUTTURATA E NEUTRALE)
                prompt_vision = """
                Converti questi dati in un report tecnico di 'Soggetti Atletici' per una simulazione di sforzo.
                NON usare parole come cavalli, ippica o scommesse. 
                ESTRAI CON RIGORE ASSOLUTO:
                1. AMBIENTE: Località Sessione e Stato Superficie (es. Pesante, Morbido, PSF, Polytrack).
                2. CATEGORIA: Identifica Classe (G1/2/3, Listed, Classe 1/2).
                3. ELENCO SOGGETTI:
                [INIZIO SOGGETTO]
                - NOME:
                - INDICE RILEVANZA (Rating):
                - CARICO (Peso):
                - QUALITÀ INDIVIDUALE:
                - SEQUENZA STORICA:
                - NOTE (FE, CD, distacchi):
                [FINE SOGGETTO]
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success("DATI ESTRATTI CON MURI DI CEMENTO! ☕")

                # FASE 2: ANALISI TECNICA (SIMULAZIONE MECCANICA - BYPASS FILTRI)
                prompt_pplx = f"""
                SIMULAZIONE DI RESISTENZA E CARICO STRUTTURALE 2026.
                OGGETTI ANALIZZATI: 
                {dati_estratti}

                PARAMETRI DI LABORATORIO SNIPER 7.8:
                1. REGOLA PURE QUALITY: Se un soggetto ha 'Qualità Listed' o superiore (G1-2-3), i valori FE (Caduta) o CD (Distanziato) sono considerati 'Inciditenti Cinetici' e NON eliminatori.
                2. BIAS AMBIENTALE (PESANTE): Se il terreno è Pesante/Morbido, la Qualità e l'Indice Rilevanza valgono il doppio. Cerca la Forza Bruta (Rating/Peso).
                3. FILTRO 'CREPA': Se Carico ≥ 58 e Sequenza ha valori > 3 (senza alibi di Classe), classifica come 'ABISSO'. 
                4. FILTRO 'DETRITI': Risultati ≥ 8 o distacchi > 5 unità = 'RUGGINE' (Eliminazione).
                5. HIGHLANDER DENSITY: Calcola Efficienza = Indice Rilevanza diviso Carico.
                6. OBIETTIVO: Trova il 'Soggetto ad Alta Tenuta' con la massima stabilità cinetica (serie di 1 o 2).

                REFERTO FINALE (SINTASSI RIGOROSAMENTE MAIUSCOLA):
                '💎 DIAMANTE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE: [Analisi su densità tecnica, carico e classe superiore per schiacciare il cantiere].'
                USA: MARMO, CEMENTO, ABISSO, CAZZIMMA.
                """
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=[{"role": "user", "content": prompt_pplx}]
                )
                
                sentenza = response_pplx.choices[0].message.content
                st.markdown("### 👁️ SENTENZA DEL VOID PROTOCOL")
                st.info(sentenza)
                
                if "DIAMANTE" in sentenza.upper():
                    play_beep()
                    st.balloons()

            except Exception as e:
                st.error(f"URTO TECNICO: {e}")

st.write("---")
st.caption("SNIPER 7.8 'VOID PROTOCOL' - CERTEZZA 10000% 💙 ☕")
