import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# --- GRAFICA BUNKER 4.0 (PIETRA E ACCIAIO INVIOLABILE) ---
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(244, 236, 207, 0.92), rgba(244, 236, 207, 0.92)), 
        url('https://images.unsplash.com/photo-1599408162145-8993d567798c?q=80&w=2070&auto=format&fit=crop');
        background-size: cover; background-attachment: fixed;
    }
    .stButton>button { background-color: #1b1b1b !important; color: #f4eccf !important; border: 3px solid #d32f2f !important; height: 4.5em; }
    </style>
    """, unsafe_allow_html=True)

# 2. CASSAFORTE API
client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
client_pplx = OpenAI(api_key=st.secrets["PERPLEXITY_API_KEY"], base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 23.0 RADAR CIRCUITO", layout="wide")
st.title("🛡️ SNIPER 23.0: 'RADAR CIRCUITO' 🐎")
st.markdown("### *'Estraiamo la verità dal tetto della foto. Niente più bugie.'* 🔫")

# 3. SCANNER AUTOMATICO
uploaded_files = st.file_uploader("📸 CARICA IL CANTIERE (HEADER + STATS):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if st.button("🔥 ATTIVA SCANNER E SERRRA I BULLONI"):
    if not uploaded_files:
        st.warning("CARICA I POSTER, SOCIO!")
    else:
        with st.spinner("IL RADAR STA LEGGENDO IL CIRCUITO E LE SUPERFICI... 🚬"):
            try:
                images_to_process = [Image.open(f) for f in uploaded_files]
                # GEMINI ORA ESTRAE ANCHE L'INTESTAZIONE (IPPODROMO, TIPO CORSA, SUPERFICIE)
                prompt_vision = """
                ANALISI TOTALE:
                1. ESTRAI INTESTAZIONE: Ippodromo, Numero Corsa, Tipo (Galoppo/Trotto), Distanza, Superficie (Erba/Sabbia/Dirt).
                2. ESTRAI TABELLA: Nome Cavallo, Peso, Rt, GG, Ultimi Arrivi.
                """
                res_v = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt_vision] + images_to_process)
                dati_raw = res_v.text

                prompt_pplx = f"""
                SISTEMA: COMANDANTE GRANITO 4.0. 
                DATI ESTRATTI: {dati_raw}

                PARAMETRI DI PERFEZIONE ASSOLUTA (RETTIFICA 23.0):
                1. AUTOMATIC TRACK DETECTION: Leggi l'intestazione. Se è 'SABBIA' o 'DIRT', la freschezza GG deve essere < 25. La sabbia non perdona la ruggine. [cite: 2026-02-24]
                2. HANDICAP WEIGHT LAW: Se il peso è > 70kg, il cavallo deve avere un Rating (Rt) superiore a 55 per essere 'Marmo'. Altrimenti è un 'Tir' senza motore.
                3. GG TRUTH: Sii spietato. GG > 45 = SCARTO IMMEDIATO. Isabel Queen aveva 59gg ed è fallita. Non ripetere l'errore.
                4. SACRO GRAAL: Solo chi ha 4 podi su 5, GG < 25, e peso sostenibile rispetto al Rating. [cite: 2026-02-20]

                REFERTO (SINTASSI MAIUSCOLA):
                '🏟️ CIRCUITO RILEVATO: [Ippodromo - Superficie]'
                '💎 SACRO GRAAL: [NOME]'
                'DENSITÀ TECNICA: [Peso vs Rt vs GG]'
                'ORDINE: [Perché questo è Granito e non sabbia mobile].'
                """
                
                response_pplx = client_pplx.chat.completions.create(model="sonar-pro", messages=[{"role": "user", "content": prompt_pplx}])
                st.info(response_pplx.choices[0].message.content)
                st.balloons()
            except Exception as e:
                st.error(f"URTO: {e}")
