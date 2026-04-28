# 🧠 MedPredict Pro | Disability Risk Engine

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange)
![Streamlit](https://img.shields.io/badge/Despliegue-Streamlit-FF4B4B)
![UPB](https://img.shields.io/badge/Institución-UPB-red)

Motor predictivo impulsado por Machine Learning para evaluar el riesgo de discapacidad basado en variables clínicas. Desarrollado como proyecto para el curso de **Analítica de Datos 2025** en la Universidad Pontificia Bolivariana (UPB).

---

## 📋 Descripción del Proyecto

MedPredict Pro es una solución de ciencia de datos *end-to-end* que busca predecir la probabilidad de que un paciente desarrolle algún tipo de discapacidad, utilizando 16 características clínicas y descartando intencionalmente variables socioeconómicas para evitar sesgos algorítmicos.

El proyecto abarca todo el ciclo de vida de los datos:
1. **Perfilado y Calidad de Datos:** Limpieza exhaustiva y análisis exploratorio (EDA) apoyado por reportes en HTML.
2. **Minería de Datos (Machine Learning):** Entrenamiento, evaluación y comparación de múltiples algoritmos (Árboles de Decisión, KNN, Redes Neuronales, SVM y Random Forest).
3. **Optimización:** Hiperparametrización del mejor modelo (Random Forest) mediante `GridSearchCV`.
4. **Despliegue:** Interfaz gráfica interactiva y moderna desarrollada en **Streamlit**.

## 📊 Métricas del Modelo

El modelo final seleccionado es un **Random Forest** optimizado (200 estimadores), el cual fue entrenado con datos de 1,753 pacientes colombianos y validado mediante 5-Fold Cross Validation (360 ajustes).

* **ROC-AUC:** 0.939
* **F1-Score:** 0.741

## 📁 Estructura del Repositorio

* `01_calidad_datos.ipynb`: Notebook con el perfilado, diagnóstico y limpieza de los datos originales.
* `02_modelo_predictivo.ipynb`: Notebook con el entrenamiento, comparación de 5 modelos e hiperparametrización.
* `03_despliegue.ipynb`: Documentación conceptual del despliegue del modelo predictivo.
* `app.py`: Código fuente de la interfaz gráfica interactiva.
* `data/`: Directorio que contiene los datasets originales y limpios listos para el modelo.
* `models/`: Modelos exportados (`best_rf_model.pkl`, `scaler.pkl` y `feature_names.pkl`).
* `reports/`: Reportes HTML generados (Pandas Profiling) y gráficas de validación (Matrices de confusión, importancia de features).
* `pantallazo_app.png`: Captura de pantalla de la interfaz gráfica funcionando.

## 🚀 Cómo ejecutar la aplicación localmente

1. Clona este repositorio:
   ```bash
   git clone https://github.com/GaviriaCast/MedPredict-Pro.git
   cd MedPredict-Pro
   ```

2. Crea y activa un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Mac/Linux:
   source venv/bin/activate
   ```

3. Instala las dependencias necesarias:
   ```bash
   pip install streamlit pandas numpy scikit-learn joblib
   ```

4. Ejecuta la aplicación de Streamlit:
   ```bash
   streamlit run app.py
   ```

## 🎓 Contexto Académico

* **Curso:** Analítica de Datos 2025
* **Práctica 4:** Calidad y Minería de Datos en Python (15%)
* **Institución:** Universidad Pontificia Bolivariana (UPB) - Medellín, Colombia.

---

## 👥 Autores

* **Gerónimo Gaviria Castañeda** — [geronimo.gaviria@upb.edu.co](mailto:geronimo.gaviria@upb.edu.co)
* **Juan José Ospina Arroyave** — [juan.ospinaa@upb.edu.co](mailto:juan.ospinaa@upb.edu.co)
