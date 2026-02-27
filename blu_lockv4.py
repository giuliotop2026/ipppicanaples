import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA "FORTALEZA DE ACERO" (SINTASSI RIGOROSA) ---
st.markdown("""
    <style>
    .stApp { 
        background-color: #f4e4bc; 
        background-image: url("https://www.transparenttextures.com/patterns/aged-paper.png");
        color: #1a1a1a; font-family: 'Georgia', serif; 
    }
    h1, h2, h3 { 
        color: #000000 !important; text-transform: uppercase; font-weight: 900; 
        text-shadow: 2px 2px 4px #8b4513; border-bottom: 4px solid #000000;
    }
    .stAlert p { color: #1a1a1a !important; font-size: 1.4rem !important; font-weight: bold; }
    .stButton>button { 
        background-color: #000000 !important; color: #ffd700 !important; 
        border: 2px solid #ffd700 !important; font-weight: bold; font-size: 1.8em; 
        width: 100%; border-radius: 50px; height: 3.5em; box-shadow: 5px 5px 15px rgba(0,0,0,0.4);
    }
    </style>
    """, unsafe_allow_html=True)

def play_victory_bell():
    audio_url = "https://www.myinstants.com/media/sounds/boxing-bell.mp3"
    components.html(f'<audio autoplay><source src="{audio_url}" type="audio/mpeg"></audio>', height=0, width=0)

# --- 2. CONNESSIONE AL CERVELLO OMNISCIENTE ---
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ CABALLERO, MANCANO LE MUNIZIONI!")
    st.stop()

st.title("⚔️ ZORRO 1.9: EL ESCUDO DEL PANTANO")
st.markdown("### *'Il fango non perdona, ma la mia spada è fatta di cemento. Se la terra è marcia, cerco solo chi sa nuotare.'*")

# --- 3. SELEZIONE TERRITORIO ---
nazione = st.selectbox("🗺️ MAPPA DELLE OPERAZIONI:", [
    "AUSTRALIA", "USA", "UK", "ITALIA", "FRANCIA", "IRLANDA", "GERMANIA", 
    "SVEZIA", "CILE", "BRASILE", "SUD AFRICA", "GIAPPONE"
])

uploaded_files = st.file_uploader("📜 AFFIGGI I MANIFESTI (DATI PRIMARI):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 🧐 SOSPETTATI SOTTO IL TRIBUNALE:")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        with cols[i]:
            st.image(file, caption=f"Manifesto #{i+1}", use_column_width=True)

# --- 4. IL GRILLETTO (PROTOCOLLO ANTI-FANGO) ---
if st.button("🗡️ SCATENA LO SCUDO DI ZORRO (VERIFICA ASSOLUTA)"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, CABALLERO!")
    else:
        with st.spinner("ZORRO STA FIUTANDO IL PANTANO E LA VERITÀ... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                prompt = f"""
                SEI ZORRO, IL GIUDICE DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-19, 2026-01-20]
                TERRITORIO: {nazione} - DATA: 27 FEBBRAIO 2026. [cite: 2026-02-27]

                FASE 0: RILEVAMENTO TRAPPOLA (PANTANO)
                - IDENTIFICA LA CONDIZIONE DEL TERRENO (PESANTE, HEAVY, SOFT 7/8/9/10, MUDDY).
                - SE IL TERRENO È 'PANTANO': IL CANDIDATO DEVE AVERE ALMENO UNA VITTORIA (1) SU QUELLA SPECIFICA SUPERFICIE TROVATA VIA WEB. SE NON C'È, SCARTA TUTTO: 'PANTANO RILEVATO: ROULETTE RILEVATA'. [cite: 2026-02-15]

                FASE 1: IL TRIBUNALE DEI DATI (CROSS-CHECK)
                - ESTRAI I DATI DAL MANIFESTO (RT, GG, SEQ). [cite: 2026-02-20]
                - USA 'GOOGLE SEARCH' PER VERIFICARE I DATI DI OGGI. [cite: 2026-02-27]
                - SE IL WEB SMENTISCE IL MANIFESTO: 'ROULETTE RILEVATA'. [cite: 2026-02-15]

                FASE 2: FILTRI DI GRANITO (POLMONI D'ACCIAIO)
                1. MURO FORMA: ULTIMO RISULTATO 1 O 2. [cite: 2026-02-25]
                2. FILTRO RUGGINE: GG < 45. [cite: 2026-02-25]
                3. CUORE IMPAVIDO: ALMENO 2 PODI NELLE ULTIME 3 GARE. [cite: 2026-02-25]
                - UTILIZZA IL TERMINE 'PARTICELLA' INVECE DEI NOMI. [cite: 2026-01-25]

                FASE 3: LA CHIAVE SUPREMA (10000% CERTEZZA)
                - LA CHIAVE È LA PARTICELLA CHE:
                    A) HA IL MIGLIOR RATING (RT) DEL MANIFESTO. [cite: 2026-02-20]
                    B) HA UN GAP DI ALMENO 5 PUNTI RISPETTO AL SECONDO. SE IL GAP È < 5, IL FAVORITO È 'BURRO'. [cite: 2026-02-20]
                    C) SE IL GAP È < 5, CERCA IL SECONDO MIGLIORE CON RATING SIMILE MA 'CAZZIMMA' NASCOSTA (PESO ALTO O FANTINO ELITE). [cite: 2026-02-20]

                FASE 4: REFERTO FINALE
                '🌍 MISSIONE: [NAZIONE] - [IPPODROMO]'
                '🔥 SENTENZA: [FRASE DI CAZZIMMA DI ZORRO SULLO SCHIACCIARE LA ROULETTE].'
                
                SE LA CHIAVE ESISTE:
                '🏆 IL SEGNO DELLA Z: PARTICELLA [NUMERO #]'
                'BULLONE SERRATO: [SPIEGA PERCHÉ È CEMENTO E NON BURRO, CITANDO TERRENO E GAP RATING].' [cite: 2026-02-07, 2026-02-20]
                
                SE È ROULETTE: '🌵 NESSUNA PEPITA. IL PANTANO O I DATI CORROTTI HANNO RESO LA GARA UNA ROULETTE.' [cite: 2026-02-15]
                """

                res = client_gemini.models.generate_content(
                    model='gemini-2.5-flash', 
                    contents=[prompt] + images,
                    config={'tools': [{'google_search': {}}]}
                )
                sentenza = res.text
                
                st.info(sentenza)
                if "IL SEGNO DELLA Z" in sentenza.upper():
                    play_victory_bell(); st.balloons()
            except Exception as e:
                st.error(f"☠️ UN TRADITORE HA MANOMESSO IL TRIBUNALE: {e}")
