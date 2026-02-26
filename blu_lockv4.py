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

st.title("🤠 SNIPER 102.0: TACTICAL SHERIFF")
st.markdown("### *'Legge Barricata. Cuore Impavido. Zero Errori.'*")

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

# --- 4. IL GRILLETTO (LA FUSIONE TATTICA TOTALE) ---
if st.button("🐎 SCATENA IL DUELLO (ANALISI TOTALE)"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, COMANDANTE!")
    else:
        with st.spinner("LO SCERIFFO STA INCROCIANDO MATEMATICA E TATTICA DI GARA... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                # IL PROMPT TATTICO SUPREMO [cite: 2026-01-20, 2026-02-25]
                prompt = f"""
                SEI L'ARCHITETTO TATTICO DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO. [cite: 2026-01-19, 2026-01-20]
                TERRITORIO: {nazione}

                FASE 1: ESTRAZIONE CINETICA
                - Identifica l'IPPODROMO, la DISTANZA e la TIPOLOGIA DI GARA (Maiden, Nastri, Handicap, Trotto, Galoppo).
                - Estrai per ogni riga: Numero, Nome, NASTRO/METRI (se presente), RT/Rec, GG, SEQ, Quota.
                - REGOLA REC TROTTO (CRITICA): Nel TROTTO, il valore 'REC' indica i minuti/secondi al km. IL NUMERO PIÙ BASSO È IL MIGLIORE (es. 11.4 batte 12.4).
                - REGOLA SEQ ITALIANA (CRITICA): Nei siti italiani (stringhe di testo es. 2-3-2-9-6), il risultato PIÙ RECENTE è l'ultimo numero a DESTRA. Nelle tabelle a colori, è il primo a SINISTRA.

                FASE 2: APPLICAZIONE FILTRI (IL PROTOCOLLO TATTICO DEFINITIVO)
                1. MURO FORMA: Il risultato PIÙ RECENTE deve essere 1 o 2. [cite: 2026-02-25]
                2. CRISTALLO 2.1 (ANTI-SQUALIFICA): Scarta SOLO se le squalifiche (RP, RI, DAI, FE, CD) sono nelle DUE gare più recenti.
                3. FILTRO RUGGINE: GG < 45. [cite: 2026-02-25]
                4. CUORE IMPAVIDO (CONTINUITÀ REALE): Analizza le 3 gare più recenti della SEQ. Il cavallo DEVE AVERE ALMENO DUE piazzamenti a podio (1, 2 o 3) in quelle 3 gare. Se ha vinto l'ultima ma le due precedenti sono pessime (es. 1-8-9 o 1-RP-0), SCARTALO come "fuoco di paglia". Vogliamo regolarità. [cite: 2026-02-20]
                5. POLMONI D'ACCIAIO & MOTORE CIECO: Identifica il miglior valore tecnico (RT/Rec). Se "N/A" ma ha vinto (SEQ recente = 1) ed è fresco (GG < 45), passa per manifesta forma in pista. Ignora le quote. [cite: 2026-02-20]
                
                PROTOCOLLI SPECIALI (PRIORITÀ ASSOLUTA):
                6. LEGGE DELLA BARRICATA (TROTTO - SECONDA FILA): Nel Trotto (specie su distanze brevi come 1600m), i Numeri MAGGIORI DI 7 (es. 8, 9, 10...) partono in seconda fila, bloccati nel traffico. SCARTA SEMPRE i numeri > 7, A MENO CHE il loro REC non sia migliore di ALMENO 0.8 SECONDI rispetto al miglior REC della prima fila (Numeri 1-7).
                7. PATCH ANTI-MAIDEN: SE È "MAIDEN", ACCETTA SOLO SEQ RECENTE "1". ACCETTA SOLO GG < 15. GAP RT >= 5 SUL SECONDO. [cite: 2026-02-25]
                8. BIAS NASTRI (LEPRE): Nelle corse a nastri, priorità assoluta alla lepre (0m) se passa i filtri.
                9. BIAS NAPOLI: Se l'ippodromo è NAPOLI, tollera un '4' recente per Polmoni d'Acciaio.
                10. SOUTHWELL KEY: Se l'ippodromo è SOUTHWELL, ignora favoriti < 3.00.

                FASE 3: REFERTO FINALE
                '🌍 BERSAGLIO: [NAZIONE] - [IPPODROMO] - [TIPO GARA]'
                
                '🔍 SCANSIONE SUPERSTITI:'
                - PARTICELLA [NUMERO]: PASSATO (GG [X], SEQ [Y], RT/REC [Z], [NOTE SU BARRICATA O CUORE IMPAVIDO se rilevanti])
                (Elenca solo i superstiti che passano TUTTE le fasi).

                SE C'È UN VERO SACRO GRAAL TATTICO:
                '💰 TAGLIA RISCOSSA: PISTOLERO [NUMERO #] - [NOME]'
                'BULLONE SERRATO: [Motivazione su RT/Rec, Barricata superata o Cuore Impavido dimostrato].'
                
                SE NON C'È PERFEZIONE TATTICA: 
                '🌵 NESSUNA PEPITA IN QUESTO FIUME. I SUPERSTITI SONO BLOCCATI DALLA BARRICATA O MANCANO DI CUORE IMPAVIDO.'
                """

                res = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt] + images)
                sentenza = res.text
                
                st.info(sentenza)
                if "TAGLIA RISCOSSA" in sentenza.upper():
                    play_victory_bell(); st.balloons()
            except Exception as e:
                st.error(f"☠️ SERPENTE NELLO STIVALE: {e}")
