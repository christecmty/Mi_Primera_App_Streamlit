import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="Mi primera app", page_icon="📊", layout="wide")

st.title("Mi primera aplicación de datos")
st.write("Esta aplicación convierte una tabla pequeña en una interfaz interactiva.")

# --------------------------------------------------
# 1. Datos
# --------------------------------------------------

datos = pd.DataFrame(
    {
        "Categoría": ["Admisiones", "Becas", "Inscripciones", "Reglamentos", "Servicios", "Soporte"],
        "Evaluaciones": [4, 4, 4, 4, 4, 4],
        "Con evidencia": [3, 2, 3, 2, 3, 3],
        "Calidad": [4.3, 3.2, 4.0, 3.0, 4.2, 3.8],
    }
)

# --------------------------------------------------
# 2. Filtro
# --------------------------------------------------
categorias = st.multiselect(
    "Selecciona una o más categorías",
    options=datos["Categoría"].tolist(),
    default=datos["Categoría"].tolist(),
)

vista = datos[datos["Categoría"].isin(categorias)]

# --------------------------------------------------
# 3. Validación
# --------------------------------------------------


if vista.empty:
    st.warning("Selecciona al menos una categoría para mostrar resultados.")
    st.stop()

# --------------------------------------------------
# 4. Indicadores
# --------------------------------------------------

total = int(vista["Evaluaciones"].sum())
cobertura = 100 * vista["Con evidencia"].sum() / total
calidad = vista["Calidad"].mean()

c1, c2, c3 = st.columns(3)
c1.metric("Evaluaciones", total)
c2.metric("Con evidencia", f"{cobertura:.1f}%")
c3.metric("Calidad promedio", f"{calidad:.2f} / 5")


# --------------------------------------------------
# 5. Visualizaciones

tab_plotly, tab_matplotlib, tab_seaborn = st.tabs(
[
"Plotly",
"Matplotlib",
"Seaborn",
]
)


# --------------------------------------------------
#Gráfica 1
# --------------------------------------------------
with tab_plotly:
    figura = px.bar(
    vista,
    x="Categoría",
    y="Calidad",
    color="Calidad",
    range_y=[0, 5],
    title="Calidad promedio por categoría",
)
st.plotly_chart(figura, use_container_width=True)

#Gráfica 2
# --------------------------------------------------
with tab_matplotlib:
    fig, ax = plt.subplots()

    ax.bar(
        vista["Categoría"],
        vista["Calidad"]
    )

    ax.set_title("Calidad promedio por categoría")
    ax.set_xlabel("Categoría")
    ax.set_ylabel("Calidad")
    ax.set_ylim(0, 5)

    plt.xticks(rotation=45)
    plt.tight_layout()


    st.pyplot(fig)

#Gráfica 3 SEABORN
# --------------------------------------------------
with tab_seaborn:
    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=(9, 5))

    sns.barplot(
        data=vista,
        x="Categoría",
        y="Calidad",
        hue="Categoría",
        palette="viridis",
        legend=False,
        ax=ax,
    )

    ax.set_title("Calidad promedio por categoría")
    ax.set_xlabel("Categoría")
    ax.set_ylabel("Calidad")
    ax.set_ylim(0, 5)
    ax.tick_params(axis="x", rotation=45)

    plt.tight_layout()

    st.pyplot(fig)

# --------------------------------------------------
# 6. Tabla
# --------------------------------------------------

with st.expander("Ver datos utilizados"):
    st.dataframe(vista, use_container_width=True, hide_index=True)

st.caption("Datos simulados con fines académicos · TI3008C")
