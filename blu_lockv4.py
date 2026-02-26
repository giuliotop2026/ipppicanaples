import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA WESTERN CHIARA (MASSIMA CONCENTRAZIONE) ---
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
    .stAlert p { color: #3d2b1f !important; font-size: 1.2rem !important; font-weight: bold; }
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

# --- 3. CONNESSIONE A GEMINI (MOTORE BLINDATO) ---
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ EHI STRANIERO, MANCANO LE MUNIZIONI (GEMINI_API_KEY) NEI SECRETS!")
    st.stop()

st.title("🤠 SALOON 'EL GRANITO' 48.0")
st.markdown("### *'Gabbia di lettura attiva. Zero errori sulle colonne. Vittoria totale.'*")

# --- 4. BACHECA DEI RICERCATI ---
nazione = st.selectbox("🗺️ TERRITORIO DI FRONTIERA:", [
    "UK", "IRLANDA", "USA", "ITALIA", "FRANCIA", "GERMANIA", 
    "SVEZIA", "CILE", "BRASILE", "SUD AFRICA", "AUSTRALIA", "GIAPPONE"
])

uploaded_files = st.file_uploader("📜 AFFIGGI I MANIFESTI (SCREENSHOT):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.markdown("### 🧐 SOSPETTATI IN BACHECA:")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        with cols[i]:
            st.image(file, caption=f"Manifesto #{i+1}", use_column_width=True)

# --- 5. IL GRILLETTO (PROTOCOLLO INFALLIBILE) ---
if st.button("🐎 SCATENA IL DUELLO (ANALIZZA)"):
    if not uploaded_files:
        st.warning("EHI COMPADRE, CARICA I MANIFESTI PRIMA DI SPARARE!")
    else:
        with st.spinner("LO SCERIFFO GEMINI STA DECIFRANDO LA MATRICE... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                # PROMPT ASSOLUTO: GABBIA DI LETTURA + FILTRI GRANITO 3.0
                prompt = f"""
                SEI LO SCERIFFO DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO.
                TERRITORIO: {nazione}

                FASE 1: GABBIA DI LETTURA (ANTI-ERRORE CRITICO)
                Devi leggere la tabella in modo chirurgico. NON SCAMBIARE LE COLONNE.
                L'ordine delle colonne è solitamente: Numero | Partente | Peso | Rt. | GG | Ultimi Arrivi.
                - PESO: IGNORALO TOTALMENTE. NON È L'RT.
                - RT (Rating/Densità): Estrai QUESTO numero. È fondamentale.
                - GG (Giorni): Estrai il numero esatto dei giorni.
                - SEQ (Ultimi Arrivi): Il primo numero a SINISTRA è l'ultima corsa.
                Se un cavallo ha N/D su GG o RT, viene eliminato istantaneamente.

                FASE 2: LE LEGGI DELLA FRONTIERA (FILTRI)
                
                REGOLE CORSE NORMALI:
                1. MURO FORMA: SEQ deve iniziare SOLO con 1 o 2.
                2. FILTRO RUGGINE: GG DEVE essere INFERIORE a 45.
                3. POLMONI D'ACCIAIO (RT): Tra chi ha superato i filtri, identifica il cavallo con la migliore Densità Tecnica (RT) reale, ignorando le quote.

                PROTOCOLLO SPECIALE MAIDEN / DEBUTTANTI:
                Se leggi 'MAIDEN' o 'DEBUTTANTI':
                1. MURO FORMA: Accetta SOLO '1'. (Scarta il '2').
                2. FILTRO RUGGINE: Accetta SOLO GG < 15.
                3. GAP RT: L'RT deve essere almeno 5 punti superiore agli altri.

                FASE 3: REFERTO FINALE (FORMATO OBBLIGATORIO)
                
                '🔍 SCANSIONE SUPERSTITI:'
                - [NOME CAVALLO]: (GG: [Valore], SEQ: [Valore], RT: [Valore])
                (Elenca QUI SOLO chi ha passato i filtri MURO FORMA e RUGGINE. Se non passano, non elencarli).

                SE C'È UN VINCITORE CON POLMONI D'ACCIAIO:
                '💰 TAGLIA RISCOSSA: PISTOLERO [NUMERO] - [NOME]'
                'BULLONE SERRATO: [Spiega in una riga perché il suo RT e la sua forma lo rendono il vero vincitore].'
                
                SE NESSUNO PASSA O SE MANCANO I REQUISITI TECNICI:
                '🌵 NESSUNA PEPITA D'ORO IN QUESTO FIUME. I POLMONI D'ACCIAIO MANCANO O LA RUGGINE È TROPPA.'
                """

                res = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt] + images)
                sentenza = res.text
                
                st.info(sentenza)
                
                if "TAGLIA" in sentenza.upper() and "NESSUNA" not in sentenza.upper():
                    play_victory_sound(); st.balloons()
            except Exception as e:
                st.error(f"☠️ SERPENTE NELLO STIVALE (ERRORE): {e}")
