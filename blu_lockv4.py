import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

# --- STILE WESTERN CUSTOM (CSS) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f0e6d2; 
        color: #5c4033; 
    }
    h1, h2, h3 {
        color: #8b4513 !important; 
        font-family: 'Georgia', serif;
        text-transform: uppercase;
        text-shadow: 2px 2px 4px #cdaa7d;
    }
    .stButton>button {
        background-color: #8b4513 !important;
        color: #f0e6d2 !important;
        border: 2px solid #5c4033 !important;
        font-weight: bold;
        height: 3em;
        width: 100%;
    }
    .stSelectbox label, .stFileUploader label {
        color: #8b4513 !important;
        font-weight: bold;
        font-size: 1.2em;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. MUSICA E SUONI DELLA FRONTIERA
def play_western_music():
    # Musica ambient da Saloon (Piano) - Esegue in loop
    music_html = """
    <audio autoplay loop>
        <source src="https://www.soundjay.com/ambient/sounds/saloon-piano-1.mp3" type="audio/mpeg">
    </audio>
    """
    components.html(music_html, height=0, width=0)

def play_shot():
    # Suono del colpo di pistola per la vittoria
    shot_html = '<audio autoplay><source src="https://www.myinstants.com/media/sounds/ricochet-sound.mp3" type="audio/mpeg"></audio>'
    components.html(shot_html, height=0, width=0)

# 2. CASSAFORTE E PROTOCOLLO TENACITY
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("☠️ MANCANO LE MUNIZIONI NEI SECRETS! LA DILIGENZA È BLOCCATA.")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

# Funzione con Cazzimma per battere l'errore 503
@retry(
    stop=stop_after_attempt(5), 
    wait=wait_exponential(multiplier=1, min=4, max=10),
    retry=retry_if_exception_type(Exception) 
)
def fiuta_tracce_gemini(prompt, images):
    return client_gemini.models.generate_content(
        model='gemini-2.5-flash', 
        contents=[prompt] + images
    )

st.set_page_config(page_title="SNIPER 15.3: WESTERN GOLD", page_icon="🤠", layout="wide")
play_western_music() # Innesca la musica all'avvio

st.title("🌵 SNIPER 15.3: 'LA LEGGE DEL WEST' 🤠")
st.markdown("### **BENVENUTO AL SALOON, PARTNER! QUI COMANDA LA CAZZIMMA!** 🔫")

# 3. MAPPA DEL TERRITORIO
col1, col2 = st.columns(2)
with col1:
    nazione = st.selectbox("🌍 SCEGLI DOVE SPARARE:", [
        "USA 🇺🇸", "ARGENTINA 🇦🇷", "ITALIA 🇮🇹", "FRANCIA 🇫🇷", "SVEZIA 🇸🇪", "UK 🇬🇧"
    ])
    nazione_clean = nazione.split(" ")[0]

with col2:
    if nazione_clean == "USA":
        tipologia = st.selectbox("🏇 MODULO:", ["DIRT/SPEED (MARKET LAW) 💰"])
    elif nazione_clean == "FRANCIA":
        tipologia = st.selectbox("🏇 MODULO:", ["GALOPPO (PATCH FANGO) 🌧️", "TROTTO"])
    else:
        tipologia = st.selectbox("🏇 MODULO:", ["DENSITÀ REALE 💪"])

# 4. CARICO DATI
uploaded_files = st.file_uploader("📜 APPICCICA I 'WANTED POSTERS' (SCREENSHOT):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    st.image(images_to_process, width=200)

if st.button("💥 PREMI IL GRILLETTO!"):
    if not uploaded_files:
        st.warning("EHI PISTOLERO! IL CARICATORE È VUOTO.")
    else:
        with st.spinner(f"LO SCERIFFO STA SCANSIONANDO IL RANCH... 🔭"):
            try:
                # FASE 1: ESTRAZIONE CON TENACITY (TENEREZZA ZERO VERSO IL 503)
                prompt_vision = f"Estrai dati tecnici per {nazione_clean}: NOME, QUOTA, RATING, PESO, SEQUENZA, NOTE."
                response_vision = fiuta_tracce_gemini(prompt_vision, images_to_process)
                dati = response_vision.text

                # FASE 2: ANALISI OFFLINE
                prompt_pplx = f"""
                SISTEMA: ANALIZZATORE WESTERN OFFLINE. USA SOLO: {dati}
                LEGGI:
                1. USA: MARKET LAW (Favoriti con quote basse e '1' recente).
                2. FRANCIA: PATCH FANGO. Quota > 12.00 = BURRONE (anche con rating alto). [cite: 2026-02-24]
                3. ROW: IGNORA QUOTE. Cerca il MARMO per densità tecnica.
                4. FERRO BEN BATTUTO: RP/RI/FE/T = BURRONE immediato.
                
                REFERTO (SINTASSI WESTERN):
                '💰 PEPITA D'ORO TROVATA: [NOME].'
                'MOTIVAZIONE: [Spiega con CAZZIMMA perché questo cavallo ha le palle quadrate].'
                TERMINI: ORO PURO, BURRONE, FERRO BEN BATTUTO, CAZZIMMA.
                """
                
                resp = client_pplx.chat.completions.create(model="sonar-pro", messages=[{"role": "user", "content": prompt_pplx}])
                st.info(resp.choices[0].message.content)
                
                if "PEPITA" in resp.choices[0].message.content.upper():
                    play_shot()
                    st.balloons()
            except Exception as e:
                st.error(f"☠️ URTO NEL REATTORE: {e}. Il server è più duro del previsto, riprova tra poco!")
