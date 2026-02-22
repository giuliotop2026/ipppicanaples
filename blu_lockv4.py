import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image

# 1. CASSAFORTE IBRIDA - DOPPIA BENZINA
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("❌ BENZINA MANCANTE! ASSICURATI DI AVERE ENTRAMBE LE CHIAVI NEI SECRETS.")
    st.stop()

# Innesco dei due Motori
client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="BLUE LOCK HYBRID - GIULIO", page_icon="👁️", layout="centered")

# --- INTERFACCIA NAPOLI POWER ---
st.title("👁️ BLUE LOCK IBRIDO 5.5 🛰️")
st.markdown("## **GLI OCCHI DI GEMINI, IL SONAR DI PERPLEXITY!** 💙 ☕")
st.write("---")

st.sidebar.markdown("### 🛠️ CANTIERE")
st.sidebar.write("**CREATA DA GIULIO SIMPATICO** 💙 ☕")
st.sidebar.write("---")
st.sidebar.info("MOTORE: HYBRID (Visione OCR + Live News Search).")

# 2. INSERIMENTO DATI (FOTO + TESTO)
st.header("1. CARICA IL MARMO 🐎")
event_info = st.text_input("NOME GARA O CAVALLO (Serve al Sonar per cercare online):", "")
uploaded_files = st.file_uploader("CARICA LE FOTO DELLE QUOTE E DEI PESI:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 ATTIVA REATTORE IBRIDO"):
    if not uploaded_files or not event_info:
        st.warning("SOCIO, MI SERVONO SIA LE FOTO CHE IL NOME DELLA GARA!")
    else:
        with st.spinner("FASE 1: GEMINI STA LEGGENDO LE FOTO... 👁️"):
            try:
                # FASE 1: GEMINI ESTRAE I DATI DALLE IMMAGINI
                prompt_vision = "Leggi attentamente tutti i cavalli, i pesi, le quote e la forma recente presenti in queste foto e crea un riassunto testuale dettagliato. IGNORA GLI ELEMENTI GRAFICI, VOGLIO SOLO I DATI PURI."
                
                # Usiamo 1.5 Flash che è stabile e non va in 429
                response_gemini = client_gemini.models.generate_content(
                    model='gemini-1.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_gemini.text
                st.success("DATI ACQUISITI DALLE FOTO! Passo il marmo al Sonar...")

                with st.spinner("FASE 2: PERPLEXITY CERCA IL FANGO E LE NEWS... 🛰️☕"):
                    # FASE 2: PERPLEXITY ANALIZZA I DATI + CERCA SUL WEB
                    prompt_pplx = f"""
                    SEI 'BLUE LOCK SONAR' DI GIULIO SIMPATICO. 
                    
                    DATI ESTRATTI DALLE FOTO DEL CANTIERE:
                    {dati_estratti}
                    
                    MISSIONE PER L'EVENTO '{event_info}':
                    1. Cerca il meteo attuale e lo stato del terreno (Fango, Erba, Heavy, ecc.).
                    2. Cerca news live (cambi guida, infortuni, dichiarazioni).
                    3. Unisci le tue ricerche online con i dati estratti dalle foto (pesi, forma).
                    
                    PROTOCOLLO RIGIDO (1-5):
                    - STABILITÀ CIRCUITO (Affinità al terreno trovato online).
                    - DENSITÀ TECNICA (Motore).
                    - POLMONI D'ACCIAIO (Resistenza).
                    - ZAVORRA/PESO (Valuta in base ai pesi letti dalle foto).
                    - FORMA RECENTE (Rigore: se non è nei primi 3, penalizza).
                    - CAZZIMMA (News trovate online).

                    SENTENZA FINALE (IN MAIUSCOLO):
                    - SCORE >= 26: '💎 DIAMANTE ASSOLUTO RILEVATO. CERTEZZA 10000% 💙.'
                    - SCORE 23-25: '⚙️ BULLONE SOLIDO. SOLO PIAZZATO. IL CEMENTO REGGE.'
                    - SCORE < 23: '❌ CANTIERE NON CERTIFICATO. RISCHIO IMPUREZZE.'
                    """
                    
                    messages = [
                        {"role": "system", "content": "Sei l'analista spietato del Progetto Blue Lock."},
                        {"role": "user", "content": prompt_pplx}
                    ]
                    
                    response_pplx = client_pplx.chat.completions.create(
                        model="sonar-pro",
                        messages=messages,
                    )
                    
                    st.markdown("### 2. LA SENTENZA DEL REATTORE 💙")
                    st.info(response_pplx.choices[0].message.content)
                    st.balloons()

            except Exception as e:
                st.error(f"URTO NEL SISTEMA IBRIDO: {e}")

# FOOTER
st.write("---")
st.caption("BLUE LOCK HYBRID - GIULIO SIMPATICO 💙 ☕ - GEMINI VISION + PERPLEXITY SONAR")
