import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image

# 1. CASSAFORTE IBRIDA
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("❌ BENZINA MANCANTE NEI SECRETS!")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="BLUE LOCK 5.8 - GIULIO", page_icon="👁️", layout="centered")

# --- INTERFACCIA ---
st.title("👁️ BLUE LOCK IBRIDO 5.8 🚀")
st.markdown("## **ANALISI TECNICA PERFORMANCE - ZERO ERRORI!** 💙 ☕")
st.write("---")

st.sidebar.info("VERSIONE 5.8: PROTOCOLLO NEUTRO ANTI-BLOCCO.")

# 2. CARICAMENTO DATI
uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 AVVIA ANALISI PRESTAZIONALE"):
    if not uploaded_files:
        st.warning("CARICA LE FOTO!")
    else:
        with st.spinner("SCANSIONE IN CORSO... 👁️"):
            try:
                # FASE 1: GEMINI 2.5 FLASH ESTRAE I DATI
                prompt_vision = """
                Analizza questi dati sportivi e convertili in formato testuale.
                ESTRAI: 
                1. Località e data dell'evento.
                2. Elenco soggetti con: Quota, Peso/Zavorra, e Sequenza Risultati Recenti.
                Sii estremamente preciso con i numeri.
                """
                response_gemini = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_gemini.text

                # FASE 2: PERPLEXITY CON LINGUAGGIO TECNICO "SAFE"
                prompt_pplx = f"""
                REPORT TECNICO SULLA STABILITÀ DELLE PERFORMANCE ATLETICHE.
                
                DATI DI INPUT:
                {dati_estratti}
                
                PROTOCOLLO DI ANALISI:
                1. Cerca informazioni meteo e condizioni della superficie per la località indicata.
                2. APPLICA IL FILTRO DI COSTANZA: Valuta la sequenza degli ultimi 3 risultati. 
                   Se un soggetto presenta un valore superiore a 3 (es. 4, 5, 6, 0, RP), deve essere classificato come 'Instabile' ed escluso.
                3. Identifica il 'Soggetto Ottimale': deve essere il secondo valore più competitivo (escludendo il leader di mercato/favorito) che rispetti il filtro di costanza.
                
                REFERTO FINALE (FORMATO RIGIDO):
                '💎 SOGGETTO OTTIMALE INDIVIDUATO: [NOME]. 
                MOTIVAZIONE: [Analisi della densità tecnica basata su peso e costanza 1-2-3].'
                
                Usa i termini di settore: MARMO, CEMENTO, ABISSO, CAZZIMMA.
                """
                
                messages = [
                    {"role": "system", "content": "Sei un esperto di analisi statistica e modellazione delle performance atletiche."},
                    {"role": "user", "content": prompt_pplx}
                ]
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=messages,
                )
                
                st.markdown("### 2. LA SENTENZA 💙")
                st.info(response_pplx.choices[0].message.content)
                st.balloons()

            except Exception as e:
                st.error(f"URTO: {e}")
