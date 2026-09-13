import streamlit as st
import pandas as pd

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA STREAMLIT
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Algoritmo Avanzado de Metabolismo Fosfocalcico y Raquitismo",
    page_icon="🦴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .main-header { font-size: 2.1rem; color: #1E3A8A; font-weight: 700; margin-bottom: 0.5rem; }
    .sub-header { font-size: 1.05rem; color: #475569; margin-bottom: 1.5rem; }
    .card-calc { background-color: #EFF6FF; border-left: 5px solid #2563EB; padding: 1rem; border-radius: 6px; margin-bottom: 1rem; }
    .card-phospho { background-color: #F0FDF4; border-left: 5px solid #16A34A; padding: 1rem; border-radius: 6px; margin-bottom: 1rem; }
    .card-rare { background-color: #FEF3C7; border-left: 5px solid #D97706; padding: 1rem; border-radius: 6px; margin-bottom: 1rem; }
    .disclaimer-box { background-color: #FEF2F2; border-left: 5px solid #DC2626; padding: 1.2rem; border-radius: 6px; margin-bottom: 1.5rem; }
    .stButton>button { width: 100%; background-color: #1E3A8A; color: white; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# ENCABEZADO Y ADVERTENCIA MÉDICA / PRIVACIDAD (DISCLAIMER)
# -----------------------------------------------------------------------------
st.markdown('<div class="main-header">🦴 Sistema Experto de Orientación Diagnóstica: Raquitismo y Osteomalacia</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Algoritmo Ampliado de Consenso (<i>Haffner et al., Pediatric Nephrology 2022</i>) e Integración de Formas Raras y Adquiridas</div>', unsafe_allow_html=True)

# ADVERTENCIA DE USO EXCLUSIVO POR PERSONAL MÉDICO
st.markdown("""
<div class="disclaimer-box">
    <h4 style="color: #991B1B; margin-top: 0;">⚠️ ADVERTENCIA DE RESPONSABILIDAD: USO EXCLUSIVO PARA PERSONAL MÉDICO ESPECIALIZADO</h4>
    <p style="color: #7F1D1D; margin-bottom: 0; font-size: 0.95rem;">
        Esta aplicación es una herramienta computacional de apoyo pedagógico y de decisión clínica asistida. <b>Está destinada exclusivamente a médicos endocrinólogos, nefrólogos pediatras, pediatras y profesionales de la salud capacitados.</b><br>
        No constituye un diagnóstico médico definitivo, ni sustituye la evaluación clínica presencial, anamnesis detallada o juicio facultativo.
    </p>
</div>
""", unsafe_allow_html=True)

st.info("🔒 **Garantía de Desidentificación de Datos**: Esta aplicación **NO almacena ni transmite datos personales identificables** (Nombre, DNI, Historia Clínica, etc.). Los parámetros ingresados se procesan exclusivamente en la memoria temporal durante la sesión.")

# -----------------------------------------------------------------------------
# BARRA LATERAL: DATOS DEMOGRÁFICOS, CLÍNICOS Y ANTECEDENTES
# -----------------------------------------------------------------------------
st.sidebar.header("📋 1. Datos del Paciente")
edad_grupo = st.sidebar.selectbox(
    "Grupo de Edad",
    ["Lactante (< 1 año)", "Preescolar (1 - 5 años)", "Escolar (6 - 11 años)", "Adolescente (12 - 18 años)", "Adulto (> 18 años)"]
)
sexo = st.sidebar.radio("Sexo Biológico", ["Femenino", "Masculino"])

st.sidebar.markdown("---")
st.sidebar.header("🚨 2. Criterios Diagnósticos Iniciales")
fa_estado = st.sidebar.selectbox(
    "Fosfatasa Alcalina (FA / ALP)",
    ["Muy Elevada (Típica de Raquitismo)", "Normal", "Disminuida / Muy Baja (Anormal)"]
)
signos_radiologicos = st.sidebar.checkbox("Signos Radiológicos de Raquitismo / Osteomalacia", value=True)
acidosis_metabolica = st.sidebar.checkbox("Acidosis Metabólica / Déficit de Bicarbonato")
insuficiencia_renal = st.sidebar.checkbox("Insuficiencia Renal Crónica (eGFR < 60 mL/min/1.73m²)")

st.sidebar.markdown("---")
st.sidebar.header("👁️ 3. Hallazgos Clínicos y Sistémicos")
alopecia = st.sidebar.checkbox("Alopecia (Parcial o Total)")
abscesos_dentales = st.sidebar.checkbox("Abscesos Dentales Espontáneos / Pérdida dental prematura")
deformidad_miembros = st.sidebar.checkbox("Deformidades Óseas (Genu varum / valgum / Rosario raquítico)")
afeccion_ocular_cne = st.sidebar.checkbox("Afección Ocular / Cristalino o SNC (Sospecha de Lowe / Cistinosis)")

st.sidebar.markdown("---")
st.sidebar.header("💊 4. Antecedentes y Exposiciones")
anticonvulsivantes = st.sidebar.checkbox("Uso crónico de Anticonvulsivantes (Inductores CYP)")
hierro_iv = st.sidebar.checkbox("Administración reciente de Hierro Carboximaltosa IV")
farmacos_tenofovir = st.sidebar.checkbox("Tratamiento con Tenofovir, Adefovir o Cisplatino")
malabsorcion = st.sidebar.checkbox("Sospecha de Malabsorción (Celíaca, Fibrosis Quística, Intestino Corto)")

# -----------------------------------------------------------------------------
# PANEL PRINCIPAL: DATOS DE LABORATORIO COMPLETO
# -----------------------------------------------------------------------------
st.subheader("🧪 Ingrese los Parámetros Complejos de Laboratorio")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Perfil Calcio-Fosfato")
    calcio_serico = st.selectbox("Calcio Sérico Total / Iónico", ["Bajo (Hipocalcemia)", "Normal", "Elevado (Hipercalcemia)"])
    fosfato_serico = st.selectbox("Fosfato Sérico (para la edad)", ["Bajo (Hipofosfatemia)", "Normal", "Elevado"])
    pth_serica = st.selectbox("Hormona Paratiroidea (PTH)", ["Elevada (Hiperparatiroidismo Secundario)", "Normal", "Disminuida / Baja"])

with col2:
    st.markdown("### Metabolitos de Vitamina D")
    vit_25oh = st.selectbox("25(OH) Vitamina D (Calcidiol)", ["Deficiente / Muy Baja (< 20 ng/mL)", "Normal (20 - 100 ng/mL)", "Elevada (> 100 ng/mL)"])
    vit_125oh = st.selectbox("1,25(OH)₂ Vitamina D (Calcitriol)", ["Baja / Inapropiadamente Normal", "Normal", "Elevada / Muy Alta"])

with col3:
    st.markdown("### Función Renal y Orina")
    fgf23 = st.selectbox("FGF23 (Intacto / C-terminal)", ["Elevado", "Normal", "Disminuido / Bajo", "No realizado"], index=3)
    tmp_gfr = st.selectbox("Reabsorción Tubular Fosfato (TmP/GFR)", ["Disminuida (Pérdida Renal de Fosfato)", "Normal"])
    calciuria = st.selectbox("Calciuria (U_Ca/Crea o Ca 24h)", ["Baja / Disminuida", "Normal", "Elevada (Hipercalciuria)"])
    proteinuria_tubular = st.sidebar.checkbox("Proteinuria de bajo peso molecular / Aminoaciduria / Glucosuria normoglucémica")

st.markdown("---")

confirmacion_medica = st.checkbox("Confirmo que soy personal médico de salud calificado y que utilizaré este informe como orientación de apoyo clínico.")

# -----------------------------------------------------------------------------
# MOTOR DE INFERENCIA EXHAUSTIVO
# -----------------------------------------------------------------------------
if st.button("🔍 Evaluar Cuadro Diagnóstico Completo"):
    if not confirmacion_medica:
        st.error("⚠️ Debe confirmar que es personal médico de salud cualificado marcando la casilla superior antes de continuar.")
    else:
        st.markdown("## 📊 Informe Diagnóstico Integral")
        
        # 1. EVALUACIÓN DE HIPOFOSFATASIA (REGLA DE ALERTA DE SEGURIDAD)
        if fa_estado == "Disminuida / Muy Baja (Anormal)":
            st.markdown('<div class="card-rare"><h4>🔴 ALERTA DE SEGURIDAD: Sospecha de Hipofosfatasia (HPP)</h4><p>La Fosfatasa Alcalina disminuida en presencia de alteración ósea es el sello distintivo de la <b>Hipofosfatasia</b> (mutaciones en <i>ALPL</i> que codifican TNSALP).<br><b>ADVERTENCIA DE SEGURIDAD:</b> La suplementación con Calcio o Vitamina D en estos pacientes está CONTRAINDICADA ya que puede agravar la hipercalcemia/hipercalciuria y la nefrocalcinosis. Evaluar fosfato de piridoxal (PLP) y substratos sustrato (PEA) o Asfotasa Alfa.</p></div>', unsafe_allow_html=True)

        # 2. EVALUACIÓN DE ENFERMEDAD RENAL CRÓNICA Y ACIDOSIS METABÓLICA
        if insuficiencia_renal:
            st.warning("⚠️ **Etiología Renal Crónica**: Cuadro compatible con **Osteopatía Renal / CKD-MBD**. La hiperfosfatemia por falla de filtración y la falta de síntesis de calcitriol generan hiperparatiroidismo secundario severo.")
        
        if acidosis_metabolica:
            st.info("💡 **Componente Tubular Detectado**: La acidosis metabólica asociada orienta a **Acidosis Tubular Renal (ATR)** o **Síndrome de Fanconi Proximal** secundario.")

        # 3. CLASIFICACIÓN PRINCIPAL PATOFISIOLÓGICA
        
        # ---------------------------------------------------------------------
        # PATRÓN A: CALCIPÉNICO (PTH ELEVADA)
        # ---------------------------------------------------------------------
        if pth_serica == "Elevada (Hiperparatiroidismo Secundario)":
            st.markdown('<div class="card-calc"><h4>🟡 Patrón Fisiopatológico: Raquitismo / Osteomalacia Calcipénica</h4><p>Respuesta paratiroidea secundaria a la disminución del calcio iónico o de la señal de la vitamina D. La PTH compensatoria induce pérdida tubular pasiva de fosfato.</p></div>', unsafe_allow_html=True)
            
            diag_calcipenicos = []

            # Causas farmacológicas / adquiridas
            if anticonvulsivantes:
                diag_calcipenicos.append({
                    "Nombre": "Raquitismo / Osteomalacia por Inductores Enzimáticos",
                    "Tipo": "Adquirido / Farmacológico",
                    "Genética": "No genético directo (Inducción de CYP3A4 / CYP24A1 por fármacos como Fenitoína, Carbamazepina, Fenobarbital)",
                    "Detalles": "Aceleración del catabolismo de la 25(OH)D y calcitriol hacia metabolitos inactivos.",
                    "Tratamiento Orientativo": "Ajuste de dosis elevadas de Vitamina D3 o Calcifediol suplementario."
                })
            
            if malabsorcion:
                diag_calcipenicos.append({
                    "Nombre": "Raquitismo Secundario a Síndrome de Malabsorción Intestinal",
                    "Tipo": "Adquirido",
                    "Genética": "Asociado a Enfermedad Celíaca, Fibrosis Quística, Intestino Corto o EII",
                    "Detalles": "Pérdida intestinal de grasas y vitaminas liposolubles (vit. D) y/o mala absorción de calcio.",
                    "Tratamiento Orientativo": "Tratamiento de la patología de base + Calcio y Vitamina D hidrosoluble o parenteral."
                })

            # Causas Nutricionales y Genéticas
            if vit_25oh == "Deficiente / Muy Baja (< 20 ng/mL)":
                diag_calcipenicos.append({
                    "Nombre": "Raquitismo Nutricional por Deficiencia de Vitamina D",
                    "Tipo": "Nutricional / Ambiental",
                    "Genética": "No hereditaria",
                    "Detalles": "Falta de exposición solar o ingesta inadecuada. Causa #1 a nivel global.",
                    "Tratamiento Orientativo": "Colecalciferol / Ergocalciferol + Suplementación con Calcio."
                })
                diag_calcipenicos.append({
                    "Nombre": "Raquitismo Dependiente de Vitamina D Tipo 1B (VDDR1B)",
                    "Tipo": "Genético Raro",
                    "Genética": "Autosómico Recesivo - Mutación en CYP2R1 (25-hidroxilasa hepática)",
                    "Detalles": "Imposibilidad de convertir Vitamina D nativa en 25(OH)D a nivel hepático.",
                    "Tratamiento Orientativo": "Calcifediol (25-OH-D3) o Calcitriol."
                })

            elif vit_25oh in ["Normal (20 - 100 ng/mL)", "Elevada (> 100 ng/mL)"]:
                if vit_125oh == "Baja / Inapropiadamente Normal":
                    diag_calcipenicos.append({
                        "Nombre": "Raquitismo Dependiente de Vitamina D Tipo 1A (VDDR1A)",
                        "Tipo": "Genético Raro",
                        "Genética": "Autosómico Recesivo - Mutación en CYP27B1 (1α-hidroxilasa renal)",
                        "Detalles": "Niveles de 25(OH)D normales con imposibilidad de sintetizar 1,25(OH)₂D activa.",
                        "Tratamiento Orientativo": "Calcitriol o Alfacalcidol de por vida + Calcio de soporte."
                    })
                elif vit_125oh == "Elevada / Muy Alta":
                    nombre_vddr2 = "Raquitismo Dependiente de Vitamina D Tipo 2A o 2B (VDDR2A / VDDR2B)"
                    if alopecia: nombre_vddr2 += " [Fuerte sospecha clínica por Alopecia concomitante]"
                    diag_calcipenicos.append({
                        "Nombre": nombre_vddr2,
                        "Tipo": "Genético Raro",
                        "Genética": "Autosómico Recesivo - Mutaciones en VDR (Receptor Vit D) o HNRNPC",
                        "Detalles": "Resistencia de los órganos diana al calcitriol. Mantiene niveles endógenos masivos de 1,25(OH)₂D.",
                        "Tratamiento Orientativo": "Altas dosis de Calcio oral o infusiones continuas de Calcio Intravenoso."
                    })
                else:
                    diag_calcipenicos.append({
                        "Nombre": "Raquitismo Nutricional por Deficiencia Severa de Calcio",
                        "Tipo": "Nutricional",
                        "Genética": "No hereditaria",
                        "Detalles": "Ingesta dietética insuficiente de calcio con niveles adecuados de Vitamina D.",
                        "Tratamiento Orientativo": "Suplementación con Calcio elemental oral (800 - 1000 mg/día)."
                    })

            for d in diag_calcipenicos:
                with st.expander(f"📌 **{d['Nombre']}** ({d['Tipo']})", expanded=True):
                    st.write(f"**Genética / Etiología:** {d['Genética']}")
                    st.write(f"**Fisiopatología:** {d['Detalles']}")
                    st.write(f"**Orientación Terapéutica:** {d['Tratamiento Orientativo']}")

        # ---------------------------------------------------------------------
        # PATRÓN B: FOSFOPÉNICO / HIPOFOSFATÉMICO (PTH NORMAL O BAJA)
        # ---------------------------------------------------------------------
        else:
            st.markdown('<div class="card-phospho"><h4>🟢 Patrón Fisiopatológico: Raquitismo / Osteomalacia Hipofosfatémica (Fosfopénica Primaria)</h4><p>Pérdida renal primaria de fosfato (TmP/GFR reducida) independiente del control de PTH.</p></div>', unsafe_allow_html=True)
            
            diag_fosfopenicos = []

            # 1. Sub-grupo con Hipercalciuria
            if calciuria == "Elevada (Hipercalciuria)" or proteinuria_tubular:
                st.error("🚨 **Alerta de Manejo**: Se detectó **HIPERCALCIURIA o DISFUNCIÓN TUBULAR PROXIMAL**. En patologías con hipercalciuria, el uso de calcitriol sin estricta supervisión está contraindicado por alto riesgo de nefrocalcinosis.")
                
                diag_fosfopenicos.append({
                    "Nombre": "Raquitismo Hipofosfatémico Hereditario con Hipercalciuria (HHRH)",
                    "Tipo": "Genético Raro",
                    "Genética": "Autosómico Recesivo - Mutación en SLC34A3 (NaPi-2c)",
                    "Detalles": "Pérdida renal de fosfato con FGF23 bajo. El fosfato bajo suprime FGF23 y estimula 1,25(OH)₂D, lo que sobreabsorbe calcio intestinal produciendo hipercalciuria severa.",
                    "Tratamiento Orientativo": "Suplementación exclusiva con Fosfato Oral (Evitar Calcitriol)."
                })
                diag_fosfopenicos.append({
                    "Nombre": "Síndrome de Fanconi Proximal Primario o Secundario",
                    "Tipo": "Tubulopatía Compleja",
                    "Genética": "Cistinosis (CTNS), Enfermedad de Dent (CLCN5/OCRL), Síndrome de Lowe, Síndrome de Fanconi-Bickel (GLUT2), Tirosinemia Tipo 1",
                    "Detalles": "Disfunción global del túbulo proximal que genera pérdida de fosfato, glucosa, aminoácidos, bicarbonato y proteínas de bajo peso molecular.",
                    "Tratamiento Orientativo": "Tratamiento de la patología metabólica de base (ej. Cisteamina) + Reemplazo de fosfato y citrato."
                })
                if farmacos_tenofovir:
                    diag_fosfopenicos.append({
                        "Nombre": "Síndrome de Fanconi Adquirido por Fármacos",
                        "Tipo": "Adquirido / Iatrogénico",
                        "Genética": "Secundario a Tenofovir, Adefovir, Cisplatino o Aminoglucósidos",
                        "Detalles": "Toxicidad mitocondrial en las células tubulares proximales renales.",
                        "Tratamiento Orientativo": "Retiro o ajuste del fármaco nefrotóxico + Soporte de fosfato y electrolitos."
                    })

            # 2. Sub-grupo Mediado por FGF23
            else:
                if hierro_iv:
                    diag_fosfopenicos.append({
                        "Nombre": "Osteomalacia / Hipofosfatemia Inducida por Hierro Carboximaltosa IV",
                        "Tipo": "Adquirido / Farmacológico",
                        "Genética": "Efecto iatrogénico secundario a formulaciones específicas de hierro parenteral",
                        "Detalles": "Inhibición de la degradación de FGF23 intacto, lo que provoca fosfaturia aguda y descenso marcado de calcitriol y fosfato sérico.",
                        "Tratamiento Orientativo": "Suspensión de hierro IV formulación carboximaltosa + Reemplazo temporal de fosfato y calcitriol."
                    })

                if fgf23 == "Elevado" or fgf23 == "No realizado":
                    nombre_xlh = "Raquitismo Hipofosfatémico Ligado al X (XLH)"
                    if abscesos_dentales or deformidad_miembros:
                        nombre_xlh += " [Manifestaciones odontológicas / esqueléticas características presentes]"
                    
                    diag_fosfopenicos.append({
                        "Nombre": nombre_xlh,
                        "Tipo": "Genético Dominante (~80% de las formas hereditarias)",
                        "Genética": "Dominante Ligada al X - Mutación en PHEX",
                        "Detalles": "Exceso de FGF23 circulante por falla de inactivación. Degrada NaPi2a/2c e inhibe la 1α-hidroxilasa.",
                        "Tratamiento Orientativo": "Burosumab (Anticuerpo monoclonal anti-FGF23) o Tratamiento Convencional (Fosfato oral + Calcitriol)."
                    })
                    diag_fosfopenicos.append({
                        "Nombre": "Otras Formas Genéticas FGF23-Mediadas (ADHR / ARHR1 / ARHR2 / ARHR3)",
                        "Tipo": "Genético Muy Raro",
                        "Genética": "Autosómico Dominante (FGF23) o Recesivo (DMP1, ENPP1, FAM20C)",
                        "Detalles": "Trastornos del procesamiento matriz-ósea o estabilización de FGF23.",
                        "Tratamiento Orientativo": "Fosfato oral + Calcitriol o evaluación de terapias dirigidas."
                    })
                    diag_fosfopenicos.append({
                        "Nombre": "Osteomalacia Inducida por Tumores (TIO / Síndrome Paraneoplásico)",
                        "Tipo": "Adquirido Neoplásico (Frecuente en Adultos)",
                        "Genética": "Secreción por tumores mesenquimales fosfatúricos benignos",
                        "Detalles": "Producción autónoma de FGF23 por un tumor (usualmente de pequeño tamaño en partes blandas o hueso).",
                        "Tratamiento Orientativo": "Localización tumoral (PET-CT 68Ga-DOTATATE / Resonancia) y resección quirúrgica curativa."
                    })

                elif fgf23 in ["Normal", "Disminuido / Bajo"]:
                    diag_fosfopenicos.append({
                        "Nombre": "Raquitismo Hipofosfatémico No mediado por FGF23 (SLC34A1 / NaPi-2a)",
                        "Tipo": "Genético Raro",
                        "Genética": "Mutación en SLC34A1 (Cotransportador NaPi-2a)",
                        "Detalles": "Falla directa en la reabsorción tubular sin participación del eje FGF23.",
                        "Tratamiento Orientativo": "Suplementación cuidadosa con fosfato oral."
                    })

            for d in diag_fosfopenicos:
                with st.expander(f"📌 **{d['Nombre']}** ({d['Tipo']})", expanded=True):
                    st.write(f"**Etiología / Genética:** {d['Genética']}")
                    st.write(f"**Fisiopatología:** {d['Detalles']}")
                    st.write(f"**Orientación Terapéutica:** {d['Tratamiento Orientativo']}")

        # ---------------------------------------------------------------------
        # TABLA DE RESUMEN CLÍNICO
        # ---------------------------------------------------------------------
        st.markdown("### 📑 Resumen de Variables Evaluadas")
        resumen_df = pd.DataFrame({
            "Parámetro Evaluado": ["Grupo Edad", "Fosfatasa Alcalina", "Calcio", "Fosfato", "PTH", "25(OH)D", "1,25(OH)₂D", "FGF23", "Calciuria", "Fármacos / Exp."],
            "Estado Ingresado": [
                edad_grupo, 
                fa_estado, 
                calcio_serico, 
                fosfato_serico, 
                pth_serica, 
                vit_25oh, 
                vit_125oh, 
                fgf23, 
                calciuria,
                "Sí" if (anticonvulsivantes or hierro_iv or farmacos_tenofovir) else "No"
            ]
        })
        st.table(resumen_df)

        st.caption("📖 Referencias de Algoritmo Ampliado: Haffner D, et al. Rickets guidance: part I—diagnostic workup. Pediatr Nephrol. 2022;37(9):2013-2036. | Carpenter TO, et al. A practical guide to rickets. 2017.")
