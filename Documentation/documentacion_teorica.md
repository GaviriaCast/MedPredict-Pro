# Documentación Teórica: MedPredict Pro

## 1. Introducción y Justificación
MedPredict Pro es una solución integral de ciencia de datos desarrollada para predecir la probabilidad de que un paciente desarrolle algún tipo de discapacidad. Esta predicción se realiza utilizando 16 características clínicas específicas. Un aspecto fundamental del diseño de este modelo es la exclusión intencional de variables socioeconómicas; esta decisión arquitectónica garantiza que las predicciones se basen estrictamente en la condición de salud del paciente, mitigando el riesgo de sesgos algorítmicos y promoviendo la equidad en las evaluaciones médicas.

## 2. Metodología de Ciencia de Datos
El desarrollo de este sistema abarcó el ciclo completo de vida de los datos:

### 2.1 Perfilado y Calidad de Datos
El primer paso consistió en la adquisición y comprensión de los datos originales. Se realizó una limpieza exhaustiva para el tratamiento de valores nulos o atípicos y se llevó a cabo un Análisis Exploratorio de Datos (EDA). Este proceso estuvo apoyado por herramientas de generación de reportes automáticos que permitieron un diagnóstico profundo de las distribuciones y correlaciones entre las variables clínicas.

### 2.2 Minería de Datos y Modelamiento (Machine Learning)
Se adoptó un enfoque comparativo para determinar el mejor algoritmo predictivo para este contexto. Los algoritmos evaluados incluyeron:
* **Árboles de Decisión:** Modelos interpretables basados en reglas de división.
* **K-Nearest Neighbors (KNN):** Clasificación basada en la proximidad de los datos en el espacio de características.
* **Redes Neuronales Artificiales:** Modelos complejos capaces de capturar relaciones no lineales avanzadas.
* **Máquinas de Vectores de Soporte (SVM):** Clasificadores robustos que buscan el hiperplano óptimo de separación entre clases.
* **Random Forest:** Un modelo de ensamble (ensemble learning) que combina múltiples árboles de decisión para mejorar la generalización, robustez y reducir el sobreajuste (overfitting).

### 2.3 Optimización de Hiperparámetros
El algoritmo de Random Forest demostró un rendimiento superior empíricamente, por lo que fue seleccionado como el modelo final. Utilizando la técnica técnica de búsqueda en cuadrícula (`GridSearchCV`) junto con validación cruzada (5-Fold Cross Validation, resultando en 360 ajustes sobre datos de 1,753 pacientes colombianos), se identificó que la configuración óptima del modelo requería 200 estimadores.

### 2.4 Despliegue en Producción
El modelo finalmente optimizado fue serializado (junto con el objeto escalador y la lista estructurada de variables de entrada) e integrado en una aplicación web interactiva. Utilizando el framework **Streamlit**, se construyó una interfaz de usuario gráfica e intuitiva que permite al personal médico ingresar las características clínicas de un paciente y obtener una inferencia probabilística del riesgo de discapacidad en tiempo real.

## 3. Resultados y Métricas de Evaluación
El modelo Random Forest optimizado alcanzó métricas de rendimiento estadístico sobresalientes:
* **ROC-AUC (Área bajo la curva ROC):** `0.939`. Esta métrica indica la excelente capacidad general del modelo para distinguir correctamente entre pacientes con riesgo de desarrollar una discapacidad y aquellos que no.
* **F1-Score:** `0.741`. Refleja un equilibrio muy sólido entre la Precisión (Precision) y la Sensibilidad (Recall), lo cual es crítico en contextos de diagnóstico asistido para balancear la detección correcta minimizando falsos positivos y falsos negativos.

---

## 4. Equipo de Desarrollo
Este proyecto académico y tecnológico fue conceptualizado y desarrollado por:

* **Gerónimo Gaviria**
* **Juan José Ospina**

**Contexto:** Curso de Analítica de Datos 2025, Universidad Pontificia Bolivariana (UPB).
