/# 📊 Guía de Construcción: Dashboard de MedPredict Pro en Power BI

¡Excelente iniciativa! Construir el dashboard es la fase donde los datos cobran vida. Basado en los requerimientos de tu proyecto (2 páginas, 6 visualizaciones incluyendo 1 personalizada, filtros, botones de navegación y branding corporativo), he estructurado esta guía paso a paso para que logremos un resultado profesional y de alto impacto.

---

## Fase 1: Conexión y Preparación de Datos

### 1. Conectar los Datos
1. Abre Power BI Desktop.
2. Ve a **Inicio > Obtener datos**.
3. Selecciona el formato de tu dataset (probablemente **Texto/CSV** o **Excel** si exportaste los datos limpios desde Python, o incluso conectar directamente a una base de datos si aplica).
4. Carga tu archivo de datos principal (ej. `datos_medicos_limpios.csv` o los resultados de las predicciones `predicciones_medpredict.csv`).

### 2. Transformación en Power Query (Opcional pero recomendado)
1. Antes de cargar, haz clic en **Transformar datos**.
2. Verifica que los tipos de datos sean correctos (ej. Edad como Número entero, Costos como Número decimal/Moneda, Fecha como Fecha).
3. Renombra las columnas a nombres amigables para el usuario final (ej. de `bmi` a `Índice de Masa Corporal (IMC)`).
4. Haz clic en **Cerrar y aplicar**.

---

## Fase 2: Branding y Estructura Visual (UI/UX)

> [!TIP]
> **Branding Corporativo**
> Antes de hacer gráficos, define el tema. Esto le dará un aspecto *premium* y coherente a tu dashboard.

1. Ve a la pestaña **Ver > Temas** y selecciona personalizar o importa un archivo JSON si tienes colores hexadecimales específicos.
2. Si no tienes un JSON, usa la paleta de colores de la interfaz de tu app en Streamlit (ej. tonos azules médicos, blanco, gris oscuro para el texto).
3. **Fondo:** Considera diseñar un fondo en PowerPoint o Figma con encabezados curvos y contenedores de gráficos, expórtalo como imagen (PNG/JPG) y ponlo de fondo de página en Power BI (Formato de página > Fondo de lienzo > Transparencia 0%).

---

## Fase 3: Construcción de la Página 1 - Visión General

**Objetivo:** Mostrar la demografía y métricas principales de los pacientes.

### 1. Tarjetas de KPI (Métricas Clave)
Añade 3 o 4 tarjetas visuales en la parte superior:
- Total de Pacientes (Recuento de IDs).
- Promedio de Edad.
- Costo Promedio (si aplica en tus datos).

### 2. Visualización 1: Gráfico de Anillos o Circular
- **Propósito:** Distribución de género o estado de fumador.
- **Configuración:** Leyenda (Género), Valores (Recuento de Pacientes).
- **Estilo:** Quita el fondo, usa colores corporativos.

### 3. Visualización 2: Gráfico de Columnas Agrupadas
- **Propósito:** Distribución de pacientes por rango de edad o región.
- **Configuración:** Eje X (Rango de Edad), Eje Y (Recuento de Pacientes).

### 4. Visualización 3: Gráfico de Líneas o Área (Si tienes datos temporales)
- **Propósito:** Evolución de registros o costos a lo largo del tiempo.
- **Configuración:** Eje X (Fecha), Eje Y (Valores a medir).

### 5. Filtros Interactivos (Segmentadores)
- Añade un segmentador para **Región**, otro para **Género** y otro para **Rango de Edad**.
- Cambia su configuración en el panel de formato a "Menú desplegable" o "Mosaico" para que luzcan modernos.

---

## Fase 4: Construcción de la Página 2 - Análisis Predictivo y Salud

**Objetivo:** Enfocarse en variables médicas y resultados de predicción.

> [!IMPORTANT]
> **Navegación:** Para cumplir el requisito, añade **Botones**. En la Página 1, inserta un botón (Insertar > Botones > Flecha derecha o En blanco con texto) y configúralo (Acción > Navegación de páginas > Destino: Página 2). Haz lo mismo en la Página 2 para volver a la Página 1.

### 6. Visualización 4: Gráfico de Dispersión (Scatter Plot)
- **Propósito:** Relación entre IMC (Índice de Masa Corporal) vs. Costos o vs. Edad.
- **Configuración:** Eje X (IMC), Eje Y (Cargos/Costos), Detalles (ID Paciente), Leyenda (Fumador/No fumador). ¡Es excelente para ver clusters y valores atípicos!

### 7. Visualización 5: Gráfico de Barras Apiladas 100%
- **Propósito:** Proporción de diagnósticos o riesgo de enfermedad por categoría de edad.

### 8. Visualización 6: Objeto Visual Personalizado (Custom Visual)
> [!NOTE]
> Este es un requisito obligatorio de tu proyecto.
- Haz clic en los tres puntos `...` en el panel de Visualizaciones -> **Obtener más objetos visuales**.
- **Recomendación:** Descarga **"Word Cloud"** (Nube de palabras) si tienes síntomas de texto, o **"Tornado Chart"** (Gráfico de tornado) para comparar métricas de hombres vs. mujeres de forma mucho más atractiva que un gráfico de barras normal.
- Intégralo con los datos correspondientes.

---

## Fase 5: Pulido Final y Tooltips

1. **Interacciones:** Asegúrate de que al hacer clic en una barra, los demás gráficos se filtren correctamente (Formato > Editar interacciones).
2. **Información sobre herramientas (Tooltips):** Añade variables extra a la sección de "Información sobre herramientas" de tus gráficos para que cuando pases el mouse, muestre más contexto (ej. al pasar el mouse por un paciente en el gráfico de dispersión, que muestre su edad exacta y región).
3. **Títulos:** Revisa que todos los gráficos tengan títulos claros y en español (ej. "Distribución de Costos por IMC y Condición de Fumador").

---

### ¿Cómo seguimos?
Dime en qué paso quieres empezar o si ya tienes cargados los datos. Si necesitas ayuda creando una medida DAX específica o configurando el visual personalizado, dímelo y lo resolvemos juntos. ¡Estoy aquí como tu asesor experto!
