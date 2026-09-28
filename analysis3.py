"""Ejemplo local de visualización con Seaborn.

Ejecutar en la terminal de VS Code con:
    python analysis3.py
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


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

sns.set_theme(style="whitegrid")

fig, ax = plt.subplots(figsize=(9, 5))

sns.barplot(
    data=datos,
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

# Fuera de Streamlit, Matplotlib muestra la ventana de la gráfica.
plt.show()
