import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Resultados de Clustering")

# Carga tu DataFrame (ajusta el nombre y tipo de archivo)
# Ejemplo con CSV:
# df = pd.read_csv("ruta/a/tu/archivo.csv")
# Ejemplo con Pickle:
# df = pd.read_pickle("ruta/a/tu/archivo.pkl")

# --- Usa la carga de datos que tú necesitas ---
df = pd.read_pickle("data/df_EDA.pkl")  # Cambia la ruta y el archivo si es necesario

# Diagrama de dispersión: ajusta 'x', 'y' y 'cluster' según tus columnas
st.subheader("Diagrama de dispersión de clusters")
fig, ax = plt.subplots(figsize=(8, 4))
sns.scatterplot(
    data=df,
    x='x',          # Cambia 'x' por el nombre de tu columna de la variable 1
    y='y',          # Cambia 'y' por el nombre de tu columna de la variable 2
    hue='cluster',  # Cambia 'cluster' por el nombre de tu columna de clusters
    palette='tab10'
)
ax.set_title('Clustering: Diagrama de dispersión')
st.pyplot(fig)
