import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# --- GRAFICA 'THE LUPIN HEIST' (ROSSO LUPIN, GIALLO ORO) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0d0d0d;
        background-image: radial-gradient(#d32f2f 0.5px, transparent 0.5px);
        background-size: 30px 30px;
        color: #fbc02d;
        font-family: 'Courier New', Courier, monospace;
    }
    h1, h2, h3 { color: #d32f2f !important; text-transform: uppercase; text-shadow: 2px 2px #000000; }
    .stButton>button { 
        background-color: #d32f2f !important; 
        color: white !important; 
        border: 2px solid #fbc02d !important;
        font-weight: bold; font-size: 1.2em;
        box-shadow: 5px 5px 0px #000000;
    }
    .stAlert { background-color: #1a1a1a; border: 2px solid #d32f2f; color: #fbc02d; }
    </style>
    """, unsafe_allow_html=True)

# 2. CASSAFORTE API (LE CHIAVI DEL CAVEAU)
client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
client_pplx = OpenAI(api_key=st.secrets["PERPLEXITY_API_KEY"], base_url="https://api.perplexity.ai")

st.title("🎩 SNIPER 25.0: 'THE LUPIN HEIST' 💎")
st.markdown("### *'NON CHIEDIAMO IL PERMESSO AL BANCO, PRENDIAMO L'ORO E SPARIIAMO.'* 🔫")

# 3. INTERFACCIA DI COLPO
col1, col2 = st.columns([1, 1])

with col1:
    tipo_colpo = st.radio("🎯 SELEZIONA BERSAGLIO:", ["IPPICA (SACRO GRAAL)", "CALCIO (BLUE LOCK LIVE)"])
    uploaded_files = st.file_uploader("📸 SCANNER CAVEAU (SCREENSHOT):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

with col2:
    st.subheader("⚙️ PROTOCOLLO BUNKER 5.0 ATTIVO")
    st.write("- **LEGGE DEL 6**: SE C'È UN 6 NELLA SEQUENZA, È TRAPPOLA.")
    st.write("- **REGOLA 4/5**: SOLO MUSTANG CON 4 PODI NELLE ULTIME 5.")
    st.write("- **GG TRUTH**: <25 SABBIA, <45 ERBA. ZERO RUGGINE.")

if st.button("🔥 METTI A SEGNO IL COLPO"):
    if not uploaded_files:
        st.warning("EHI LUPIN, CARICA LE FOTO DEL CAVEAU!")
    else:
        with st.spinner("JIGEN STA PRENDENDO LA MIRA... 🚬"):
            try:
                images = [Image.open(f) for f in uploaded_files]
                # ESTRAZIONE CHIRURGICA
                prompt_v = "ESTRAI INTESTAZIONE (CIRCUITO, SUPERFICIE, TIPO) E TABELLA (NOME, PESO, RT, GG, SEQUENZA)."
                res_v = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt_v] + images)
                dati_raw = res_v.text

                # ANALISI LUPIN STYLE
                prompt_p = f"""
                SISTEMA: COMANDANTE LUPIN. PARLA IN MODO WITTY, DURO E SICURO. 
                DATI: {dati_raw}. TARGET: {tipo_colpo}.
                
                PROTOCOLLO DI FURTO (ZERO ERRORI):
                1. ANALISI CIRCUITO: Estrai l'ippodromo dal 'tetto' della foto. Se è Sabbia, sii spietato sui GG. [cite: 2026-02-25]
                2. LEGGE DEL 6: Escludi chiunque abbia un '6' o peggio negli ultimi 5 esiti. [cite: 2026-02-25]
                3. REQUISITI MARMO: Almeno 4 podi su 5. GG < 25 (Sabbia) o < 45 (Erba). [cite: 2026-02-15, 2026-02-24, 2026-02-25]
                4. BLUE LOCK RULES: Se Calcio Live, cerca 0-0 dopo 20' con favorito <1.60. No Svizzera/Italia (salvo Under 4.5). [cite: 2026-01-13, 2026-01-21, 2026-01-22]
                5. DENSITÀ TECNICA: Calcola se il motore schiaccia il favorito di carta indipendentemente dalla quota. [cite: 2026-02-20]

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💎 SACRO GRAAL INDIVIDUATO: [NOME]'
                'ORDINE TATTICO: [Punta Piazzato o Over Live - Spiegazione tecnica]'
                'BULLONE SERRATO: [Perché il caveau è stato violato].'
                """
                
                res_p = client_pplx.chat.completions.create(model="sonar-pro", messages=[{"role": "user", "content": prompt_p}])
                st.info(res_p.choices[0].message.content)
                st.balloons()
            except Exception as e:
                st.error(f"☠️ ALLARME SCATTATO: {e}")
