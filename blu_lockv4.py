import streamlit as st
from google import genai
from PIL import Image
import streamlit.components.v1 as components

# --- 1. GRAFICA WESTERN CHIARA (MASSIMA LEGGIBILITÀ) ---
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

# --- 3. CONNESSIONE A GEMINI ---
try:
    client_gemini = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("☠️ EHI STRANIERO, MANCANO LE MUNIZIONI (GEMINI_API_KEY)!")
    st.stop()

st.title("🤠 SALOON 'EL GRANITO'")
st.markdown("### *'Tutti i filtri attivi: Nastri, Maiden e Polmoni d'Acciaio.'*")

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

# --- 5. IL GRILLETTO (PROTOCOLLO PERFETTO 15.15) ---
if st.button("🐎 SCATENA IL DUELLO (ANALIZZA)"):
    if not uploaded_files:
        st.warning("EHI COMPADRE, CARICA I MANIFESTI PRIMA DI SPARARE!")
    else:
        with st.spinner("LO SCERIFFO GEMINI APPLICA TUTTE LE LEGGI... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                # PROMPT ASSOLUTO: TUTTI I FILTRI DEL VECCHIO CODICE
                prompt = f"""
                SEI LO SCERIFFO DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO.
                TERRITORIO: {nazione}

                FASE 1: IDENTIFICAZIONE BERSAGLI E TIPO DI CORSA
                Analizza l'immagine e capisci se la corsa è MAIDEN/DEBUTTANTI, a NASTRI (presenza di metri come 0m, 20m) o PIANO/NORMALE.
                Per ogni cavallo estrai: Numero, Nome, RT (o Rec), GG, SEQ (Ultimi Arrivi - il primo a sinistra è l'ultimo risultato), Nastro (se applicabile).
                Se un dato è mancante, consideralo 'N/D' e il cavallo viene automaticamente SCARTATO.

                FASE 2: LE LEGGI DELLA FRONTIERA (GRANITO 3.0)
                
                REGOLE PER CORSE NORMALI O A NASTRI:
                1. MURO FORMA: SEQ deve iniziare con 1 o 2. [cite: 2026-02-25]
                2. FILTRO RUGGINE: GG < 45. [cite: 2026-02-25]
                3. BIAS NASTRI: Se la corsa è a nastri, dai priorità assoluta alla "lepre" (0m) se ha passato i filtri 1 e 2.
                4. POLMONI D'ACCIAIO: Cerca il secondo migliore per densità tecnica (RT) ignorando le quote. Il valore RT DEVE essere dominante. [cite: 2026-02-20]

                PROTOCOLLO SPECIALE MAIDEN / DEBUTTANTI:
                1. MURO FORMA: Accetta SOLO '1'. Il '2' è instabile.
                2. FILTRO RUGGINE: Accetta SOLO GG < 15.
                3. GAP RT: L'RT deve essere almeno 5 punti superiore al secondo.

                FORMATO OUTPUT RICHIESTO (SII SPIETATO E BREVE):
                
                '🔍 SCANSIONE SUPERSTITI:'
                - [NOME CAVALLO]: PASSATO (TIPO CORSA: [Maiden/Nastri/Normale], GG [X], SEQ [Y], RT [Z], NASTRO [Metri se applicabile])
                (Elenca SOLO chi supera tutti i filtri. È OBBLIGATORIO indicare l'RT).

                SE C'È UN SUPERSTITE CON VERI POLMONI D'ACCIAIO:
                '💰 TAGLIA RISCOSSA: PISTOLERO [NUMERO] - [NOME]'
                'BULLONE SERRATO: [Spiega in una riga perché il suo RT/Densità e i filtri lo rendono il Sacro Graal].'
                
                SE NESSUNO PASSA I FILTRI O L'RT È TROPPO DEBOLE:
                '🌵 NESSUNA PEPITA D'ORO IN QUESTO FIUME. NESSUNO HA I REQUISITI DI CEMENTO O I POLMONI D'ACCIAIO.'
                """

                res = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt] + images)
                sentenza = res.text
                
                st.info(sentenza)
                
                if "TAGLIA" in sentenza.upper() and "NESSUNA" not in sentenza.upper():
                    play_victory_sound(); st.balloons()
            except Exception as e:
                st.error(f"☠️ SERPENTE NELLO STIVALE (ERRORE): {e}")
