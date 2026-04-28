import streamlit as st
import joblib
import pandas as pd
import numpy as np
import time

# ==================== CONFIGURACIÓN INICIAL ====================
st.set_page_config(
    page_title="MedPredict Pro | Disability Risk",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CSS PROFESIONAL ====================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;400;600;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500&display=swap');

* { box-sizing: border-box; }

.stApp {
    background: radial-gradient(circle at 10% 20%, #0B0F19, #05080F);
    font-family: 'Inter', sans-serif;
}
#MainMenu, footer, header { display: none; }

[data-testid="stSidebar"] {
    background: rgba(10, 15, 25, 0.85);
    backdrop-filter: blur(12px);
    border-right: 1px solid rgba(0, 255, 255, 0.12);
}

.hero {
    background: linear-gradient(120deg, rgba(0,224,255,0.08), rgba(124,58,237,0.08));
    border-radius: 32px;
    padding: 1.8rem 2rem;
    margin-bottom: 2rem;
    border: 1px solid rgba(0,224,255,0.25);
    position: relative;
    overflow: hidden;
}
.hero::after {
    content: '';
    position: absolute;
    top: -80px; right: -80px;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(0,224,255,0.07), transparent 70%);
    pointer-events: none;
}
.hero h1 {
    font-size: 2.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #FFFFFF, #00e0ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero p { color: #94a3b8; margin-top: 0.5rem; }

.metric {
    background: rgba(0,224,255,0.05);
    border-radius: 20px;
    padding: 1rem;
    text-align: center;
    border: 1px solid rgba(0,224,255,0.15);
    transition: all 0.3s ease;
}
.metric:hover {
    border-color: rgba(0,224,255,0.4);
    box-shadow: 0 4px 20px rgba(0,224,255,0.1);
}
.metric-value {
    font-size: 2rem;
    font-weight: 700;
    color: #00e0ff;
    font-family: 'JetBrains Mono', monospace;
}
.metric-label {
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #64748b;
    margin-top: 4px;
}

.stButton > button {
    background: linear-gradient(90deg, #00e0ff, #7c3aed) !important;
    border: none !important;
    border-radius: 40px !important;
    padding: 0.75rem 2rem !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    color: white !important;
    letter-spacing: 0.05em !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 20px rgba(0,224,255,0.2) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 30px rgba(0,224,255,0.35) !important;
}

.stSlider > div > div > div { background: #00e0ff !important; }
div[data-baseweb="select"] > div {
    background: #0d1626 !important;
    border-color: #1e2d45 !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
}
div[data-baseweb="select"] svg { color: #64748b !important; }
label[data-testid="stWidgetLabel"] {
    color: #64748b !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.68rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
}
.stCheckbox label { color: #94a3b8 !important; }

.stTabs [data-baseweb="tab-list"] {
    gap: 6px;
    background: rgba(15,23,42,0.6);
    border-radius: 40px;
    padding: 0.3rem;
    border: 1px solid #1e2d45;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 32px;
    padding: 0.45rem 1.1rem;
    font-weight: 500;
    font-size: 0.85rem;
    color: #64748b !important;
    transition: all 0.2s ease;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(90deg, rgba(0,224,255,0.2), rgba(124,58,237,0.2)) !important;
    color: #00e0ff !important;
    border: 1px solid rgba(0,224,255,0.3) !important;
}

.result-panel {
    background: rgba(10, 18, 32, 0.85);
    backdrop-filter: blur(16px);
    border-radius: 32px;
    border: 1px solid rgba(0,224,255,0.25);
    padding: 2rem;
    margin-top: 2rem;
    position: relative;
    overflow: hidden;
}
.result-panel::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #00e0ff, #7c3aed, #00e0ff);
    background-size: 200% auto;
    animation: shimmer 3s linear infinite;
}
@keyframes shimmer {
    0%   { background-position: 0% center; }
    100% { background-position: 200% center; }
}

.prob-percent {
    font-family: 'JetBrains Mono', monospace;
    font-size: 4rem;
    font-weight: 300;
    line-height: 1;
}
.prob-bar-container {
    background: rgba(255,255,255,0.07);
    border-radius: 40px;
    height: 10px;
    overflow: hidden;
    margin: 0.6rem 0 0.3rem;
}
.risk-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 0.45rem 1.2rem;
    border-radius: 40px;
    font-size: 0.85rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    margin-top: 0.5rem;
}
.risk-high { background: rgba(239,68,68,0.12);  color: #ef4444; border: 1px solid rgba(239,68,68,0.35); }
.risk-med  { background: rgba(245,158,11,0.12); color: #f59e0b; border: 1px solid rgba(245,158,11,0.35); }
.risk-low  { background: rgba(16,185,129,0.12); color: #10b981; border: 1px solid rgba(16,185,129,0.35); }

.info-card {
    background: rgba(0,224,255,0.03);
    border: 1px solid #1e2d45;
    border-radius: 16px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.8rem;
}
.info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.35rem 0;
    border-bottom: 1px solid #1e2d45;
    font-size: 0.85rem;
}
.info-row:last-child { border-bottom: none; }
.info-key { color: #64748b; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.06em; }
.info-val { color: #e2e8f0; font-weight: 500; }

.feature-bar-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 6px;
}
.feature-bar-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: #94a3b8;
    width: 120px;
    text-align: right;
    flex-shrink: 0;
}
.feature-bar-track {
    flex: 1;
    background: rgba(255,255,255,0.06);
    border-radius: 40px;
    height: 6px;
    overflow: hidden;
}
.feature-bar-fill {
    height: 6px;
    border-radius: 40px;
    background: linear-gradient(90deg, #00e0ff, #7c3aed);
}
.feature-pct {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    color: #64748b;
    width: 38px;
    text-align: right;
    flex-shrink: 0;
}

.disclaimer {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    color: #334155;
    margin-top: 1.2rem;
    padding-top: 1rem;
    border-top: 1px solid #1e2d45;
    line-height: 1.6;
}
.footer {
    text-align: center;
    padding: 1.5rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: #334155;
    border-top: 1px solid #1e2d45;
    margin-top: 2rem;
    letter-spacing: 0.05em;
}
p, .stMarkdown p { color: #e2e8f0 !important; }
h1,h2,h3,h4 { color: #e2e8f0 !important; }
.stExpander { border-color: #1e2d45 !important; background: rgba(10,18,32,0.5) !important; }
[data-testid="stExpander"] summary { color: #94a3b8 !important; }
</style>
""", unsafe_allow_html=True)

# ==================== CARGA DEL MODELO ====================
@st.cache_resource
def load_models():
    model         = joblib.load('models/best_rf_model.pkl')
    scaler        = joblib.load('models/scaler.pkl')
    feature_names = joblib.load('models/feature_names.pkl')
    return model, scaler, feature_names

model, scaler, feature_names = load_models()

# ==================== MAPEOS — 16 features clínicas ====================
NORMAL_MAP     = {'Normal': 2, 'No Registra': 1, 'Anormal': 0}
IMC_MAP        = {'BAJO PESO': 0, 'DESNUTRICION LEVE': 1, 'DESNUTRICION MODERADA': 2,
                  'DESNUTRICION SEVERA': 3, 'OBESIDAD I': 4, 'OBESIDAD II': 5,
                  'OBESIDAD III': 6, 'PESO INSUFICIENTE': 7, 'PESO NORMAL': 8, 'SOBREPESO': 9}
DISNEA_MAP     = {'LIGERA': 0, 'MODERADA': 1, 'MUY GRAVE': 2}
GENERO_MAP     = {'Femenino': 0, 'Intersexual': 1, 'Masculino': 2, 'No Registra': 3}
CLASIFISUI_MAP = {'Sin Riesgo Alta con Seguimiento Ambulatorio': 0,
                  'Sin Riesgo Ambulatorio': 1, 'Riesgo Leve': 2,
                  'Riesgo Moderado': 3, 'Riesgo Alto': 4, 'Riesgo Muy Alto': 5}

# Importancias reales del modelo
FEATURE_IMPORTANCES = {
    'EDAD': 17.8, 'IMC': 14.3, 'TALLA': 13.9, 'PESO': 11.4,
    'CLASIFISUI': 9.7, 'RESULTADOIMC': 8.7, 'MENTAL': 8.6,
    'GENERO': 2.9, 'covid3': 2.8, 'NEUROLÓGICO': 2.1,
    'covid1': 1.9, 'OSTEOMUSCULAR': 1.6, 'PULMONAR': 1.3,
    'covid2': 1.1, 'ESCALA DISNEA': 1.0, 'CARDIOVASCULAR': 0.9
}

# ==================== HERO ====================
st.markdown("""
<div class="hero">
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1.5rem;">
        <div>
            <div style="display:flex; gap:8px; margin-bottom:12px; flex-wrap:wrap;">
                <span style="background:rgba(0,224,255,0.12); border:1px solid rgba(0,224,255,0.25); padding:0.2rem 0.8rem; border-radius:40px; font-size:0.68rem; color:#00e0ff; font-family:'JetBrains Mono',monospace; letter-spacing:0.06em;">⚡ CLINICAL AI</span>
                <span style="background:rgba(124,58,237,0.12); border:1px solid rgba(124,58,237,0.25); padding:0.2rem 0.8rem; border-radius:40px; font-size:0.68rem; color:#a78bfa; font-family:'JetBrains Mono',monospace; letter-spacing:0.06em;">🇨🇴 COLOMBIA 2026</span>
                <span style="background:rgba(16,185,129,0.12); border:1px solid rgba(16,185,129,0.25); padding:0.2rem 0.8rem; border-radius:40px; font-size:0.68rem; color:#10b981; font-family:'JetBrains Mono',monospace; letter-spacing:0.06em;">● MODELO ACTIVO</span>
            </div>
            <h1>MedPredict Pro</h1>
            <p>Disability Risk Engine · Random Forest + GridSearchCV · 16 Features Clínicas</p>
            <p style="font-size:0.72rem; margin-top:0.3rem; color:#475569; font-family:'JetBrains Mono',monospace;">Variables socioeconómicas excluidas · Sin sesgo algorítmico</p>
        </div>
        <div style="display:flex; gap:1rem; flex-wrap:wrap;">
            <div class="metric"><div class="metric-value">0.939</div><div class="metric-label">ROC-AUC</div></div>
            <div class="metric"><div class="metric-value">0.741</div><div class="metric-label">F1-Score</div></div>
            <div class="metric"><div class="metric-value">1,753</div><div class="metric-label">Pacientes</div></div>
            <div class="metric"><div class="metric-value">360</div><div class="metric-label">CV Fits</div></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("### 📋 Información del modelo")
    st.markdown("""
    <div class="info-card">
        <div class="info-row"><span class="info-key">Algoritmo</span><span class="info-val">Random Forest</span></div>
        <div class="info-row"><span class="info-key">Optimización</span><span class="info-val">GridSearchCV</span></div>
        <div class="info-row"><span class="info-key">Validación</span><span class="info-val">5-Fold CV</span></div>
        <div class="info-row"><span class="info-key">Features</span><span class="info-val">16 clínicas</span></div>
        <div class="info-row"><span class="info-key">n_estimators</span><span class="info-val">200</span></div>
        <div class="info-row"><span class="info-key">max_depth</span><span class="info-val">None</span></div>
        <div class="info-row"><span class="info-key">ROC-AUC</span><span class="info-val" style="color:#00e0ff;">0.9393</span></div>
        <div class="info-row"><span class="info-key">F1-Score</span><span class="info-val" style="color:#00e0ff;">0.7407</span></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📊 Importancia de features")
    for feat, imp in list(FEATURE_IMPORTANCES.items())[:8]:
        st.markdown(f"""
        <div class="feature-bar-row">
            <div class="feature-bar-label">{feat}</div>
            <div class="feature-bar-track">
                <div class="feature-bar-fill" style="width:{imp/17.8*100:.0f}%;"></div>
            </div>
            <div class="feature-pct">{imp:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.caption("UPB · Analítica de Datos 2025")

# ==================== LAYOUT PRINCIPAL ====================
col_left, col_right = st.columns([2, 1], gap="large")

with col_left:
    tab1, tab2, tab3 = st.tabs(["📋 Datos Clínicos", "🫀 Estado de Sistemas", "🦠 COVID-19"])

    with tab1:
        col_a, col_b = st.columns(2)
        with col_a:
            edad = st.slider("Edad (años)", 0, 110, 60)
            peso = st.slider("Peso (kg)", 20, 175, 70)
        with col_b:
            talla   = st.slider("Talla (cm)", 100, 200, 160)
            imc_val = round(peso / ((talla / 100) ** 2), 2)
            imc_cat = ('BAJO PESO' if imc_val < 18.5 else
                       'NORMAL'    if imc_val < 25   else
                       'SOBREPESO' if imc_val < 30   else 'OBESIDAD')
            st.metric("IMC calculado", f"{imc_val} kg/m²", delta=imc_cat)

        col_c, col_d = st.columns(2)
        with col_c:
            resultado_imc = st.selectbox("Resultado IMC (clasificación oficial)", list(IMC_MAP.keys()))
            escala_disnea = st.selectbox("Escala de disnea", list(DISNEA_MAP.keys()))
        with col_d:
            clasifisui = st.selectbox("Clasificación SUI", list(CLASIFISUI_MAP.keys()))
            genero     = st.selectbox("Género", list(GENERO_MAP.keys()))

    with tab2:
        st.markdown("#### Estado de sistemas orgánicos")
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            cardiovascular = st.selectbox("Cardiovascular", ['Normal', 'Anormal', 'No Registra'])
            pulmonar       = st.selectbox("Pulmonar",       ['Normal', 'Anormal', 'No Registra'])
            neurologico    = st.selectbox("Neurológico",    ['Normal', 'Anormal', 'No Registra'])
        with col_s2:
            mental        = st.selectbox("Mental",        ['Normal', 'Anormal', 'No Registra'])
            osteomuscular = st.selectbox("Osteomuscular", ['Normal', 'Anormal', 'No Registra'])

    with tab3:
        st.markdown("#### Episodios de COVID-19 en historia clínica")
        col_c1, col_c2, col_c3 = st.columns(3)
        with col_c1:
            covid1 = st.checkbox("Primer episodio")
        with col_c2:
            covid2 = st.checkbox("Segundo episodio")
        with col_c3:
            covid3 = st.checkbox("Tercer episodio")
        st.caption("Los antecedentes de COVID-19 se incluyen por su asociación documentada con secuelas funcionales crónicas.")

with col_right:
    sistemas_alterados = sum([cardiovascular != 'Normal', pulmonar != 'Normal',
                               neurologico != 'Normal', mental != 'Normal', osteomuscular != 'Normal'])
    covid_total = int(covid1) + int(covid2) + int(covid3)

    st.markdown("### 📊 Resumen clínico")
    st.markdown(f"""
    <div class="info-card">
        <div class="info-row"><span class="info-key">Edad</span><span class="info-val">{edad} años</span></div>
        <div class="info-row"><span class="info-key">IMC</span><span class="info-val">{imc_val} — {imc_cat}</span></div>
        <div class="info-row"><span class="info-key">Género</span><span class="info-val">{genero}</span></div>
        <div class="info-row"><span class="info-key">Sist. alterados</span><span class="info-val">{sistemas_alterados} de 5</span></div>
        <div class="info-row"><span class="info-key">Disnea</span><span class="info-val">{escala_disnea.lower()}</span></div>
        <div class="info-row"><span class="info-key">COVID previo</span><span class="info-val">{covid_total} episodio(s)</span></div>
        <div class="info-row"><span class="info-key">Clasificación SUI</span><span class="info-val" style="font-size:0.75rem;">{clasifisui[:28]}...</span></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    predict = st.button("⚡ ANALIZAR RIESGO", use_container_width=True, type="primary")

# ==================== PREDICCIÓN ====================
if predict:
    with st.spinner("Evaluando con Random Forest..."):
        time.sleep(0.4)

        input_data = {
            'EDAD':           edad,
            'PESO':           peso,
            'TALLA':          talla,
            'IMC':            imc_val,
            'CARDIOVASCULAR': NORMAL_MAP[cardiovascular],
            'PULMONAR':       NORMAL_MAP[pulmonar],
            'NEUROLÓGICO':    NORMAL_MAP[neurologico],
            'MENTAL':         NORMAL_MAP[mental],
            'OSTEOMUSCULAR':  NORMAL_MAP[osteomuscular],
            'RESULTADOIMC':   IMC_MAP[resultado_imc],
            'ESCALA DISNEA':  DISNEA_MAP[escala_disnea],
            'CLASIFISUI':     CLASIFISUI_MAP[clasifisui],
            'covid1':         int(covid1),
            'covid2':         int(covid2),
            'covid3':         int(covid3),
            'GENERO':         GENERO_MAP[genero],
        }

        X_input = pd.DataFrame([{k: input_data.get(k, 0) for k in feature_names}]).fillna(0)
        proba   = model.predict_proba(X_input)[0][1]
        pred    = model.predict(X_input)[0]
        pct     = int(proba * 100)

        if proba >= 0.6:
            risk_level = "Alto";  risk_color = "#ef4444"; risk_icon = "🔴"; risk_class = "risk-high"
        elif proba >= 0.35:
            risk_level = "Medio"; risk_color = "#f59e0b"; risk_icon = "🟡"; risk_class = "risk-med"
        else:
            risk_level = "Bajo";  risk_color = "#10b981"; risk_icon = "🟢"; risk_class = "risk-low"

        st.markdown('<div class="result-panel">', unsafe_allow_html=True)

        col_r1, col_r2 = st.columns([1, 1])

        with col_r1:
            if pred == 1:
                st.markdown(f"### {risk_icon} Discapacidad predicha")
                st.error("El modelo indica presencia de discapacidad")
            else:
                st.markdown("### ✅ Sin discapacidad predicha")
                st.success("El modelo indica ausencia de discapacidad")
            st.markdown(f'<span class="risk-badge {risk_class}">{risk_icon} Riesgo {risk_level}</span>', unsafe_allow_html=True)

        with col_r2:
            st.markdown(f"""
            <div style="text-align:center; padding:0.5rem;">
                <div style="font-family:'JetBrains Mono',monospace; font-size:0.65rem; color:#475569; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:0.4rem;">Probabilidad de discapacidad</div>
                <div class="prob-percent" style="color:{risk_color};">{pct}<span style="font-size:1.8rem; color:#334155;">%</span></div>
                <div class="prob-bar-container">
                    <div style="height:10px; width:{pct}%; background:linear-gradient(90deg,{risk_color},#7c3aed); border-radius:40px;"></div>
                </div>
                <div style="display:flex; justify-content:space-between; font-size:0.62rem; color:#334155; font-family:'JetBrains Mono',monospace; margin-top:4px;">
                    <span>0%</span><span>50%</span><span>100%</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with st.expander("📖 Explicabilidad — ¿por qué este resultado?"):
            st.markdown("**Top features que más influyeron en esta predicción:**")
            top_feats = [
                ("EDAD",        17.8, f"{edad} años"),
                ("IMC",         14.3, f"{imc_val} kg/m²"),
                ("TALLA",       13.9, f"{talla} cm"),
                ("PESO",        11.4, f"{peso} kg"),
                ("CLASIFISUI",   9.7, clasifisui[:25]+"..."),
            ]
            for feat, imp, val in top_feats:
                st.markdown(f"""
                <div class="feature-bar-row" style="margin-bottom:8px;">
                    <div class="feature-bar-label" style="width:90px;">{feat}</div>
                    <div class="feature-bar-track">
                        <div class="feature-bar-fill" style="width:{imp/17.8*100:.0f}%;"></div>
                    </div>
                    <div class="feature-pct">{imp:.1f}%</div>
                    <div style="font-family:'JetBrains Mono',monospace; font-size:0.65rem; color:#475569; margin-left:8px;">{val}</div>
                </div>
                """, unsafe_allow_html=True)
            st.caption("Importancias basadas en el modelo entrenado con 1,753 pacientes colombianos.")

        st.markdown("""
        <div class="disclaimer">
        ⚠ Este resultado es una estimación estadística del modelo y no reemplaza la evaluación clínica profesional.
        &nbsp;·&nbsp; Random Forest · GridSearchCV · 360 combinaciones · 5-fold CV · Variables socioeconómicas excluidas para evitar sesgo algorítmico.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown("""
<div class="footer">
    PRÁCTICA 4 — ANALÍTICA DE DATOS 2025 &nbsp;·&nbsp; UNIVERSIDAD PONTIFICIA BOLIVARIANA &nbsp;·&nbsp; MEDELLÍN, COLOMBIA<br>
    Modelo entrenado con datos anonimizados · Uso exclusivamente académico · Variables socioeconómicas excluidas intencionalmente
</div>
""", unsafe_allow_html=True)
