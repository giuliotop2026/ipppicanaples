import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA WESTERN SALOON (LIGHT THEME) ---
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
        box-shadow: 4px 4px 10px rgba(0,0,0,0.3);
    }
    .stButton>button:hover { background-color: #ffd700 !important; color: #0e2a1d !important; }
    </style>
    """, unsafe_allow_html=True)

def play_victory_bell():
    audio_url = "https://www.myinstants.com/media/sounds/boxing-bell.mp3"
    components.html(f'<audio autoplay><source src="{audio_url}" type="audio/mpeg"></audio>', height=0, width=0)

# --- 2. CONNESSIONE AL CERVELLO OMNISCIENTE ---
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ EHI STRANIERO, MANCANO LE MUNIZIONI (GEMINI_API_KEY)!")
    st.stop()

st.title("🤠 SNIPER 106.0: THE FAVORITE'S LAW")
st.markdown("### *'USA Focus: Favorito Tecnico. Zero Miracoli. Perfezione Blue Lock.'*")

# --- 3. SELEZIONE TERRITORIO (ARSENALE COMPLETO) ---
# Abbiamo ripristinato Germania, Brasile, Giappone, Cile e Svezia [cite: 2026-02-26]
nazione = st.selectbox("🗺️ TERRITORIO DI CACCIA:", [
    "UK", "USA", "ITALIA", "FRANCIA", "IRLANDA", "GERMANIA", 
    "SVEZIA", "CILE", "BRASILE", "SUD AFRICA", "AUSTRALIA", "GIAPPONE"
])

uploaded_files = st.file_uploader("📜 AFFIGGI I MANIFESTI (STATISTICHE):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 🧐 SOSPETTATI IN BACHECA:")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        with cols[i]:
            st.image(file, caption=f"Manifesto #{i+1}", use_column_width=True)

# --- 4. IL GRILLETTO (PROTOCOLLO 106.0 - USA BLINDATO) ---
if st.button("🐎 SCATENA IL DUELLO (ANALISI TOTALE)"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, COMANDANTE!")
    else:
        with st.spinner("LO SCERIFFO STA CERCANDO IL FAVORITO CON I POLMONI D'ACCIAIO... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                prompt = f"""
                SEI L'ARCHITETTO TATTICO DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-19, 2026-01-20]
                TERRITORIO: {nazione}

                FASE 1: ESTRAZIONE CINETICA (VISION)
                - Identifica l'IPPODROMO, la DISTANZA, la TIPOLOGIA DI GARA e il NUMERO TOTALE DI PARTENTI.
                - Estrai per ogni riga: Numero, Nome, RT/Rec, GG, SEQ, Quota.
                - IDENTIFICA IL FAVORITO (CAVALLO CON LA QUOTA PIÙ BASSA). [cite: 2026-02-26]
                - REGOLA LETTURA PIATTAFORMA: Testo (es. 8-8-7-2-2) -> l'ultimo è A DESTRA. Quadrati colorati -> l'ultimo è IL PRIMO A SINISTRA. Applica SEMPRE.

                FASE 2: APPLICAZIONE FILTRI (IL PROTOCOLLO DEFINITIVO 106.0)
                1. MURO FORMA: L'ultimo risultato valido deve essere 1 o 2. [cite: 2026-02-25]
                2. CRISTALLO 2.1 (ANTI-SQUALIFICA): Scarta SOLO se le squalifiche (RP, RI, DAI, FE, CD) sono nelle DUE gare più recenti.
                3. FILTRO RUGGINE: GG < 45. [cite: 2026-02-25]
                4. CUORE IMPAVIDO: Ultime 3 gare: ALMENO DUE piazzamenti a podio (1, 2 o 3).
                
                PROTOCOLLI SPECIALI (PRIORITÀ ASSOLUTA):
                5. LA LEGGE DEL FAVORITO (SOLO IN TERRITORIO "USA"): 
                   - IL CANDIDATO DEVE ESSERE IL FAVORITO (QUOTA PIÙ BASSA) O AVERE UNA QUOTA MOLTO VICINA AD ESSO (MAX +2.00 DI SCARTO).
                   - SCARTA CATEGORICAMENTE OGNI CAVALLO CON QUOTA > 8.00, ANCHE SE HA PARAMETRI PERFETTI. [cite: 2026-02-26]
                   - IL SACRO GRAAL USA È L'UNIONE TRA IL FAVORITO DEL MERCATO E LA MIGLIORE DENSITÀ TECNICA (RT/REC). SE IL FAVORITO HA UN RT DEBOLE RISPETTO AL GRUPPO, SCARTA TUTTO. [cite: 2026-02-20, 2026-02-26]
                6. ECCEZIONE MOTORE CIECO USA: SE RT È N/A, IL FAVORITO PASSA SOLO SE HA GG < 45 E ULTIME DUE GARE ENTRAMBE A PODIO (ES. 1,1 O 1,2 O 2,1 O 2,2). [cite: 2026-02-20]
                7. PATCH ANTI-MAIDEN: SE È "MAIDEN", ACCETTA SOLO SEQ RECENTE "1". GG < 15. GAP RT >= 5. [cite: 2026-02-25]

                FASE 3: REFERTO FINALE
                '🌍 BERSAGLIO: [NAZIONE] - [IPPODROMO] - DISTANZA: [DISTANZA]'
                
                '🔍 SCANSIONE SUPERSTITI:'
                - PARTICELLA [NUMERO]: PASSATO (GG [X], SEQ [Y], RT/REC [Z], QUOTA [Q])
                
                SE C'È UN VERO SACRO GRAAL (FAVORITO + TECNICO):
                '💰 TAGLIA RISCOSSA: PISTOLERO [NUMERO #] - [NOME]'
                'BULLONE SERRATO: [Conferma che è il favorito con i polmoni d'acciaio].'
                
                SE NON C'È PERFEZIONE: 
                '🌵 NESSUNA PEPITA IN QUESTO FIUME. IL FAVORITO È DEBOLE O IL TECNICO HA QUOTA TROPPO ALTA.'
                """

                res = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt] + images)
                sentenza = res.text
                
                st.info(sentenza)
                if "TAGLIA RISCOSSA" in sentenza.upper():
                    play_victory_bell(); st.balloons()
            except Exception as e:
                st.error(f"☠️ SERPENTE NELLO STIVALE: {e}")
                
