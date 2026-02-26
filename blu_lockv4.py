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

st.title("🤠 SNIPER 105.0: THE BLIND SIGHT")
st.markdown("### *'Mirino Infallibile. Forma Devastante. Zero Allucinazioni.'*")

# --- 3. SELEZIONE TERRITORIO ---
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

# --- 4. IL GRILLETTO (LA FUSIONE TATTICA TOTALE E SPIETATA) ---
if st.button("🐎 SCATENA IL DUELLO (ANALISI TOTALE)"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, COMANDANTE!")
    else:
        with st.spinner("LO SCERIFFO STA CALCOLANDO LE DISTANZE E VERIFICANDO I MOTORI... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                prompt = f"""
                SEI L'ARCHITETTO TATTICO DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-20]
                TERRITORIO: {nazione}

                FASE 1: ESTRAZIONE CINETICA PERFETTA E UNIVERSALE
                - Identifica l'IPPODROMO, la DISTANZA esatta (es. 1600m, 2850m), la TIPOLOGIA DI GARA e il NUMERO TOTALE DI PARTENTI.
                - Estrai per ogni riga: Numero, Nome, RT/Rec, GG, SEQ, Quota e cambi equipaggiamento.
                - DIVIETO DI ALLUCINAZIONE RT: FAI UN DOPPIO CONTROLLO VISIVO. Assicurati di non scambiare l'RT con i Giorni (GG). Se la colonna 'Rt.' o 'Rec' è veramente vuota, SCRIVI "N/A".
                - REGOLA LETTURA PIATTAFORMA: Testo (es. 8-8-7-2-2) -> l'ultimo è A DESTRA. Quadrati colorati -> l'ultimo è IL PRIMO A SINISTRA. Applica SEMPRE.
                - IGNORA LE QUOTE COME INDICATORE DI FORZA. [cite: 2026-02-20]

                FASE 2: APPLICAZIONE FILTRI (IL PROTOCOLLO DEFINITIVO)
                1. MURO FORMA: L'ultimo risultato valido deve essere 1 o 2.
                2. CRISTALLO 2.1 (ANTI-SQUALIFICA): Scarta SOLO se le squalifiche (RP, RI, DAI, FE) sono nelle DUE gare più recenti.
                3. FILTRO RUGGINE: GG < 45.
                4. CUORE IMPAVIDO: Ultime 3 gare: ALMENO DUE piazzamenti a podio (1, 2 o 3).
                
                PROTOCOLLI TECNICI E CHILOMETRICI (PRIORITÀ ASSOLUTA):
                5. POLMONI D'ACCIAIO E "MOTORE CIECO" (USO ESTREMO E SPIETATO):
                   - Cerca chi ha il miglior valore tecnico (RT/Rec). Se l'RT è debole e non da vertice, SCARTALO SENZA PIETÀ.
                   - ECCEZIONE MOTORE CIECO: Applica questa regola SOLO SE la casella RT/Rec è INEQUIVOCABILMENTE vuota o "N/A". SE è davvero vuota, il cavallo passa SOLO SE ha una FORMA DEVASTANTE: GG < 20 E le sue ultime DUE gare sono entrambe a podio (es. SEQ che inizia con 1,1 o 1,2 o 2,1). Se ha un solo '1' e poi numeri scarsi, o se GG è >= 20, SCARTALO, è un bluff!
                6. LEGGE DEL CAMPO RIDOTTO E CAZZIMMA (PARTENTI <= 7): Tolleranza zero. Il superstite DEVE avere RT/Rec dominante (gap >= 5) OPPURE un "Cambio Tattico". Se ha attivato correttamente l'ECCEZIONE MOTORE CIECO estrema, supera questo vincolo di diritto.
                7. LEGGE DELLA BARRICATA CON RADAR CHILOMETRICO (CRITICO): 
                   - SE LA DISTANZA È <= 2100m (Gara Sprint): Scarta i numeri > 7 a meno che il loro REC non sia migliore di almeno 0.8s sulla prima fila.
                   - SE LA DISTANZA È > 2100m (Gara Maratona, es. 2850m): LA LEGGE DELLA BARRICATA È COMPLETAMENTE DISATTIVATA! Non scartare i numeri alti, valuta tutti i cavalli basandoti solo sulla forma, perché nella maratona il traffico iniziale non è fatale.
                8. PATCH ANTI-MAIDEN: SE È "MAIDEN", ACCETTA SOLO SEQ RECENTE "1". GG < 15. GAP RT >= 5.

                FASE 3: REFERTO FINALE
                '🌍 BERSAGLIO: [NAZIONE] - [IPPODROMO] - DISTANZA: [DISTANZA] - PARTENTI: [NUMERO]'
                
                '🔍 SCANSIONE SUPERSTITI:'
                - PARTICELLA [NUMERO]: PASSATO (GG [X], SEQ [Y], RT/REC [Z], [NOTE SU SALVACONDOTTO O BARRICATA])
                
                SE C'È UN VERO SACRO GRAAL TATTICO:
                '💰 TAGLIA RISCOSSA: PISTOLERO [NUMERO #] - [NOME]'
                'BULLONE SERRATO: [Motivazione].'
                
                SE NON C'È PERFEZIONE: 
                '🌵 NESSUNA PEPITA IN QUESTO FIUME. I SUPERSTITI MANCANO DI POLMONI D'ACCIAIO O FORMA DEVASTANTE.'
                """

                res = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt] + images)
                sentenza = res.text
                
                st.info(sentenza)
                if "TAGLIA RISCOSSA" in sentenza.upper():
                    play_victory_bell(); st.balloons()
            except Exception as e:
                st.error(f"☠️ SERPENTE NELLO STIVALE: {e}")
