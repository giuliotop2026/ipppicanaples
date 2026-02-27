import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA "HACIENDA DE LA VEGA" ---
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
    .stAlert p { color: #1a1a1a !important; font-size: 1.4rem !important; font-weight: bold; font-style: italic; }
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

# --- 2. CONNESSIONE AL CERVELLO DEL VENDICATORE CON MOTORE DI RICERCA ---
try:
    # IL CERVELLO ORA HA LA "MIRA TELESCOPICA" (SEARCH TOOL)
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ CABALLERO, LA SERRATURA È BLOCCATA! CONTROLLA LA GEMINI_API_KEY.")
    st.stop()

st.title("⚔️ ZORRO: THE SEARCHING BLADE")
st.markdown("### *'La mia spada colpisce ciò che l'occhio non vede. Fiuto il vento e trovo la verità tra le ombre del web.'*")

# --- 3. SELEZIONE TERRITORIO ---
nazione = st.selectbox("🗺️ MAPPA DELLE MISSIONI:", [
    "AUSTRALIA", "UK", "USA", "ITALIA", "FRANCIA", "IRLANDA", "GERMANIA", 
    "SVEZIA", "CILE", "BRASILE", "SUD AFRICA", "GIAPPONE"
])

uploaded_files = st.file_uploader("📜 AFFIGGI I MANIFESTI DEI RICERCATI:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 🧐 SOSPETTATI SOTTO IL MANTELLO:")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        with cols[i]:
            st.image(file, caption=f"Manifesto #{i+1}", use_column_width=True)

# --- 4. IL GRILLETTO (PROTOCOLLO ZORRO 1.2 CON WEB SEARCH) ---
if st.button("🗡️ INCIDI LA 'Z' (ANALISI TOTALE CON RICERCA)"):
    if not uploaded_files:
        st.warning("UN VERO CAVALIERE NON SCENDE IN CAMPO SENZA MAPPA! CARICA I FILE.")
    else:
        with st.spinner("ZORRO STA SCANSIONANDO IL WEB E LE OMBRE... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                prompt = f"""
                SEI ZORRO, IL DIFENSORE DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-19, 2026-01-20]
                TERRITORIO ATTUALE: {nazione} - DATA ODIERNA: 27 FEBBRAIO 2026. [cite: 2026-02-27]

                FASE 1: ESTRAZIONE E RICERCA (MIRA TELESCOPICA)
                - IDENTIFICA L'IPPODROMO E IL NUMERO DI GARA DALLE IMMAGINI.
                - SE I DATI (RT/RATING, GG, SEQ) SONO MANCANTI O VUOTI (TIPICO IN AUSTRALIA/USA): 
                  USA OBBLIGATORIAMENTE LO STRUMENTO 'GOOGLE SEARCH' PER TROVARE LE STATISTICHE DI QUELLA SPECIFICA GARA E DEI CAVALLI PARTENTI.
                  CERCA: 'HORSE RACING RESULTS [IPPODROMO] [DATA]', 'RATING CAVALLO [NOME]', 'LAST RUNS [NOME CAVALLO]'. [cite: 2026-02-27]

                FASE 2: FILTRI DI GRANITO (ZERO ERRORI)
                1. MURO FORMA: L'ULTIMO RISULTATO DEVE ESSERE 1 O 2. SE IL WEB DICE CHE HA PERSO L'ULTIMA, SCARTALO. [cite: 2026-02-25]
                2. FILTRO RUGGINE: GG < 45. SE IL WEB DICE CHE NON CORRE DA MESI, SCARTALO. [cite: 2026-02-25]
                3. CUORE IMPAVIDO: ALMENO DUE PODI (1, 2, 3) NELLE ULTIME 3 GARE. [cite: 2026-02-25]
                
                FASE 3: LEGGI SUPREME (POLMONI D'ACCIAIO)
                4. LA CHIAVE DEL VINCITORE: CERCA IL SECONDO MIGLIORE PER DENSITÀ TECNICA (RATING) CHE SCHIACCIA IL FAVORITO DI CARTA INSTABILE. [cite: 2026-02-20]
                5. USA FOCUS: SE TERRITORIO USA, IL CANDIDATO DEVE ESSERE IL FAVORITO O MOLTO VICINO (SCARTO MAX +2.00) E QUOTA < 8.00. [cite: 2026-02-26]

                FASE 4: REFERTO FINALE DEL VENDICATORE
                '🌍 MISSIONE: [NAZIONE] - [IPPODROMO]'
                '🔥 MOTIVAZIONE: [UNA FRASE DI CAZZIMMA DI ZORRO SUL TROVARE LA VERITÀ NASCOSTA].'
                
                '🔍 SCANSIONE SUPERSTITI (DATI TROVATI SUL WEB):'
                - PARTICELLA [NUMERO]: PASSATO (GG [X], SEQ [Y], RATING [Z], QUOTA [Q])
                
                SE TROVI IL SACRO GRAAL (10000% CERTEZZA):
                '🏆 IL SEGNO DELLA Z: PARTICELLA [NUMERO #] - [NOME]'
                'BULLONE SERRATO: [SPIEGA COSA HA TROVATO IL WEB SUI POLMONI D'ACCIAIO DI QUESTO CAVALLO].' [cite: 2026-02-07, 2026-02-20]
                
                SE NON C'È PERFEZIONE: '🌵 NESSUNA PEPITA NEL DESERTO. NEMMENO IL VENTO PORTA NOTIZIE DI CAMPIONI OGGI.' [cite: 2026-02-15]
                """

                # ESECUZIONE CON STRUMENTO DI RICERCA ATTIVATO
                res = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt] + images,
                    config={'tools': [{'google_search': {}}]}
                )
                sentenza = res.text
                
                st.info(sentenza)
                if "TAGLIA RISCOSSA" in sentenza.upper() or "SEGNO DELLA Z" in sentenza.upper():
                    play_victory_bell(); st.balloons()
            except Exception as e:
                st.error(f"☠️ UN SERPENTE HA MORSO IL CAVALLO: {e}")
                
