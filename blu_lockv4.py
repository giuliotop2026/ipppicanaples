import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA WESTERN CHIARA (SALOON MEZZOGIORNO DI FUOCO) ---
st.markdown("""
    <style>
    .stApp { 
        background-color: #f4e4bc; 
        background-image: url("https://www.transparenttextures.com/patterns/aged-paper.png");
        color: #3d2b1f; 
        font-family: 'Courier New', Courier, monospace; 
    }
    h1, h2, h3 { 
        color: #8b4513 !important; 
        text-transform: uppercase; 
        font-weight: 900; 
        text-shadow: 1px 1px 2px #cda26e;
        border-bottom: 3px solid #5a3a22;
    }
    .stAlert p { color: #3d2b1f !important; font-size: 1.3rem !important; font-weight: bold; }
    .stButton>button { 
        background-color: #a0522d !important; color: #fff8dc !important; 
        border: 3px solid #5a3a22 !important; font-weight: bold; font-size: 1.5em; 
        width: 100%; border-radius: 8px; height: 3.5em;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    .stButton>button:hover { background-color: #8b4513 !important; color: #ffd700 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. RADAR ACUSTICO ---
def play_victory_sound():
    audio_url = "https://www.myinstants.com/media/sounds/boxing-bell.mp3"
    components.html(f'<audio autoplay><source src="{audio_url}" type="audio/mpeg"></audio>', height=0, width=0)

# --- 3. CONNESSIONE AL CERVELLO GEMINI ---
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ EHI STRANIERO, MANCANO LE MUNIZIONI NEI SECRETS (GEMINI_API_KEY)!")
    st.stop()

st.title("🤠 SNIPER 51.0: IRON LUNG")
st.markdown("### *'Protocollo Granito 3.0 Evoluto. Densità Tecnica Totale.'*")

# --- 4. BACHECA DEI RICERCATI ---
nazione = st.selectbox("🗺️ TERRITORIO DI CACCIA:", [
    "UK", "IRLANDA", "USA", "ITALIA", "FRANCIA", "GERMANIA", 
    "SVEZIA", "CILE", "BRASILE", "SUD AFRICA", "AUSTRALIA", "GIAPPONE"
])

uploaded_files = st.file_uploader("📜 AFFIGGI I MANIFESTI (STATISTICHE):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 🧐 SOSPETTATI IN BACHECA:")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        with cols[i]:
            st.image(file, caption=f"Manifesto #{i+1}", use_container_width=True)

# --- 5. IL GRILLETTO (PROTOCOLLO INFALLIBILE) ---
if st.button("🐎 SCATENA IL DUELLO (TROVA IL VINCITORE)"):
    if not uploaded_files:
        st.warning("EHI COMPADRE, CARICA I MANIFESTI!")
    else:
        with st.spinner("LO SCERIFFO STA SCANSIONANDO L'ABISSO... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                prompt = f"""
                SEI LO SCERIFFO DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-19, 2026-01-20]
                TERRITORIO: {nazione}

                FASE 1: GABBIA DI LETTURA
                Identifica: Numero, Nome, RT (Rating/Rec), GG (Giorni), SEQ (Ultimi Arrivi).
                NON SCAMBIARE IL PESO CON L'RT.

                FASE 2: LEGGI DELLA FRONTIERA (GRANITO 3.0 EVOLUTO)
                1. MURO FORMA: Cerca chi ha 1 o 2 come ultimo esito. [cite: 2026-02-25]
                2. FILTRO RUGGINE: Preferenza GG < 45. [cite: 2026-02-25]
                3. ECCEZIONE "POLMONI D'ACCIAIO": Se un cavallo ha un RT (Rating) molto superiore agli altri, tollera GG fino a 90 (come successo con la numero 7 a Laval). La densità tecnica batte la ruggine temporanea. [cite: 2026-02-20]
                4. IL SECONDO MIGLIORE: Identifica il cavallo che garantisce il piazzamento (1-2-3) schiacciando il favorito instabile. [cite: 2026-02-20]

                REFERTO FINALE (SINTETICO):
                '💰 TAGLIA RISCOSSA: PISTOLERO [NUMERO #] - [NOME]'
                'MOTIVO: [Analisi su RT e Forma recente].'
                'BULLONE SERRATO: [Dati GG e SEQ].'
                
                SE NESSUNO HA I REQUISITI MINIMI:
                '🌵 NESSUNA PEPITA IN QUESTO FIUME.'
                """

                res = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt] + images)
                sentenza = res.text
                
                st.info(sentenza)
                if "TAGLIA" in sentenza.upper():
                    play_victory_sound(); st.balloons()
            except Exception as e:
                st.error(f"☠️ SERPENTE NELLO STIVALE: {e}")
