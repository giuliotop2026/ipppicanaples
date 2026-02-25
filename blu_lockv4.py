import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# --- GRAFICA 'THE GREAT HEIST' (STILE LUPIN III) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0d0d0d;
        background-image: linear-gradient(rgba(211, 47, 47, 0.1) 1px, transparent 1px), 
                          linear-gradient(90deg, rgba(211, 47, 47, 0.1) 1px, transparent 1px);
        background-size: 20px 20px;
        color: #ffeb3b;
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton>button { 
        background-color: #d32f2f !important; 
        color: white !important; 
        border: 3px solid #ffeb3b !important;
        font-weight: bold; font-size: 1.5em;
        box-shadow: 8px 8px 0px #000000;
    }
    .stAlert { background-color: #1a1a1a; border-left: 10px solid #d32f2f; }
    </style>
    """, unsafe_allow_html=True)

# 2. CHIAVI DEL CAVEAU (API)
client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
client_pplx = OpenAI(api_key=st.secrets["PERPLEXITY_API_KEY"], base_url="https://api.perplexity.ai")

st.title("🎩 SNIPER 26.0: 'LUPIN'S FINAL TRIGGER' 💎")
st.markdown("### *'Se il banco ha l'oro, noi abbiamo il piano. Zero errori.'* 🔫")

# 3. SCANNER DI PRECISIONE
uploaded_files = st.file_uploader("📸 SCANNER CAVEAU (SCREENSHOT):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if st.button("🚨 METTI A SEGNO IL FURTO"):
    if not uploaded_files:
        st.warning("EHI LUPIN, CARICA I POSTER DEL CAVEAU!")
    else:
        with st.spinner("JIGEN STA TARANDO IL MIRINO... 🚬"):
            try:
                images = [Image.open(f) for f in uploaded_files]
                # ESTRAZIONE PARTICELLE (NON NOMI)
                prompt_v = "ESTRAI: Circuito, Superficie, NUMERO (#), Peso, Rt, GG, Sequenza (Ordina dal più recente)."
                res_v = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt_v] + images)
                dati_raw = res_v.text

                prompt_p = f"""
                SISTEMA: COMANDANTE LUPIN. PARLA COME UN LADRO GENTILUOMO SPIETATO. 
                DATI: {dati_raw}

                REGOLE DEL FURTO PERFETTO (BUNKER 6.0):
                1. IDENTITÀ PER PARTICELLE: Ignora i nomi, usa solo i NUMERI (#). Evita confusioni tra simili (es. Ginger vs Ginger Gadd). [cite: 2026-01-25]
                2. LEGGE DEL TREND RECENTE: Se l'ultimo risultato della sequenza NON è un podio (1, 2, 3), è ABISSO. Non importa quanti 1 ha prima. Il motore deve essere caldo ORA. [cite: 2026-02-25]
                3. FILTRO RUGGINE: GG < 20 per Sabbia, < 40 per Erba. Ogni giorno in più è una crepa nel marmo. [cite: 2026-02-24]
                4. SACRO GRAAL: Deve avere 4 podi su 5, GG perfetto, e l'ULTIMA USCITA deve essere un 1 o un 2. [cite: 2026-02-25]

                REFERTO (SINTASSI MAIUSCOLA):
                '💎 SACRO GRAAL INDIVIDUATO: [NUMERO #]'
                'PIANO DI FUGA: [Perché questo numero schiaccia il caveau]'
                'BULLONE SERRATO: [Analisi della densità tecnica reale].'
                """
                
                res_p = client_pplx.chat.completions.create(model="sonar-pro", messages=[{"role": "user", "content": prompt_p}])
                st.info(res_p.choices[0].message.content)
                st.balloons()
            except Exception as e:
                st.error(f"☠️ ALLARME SCATTATO: {e}")
