import streamlit as st
import pandas as pd

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA STREAMLIT
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Enfoque Diagnóstico del Raquitismo y Metabolismo Fosfocalcico",
    page_icon="🦴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .main-header { font-size: 2.2rem; color: #1E3A8A; font-weight: 700; margin-bottom: 0.5rem; }
    .sub-header { font-size: 1.1rem; color: #475569; margin-bottom: 1.5rem; }
    .card-calc { background-color: #EFF6FF; border-left: 5px solid #2563EB; padding: 1rem; border-radius: 6px; margin-bottom: 1rem; }
    .card-phospho { background-color: #F0FDF4; border-left: 5px solid #16A34A; padding: 1rem; border-radius: 6px; margin-bottom: 1rem; }
    .disclaimer-box { background-color: #FEF2F2; border-left: 5px solid #DC2626; padding: 1.2rem; border-radius: 6px; margin-bottom: 1.5rem; }
    .stButton>button { width: 100%; background-color: #1E3A8A; color: white; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# ENCABEZADO Y ADVERTENCIA MÉDICA / PRIVACIDAD (DISCLAIMER)
# -----------------------------------------------------------------------------
st.markdown('<div class="main-header">🦴 Herramienta de Orientación Diagnóstica: Metabolismo Fosfocálcico y Raquitismo</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Basado en las Guías Educativas de Raquitismo (<i>Haffner et al., Pediatric Nephrology 2022</i>)</div>', unsafe_allow_html=True)

# ADVERTENCIA DE USO EXCLUSIVO POR PERSONAL MÉDICO
st.markdown("""
<div class="disclaimer-box">
    <h4 style="color: #991B1B; margin-top: 0;">⚠️ ADVERTENCIA: USO EXCLUSIVO PARA PERSONAL MÉDICO ESPECIALIZADO</h4>
    <p style="color: #7F1D1D; margin-bottom: 0; font-size: 0.95rem;">
        Esta aplicación es un algoritmo computacional de apoyo educativo y de orientación académica. <b>Está destinada exclusivamente a médicos, endocrinólogos, nefólogos pediatras y profesionales de la salud capacitados.</b><br>
        No constituye un diagnóstico médico vinculante, ni sustituye el juicio clínico profesional, la anamnesis ni la evaluación presencial del paciente.
    </p>
</div>
""", unsafe_allow_html=True)

st.info("🔒 **Garantía de Desidentificación de Datos**: Esta aplicación **NO almacena ni solicita identificadores personales** (Nombre, DNI, Historia Clínica, etc.). Únicamente procesa la edad, el sexo y los parámetros de laboratorio de forma anónima durante la sesión actual.")

# -----------------------------------------------------------------------------
# BARRA LATERAL: DATOS DEMOGRÁFICOS Y SIGNOS CLÍNICOS
# -----------------------------------------------------------------------------
st.sidebar.header("📋 1. Datos del Paciente (Anonimizados)")
edad_grupo = st.sidebar.selectbox(
    "Grupo de Edad",
    ["Lactante (< 1 año)", "Preescolar (1 - 5 años)", "Escolar (6 - 11 años)", "Adolescente (12 - 18 años)", "Adulto (> 18 años)"]
)
sexo = st.sidebar.radio("Sexo Biológico", ["Femenino", "Masculino"])

st.sidebar.markdown("---")
st.sidebar.header("🚨 2. Criterios Diagnósticos Iniciales")
fa_elevada = st.sidebar.checkbox("Fosfatasa Alcalina (FA / ALP) Elevada para la edad", value=True)
signos_radiologicos = st.sidebar.checkbox("Signos Radiológicos de Raquitismo / Osteomalacia", value=True)
acidosis_metabolica = st.sidebar.checkbox("Acidosis Metabólica (Bicarbonato bajo / Déficit de base)")
insuficiencia_renal = st.sidebar.checkbox("Insuficiencia Renal / Creatinina Elevada (eGFR < 60 mL/min/1.73m²)")

st.sidebar.markdown("---")
st.sidebar.header("👁️ 3. Hallazgos Clínicos Adicionales")
alopecia = st.sidebar.checkbox("Alopecia (Parcial o Total)")
abscesos_dentales = st.sidebar.checkbox("Abscesos Dentales Espontáneos sin caries previas")
deformidad_miembros = st.sidebar.checkbox("Deformidades en extremidades (Genu varum / Genu valgum)")

# -----------------------------------------------------------------------------
# PANEL PRINCIPAL: DATOS DE LABORATORIO
# -----------------------------------------------------------------------------
st.subheader("🧪 Ingrese los Resultados de Laboratorio")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Parámetros Séricos Básicos")
    calcio_serico = st.selectbox("Calcio Sérico (Total / Iónico)", ["Bajo (Hipocalcemia)", "Normal", "Elevado (Hipercalcemia)"])
    fosfato_serico = st.selectbox("Fosfato Sérico para la edad", ["Bajo (Hipofosfatemia)", "Normal", "Elevado"])
    pth_serica = st.selectbox("Hormona Paratiroidea (PTH)", ["Elevada (Hiperparatiroidismo Secundario)", "Normal o Baja"])

with col2:
    st.markdown("### Metabolitos de Vitamina D")
    vit_25oh = st.selectbox("25(OH) Vitamina D (Calcidiol)", ["Deficiente / Muy Baja (< 20 ng/mL)", "Normal (20 - 100 ng/mL)", "Elevada (> 100 ng/mL)"])
    vit_125oh = st.selectbox("1,25(OH)₂ Vitamina D (Calcitriol)", ["Baja / Inapropiadamente Normal", "Normal", "Elevada"])

with col3:
    st.markdown("### Función Renal y Orina")
    fgf23 = st.selectbox("Factor de Crecimiento de Fibroblastos 23 (FGF23)", ["Elevado", "Normal o Bajo", "No disponible / No realizado"], index=2)
    tmp_gfr = st.selectbox("Reabsorción Tubular Máxima de Fosfato (TmP/GFR)", ["Disminuida (Pérdida Renal de Fosfato)", "Normal"])
    calciuria = st.selectbox("Calciuria en Orina (U_Ca/Crea o Ca 24h)", ["Baja / Disminuida", "Normal", "Elevada (Hipercalciuria)"])

st.markdown("---")

confirmacion_medica = st.checkbox("Confirmo que soy personal médico de salud calificado y que usaré este resultado como apoyo de orientación.")

# -----------------------------------------------------------------------------
# MOTOR DE INFERENCIA Y LÓGICA DIAGNÓSTICA
# -----------------------------------------------------------------------------
if st.button("🔍 Evaluar Orientación Diagnóstica"):
    if not confirmacion_medica:
        st.error("⚠️ Debe confirmar que es personal médico cualificado marcando la casilla superior antes de ver la evaluación.")
    else:
        st.markdown("## 📊 Resultados de la Evaluación Diagnóstica")
        
        if insuficiencia_renal:
            st.warning("⚠️ **Atención**: En presencia de Enfermedad Renal Crónica, la alteración del metabolismo fosfocálcico se encuadra en la **Osteopatía Renal / CKD-MBD** (hiperparatiroidismo secundario por retención de fosfato y deficiencia de calcitriol).")
        
        if acidosis_metabolica:
            st.info("💡 **Nota**: La Acidosis Metabólica orienta a **Acidosis Tubular Renal (ATR)** o **Síndrome de Fanconi Proximal**, donde la pérdida de fosfato y bicarbonato genera raquitismo secundario.")

        # Clasificación principal
        if pth_serica == "Elevada (Hiperparatiroidismo Secundario)":
            st.markdown('<div class="card-calc"><h4>🟡 Patrón Sugerente: Raquitismo Calcipénico</h4><p>Respuesta paratiroidea elevada. La PTH contrarresta la hipocalcemia aumentando la resorción ósea e induciendo pérdida renal de fosfato en el túbulo proximal (degradación de NaPi2a/2c).</p></div>', unsafe_allow_html=True)
            
            diagnosticos = []
            if vit_25oh == "Deficiente / Muy Baja (< 20 ng/mL)":
                diagnosticos.append({
                    "Nombre": "Raquitismo Nutricional por Deficiencia de Vitamina D",
                    "Frecuencia": "Muy Frecuente (Causa #1 a nivel mundial)",
                    "Genética": "No hereditaria (Ambiental / Nutricional)",
                    "Detalles": "Niveles deficientes de 25(OH)D reducen la absorción intestinal de calcio y fosfato.",
                    "Tratamiento Orientativo": "Vitamina D (Colecalciferol / Ergocalciferol) + Calcio oral."
                })
                diagnosticos.append({
                    "Nombre": "Raquitismo Dependiente de Vitamina D Tipo 1B (VDDR1B)",
                    "Frecuencia": "Muy Rara",
                    "Genética": "Mutación en CYP2R1 (Deficiencia de 25-hidroxilasa hepática)",
                    "Detalles": "Incapacidad hepática para hidroxilar la vitamina D a 25(OH)D.",
                    "Tratamiento Orientativo": "Calcifediol o Calcitriol."
                })
            elif vit_25oh in ["Normal (20 - 100 ng/mL)", "Elevada (> 100 ng/mL)"]:
                if vit_125oh == "Baja / Inapropiadamente Normal":
                    diagnosticos.append({
                        "Nombre": "Raquitismo Dependiente de Vitamina D Tipo 1A (VDDR1A)",
                        "Frecuencia": "Rara",
                        "Genética": "Mutación en CYP27B1 (Deficiencia de 1α-hidroxilasa renal)",
                        "Detalles": "25(OH)D normal con falla en la conversión renal a 1,25(OH)₂D.",
                        "Tratamiento Orientativo": "Calcitriol o Alfacalcidol de por vida + Calcio."
                    })
                elif vit_125oh == "Elevada":
                    diag_name = "Raquitismo Dependiente de Vitamina D Tipo 2A / 2B (VDDR2A / VDDR2B)"
                    if alopecia: diag_name += " [Alta probabilidad por presencia de Alopecia]"
                    diagnosticos.append({
                        "Nombre": diag_name,
                        "Frecuencia": "Muy Rara",
                        "Genética": "Mutación en VDR (Receptor de Vitamina D) o HNRNPC",
                        "Detalles": "Resistencia periférica al Calcitriol con niveles endógenos compensatorios de 1,25(OH)₂D muy altos.",
                        "Tratamiento Orientativo": "Dosis altas de Calcio oral o Calcio intravenoso continuo."
                    })
                else:
                    diagnosticos.append({
                        "Nombre": "Raquitismo Nutricional por Deficiencia Severa de Calcio",
                        "Frecuencia": "Frecuente en ciertas regiones",
                        "Genética": "No hereditaria",
                        "Detalles": "Ingesta de calcio insuficiente a pesar de niveles normales de Vitamina D.",
                        "Tratamiento Orientativo": "Suplementación con Calcio elemental oral."
                    })
            
            for d in diagnosticos:
                with st.expander(f"📌 **{d['Nombre']}**", expanded=True):
                    st.write(f"**Frecuencia:** {d['Frecuencia']}")
                    st.write(f"**Bases Genéticas:** {d['Genética']}")
                    st.write(f"**Fisiopatología:** {d['Detalles']}")
                    st.write(f"**Orientación Terapéutica:** {d['Tratamiento Orientativo']}")

        else:
            # PTH Normal o Baja -> Hipofosfatémico
            st.markdown('<div class="card-phospho"><h4>🟢 Patrón Sugerente: Raquitismo Hipofosfatémico (Fosfopénico Primario)</h4><p>PTH normal o baja con fuga renal directa de fosfato (TmP/GFR disminuida).</p></div>', unsafe_allow_html=True)
            
            diagnosticos_fosfo = []
            if calciuria == "Elevada (Hipercalciuria)":
                st.error("🚨 **Alerta de Seguridad Clínica**: Se detectó **HIPERCALCIURIA**. En raquitismos hipofosfatémicos con hipercalciuria, los suplementos de fosfato deben ajustarse con cuidado y está **contraindicado el uso de calcitriol sin estrecho monitoreo** para evitar nefrocalcinosis.")
                diagnosticos_fosfo.append({
                    "Nombre": "Raquitismo Hipofosfatémico Hereditario con Hipercalciuria (HHRH)",
                    "Frecuencia": "Rara",
                    "Genética": "Mutación en SLC34A3 (Cotransportador NaPi2c)",
                    "Detalles": "Pérdida renal de fosfato con FGF23 bajo. Esto sobreestimula la 1,25(OH)₂D, aumentando la absorción intestinal de calcio e induciendo hipercalciuria e hipercalcinosis.",
                    "Tratamiento Orientativo": "Fosfato oral exclusivo (No administrar Calcitriol)."
                })
                diagnosticos_fosfo.append({
                    "Nombre": "Enfermedad de Dent (Tipo 1 / 2) o Síndrome de Fanconi",
                    "Frecuencia": "Rara (Ligada al X)",
                    "Genética": "Genes CLCN5 / OCRL / CTNS",
                    "Detalles": "Disfunción tubular proximal con proteinuria de bajo peso molecular y fuga de electrolitos.",
                    "Tratamiento Orientativo": "Manejo tubular sintomático."
                })
            else:
                if fgf23 == "Elevado":
                    diag_xlh = "Raquitismo Hipofosfatémico Ligado al X (XLH)"
                    if abscesos_dentales or deformidad_miembros:
                        diag_xlh += " [Características clínicas compatibles presentes]"
                    diagnosticos_fosfo.append({
                        "Nombre": diag_xlh,
                        "Frecuencia": "~80% de los raquitismos hipofosfatémicos hereditarios",
                        "Genética": "Mutación en PHEX (Dominante ligado al X)",
                        "Detalles": "Exceso de FGF23 que degrada los cotransportadores NaPi2a/2c e inhibe la 1α-hidroxilasa renal.",
                        "Tratamiento Orientativo": "Burosumab (Anticuerpo monoclonal anti-FGF23) o Tratamiento convencional (Fosfato oral + Calcitriol)."
                    })
                    diagnosticos_fosfo.append({
                        "Nombre": "Otras Formas Mediadas por FGF23 (ADHR, ARHR, Osteomalacia Inducida por Tumor - TIO)",
                        "Frecuencia": "Muy Raras / Adquiridas",
                        "Genética": "Genes FGF23, DMP1, ENPP1, FAM20C o Secreción tumoral paraneoplásica",
                        "Detalles": "Exceso mantenido de FGF23 circulante.",
                        "Tratamiento Orientativo": "Estudio genético amplio o búsqueda de tumor mesenquimal (PET-CT Dotatoc) en TIO."
                    })
                else:
                    diagnosticos_fosfo.append({
                        "Nombre": "Raquitismo Hipofosfatémico Primario a clasificar (Requiere medir FGF23)",
                        "Frecuencia": "Variable",
                        "Genética": "Estudio genético mediante Panel de Raquitismo / Exoma",
                        "Detalles": "Se requiere confirmar FGF23 y TmP/GFR en ayunas para diferenciar XLH vs HHRH vs Tubulopatías.",
                        "Tratamiento Orientativo": "Completar perfil fosfofórico en ayunas."
                    })

            for d in diagnosticos_fosfo:
                with st.expander(f"📌 **{d['Nombre']}**", expanded=True):
                    st.write(f"**Frecuencia:** {d['Frecuencia']}")
                    st.write(f"**Bases Genéticas:** {d['Genética']}")
                    st.write(f"**Fisiopatología:** {d['Detalles']}")
                    st.write(f"**Orientación Terapéutica:** {d['Tratamiento Orientativo']}")

        # Resumen
        st.markdown("### 📑 Resumen del Perfil Ingresado")
        resumen_df = pd.DataFrame({
            "Parámetro": ["Edad", "Sexo", "Fosfatasa Alcalina", "Calcio", "Fosfato", "PTH", "25(OH)D", "1,25(OH)₂D", "FGF23", "Calciuria"],
            "Estado": [edad_grupo, sexo, "Elevada" if fa_elevada else "Normal", calcio_serico, fosfato_serico, pth_serica, vit_25oh, vit_125oh, fgf23, calciuria]
        })
        st.table(resumen_df)

        st.caption("📖 Referencia de Algoritmo: Haffner D, et al. Rickets guidance: part I—diagnostic workup. Pediatr Nephrol. 2022;37(9):2013-2036.")
