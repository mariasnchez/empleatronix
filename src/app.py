import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title('EMPLEATRONIX')

st.write('Todos los datos sobre los empleados de una aplicación')

DATA_URL = ('data/employees.csv')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data = load_data(10000)

st.write(data)

# BOTONES
col1, col2, col3 = st.columns(3)

color = col1.color_picker('Elige un color para las barras', '#00f900')
on1 = col2.toggle('Mostrar el nombre', value=True)
on2 = col3.toggle('Mostrar sueldo en la barra', value=False)


# GRÁFICA
empleados = data

nombre = empleados['full name']
salario = empleados['salary']

fig, ax = plt.subplots()

if on1:
    ax.barh(nombre, salario, color=color)
else:
    ax.barh(nombre, salario, color=color)
    ax.set_yticklabels([]) 

if on2:
    bars = ax.barh(nombre, salario, color=color)
    ax.bar_label(bars, fmt='%d€', padding=3)
else:
    ax.barh(nombre, salario, color=color)


st.pyplot(fig)
