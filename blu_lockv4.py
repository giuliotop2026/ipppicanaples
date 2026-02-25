import streamlit as st
from google import genai
from openai import OpenAI
from PIL import Image
import streamlit.components.v1 as components
import datetime

# --- GRAFICA DA BUNKER ANTI-ATOMICO (MARMO E ACCIAIO) ---
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(244, 236, 207, 0.90), rgba(244, 236, 207, 0.90)), 
        url('https://images.unsplash.com/photo-1518640467707-6811f4a6ab73?q=80&w=2070&auto=format&fit=crop');
        background-size: cover; background-position: center; background-attachment: fixed;
        color: #3e2723; font-family: 'Georgia', serif;
    }
    h1, h2, h3 { color: #5d4037 !important; text-transform: uppercase; letter-spacing: 2px; }
    .stButton>button { background-color: #3e2723 !important; color: #f4eccf !important; border-radius: 0px; font-weight: bold; width: 100%; height: 4em; border: 4px solid #1b1b1b; }
    .stAlert { background-color: rgba(224, 197, 160, 0.98); border: 3px solid #3e2723; }
    </style>
    """, unsafe_allow_html=True)

def play_ricochet():
    html = '<audio autoplay><source src="https://www.myinstants.com/media/sounds/ricochet-sound.mp3" type="audio/mpeg"></audio>'
    components.html(html, height=0, width=0)

# 2. CASSAFORTE API
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    PPLX_API_KEY = st.secrets["PERPLEXITY_API_KEY"]
except KeyError:
    st.error("☠️ MUNIZIONI MANCANTI NEI SECRETS!")
    st.stop()

client_gemini = genai.Client(api_key=GEMINI_API_KEY)
client_pplx = OpenAI(api_key=PPLX_API_KEY, base_url="https://api.perplexity.ai")

st.set_page_config(page_title="SNIPER 22.0 GRANITO BLINDATO", page_icon="🛡️", layout="wide")

st.title("🛡️ SNIPER 22.0: 'GRANITO BLINDATO' 💎")
st.markdown("### *'La perfezione non è vincere una volta, è non cadere mai nell'abisso.'* 🔫 🥃")

# 3. MATRICE DI PRECISIONE
col1, col2 = st.columns([1, 2])

with col1:
    nazione = st.selectbox("🗺️ TERRITORIO DI CACCIA:", ["ITALIA", "SVEZIA", "USA", "UK", "FRANCIA", "GERMANIA", "AUSTRALIA"])
    ippodromo = st.text_input("🏟️ IPPODROMO / CANTIERE:")
    uploaded_files = st.file_uploader("📜wanted posters (SCREENSHOT):", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

with col2:
    st.subheader("⚙️ PROTOCOLLO GRANITO 3.0 ATTIVO")
    st.write("- Focus: **PIAZZATO BLINDATO** (Place)")
    st.write("- Filtro: **POLMONI D'ACCIAIO** (Regolarità 4/5)")
    st.write("- Freshness: **GG < 30** (Niente Ruggine)")

if st.button("🔥 ESEGUI RETTIFICA FINALE (ZERO ERRORI)"):
    if not uploaded_files or not ippodromo:
        st.warning("EHI SOCIO! CARICA I DATI PER IL SACRO GRAAL.")
    else:
        with st.spinner(f"ANALISI CHIRURGICA DEL MARMO IN CORSO... 🚬"):
            try:
                images_to_process = [Image.open(f) for f in uploaded_files]
                prompt_vision = "ESTRAI TUTTI I DATI: NOME, QUOTA, POSIZIONI RECENTI (ULTIME 5), GG (GIORNI), PESO."
                response_vision = client_gemini.models.generate_content(model='gemini-2.5-flash', contents=[prompt_vision] + images_to_process)
                dati_estratti = response_vision.text

                prompt_pplx = f"""
                SISTEMA: ANALIZZATORE GRANITO 3.0. PARLA COME UN COWBOY CHE CERCA IL SACRO GRAAL.
                DATI: {dati_estratti}. IPPODROMO: {ippodromo}. NAZIONE: {nazione}.

                REGOLE DI PERFEZIONE (PROTOCOLLO GRANITO):
                1. FOCUS PIAZZATO (PLACE): Ignora la quota del vincente. Cerca la quota del PIAZZATO tra 1.50 e 2.20.
                2. REGOLARITÀ INVIOLABILE: Il cavallo deve avere almeno 4 podi (1, 2, 3) nelle ultime 5 uscite. ZERO '0', ZERO 'RP', ZERO '6'.
                3. FRESHNESS FILTER: GG < 30 è obbligatorio. Sopra i 30 giorni è ruggine, sopra i 60 è ABISSO.
                4. DENSITÀ TECNICA: Scegli il cavallo che schiaccia il favorito per costanza e polmoni d'acciaio.
                5. ZERO TOLLERANZA SVEZIA/ITALIA: Primo nastro pulito. Niente sanzioni recenti.

                REFERTO FINALE (SINTASSI MAIUSCOLA):
                '💎 IL SACRO GRAAL INDIVIDUATO: [NOME]'
                'ORDINE TATTICO: [Punta Piazzato - Spiegazione della densità tecnica]'
                'BULLONE SERRATO: [Perché questo cavallo è marmo puro].'
                """
                
                response_pplx = client_pplx.chat.completions.create(model="sonar-pro", messages=[{"role": "user", "content": prompt_pplx}])
                st.info(response_pplx.choices[0].message.content)
                play_ricochet(); st.balloons()
            except Exception as e:
                st.error(f"☠️ URTO NEL REATTORE: {e}")
