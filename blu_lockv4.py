import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA "PALACIO DEL VENGADOR" ---
st.markdown("""
    <style>
    .stApp { 
        background-color: #f4e4bc; 
        background-image: url("https://www.transparenttextures.com/patterns/aged-paper.png");
        color: #1a1a1a; 
        font-family: 'Georgia', serif; 
    }
    h1, h2, h3 { 
        color: #000000 !important; 
        text-transform: uppercase; 
        font-weight: 900; 
        text-shadow: 2px 2px 4px #8b4513;
        border-bottom: 4px solid #000000;
    }
    .stAlert p { color: #1a1a1a !important; font-size: 1.4rem !important; font-weight: bold; }
    .stButton>button { 
        background-color: #000000 !important; color: #ffd700 !important; 
        border: 2px solid #ffd700 !important; font-weight: bold; font-size: 1.8em; 
        width: 100%; border-radius: 50px; height: 3.5em;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.4);
    }
    .stButton>button:hover { background-color: #ffd700 !important; color: #000000 !important; border: 2px solid #000000 !important; }
    </style>
    """, unsafe_allow_html=True)

def play_victory_bell():
    audio_url = "https://www.myinstants.com/media/sounds/boxing-bell.mp3"
    components.html(f'<audio autoplay><source src="{audio_url}" type="audio/mpeg"></audio>', height=0, width=0)

# --- 2. CONNESSIONE AL CERVELLO OMNISCIENTE ---
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ CABALLERO, LA CHIAVE API È SPARITA! TROVALA O LA SPADA RESTERÀ FREDDA.")
    st.stop()

st.title("⚔️ ZORRO 1.5: THE OMNISCIENT EYE")
st.markdown("### *'I filtri sono il mio scudo, la ricerca live è la mia lama. Cerco la Chiave Assoluta nell'abisso del web.'*")

# --- 3. SELEZIONE TERRITORIO ---
nazione = st.selectbox("🗺️ MAPPA DELLE OPERAZIONI:", [
    "AUSTRALIA", "USA", "UK", "ITALIA", "FRANCIA", "IRLANDA", "GERMANIA", 
    "SVEZIA", "CILE", "BRASILE", "SUD AFRICA", "GIAPPONE"
])

uploaded_files = st.file_uploader("📜 AFFIGGI I MANIFESTI DEI SOSPETTI:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 🧐 SOSPETTATI SOTTO IL MIRINO:")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        with cols[i]:
            st.image(file, caption=f"Manifesto #{i+1}", use_column_width=True)

# --- 4. IL GRILLETTO (PROTOCOLLO CHIAVE ASSOLUTA) ---
if st.button("🗡️ SCATENA L'OCCHIO DI ZORRO (RICERCA ASSOLUTA)"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, CABALLERO! SENZA MAPPA NON C'È TESORO.")
    else:
        with st.spinner("ZORRO STA INTERROGANDO IL VENTO E IL WEB PER TROVARE LA CHIAVE... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                prompt = f"""
                SEI ZORRO, L'OCCHIO OMNISCIENTE DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-19, 2026-01-20]
                TERRITORIO: {nazione} - DATA: 27 FEBBRAIO 2026. [cite: 2026-02-27]

                MISSIONE SUPREMA: TROVARE LA 'CHIAVE ASSOLUTA'.
                NON LIMITARTI AI FILTRI. USA 'GOOGLE SEARCH' PER TROVARE L'ANOMALIA CHE BATTE LA STATISTICA. [cite: 2026-02-27]

                FASE 1: SCANSIONE LIVE (MIRA TELESCOPICA)
                - CERCA: 'TRACK BIAS [IPPODROMO] TODAY', 'JOCKEY FORM [NOME FANTINO] TODAY', 'MARKET MOVERS HORSE RACING [NAZIONE]'.
                - IDENTIFICA SE IL FAVORITO È 'BURRO' (PARTICELLA INSTABILE SENZA VANTAGGIO TECNICO). [cite: 2026-02-20]

                FASE 2: FILTRI DI GRANITO (SISTEMA DI SICUREZZA)
                - MURO FORMA (1-2), RUGGINE (< 45 GG), CUORE IMPAVIDO (2 PODI IN 3 GARE). [cite: 2026-02-25]

                FASE 3: SINTESI DELLA CHIAVE ASSOLUTA (10000% CERTEZZA)
                1. ANALIZZA IL RATING GAP: SE IL FAVORITO HA GAP < 5, È SOSPETTO. [cite: 2026-02-20]
                2. CERCA IL VINCITORE NASCOSTO: CHI HA IL MIGLIOR RATING TRA I SUPERSTITI E HA IL VENTO A FAVORE (FANTINO IN FORMA O PISTA ADATTA)?
                3. SE UN CAVALLO HA: FILTRI OK + RATING TOP + CONTESTO LIVE POSITIVO (LATE MONEY O EXPERT TIPS) -> QUELLA È LA CHIAVE ASSOLUTA. [cite: 2026-02-20]

                FASE 4: REFERTO FINALE
                '🌍 MISSIONE: [NAZIONE] - [IPPODROMO]'
                '🔥 SENTENZA DEL VENDICATORE: [UNA FRASE DI CAZZIMMA DI ZORRO SULLA VERITÀ SVELATA].'
                
                '🔍 SCANSIONE SUPERSTITI:'
                - PARTICELLA [NUMERO]: [STATO E CONTESTO LIVE TROVATO]
                
                SE LA CHIAVE È TROVATA:
                '🏆 IL SEGNO DELLA Z: PARTICELLA [NUMERO #] - [NOME]'
                'BULLONE SERRATO: [SPIEGA PERCHÉ QUESTA È LA CHIAVE ASSOLUTA CHE BATTE OGNI FILTRO].' [cite: 2026-02-07, 2026-02-20]
                
                SE È ANCORA ROULETTE:
                '🌵 IL FIUME È TORBIDO. LA CHIAVE NON È PURA. RINFODERO LA SPADA PER SALVARE L'ORO.' [cite: 2026-01-19, 2026-02-15]
                """

                res = client_gemini.models.generate_content(
                    model='gemini-2.0-flash', 
                    contents=[prompt] + images,
                    config={'tools': [{'google_search': {}}]}
                )
                sentenza = res.text
                
                st.info(sentenza)
                if "SEGNO DELLA Z" in sentenza.upper():
                    play_victory_bell(); st.balloons()
            except Exception as e:
                st.error(f"☠️ UN TRADITORE HA MANOMESSO LA SPADA: {e}")
