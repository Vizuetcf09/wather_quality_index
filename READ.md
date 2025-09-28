# ***Titulo***

# **Predicción de la Calidad del Agua en México Mediante Algoritmos de Aprendizaje Automático**

***`Vizuet_CF ⛺`***

## **Descripción**

Se utilizaron los datos de la calidad del agua (CA), provenientes de la Comisión Nacional del Agua (CONAGUA., 2021), que consta de 2,500 sitios de monitoreo, de los cuales 788 corresponden al análisis de aguas superficiales que considera 8 indicadores.

### **Indicadores**

1. Demanda Bioquímica de Oxígeno a cinco días (DBO5)
2. Demanda Química de Oxígeno (DQO)
3. Sólidos Suspendidos Totales (SST)
4. Coliformes Fecales (CF)
5. *Escherichia coli* (E_COLI)
6. Enterococos (ENTEROC)
7. Porcentaje de Saturación de Oxigeno (OD%)
8. Toxicidad (TOX)

## **Semáforo**

La calidad del agua se determinó a través de un semáforo que considera 3 colores verde, amarillo y rojo, y se obtiene integrando los resultados de los 8 indicadores antes mencionados (CONAGUA., 2021).

## **Preprocesamiento de los datos**

Se eliminaron dos indicadores de la CA (ENTEROC y TOX); el data set utilizado está compuesto por 8 columnas.

**Nombre de las columnas**
1. DBO_mg/L
2. DQO_mg/L              
3. SST_mg/L              
4. COLI_FEC_NMP_100mL    
5. E_COLI_NMP_100mL      
6. OD_PORC               
7. SEMAFORO               
8. NUM_SEMAFORO

Los colores del semáforo de la calidad del agua se ordenaron alfabéticamente y se les asignó un numero (1, 2 y 3); posteriormente se almacenaron en la columna 8 (NUM_SEMAFORO).

**Numero por color**

- Amarillo - 1
- Rojo - 2
- Verde - 3

## **Entrenamiento**

Para el entrenamiento del modelo se tomaron en cuenta 6 indicadores (DBO5, DQO, SST, CF, E_COLIi y OD%) para predecir la CA de acuerdo al numero asignado para cada color del semaforo.

## Randomized

### Importamos las librerías