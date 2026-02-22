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

# Innesco dei due Motori (con la nuova architettura)
client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="BLUE LOCK AUTOMATIC 2.5 - GIULIO", page_icon="👁️", layout="centered")

# --- INTERFACCIA NAPOLI POWER ---
st.title("👁️ BLUE LOCK IBRIDO 5.6 🚀")
st.markdown("## **MOTORE 2.5 FLASH INNESCATO: L'OCCHIO SUPREMO E IL SONAR LIVE!** 💙 ☕")
st.write("---")

st.sidebar.markdown("### 🛠️ CANTIERE")
st.sidebar.write("**CREATA DA GIULIO SIMPATICO** 💙 ☕")
st.sidebar.write("---")
st.sidebar.info("MOTORE: GEMINI 2.5 FLASH (Visione) + PERPLEXITY (Live News).")

# 2. INSERIMENTO DATI (SOLO FOTO AUTOMATICO)
st.header("1. SGANCIATE LE FOTO DEL CANTIERE 🐎")
st.info("CARICA LE FOTO. IL MOTORE 2.5 LEGGERÀ IL NOME DELLA GARA E I PESI CON ZERO ERRORI.")
uploaded_files = st.file_uploader("CARICA LE FOTO DELLE QUOTE E DEI PESI:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("🔥 ATTIVA PILOTA AUTOMATICO 2.5"):
    if not uploaded_files:
        st.warning("SOCIO, CARICA ALMENO UNA FOTO PER INIZIARE!")
    else:
        with st.spinner("FASE 1: IL MOTORE 2.5 FLASH STA LEGGENDO IL MARMO... 👁️"):
            try:
                # FASE 1: GEMINI 2.5 FLASH ESTRAE I DATI E IDENTIFICA LA GARA
                prompt_vision = """
                Sei l'occhio assoluto del Blue Lock. Analizza queste immagini e scrivi un report testuale.
                DEVI TROVARE:
                1. NOME DELLA GARA E IPPODROMO: Cerca qualsiasi scritta che indichi dove si corre o il nome dei cavalli.
                2. DATI TECNICI: Tutti i pesi (zavorra), quote, forma recente (ultimi piazzamenti) e commenti visibili.
                Estrai tutto in modo clinico e spietato.
                """
                
                # INNESCO DEL NUOVO MOTORE BLINDATO TROVATO NELLA SCANSIONE
                response_gemini = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_gemini.text
                st.success("DATI ACQUISITI DAL 2.5 FLASH! Passo il pacchetto al Sonar Perplexity... ☕")

                with st.spinner("FASE 2: PERPLEXITY CERCA IL FANGO E LA CAZZIMMA LIVE... 🛰️"):
                    # FASE 2: PERPLEXITY ANALIZZA I DATI + CERCA SUL WEB
                    prompt_pplx = f"""
                    SEI 'BLUE LOCK SONAR' DI GIULIO SIMPATICO. 
                    
                    DATI ESTRATTI DALLE FOTO DEL CANTIERE:
                    {dati_estratti}
                    
                    MISSIONE:
                    1. Usa i dati qui sopra per capire che gara è e cerca sul web il METEO ATTUALE e lo STATO DEL TERRENO.
                    2. Cerca news live sui cavalli estratti (cambi guida, infortuni, dichiarazioni).
                    3. Unisci le tue ricerche online con i dati delle foto (pesi, forma recente).
                    
                    PROTOCOLLO RIGIDO (1-5):
                    - STABILITÀ CIRCUITO (Affinità al terreno trovato online).
                    - DENSITÀ TECNICA (Motore relativo al campo).
                    - POLMONI D'ACCIAIO (Resistenza).
                    - ZAVORRA/PESO (Valuta in base ai pesi letti dalle foto).
                    - FORMA RECENTE (Rigore: se non è nei primi 3 di recente, penalizza forte).
                    - CAZZIMMA (News trovate online).

                    SENTENZA FINALE (IN MAIUSCOLO):
                    - SCORE >= 26: '💎 DIAMANTE ASSOLUTO RILEVATO. CERTEZZA 10000% 💙.'
                    - SCORE 23-25: '⚙️ BULLONE SOLIDO. SOLO PIAZZATO. IL CEMENTO REGGE.'
                    - SCORE < 23: '❌ CANTIERE NON CERTIFICATO. RISCHIO IMPUREZZE.'
                    
                    NOTE DI GIULIO: IL VINCENTE NON È IL PIÙ VELOCE, MA QUELLO CHE TIEN' 'A CAZZIMMA OGGI.
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
st.caption("BLUE LOCK HYBRID FULL AUTOMATIC - GIULIO SIMPATICO 💙 ☕ - GEMINI 2.5 FLASH")
