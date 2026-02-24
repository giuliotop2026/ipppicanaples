import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

# --- STILE WESTERN CUSTOM (CSS DEL SALOON) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f0e6d2; 
        color: #5c4033; 
        font-family: 'Georgia', serif;
    }
    h1, h2, h3 {
        color: #8b4513 !important; 
        text-transform: uppercase;
        text-shadow: 2px 2px 4px #cdaa7d;
    }
    .stButton>button {
        background-color: #8b4513 !important;
        color: #f0e6d2 !important;
        border: 2px solid #5c4033 !important;
        font-weight: bold;
        width: 100%;
        height: 3.5em;
    }
    .stSelectbox label, .stFileUploader label {
        color: #8b4513 !important;
        font-weight: bold;
        font-size: 1.2em;
    }
    .stAlert {
        background-color: #f8f0e3;
        border: 2px solid #8b4513;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. MUNIZIONI AUDIO
def play_shot():
    # Suono di un ricochet western
    shot_html = '<audio autoplay><source src="https://www.myinstants.com/media/sounds/ricochet-sound.mp3" type="audio/mpeg"></audio>'
    components.html(shot_html, height=0, width=0)

# 2. CASSAFORTE DELLO SCERIFFO E PROTOCOLLO TENACITY (ANTI-503)
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("☠️ PORCA PALETTA! MANCANO LE MUNIZIONI NEI SECRETS! LA DILIGENZA È FERMA.")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

# Il sistema proverà a sparare fino a 5 volte se il server di Google scotta (errore 503)
@retry(
    stop=stop_after_attempt(5), 
    wait=wait_exponential(multiplier=1, min=4, max=10),
    retry=retry_if_exception_type(Exception) 
)
def fiuta_tracce_gemini(prompt, images):
    return client_gemini.models.generate_content(
        model='gemini-2.0-flash', # Potenza cinetica Gemini 2.5/2.0
        contents=[prompt] + images
    )

st.set_page_config(page_title="SNIPER 15.3: WESTERN GOLD", page_icon="🤠", layout="wide")

# --- INTERFACCIA DEL SALOON ---
st.title("🌵 SNIPER 15.3: 'LA LEGGE DEL WEST' 🤠")
st.markdown("### **BENVENUTO PARTNER! SCHIACCIA PLAY E CARICA I WANTED POSTERS!** 🥃")

# PULSANTE PLAY PER IL PIANO DEL SALOON
st.audio("https://www.soundjay.com/ambient/sounds/saloon-piano-1.mp3", format="audio/mp3")

st.markdown("---")

# 3. MAPPA DEI TERRITORI (TUTTE LE NAZIONI)
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🗺️ SCEGLI DOVE SPARARE:")
    nazione = st.selectbox("", [
        "USA 🇺🇸", "ARGENTINA 🇦🇷", "ITALIA 🇮🇹", "FRANCIA 🇫🇷", "SVEZIA 🇸🇪", "UK 🇬🇧", 
        "SUD AFRICA 🇿🇦", "AUSTRALIA 🇦🇺", "GERMANIA 🇩🇪", "ARABIA SAUDITA 🇸🇦", "BRASILE/CILE/MESSICO 🌎"
    ])
    nazione_clean = nazione.split(" ")[0]

with col2:
    st.markdown("#### 🐎 TIPO DI DUELLO (MODULO):")
    if nazione_clean == "USA":
        tipologia = st.selectbox("", ["DIRT/SPEED (MARKET LAW) 💰"])
    elif nazione_clean == "ARGENTINA":
        tipologia = st.selectbox("", ["DIRT/SPEED (DENSITÀ REALE) 💪"])
    elif nazione_clean in ["ITALIA", "FRANCIA", "SVEZIA"]:
        tipologia = st.selectbox("", ["TROTTO (FERRO BEN BATTUTO) 🔨", "GALOPPO PIANO 🏇", "HANDICAP/NASTRI ⚖️"])
    else:
        tipologia = st.selectbox("", ["FLAT/PIANO 🏇", "HANDICAP/ZAVORRA ⚖️", "DIRT/SPEED 💨"])

# 4. CARICO IDENTIKIT
st.markdown("#### 📜 APPICCICA QUI I 'WANTED POSTERS' (GLI SCREENSHOT):")
uploaded_files = st.file_uploader("", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    cols = st.columns(len(images_to_process))
    for i, img in enumerate(images_to_process):
        cols[i].image(img, use_container_width=True)

if st.button("🔥 PREMI IL GRILLETTO (ANALIZZA I DATI)"):
    if not uploaded_files:
        st.warning("EHI COWBOY! IL CARICATORE È VUOTO! CARICA I DATI.")
    else:
        with st.spinner(f"LO SCERIFFO STA FIUTANDO LA PISTA IN {nazione_clean}... 🔭"):
            try:
                # FASE 1: ESTRAZIONE CINETICA (CON TENACITY ANTI-503)
                prompt_vision = f"""
                Analizza questi documenti per {nazione_clean}. NON CERCARE SUL WEB. LEGGI SOLO LE IMMAGINI.
                ESTRAI: NOME, QUOTA (Odds), RATING, PESO, SEQUENZA STORICA (numeri), NOTE (FE, T, CD, RP, RI).
                """
                response_vision = fiuta_tracce_gemini(prompt_vision, images_to_process)
                dati_estratti = response_vision.text
                st.success(f"INDIDZI RACCOLTI CON GEMINI! 🥃")

                # FASE 2: ANALISI DINAMICA DELLO SCERIFFO (SONAR-PRO)
                prompt_pplx = f"""
                SISTEMA: SEI UN VECCHIO SCERIFFO DEL WEST. PARLA COME UN COWBOY DURU E USA FRASI ICONICHE DAI FILM DI SERGIO LEONE O CLINT EASTWOOD.
                USA SOLO QUESTI DATI: {dati_estratti}

                LE LEGGI DELLO SCERIFFO 15.3:
                1. USA: MARKET LAW. Confronta i favoriti (quote basse). Il migliore deve avere almeno un '1' recente.
                2. FRANCIA (LEGGE LOHENGREEN): Se la quota è superiore a 12.00, quel ronzino finisce nel BURRONE anche se ha un rating alto. Nel fango francese, il mercato deve confermare il cemento (Quota < 12.00). [cite: 2026-02-24]
                3. ROW/ARG: IGNORA LE QUOTE. Cerca il secondo cavallo migliore per densità tecnica e polmoni d'acciaio. [cite: 2026-02-20]
                4. FERRO BEN BATTUTO (Universale): RP, RI, DAI, 0, Squalificato, FE o T = BURRONE immediato. [cite: 2026-02-23]
                5. HIGHLANDER: Efficienza = Rating / (Carico * Distanza). [cite: 2026-02-20]
                6. NO 4° POSTI: Il '4' è ruggine cronica. [cite: 2026-02-23]

                RAPPORTO FINALE (SINTASSI MAIUSCOLA E DINAMICA):
                '💰 PEPITA D'ORO TROVATA: [NOME].'
                'LA SCOMMESSA DEL PISTOLERO (MOTIVAZIONE): [Spiega con CAZZIMMA perché questo purosangue ha le palle quadrate e cita una frase western iconica adattata alla situazione. Spiega perché rispetta la legge locale di {nazione_clean}].'
                
                TERMINI OBBLIGATORI: ORO PURO, BURRONE, FERRO BEN BATTUTO, CAZZIMMA, MARKET LAW.
                """
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=[{"role": "user", "content": prompt_pplx}]
                )
                
                sentenza = response_pplx.choices[0].message.content
                
                # Visualizzazione Verdetto
                st.markdown("""<div style='background-color: #f8f0e3; border: 3px dashed #8b4513; padding: 20px; border-radius: 10px;'>
                                <h3 style='text-align: center;'>📜 IL VERDETTO DELLO SCERIFFO 📜</h3>""", unsafe_allow_html=True)
                st.info(sentenza)
                st.markdown("</div>", unsafe_allow_html=True)

                if "PEPITA" in sentenza.upper():
                    play_shot()
                    st.balloons()
                    st.success("CENTRO PERFETTO, PARTNER! ANDIAMO A INCASSARE L'ORO! 💰")

            except Exception as e:
                st.error(f"☠️ SERPENTE NELLO STIVALE! URTO TECNICO: {e}")
