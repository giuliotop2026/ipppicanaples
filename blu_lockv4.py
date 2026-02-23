import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# 1. NOTIFICA SONORA - PROTOCOLLO SONIC
def play_beep():
    beep_html = """
    <audio autoplay>
      <source src="https://www.soundjay.com/buttons/beep-01a.mp3" type="audio/mpeg">
    </audio>
    """
    components.html(beep_html, height=0, width=0)

# 2. CASSAFORTE - DOPPIA BENZINA
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("❌ CHIAVI MANCANTI NEI SECRETS! AGGIUNGI GEMINI_API_KEY E PERPLEXITY_API_KEY.")
    st.stop()

# Innesco motori
client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="PERFORMANCE ANALYTICS 6.7", page_icon="📈", layout="centered")

# --- INTERFACCIA ---
st.title("📈 PERFORMANCE ANALYTICS 6.7 🚀")
st.markdown("## **MODELLAZIONE ANALITICA: PROTOCOLLO LUNGHEZZE** 💙 ☕")
st.write("---")

st.sidebar.info("VERSIONE 6.7: PATCH LUNGHEZZE SUD AFRICA + USA BEYER.")

# 3. CARICAMENTO DATI
uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 AVVIA MODELLAZIONE ANALITICA"):
    if not uploaded_files:
        st.warning("CARICA LE FOTO PER INIZIARE!")
    else:
        with st.spinner("SCANSIONE ABISSO IN CORSO... 👁️"):
            try:
                # FASE 1: VISIONE
                prompt_vision = """
                Analizza questi dati e convertili in formato testuale professionale.
                ESTRAI CON RIGORE: 
                1. Località e data (Cerca riferimenti 2026).
                2. Numero di partenti e piazzati totali (es. 1-2 o 1-3).
                3. Elenco partecipanti con: Quota, Peso/Zavorra, e Sequenza Risultati Recenti (numeri E distacchi in lunghezze se presenti).
                """
                response_gemini = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_gemini.text
                st.success("DATI ACQUISITI! INNESCAMENTO SONAR 6.7... ☕")

                # FASE 2: ANALISI PERPLEXITY 6.7
                prompt_pplx = f"""
VALUTAZIONE TECNICA SULLA STABILITÀ DELLE PERFORMANCE 2026.
DATI DI INPUT: {dati_estratti}

REQUISITO TEMPORALE: Usa esclusivamente dati del 2026.

PROTOCOLLO FRANCIA (PSF/TURF - PATCH 6.9):
1. FILTRO ZAVORRA CRITICA: Se il peso è ≥ 58kg, la forma recente deve essere 1-1 o 1-2. Se compare un 3 o un 4, è ABISSO (il peso schiaccia il motore).
2. REGOLA LUNGHEZZE FRANCIA: Un 4° posto è MARMO solo se il distacco è < 2.5 lunghezze. Se distacco > 5 lunghezze, è RUGGINE totale, a prescindere dal nome.
3. PREFERENZA LEGGEREZZA: Identifica soggetti con peso < 56kg e almeno un piazzamento 1-2-3 recente (Alta densità tecnica).

PROTOCOLLO SUD AFRICA (LUNGHEZZE & DUAL-PLACE):
1. ANALISI DISTANZA REALE: 
   - 4° o 5° con distacco < 2.0 lunghezze: CLASSIFICAZIONE 'MARMO'.
   - 2° o 3° con distacco > 5.0 lunghezze: CLASSIFICAZIONE 'BULLONE ARRUGINITO' (Abisso).
2. FILTRO DUAL-PLACE (2 PIAZZATI): 
   - Accetta solo 1-1, 1-2 o 'MARMO 4/5'. Ogni 8°, 9° o 0 recente è ABISSO ISTANTANEO.

PROTOCOLLO USA (DIRT/BEYER):
- Se USA DIRT: Ignora peso. Cerca Beyer Speed Figures crescenti nel 2026. 
- Requisito: Sequenza 1-2 nelle ultime due gare. Il 3° è ABISSO.

PROTOCOLLO EUROPA GENERALE (TURF):
- FILTRO FORMA: Qualsiasi valore > 3 è ABISSO.
- REGOLA HIGHLANDER: Identifica il 'Secondo Migliore' per densità tecnica (Rating/Peso).

REFERTO FINALE:
'💎 SOGGETTO AD ALTA EFFICIENZA: [NOME]. 
MOTIVAZIONE: [Analisi distacchi, zavorra e densità per garantire il MARMO oggi].'

TERMINI OBBLIGATORI: MARMO, CEMENTO, ABISSO, CAZZIMMA. SINTASSI MAIUSCOLA.
"""
                
                messages = [
                    {"role": "system", "content": "Sei un analista senior esperto in modellazione statistica sportiva."},
                    {"role": "user", "content": prompt_pplx}
                ]
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=messages,
                )
                
                sentenza = response_pplx.choices[0].message.content
                st.markdown("### 2. SENTENZA TECNICA 💙")
                st.info(sentenza)
                
                if "DIAMANTE" in sentenza.upper() or "SOGGETTO" in sentenza.upper():
                    play_beep()
                    st.balloons()

            except Exception as e:
                st.error(f"URTO TECNICO: {e}")
