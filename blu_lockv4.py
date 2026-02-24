import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# --- GRAFICA DA SALOON (CSS CUSTOM) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f4eccf; /* Colore pergamena antica */
        color: #5d4037; /* Marrone cuoio */
        font-family: 'Georgia', serif;
    }
    h1, h2, h3 {
        color: #8b4513 !important;
        text-transform: uppercase;
        text-shadow: 2px 2px 4px #cdaa7d;
    }
    .stButton>button {
        background-color: #8b4513 !important;
        color: #f4eccf !important;
        border: 2px solid #3e2723 !important;
        font-weight: bold;
        width: 100%;
        height: 3.5em;
        text-transform: uppercase;
    }
    .stSelectbox label, .stFileUploader label {
        color: #3e2723 !important;
        font-weight: bold;
        font-size: 1.1em;
    }
    .stAlert {
        background-color: #e0c5a0;
        border: 2px solid #8b4513;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. NOTIFICA SONORA (IL RINTOCCO DEL DUELLO)
def play_beep():
    # Suono di un colpo di pistola secco
    beep_html = '<audio autoplay><source src="https://www.myinstants.com/media/sounds/ricochet-sound.mp3" type="audio/mpeg"></audio>'
    components.html(beep_html, height=0, width=0)

# 2. CASSAFORTE API
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("☠️ PORCA PALETTA! MANCANO LE MUNIZIONI NEI SECRETS! LA DILIGENZA È FERMA.")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 15.3 WESTERN EDITION", page_icon="🤠", layout="wide")

st.title("🌵 SNIPER 15.3: 'LA LEGGE DEL WEST' 🤠")
st.markdown("### *'Vedi, il mondo si divide in due categorie: chi ha la pistola carica e chi scava. Tu... analizzi.'* 🔫 🥃")

# 3. SISTEMA DI SELEZIONE A MATRICE TOTALE
col1, col2 = st.columns(2)

with col1:
    nazione = st.selectbox("🗺️ SCEGLI IL TERRITORIO DI CACCIA:", [
        "USA", "ARGENTINA", "ITALIA", "FRANCIA", "SVEZIA", "UK", "SUD AFRICA", 
        "AUSTRALIA", "GERMANIA", "ARABIA SAUDITA", "BRASILE/CILE/MESSICO"
    ])

with col2:
    if nazione == "USA":
        tipologia = st.selectbox("🏇 MODULO:", ["DIRT/SPEED (MARKET LAW)"])
    elif nazione == "ARGENTINA":
        tipologia = st.selectbox("🏇 MODULO:", ["DIRT/SPEED (DENSITÀ REALE)", "HANDICAP/ZAVORRA"])
    elif nazione in ["ITALIA", "FRANCIA", "SVEZIA"]:
        tipologia = st.selectbox("🏇 MODULO:", ["TROTTO (BULLONE SERRATO)", "GALOPPO PIANO", "HANDICAP/NASTRI"])
    else:
        tipologia = st.selectbox("🏇 MODULO:", ["FLAT/PIANO", "HANDICAP/ZAVORRA", "DIRT/SPEED"])

# 4. CARICAMENTO IDENTIKIT
uploaded_files = st.file_uploader("📜 APPICICA I 'WANTED POSTERS' (GLI SCREENSHOT):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images_to_process = [Image.open(f) for f in uploaded_files]
    for img in images_to_process:
        st.image(img, use_container_width=True)

if st.button("💥 PREMI IL GRILLETTO (ANALIZZA I DATI)"):
    if not uploaded_files:
        st.warning("EHI COWBOY! IL CARICATORE È VUOTO! CARICA I DATI.")
    else:
        # Frase iconica casuale durante il caricamento
        with st.spinner("'Quando un uomo con la pistola incontra un uomo col fucile, quello con la pistola è un uomo morto.'... SCANSIONE IN CORSO... 🚬"):
            try:
                # FASE 1: ESTRAZIONE CINETICA (GEMINI 2.5 FLASH)
                prompt_vision = f"""
                Converti questi dati in un report tecnico per {nazione}.
                NON CERCARE SUL WEB. LEGGI SOLO QUESTE IMMAGINI.
                ESTRAI: NOME, QUOTA (Odds), RATING, PESO, SEQUENZA, NOTE (FE, T, CD, RP, RI).
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + images_to_process
                )
                dati_estratti = response_vision.text
                st.success(f"YEE-HAW! INDIZI RACCOLTI CON GEMINI 2.5! 🥃")

                # FASE 2: ANALISI DELLO SCERIFFO OFFLINE
                prompt_pplx = f"""
                SISTEMA: SEI UN VECCHIO SCERIFFO DEL WEST. PARLA COME UN COWBOY DURO E USA FRASI ICONICHE DEI FILM WESTERN ITALIANI.
                USA SOLO QUESTI DATI: {dati_estratti}

                PARAMETRI DI PERFEZIONE 15.3:
                1. SE NAZIONE == 'USA': Applica MARKET LAW. Identifica i cavalli con le QUOTE PIÙ BASSE. Confrontali e scegli il migliore tra i favoriti. Deve avere almeno un '1' recente. [cite: 2026-02-23]
                2. SE NAZIONE == 'FRANCIA': IGNORA LE QUOTE, MA APPLICA LA PATCH FANGO (CAGNES/ANGERS). SE LA QUOTA È SUPERIORE A 12.00, IL SOGGETTO È BURRONE IMMEDIATO ANCHE CON RATING ALTO. IL MARMO DEVE AVERE UN MINIMO DI CONSENSO (QUOTA < 12.00). [cite: 2026-02-24]
                3. SE NAZIONE != 'USA' E NAZIONE != 'FRANCIA': IGNORA LE QUOTE. Cerca il secondo migliore per densità tecnica reale, regolarità e polmoni d'acciaio. [cite: 2026-02-20]
                4. BULLONE SERRATO (UNIVERSALE): RP, RI, DAI, 0, Squalificato, FE o T = ABISSO MECCANICO immediato. [cite: 2026-02-23]
                5. HIGHLANDER: Efficienza = Rating / (Carico * Distanza). [cite: 2026-02-20]
                6. NO 4° POSTI: Chi arriva spesso 4° è RUGGINE. [cite: 2026-02-23]

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💰 PEPITA D'ORO INDIVIDUATA: [NOME]. 
                LA SCOMMESSA DEL PISTOLERO: [Analisi specifica per {nazione} con citazione western iconica].'
                TERMINI OBBLIGATORI: MARMO, CEMENTO, ABISSO, CAZZIMMA, BULLONE SERRATO.
                """
                
                response_pplx = client_pplx.chat.completions.create(
                    model="sonar-pro",
                    messages=[{"role": "user", "content": prompt_pplx}]
                )
                
                sentenza = response_pplx.choices[0].message.content
                
                # Visualizzazione finale stile Western
                st.markdown("""<div style='background-color: #f8f0e3; border: 3px dashed #8b4513; padding: 20px; border-radius: 10px;'>
                                <h3 style='text-align: center;'>📜 IL VERDETTO DELLO SCERIFFO 📜</h3>""", unsafe_allow_html=True)
                st.info(sentenza)
                st.markdown("</div>", unsafe_allow_html=True)
                
                if "PEPITA" in sentenza.upper() or "DIAMANTE" in sentenza.upper():
                    play_beep()
                    st.balloons()
                    st.success("AL CUORE, RAMON, AL CUORE! ABBIAMO L'ORO! 💰")

            except Exception as e:
                st.error(f"☠️ SERPENTE NELLO STIVALE! URTO TECNICO: {e}")
