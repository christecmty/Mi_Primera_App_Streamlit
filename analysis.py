import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


datos = pd.DataFrame({
    "Categoría": [
        "Admisiones",
        "Becas",
        "Inscripciones",
        "Reglamentos",
        "Servicios",
        "Soporte"
    ],
    "Calidad": [4.3, 3.2, 4.0, 3.0, 4.2, 3.8]
})

fig, ax = plt.subplots()

ax.bar(
    datos["Categoría"],
    datos["Calidad"]
)

ax.set_title("Calidad promedio por categoría")
ax.set_xlabel("Categoría")
ax.set_ylabel("Calidad")
ax.set_ylim(0, 5)

plt.xticks(rotation=45)
plt.tight_layout()
#plt.show()

st.pyplot(fig)