import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA "HACIENDA DE LA VEGA" (LIGHT THEME) ---
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

# --- 2. CONNESSIONE AL CERVELLO DEL VENDICATORE ---
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ CABALLERO, MANCANO LE MUNIZIONI NELLA SERRATURA (GEMINI_API_KEY)!")
    st.stop()

st.title("⚔️ ZORRO: IL VENDICATORE DEL CANTIERE")
st.markdown("### *'Non serve vedere i numeri per sentire il cuore di un campione. Colpisco nell'ombra, lascio il segno dell'oro.'*")

# --- 3. SELEZIONE TERRITORIO (ARSENALE GEOPOLITICO COMPLETO) ---
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

# --- 4. IL GRILLETTO (PROTOCOLLO ZORRO 1.0) ---
if st.button("🗡️ INCIDI LA 'Z' (ANALISI SPIETATA)"):
    if not uploaded_files:
        st.warning("UN VERO CAVALIERE NON SCENDE IN CAMPO SENZA MAPPA! CARICA I FILE.")
    else:
        with st.spinner("ZORRO STA FIUTANDO IL VENTO E LE OMBRE... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                prompt = f"""
                SEI ZORRO, IL DIFENSORE DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-19, 2026-01-20]
                TERRITORIO: {nazione}

                FASE 1: ESTRAZIONE CINETICA (VISION)
                - IDENTIFICA IPPODROMO E DISTANZA.
                - IDENTIFICA IL FAVORITO (QUOTA PIÙ BASSA). [cite: 2026-02-26]

                FASE 2: APPLICAZIONE FILTRI (IL PROTOCOLLO DEL VENDICATORE)
                1. MURO FORMA: L'ULTIMO RISULTATO DEVE ESSERE 1 O 2. [cite: 2026-02-25]
                2. CRISTALLO 2.1: SCARTA SQUALIFICHE (RP, RI, DAI, FE, CD) NELLE ULTIME DUE GARE.
                3. FILTRO RUGGINE: GG < 45. [cite: 2026-02-25]
                4. CUORE IMPAVIDO: ALMENO DUE PODI (1, 2 O 3) NELLE ULTIME 3 GARE.

                FASE 3: LEGGI TERRITORIALI (PRIORITÀ ASSOLUTA)
                5. LA LEGGE DEL FAVORITO (USA): IL CANDIDATO DEVE ESSERE IL FAVORITO (< 8.00) E AVERE LA MIGLIORE DENSITÀ TECNICA (RT). SE IL FAVORITO È SPORCO, SCARTA TUTTO. [cite: 2026-02-26]
                6. LEGGE DELL'OMBRA (SHADOW LAW - SOLO AUSTRALIA): 
                   - SE IL TERRITORIO È "AUSTRALIA" E LE COLONNE TABELLARI SONO VUOTE: 
                     A) IL CANDIDATO DEVE ESSERE IL FAVORITO ASSOLUTO (QUOTA < 3.00).
                     B) IL PESO DEVE ESSERE COMPETITIVO (TECHNICAL DENSITY IMPLICITA).
                     C) SE IL FAVORITO HA QUOTA < 3.00 IN CAMPO RIDOTTO (<= 7), SUPERA DI DIRITTO I FILTRI DI DENSITÀ.
                7. PATCH ANTI-MAIDEN: SEQ 1, GG < 15, GAP RT >= 5. [cite: 2026-02-25]

                FASE 4: REFERTO FINALE DA VENDICATORE
                '🌍 MISSIONE: [NAZIONE] - [IPPODROMO]'
                '🔥 MOTIVAZIONE DA COMBATTIMENTO: [INSERISCI UNA FRASE MOTIVAZIONALE DI ZORRO ADATTA ALLA CORSA].'
                
                '🔍 SCANSIONE SUPERSTITI:'
                - PARTICELLA [NUMERO]: PASSATO (GG [X], SEQ [Y], RT/REC [Z], QUOTA [Q])
                
                SE C'È IL SACRO GRAAL:
                '🏆 IL SEGNO DELLA Z: PARTICELLA [NUMERO #] - [NOME]'
                'BULLONE SERRATO: [SPIEGA PERCHÉ QUESTO CAVALLO HA LA CAZZIMMA PER STRACCIARE TUTTI].'
                
                SE NON C'È PERFEZIONE: 
                '🌵 NESSUNA PEPITA NEL DESERTO. UN CAVALIERE SA QUANDO RINFODERARE LA SPADA.'
                """

                res = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt] + images)
                sentenza = res.text
                
                st.info(sentenza)
                if "SEGNO DELLA Z" in sentenza.upper():
                    play_victory_bell(); st.balloons()
            except Exception as e:
                st.error(f"☠️ UN SERPENTE HA MORSO IL CAVALLO: {e}")
