import streamlit as st
from openai import OpenAI
from PIL import Image
import base64
import io

# 1. CASSAFORTE PERPLEXITY - RECUPERO BENZINA
try:
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("❌ CHIAVE PERPLEXITY NON TROVATA! AGGIUNGI 'PERPLEXITY_API_KEY' NEI SECRETS.")
    st.stop()

# Innesco del Sonar Perplexity
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="BLUE LOCK PERPLEXITY - GIULIO", page_icon="🕵️‍♂️", layout="centered")

# --- INTERFACCIA NAPOLI POWER ---
st.title("🕵️‍♂️ BLUE LOCK SONAR 5.0 (PPLX) 🛰️")
st.markdown("## **L'INTELLIGENCE CHE SCANSIONA LE NEWS E IL FANGO IN TEMPO REALE!** 💙 ☕")
st.write("---")

# AREA CREDITS
st.sidebar.markdown("### 🛠️ CANTIERE")
st.sidebar.write("**CREATA DA GIULIO SIMPATICO** 💙 ☕")
st.sidebar.write("---")
st.sidebar.info("MOTORE: PERPLEXITY SONAR - RICERCA LIVE ILLIMITATA.")

# 2. INSERIMENTO DATI
st.header("1. PUNTA IL MIRINO 🐎")
# Poiché Perplexity è focalizzato sul testo, inseriamo i nomi dei cavalli o della gara
event_info = st.text_input("INSERISCI NOME GARA O CAVALLI (ES: Hereford Corsa 1, Queen Maeve)", "")

if st.button("🔥 ATTIVA SONAR PERPLEXITY"):
    if not event_info:
        st.warning("SOCIO, DIMMI COSA DEVO CERCARE NELL'ABISSO!")
    else:
        with st.spinner("IL SONAR STA SETACCIANDO IL WEB E IL FANGO... ☕"):
            try:
                # PROTOCOLLO DI RICERCA NEWS E METEO
                prompt_pplx = f"""
                SEI IL SISTEMA 'BLUE LOCK SONAR' DI GIULIO SIMPATICO. 
                
                MISSIONE: SCANSIONA IL WEB PER L'EVENTO: {event_info}
                TROVA:
                1. METEO ATTUALE SULLA LOCALITÀ E STATO DEL TERRENO (FANGO, ERBA, SABBIA).
                2. NEWS DELL'ULTIMO MINUTO (CAMBI GUIDA, INFORTUNI, DICHIARAZIONI CAZZIMMA).
                3. ANALISI TECNICA: CHI È IL 'SECONDO MIGLIORE' CHE PUÒ SCHIACCIARE IL FAVORITO IN QUESTE CONDIZIONI?

                PROTOCOLLO RIGIDO (1-5):
                - STABILITÀ CIRCUITO (AFFINITÀ AL TERRENO DI OGGI).
                - DENSITÀ TECNICA (MOTORE BASATO SULLE NEWS).
                - POLMONI D'ACCIAIO (RESISTENZA CON IL FANGO TROVATO).
                - CAZZIMMA (VOGLIA DI VINCERE RILEVATA NELLE NEWS).

                SENTENZA FINALE (IN MAIUSCOLO):
                - SCORE >= 24: '💎 DIAMANTE ASSOLUTO RILEVATO. CERTEZZA 10000% 💙.'
                - SCORE < 24: '❌ CANTIERE NON CERTIFICATO. RISCHIO IMPUREZZE.'

                USA TERMINI: CEMENTO, MARMO, ABISSO, CAZZIMMA.
                NOTE DI GIULIO: IL VINCENTE NON È IL PIÙ VELOCE, MA QUELLO CHE TIEN' 'A CAZZIMMA OGGI.
                """
                
                messages = [
                    {"role": "system", "content": "Sei un esperto di analisi ippica e calcio del Progetto Blue Lock."},
                    {"role": "user", "content": prompt_pplx}
                ]
                
                response = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=messages,
                )
                
                st.markdown("### 2. LA SENTENZA DEL SONAR 💙")
                st.success(response.choices[0].message.content)
                st.balloons()
                
            except Exception as e:
                st.error(f"URTO NEL SISTEMA PERPLEXITY: {e}")

# FOOTER
st.write("---")
st.caption("BLUE LOCK SONAR - GIULIO SIMPATICO 💙 ☕ - POWERED BY PERPLEXITY")
