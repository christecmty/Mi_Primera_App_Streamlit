"""Ejemplo local de visualización con Plotly.

Ejecutar en la terminal de VS Code con:
    python analysis2.py
"""

import pandas as pd
import plotly.express as px


datos = pd.DataFrame(
    {
        "Categoría": [
            "Admisiones",
            "Becas",
            "Inscripciones",
            "Reglamentos",
            "Servicios",
            "Soporte",
        ],
        "Evaluaciones": [4, 4, 4, 4, 4, 4],
        "Con evidencia": [3, 2, 3, 2, 3, 3],
        "Calidad": [4.3, 3.2, 4.0, 3.0, 4.2, 3.8],
    }
)

figura = px.bar(
    datos,
    x="Categoría",
    y="Calidad",
    color="Calidad",
    text="Calidad",
    hover_data=["Evaluaciones", "Con evidencia"],
    range_y=[0, 5],
    title="Calidad promedio por categoría",
    color_continuous_scale="Blues",
)

figura.update_traces(textposition="outside")
figura.update_layout(coloraxis_showscale=False)

# Fuera de Streamlit, Plotly abre la gráfica en el navegador.
figura.show()
