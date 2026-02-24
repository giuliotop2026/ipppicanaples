import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components

# --- STILE WESTERN CUSTOM (CSS) ---
# Iniettiamo un po' di stile da Saloon per rendere tutto color pergamena e cuoio.
st.markdown("""
    <style>
    .stApp {
        background-color: #f0e6d2; /* Colore pergamena chiaro */
        color: #5c4033; /* Marrone cuoio */
    }
    h1, h2, h3 {
        color: #8b4513 !important; /* Marrone sella */
        font-family: 'Georgia', serif;
        text-transform: uppercase;
        text-shadow: 2px 2px 4px #cdaa7d;
    }
    .stButton>button {
        background-color: #8b4513 !important;
        color: #f0e6d2 !important;
        border: 2px solid #5c4033 !important;
        font-weight: bold;
    }
    .stSelectbox label, .stFileUploader label {
        color: #8b4513 !important;
        font-weight: bold;
        font-size: 1.2em;
    }
    .stAlert {
        background-color: #f0e6d2;
        border: 2px solid #8b4513;
        color: #5c4033;
    }
    /* Modifica i colori dei messaggi di successo/info/errore per adattarli al tema */
    .stSuccess { background-color: #d4edda; border-color: #c3e6cb; color: #155724; }
    .stInfo { background-color: #d1ecf1; border-color: #bee5eb; color: #0c5460; }
    .stError { background-color: #f8d7da; border-color: #f5c6cb; color: #721c24; }
    </style>
    """, unsafe_allow_html=True)

# 1. SUONO DELLO SPARO (PROTOCOLLO WESTERN)
# Usiamo un suono che ricorda un colpo di frusta o uno sparo secco.
def play_shot():
    # Link temporaneo a un suono western (sostituibile se ne hai uno migliore)
    shot_html = '<audio autoplay><source src="https://www.myinstants.com/media/sounds/ricochet-sound.mp3" type="audio/mpeg"></audio>'
    components.html(shot_html, height=0, width=0)

# 2. CASSAFORTE DELLO SCERIFFO (API)
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("☠️ PORCA PALETTA! MANCANO LE MUNIZIONI NEI SECRETS! LA DILIGENZA NON PARTE.")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 15.3: WESTERN EDITION", page_icon="🤠", layout="wide")

st.title("🌵 SNIPER 15.3: 'LA LEGGE DEL WEST' 🤠")
st.markdown("### **IN SELLA, PARTNER! QUI CI VUOLE PURA CAZZIMMA!** 🔫 🥃")
st.markdown("---")

# 3. MAPPA DEL TERRITORIO (MATRICE TOTALE)
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🗺️ SCEGLI IL TUO TERRITORIO DI CACCIA:")
    nazione = st.selectbox("NAZIONE:", [
        "USA 🇺🇸", "ARGENTINA 🇦🇷", "ITALIA 🇮🇹", "FRANCIA 🇫🇷", "SVEZIA 🇸🇪", "UK 🇬🇧", "SUD AFRICA 🇿🇦", 
        "AUSTRALIA 🇦🇺", "GERMANIA 🇩🇪", "ARABIA SAUDITA 🇸🇦", "BRASILE/CILE/MESSICO 🌎"
    ])
    # Puliamo la stringa nazione dalle emoji per i prompt
    nazione_clean = nazione.split(" ")[0]

with col2:
    st.markdown("#### 🐎 TIPO DI DUELLO (MODULO):")
    if nazione_clean == "USA":
        tipologia = st.selectbox("MODULO:", ["DIRT/SPEED (MARKET LAW - Segui i Soldi) 💰"])
    elif nazione_clean == "ARGENTINA":
        tipologia = st.selectbox("MODULO:", ["DIRT/SPEED (DENSITÀ REALE - Pura Potenza) 💪"])
    elif nazione_clean in ["ITALIA", "FRANCIA", "SVEZIA"]:
        tipologia = st.selectbox("MODULO:", ["TROTTO (FERRO BEN BATTUTO) 🔨", "GALOPPO PIANO 🏇", "HANDICAP/NASTRI ⚖️"])
    else:
        tipologia = st.selectbox("MODULO:", ["FLAT/PIANO 🏇", "HANDICAP/ZAVORRA ⚖️", "DIRT/SPEED 💨"])

st.markdown("---")

# 4. CARICO DELLA DILIGENZA (DATI)
st.markdown("#### 📜 APPICICA QUI I 'WANTED POSTERS' (I TUOI SCREENSHOT):")
uploaded_files = st.file_uploader("", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("##### 🔎 INDIZI RACCOLTI:")
    cols = st.columns(len(uploaded_files))
    for i, img_file in enumerate(uploaded_files):
        img = Image.open(img_file)
        cols[i].image(img, use_container_width=True)
    st.markdown("---")

# BOTTONE DI FUOCO
if st.button("💥 PREMI IL GRILLETTO (ANALIZZA I DATI)"):
    if not uploaded_files:
        st.warning("EHI COWBOY! IL CARICATORE È VUOTO! CARICA QUEI DANNATI DATI PRIMA DI SPARARE.")
    else:
        # Spinner stile Western
        with st.spinner(f"SELLANDO IL CAVALLO... IL SEGUGIO GEMINI STA FIUTANDO LA PISTA IN {nazione_clean}... 🔭"):
            try:
                # FASE 1: ESTRAZIONE CINETICA (GEMINI 2.5 FLASH - IL SEGUGIO)
                prompt_vision = f"""
                Ehi vecchio mio. Guarda questi documenti del ranch in {nazione_clean}.
                NON CERCARE IN GIRO. LEGGI SOLO QUELLO CHE VEDI QUI.
                Tira fuori questi dati con precisione: NOME del cavallo, QUOTA (Odds), RATING, PESO che porta, la sua SEQUENZA storica, e se vedi note strane come FE, T, CD, RP, RI.
                """
                response_vision = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt_vision] + [Image.open(f) for f in uploaded_files]
                )
                dati_estratti = response_vision.text
                st.success(f"YEE-HAW! TRACCE INDIVIDUATE IN {nazione_clean} GRAZIE AL FIUTO DI GEMINI! 🥃")

                # FASE 2: ANALISI SPECIALIZZATA (LO SCERIFFO OFFLINE)
                prompt_pplx = f"""
                SISTEMA: SEI UN VECCHIO SCERIFFO DEL WEST, ESPERTO DI CAVALLI E DI LEGGI DELLA PRATERIA. PARLA COME UN COWBOY DURO. NON USARE INTERNET.
                USA SOLO QUESTI DATI CHE TI HO DATO: {dati_estratti}

                LE LEGGI DELLO SCERIFFO 15.3 (GLOBAL HYBRID):
                1. SE SIAMO IN 'USA': Applica la LEGGE DEL MERCATO (Market Law). Guarda i cavalli con la taglia più bassa (quote basse). Mettili a confronto. Il migliore deve avere il sangue agli occhi (almeno un '1' recente).
                2. SE SIAMO IN 'FRANCIA': IGNORA LE QUOTE, ma occhio al FANGO (Patch Erba Pesante). Se il terreno è pesante e la quota è sopra 12.00, è un cavallo da soma, non da corsa. Il diamante nel fango deve avere un minimo di rispetto dal mercato (quota < 12.00).
                3. SE SIAMO ALTROVE (NON USA, NON FRANCIA): AL DIAVOLO LE QUOTE. Cerca il secondo cavallo migliore per potenza pura (densità tecnica), che non sbaglia un colpo e ha polmoni d'acciaio.
                4. FERRO BEN BATTUTO (Universale): Se vedi RP, RI, DAI, 0, Squalificato, FE o T, quel cavallo è zoppo. Buttalo nel BURRONE (Abisso) immediatamente.
                5. HIGHLANDER: Efficienza = Rating / (Carico * Distanza). Chi non regge il peso, non arriva al saloon.
                6. NO 4° POSTI: Chi arriva sempre 4° è solo ruggine sulla pistola.

                RAPPORTO DELLO SCERIFFO (SINTASSI WESTERN OBBLIGATORIA):
                Devi usare questo formato esatto:
                '💰 PEPITA D'ORO (DIAMANTE) TROVATA: [NOME DEL CAVALLO].'
                'LA SCOMMESSA DEL PISTOLERO (MOTIVAZIONE): [Qui devi spiegare perché questo cavallo ha più **CAZZIMMA** degli altri in {nazione_clean}. Usa frasi tipo "ha le palle quadrate", "non teme la polvere", "è oro puro contro il piombo degli altri". Spiega perché rispetta la legge locale.]'
                
                TERMINI CHE DEVI USARE NEL RAPPORTO: PEPITA D'ORO (invece di Diamante), ORO PURO (invece di Cemento/Marmo), BURRONE (invece di Abisso), CAZZIMMA, FERRO BEN BATTUTO (invece di Bullone Serrato).
                """
                
                with st.spinner("LO SCERIFFO STA CARICANDO LA SEI COLPI... L'ANALISI È IN CORSO... 🧐"):
                    response_pplx = client_pplx.chat.completions.create(
                        model="sonar-pro",
                        messages=[{"role": "user", "content": prompt_pplx}]
                    )
                    
                    sentenza = response_pplx.choices[0].message.content
                    
                    # Visualizzazione del risultato in uno stile più "cartaceo"
                    st.markdown("""<div style='background-color: #f8f0e3; border: 3px dashed #8b4513; padding: 20px; border-radius: 10px;'>
                                    <h3 style='text-align: center;'>📜 VERDETTO DELLO SCERIFFO 📜</h3>
                                """, unsafe_allow_html=True)
                    st.info(sentenza)
                    st.markdown("</div>", unsafe_allow_html=True)

                    if "PEPITA D'ORO" in sentenza.upper() or "DIAMANTE" in sentenza.upper():
                        play_shot() # Suono dello sparo!
                        st.balloons()
                        st.success("BOOM! CENTRO PERFETTO, PARTNER! QUESTA È ROBA CHE SCOTTA! 💸")

            except Exception as e:
                st.error(f"☠️ SERPENTE NELLO STIVALE! QUALCOSA È ANDATO STORTO NEL REATTORE: {e}")
                st.markdown("#### Riprova, cowboy, e mira meglio!")
