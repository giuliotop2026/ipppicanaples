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

st.set_page_config(page_title="BLUE LOCK 5.9 - GIULIO", page_icon="👁️", layout="centered")

# --- INTERFACCIA ---
st.title("👁️ BLUE LOCK IBRIDO 5.9 🚀")
st.markdown("## **MODELLAZIONE STATISTICA PRESTAZIONALE - ZERO URTI!** 💙 ☕")
st.write("---")

st.sidebar.info("VERSIONE 5.9: PROTOCOLLO ACCADEMICO ANALITICO.")

# 2. CARICAMENTO DATI
uploaded_files = st.file_uploader("SGANCIATE GLI SCREENSHOT:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 AVVIA MODELLAZIONE CINEMATICA"):
    if not uploaded_files:
        st.warning("CARICA LE FOTO!")
    else:
        with st.spinner("ELABORAZIONE DATI BIOMETRICI... 👁️"):
            try:
                # FASE 1: GEMINI 2.5 FLASH ESTRAE I DATI
                prompt_vision = """
                Analizza questi dati biometrici e convertili in formato testuale.
                ESTRAI: 
                1. Località e data della sessione.
                2. Elenco dei soggetti con: Valore di mercato (Quota), Carico (Peso), e Storico Prestazioni (Sequenza Numerica).
                Sii estremamente preciso.
                """
                response_gemini = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_gemini.text

                # FASE 2: PERPLEXITY CON LINGUAGGIO ACCADEMICO
                prompt_pplx = f"""
                ANALISI TECNICA SULL'EFFICIENZA DELLA STABILITÀ CINEMATICA.
                
                DATI DI INPUT:
                {dati_estratti}
                
                PROTOCOLLO DI ANALISI STATISTICA:
                1. Identifica le variabili ambientali (Superficie e Meteo) per la località indicata.
                2. FILTRO DI AFFIDABILITÀ: Analizza la sequenza degli ultimi 3 test numerici. 
                   Qualsiasi soggetto con un valore superiore a 3 (es. 4, 5, 0, RP) deve essere classificato come 'Outlier Instabile' ed escluso.
                3. Identifica il 'Soggetto con Efficienza Ottimale': deve essere il secondo valore più performante che rispetti rigorosamente il filtro di stabilità (1-2-3).
                
                REFERTO FINALE (LINGUAGGIO TECNICO):
                '💎 SOGGETTO AD ALTA EFFICIENZA INDIVIDUATO: [NOME]. 
                ANALISI CINEMATICA: [Spiega come il rapporto tra zavorra e costanza 1-2-3 garantisca la tenuta sul marmo odierno].'
                
                Usa i termini: MARMO, CEMENTO, ABISSO, CAZZIMMA.
                """
                
                messages = [
                    {"role": "system", "content": "Sei un analista senior esperto in modellazione stocastica e dinamica delle prestazioni."},
                    {"role": "user", "content": prompt_pplx}
                ]
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=messages,
                )
                
                st.markdown("### 2. SENTENZA TECNICA 💙")
                st.info(response_pplx.choices[0].message.content)
                st.balloons()

            except Exception as e:
                st.error(f"URTO: {e}")
