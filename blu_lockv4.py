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

st.title("🤠 SNIPER 103.0: CAZZIMMA SHERIFF")
st.markdown("### *'Campo Ridotto. Polmoni d'Acciaio. Zero Errori.'*")

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

# --- 4. IL GRILLETTO (LA FUSIONE TATTICA E CAZZIMMA) ---
if st.button("🐎 SCATENA IL DUELLO (ANALISI TOTALE)"):
    if not uploaded_files:
        st.warning("CARICA I MANIFESTI, COMANDANTE!")
    else:
        with st.spinner("LO SCERIFFO CERCA LA CAZZIMMA E I POLMONI D'ACCIAIO... ⏳"):
            try:
                images = [Image.open(f) for f in uploaded_files]

                # IL PROMPT TATTICO SUPREMO 103.0 [cite: 2026-02-18, 2026-02-20]
                prompt = f"""
                SEI L'ARCHITETTO TATTICO DEL 'PROGETTO BLUE LOCK'. SINTASSI: RIGOROSAMENTE IN MAIUSCOLO.
                TERRITORIO: {nazione}

                FASE 1: ESTRAZIONE CINETICA PERFETTA
                - Identifica l'IPPODROMO, la DISTANZA, la TIPOLOGIA DI GARA (Maiden, Nastri, Handicap, Trotto, Galoppo) e il NUMERO TOTALE DI PARTENTI.
                - Estrai per ogni riga: Numero, Nome, NASTRO/METRI (se presente), RT/Rec, GG, SEQ, Quota. ESTRAI ANCHE LE INFORMAZIONI SUI CAMBI EQUIPAGGIAMENTO (es. "paraocchi") DALLA SEZIONE SIGNPOSTS O COMMENTI.
                - LETTURA SEQ (CRITICA): Fai ESTREMA attenzione alla lettura della sequenza. Se c'è scritto "8-8-7-2-2", significa che gli ultimi due risultati sono secondi posti. Non sbagliare l'estrazione del dato più recente!
                - IGNORA LE QUOTE COME INDICATORE DI FORZA. I bookmaker creano favoriti finti che sono particelle instabili. Noi cerchiamo i "Polmoni d'Acciaio" e la "Cazzimma" [cite: 2026-02-18, 2026-02-20].

                FASE 2: APPLICAZIONE FILTRI (IL PROTOCOLLO DEFINITIVO)
                1. MURO FORMA: L'ultimo risultato valido (effettivo) deve essere 1 o 2.
                2. CRISTALLO 2.1 (ANTI-SQUALIFICA): Scarta SOLO se le squalifiche (RP, RI, DAI, FE) sono nelle DUE gare più recenti.
                3. FILTRO RUGGINE: GG < 45.
                4. CUORE IMPAVIDO (CONTINUITÀ REALE): Analizza le ultime 3 gare: DEVE AVERE ALMENO DUE piazzamenti a podio (1, 2 o 3). Nessun fuoco di paglia.
                
                PROTOCOLLI SPECIALI (PRIORITÀ ASSOLUTA):
                5. LEGGE DEL CAMPO RIDOTTO E CAZZIMMA (CRITICA): SE I PARTENTI SONO 7 O MENO (Pagamento Piazzato a 2): La tolleranza è zero. Il superstite DEVE avere un RT/Rec palesemente dominante (Polmoni d'Acciaio) OPPURE avere un "Cambio Tattico / Cazzimma" (es. mette il paraocchi per la prima volta). Se il favorito di quota ha un RT debole, è una trappola: trova il vero mostro nascosto che lo schiaccerà [cite: 2026-02-18, 2026-02-20].
                6. LEGGE DELLA BARRICATA (TROTTO - SECONDA FILA): Scarta i numeri > 7 (seconda fila) a meno che il loro REC non sia migliore di almeno 0.8 secondi rispetto alla prima fila.
                7. PATCH ANTI-MAIDEN: SE È "MAIDEN", ACCETTA SOLO SEQ RECENTE "1". ACCETTA SOLO GG < 15. GAP RT >= 5 SUL SECONDO.
                8. BIAS NASTRI: Nelle corse a nastri, priorità assoluta alla lepre (0m).

                FASE 3: REFERTO FINALE
                '🌍 BERSAGLIO: [NAZIONE] - [IPPODROMO] - [TIPO GARA] - PARTENTI: [NUMERO]'
                
                '🔍 SCANSIONE SUPERSTITI:'
                - PARTICELLA [NUMERO]: PASSATO (GG [X], SEQ [Y], RT/REC [Z], [NOTE SU CAZZIMMA, EQUIPAGGIAMENTO O BARRICATA])
                (Elenca solo i superstiti che passano TUTTE le fasi).

                SE C'È UN VERO SACRO GRAAL TATTICO:
                '💰 TAGLIA RISCOSSA: PISTOLERO [NUMERO #] - [NOME]'
                'BULLONE SERRATO: [Motivazione su Polmoni d'Acciaio (RT dominante), Cazzimma (equipaggiamento), ignorando le quote trappola].'
                
                SE NON C'È PERFEZIONE TATTICA O MANCA LA CAZZIMMA IN CAMPO RIDOTTO: 
                '🌵 NESSUNA PEPITA IN QUESTO FIUME. I SUPERSTITI SONO BLOCCATI DALLA BARRICATA O MANCANO DI POLMONI D'ACCIAIO.'
                """

                res = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt] + images)
                sentenza = res.text
                
                st.info(sentenza)
                if "TAGLIA RISCOSSA" in sentenza.upper():
                    play_victory_bell(); st.balloons()
            except Exception as e:
                st.error(f"☠️ SERPENTE NELLO STIVALE: {e}")
