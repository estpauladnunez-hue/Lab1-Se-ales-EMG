# Laboratorio 1- Analisis estadistico de una señal.
Informe de laboratorio acerca del Análisis estadístico de una señal EMG enfocada en neuropatia.
# RESUMEN
En este laboratorio de Procesamiento Digital de Señales (PDS) se desarrolló un código en Python, ejecutado en Spyder, para analizar estadísticamente una señal electromiográfica (EMG) asociada a neuropatía, obtenida de la base de datos PhysioNet. Se calcularon parámetros como media, desviación estándar, coeficiente de variación e histogramas, complementados con funciones de probabilidad. Además, se evaluó el impacto de distintos tipos de ruido —gaussiano, impulso y artefacto— mediante el cálculo de la relación señal-ruido (SNR), con el fin de comprender cómo las perturbaciones afectan la calidad de las señales biomédicas.

# INTRODUCION 
El análisis estadístico de señales biomédicas permite caracterizar su comportamiento, identificar patrones y cuantificar variaciones relevantes para el diagnóstico clínico. En este laboratorio, correspondiente a la asignatura de Procesamiento Digital de Señales (PDS), se trabajó con una señal electromiográfica (EMG) asociada a neuropatía, obtenida de la base de datos PhysioNet. Se empleó Python (Spyder) para calcular parámetros estadísticos fundamentales y representar gráficamente la distribución de la señal. Asimismo, se introdujeron diferentes tipos de ruido con el fin de medir su efecto mediante la relación señal-ruido (SNR), reforzando así la comprensión del preprocesamiento y limpieza de señales en aplicaciones médicas.


# ANALISIS ESTADISTICO DE LA SEÑAL
# Señal (Emg) - Physio.Net:

Para llevar a cabo esta práctica, comenzamos buscando una señal electromiográfica (EMG) disponible en PhysioNet, pues la señal que elegimos corresponde a un pasiente con una Neuropatia. Para ser más especificos, la condicion del Paciente (Neuropatia/Neuropatia Periferica), basicamente consiste en un problema de los nervios que produce dolor, adormecimiento, cosquilleo, hinchazón y debilidad muscular en distintas partes del cuerpo. Esto por lo general, comienza en las manos o los pies y empeora con el tiempo. El cáncer o su tratamiento, como la quimioterapia, pueden causar neuropatía. También pueden causarla las lesiones físicas, las infecciones, las sustancias tóxicas o las afecciones como diabetes, insuficiencia de los riñones o desnutrición. Por otro lado, en una señal electromiográfica (EMG) de un paciente con esta condicion, podríamos observar varias alteraciones en la actividad muscular, tales como:

Disminución de la amplitud
2.Aumento de la latencia: (Un retraso en la activación muscular causado por la conducción nerviosa más lenta o bloqueada).
3.Actividad espontánea anormal
4.Disminución de la frecuencia de activación
5.Alteraciones en la reclutación de unidades motoras: (Se pueden ver cambios en la cantidad y el tamaño de los potenciales de unidad motora, indicando reinnervación o pérdida neuronal).
Ahora bien, luego de tener presente esta informacion, seguimos para descargar los archivos .dat y .hea correspondientes a dicha señal. Con estos archivos en nuestro poder, importamos la señal a Python (Spyder) y empleamos la librería wfdb para leer y visualizar los datos, facilitando así su analisis.
<img width="544" height="303" alt="image" src="https://github.com/user-attachments/assets/1e40c53d-ec74-45dd-9aa3-671e85f7c4d2" />
         |Figura 1: Señal EMG original de un paciente con neuropatía.|
La señal Fisiologica Electromiografica (EMG) Corresponde al registro en el musculo tibial anterior de un Paciente de 62 años, sexo masculino, con diagnostico de dolor lumbar cronico y neuropatia radiculopatía derecha en la raíz nerviosa L5.
La señal fue capturada mediante un electrodo concéntrico de 25mm, mientras el paciente realizaba una dosiflexión suave del pie contra resistencia, seguida de relajación.

Por todo lo anterior, es escencial que podamos realizar las mediciones que se realizaran con el paso del codigo (Informe) para un optimo analisis por lo que tenemos lo siguiente:
# Importacion de la señal y librerias:
El análisis como tal de los datos de la señal se realiza por medio de la programación mencionada, esto junto a librerías en donde tenemos a Numpy y SciPy para poder calcular nuestros estadísticos descriptivos, pues nuestro código comienza con la implementación de las librerías necesarias para el óptimo funcionamiento de nuestro laboratorio:

```python
import os
import wfdb
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
plt.close('all') 


#Vincular la carpeta como directorio
os.chdir(r'C:\Users\Paola\Documents\Lab 1 Señales')

# Importar señal
datos, info = wfdb.rdsamp('emg_neuropathy', sampfrom=50, sampto=1000)
datos = np.array(datos).flatten()

# Graficar señal original
plt.figure(figsize=(10, 5))
plt.plot(datos, label="Señal EMG Original", color='c')
plt.xlabel("Tiempo (ms)")
plt.ylabel("Amplitud (mV)")
plt.title("Señal EMG-Neuropatía")
plt.legend()
plt.grid()
plt.show()
```
Pues esta sección es esencial ya que permite la manipulación del sistema de archivos y directorios, para leer y manipular registros de datos biomédicos almacenados que en este caso se encuentra en formato PhysioNet, para la generación de gráficos en este caso de la señal EMG en el dominio del tiempo, utilizando la librería de matplotlib, se grafica la señal, incluyendo los ejes para indicar la unidad de tiempo y la amplitud (Caracteristicas estadísticas).
Se calcula la media de la señal de dos formas:

# 1.La Media
a) Manualmente: Sumando todos los valores y dividiendo por el total de datos.
     <img width="366" height="72" alt="image" src="https://github.com/user-attachments/assets/42ce86a7-df5f-4bcf-9967-ec6093e72cfc" />
       |Ecu 1: Formula para calcular la Media.|

b) Usando Numpy.mean(), que proporciona un método más eficiente y rapido.
```python
#Media
sumatoriadatos = 0
for i in datos:
    sumatoriadatos += i
#datos sumados
media=sumatoriadatos/info['sig_len']
print(f"Media: {media}")

mean=np.mean(datos)
print(f"Media Numpy: {mean}")
```
# 2.Desviacion Estandar:
Se calcula la desviación estándar de la señal, que mide la dispersión de los valores respecto a la media:

a) Manualmente: Elevando al cuadrado la diferencia entre cada valor y la media, sumando y dividiendo por (N-1).
<img width="281" height="130" alt="image" src="https://github.com/user-attachments/assets/36535c07-807e-428f-89e5-865372383508" />
     |Ecu 2: Formula para calcular la Desviacion Estandar.|

b) Usando numpy.std(), con ddof=1 para la corrección muestral.
```python
#DESVIACION ESTANDAR 
resta=datos-media
#print(resta)
resta2=resta**2
#print(resta2)
sumatoriaresta=0
for i in resta2:
    sumatoriaresta += i    
#print(sumatoriaresta)
S=np.sqrt(sumatoriaresta/(info['sig_len']-1)) ###nan
print(f"Desviacion estandar: {S}")

desviacion_muestral = np.std(datos, ddof=1)  # ddof=1 para muestra
print(f"Desviación estándar Numpy: {desviacion_muestral:.4f}")
```
# 3.Coeficiente de Variación:
El siguiente segmento de nuestro código, consiste en calcular el coeficiente de variación (CV) que en este caso expresa la relación entre la desviación estándar y la media como un porcentaje, es decir, Indica la variabilidad de la señal en comparación con su valor promedio:
<img width="91" height="54" alt="image" src="https://github.com/user-attachments/assets/1c0ca418-bd8f-4493-8296-d96bbee02820" />
     |Ecu 3: Formula para calcular el Coeficiente de Variación.|
```python
#COEFICIENTE DE VARIACIÓN
CV =(S/media)*100
print(f"Coeficiente de Variación: {CV}%")

# Calcular coeficiente de variación (en porcentaje)
cv = (desviacion_muestral / mean) * 100
print(f"Coeficiente de Variación Numpy: {cv:.2f}%")
```
# 4.Calculo de la Curtosis
```python
#Curtosis
curtosis_valor = kurtosis(datos)
print(f"Curtosis: {curtosis_valor}")
```
# Comparación de resultados:
Los resultados obtenidos manualmente y mediante NumPy muestran una gran similitud, con diferencias mínimas en la precisión de los decimales como se puede evidenciar acontinuación:
<img width="335" height="106" alt="image" src="https://github.com/user-attachments/assets/e61fc008-8c52-4af6-a415-a3d7f577d9e9" />
    |Figura 2: Comparación de resultados (Manual vs NumPy) de los Estadisticos Descriptivos de La Media, Desviación Estandar y el Coeficiente de Variación.|
# 5..Histograma & Función de Probabilidad:
Este gráfico representa la distribución de amplitudes de la señal EMG mediante un histograma y una estimación de densidad Kernel (KDE). La estimación KDE suaviza la distribución, permitiendo observar de manera más clara la tendencia subyacente de los datos sin depender estrictamente del tamaño o posición de los intervalos del histograma.
En nuestro caso, la curva de densidad fue ajustada debido a que inicialmente presentaba valores excesivamente dispersos, lo que mejoró la visualización y facilitó la interpretación de la forma real de la distribución de la señal:
<img width="546" height="368" alt="image" src="https://github.com/user-attachments/assets/77abaea0-8e18-4548-bbf7-afc1e3566be1" />
|Figura 3: Resultado de Histograma junto con la Función de Pobabilidad (Campana de Gauss).|
```python
# Histograma con función de densidad
plt.close('all')  # Evita que se acumulen las gráficas anteriores
plt.figure(figsize=(8, 5))
plt.hist(datos, bins=50, density=True, alpha=0.6, color='orange', label='Histograma')

# Función de densidad usando KDE
kde = gaussian_kde(datos)
x_vals = np.linspace(min(datos), max(datos), 1000)
plt.plot(x_vals, kde(x_vals), color='blue', lw=2, label='Densidad KDE')
plt.title("Histograma con Función de Densidad")
plt.xlabel("Amplitud (mV)")
plt.ylabel("Densidad")
plt.legend()
plt.grid(True)
plt.show()
```
En la Figura 3 se presenta un histograma acompañado de la estimación de la función de densidad de probabilidad (curva de tipo Gauss) para la señal EMG procesada digitalmente.
Las barras naranjas representan la distribución de los valores de amplitud, evidenciando que la mayoría de los datos se concentran alrededor de 0 mV, con una forma aproximadamente simétrica.
La curva azul corresponde a la estimación de densidad de probabilidad obtenida mediante el método Kernel Density Estimation (KDE), la cual muestra un pico pronunciado en torno a 0 mV. Esto indica que la amplitud de la señal presenta una alta concentración en este valor y que la probabilidad de encontrar valores alejados es menor, sugiriendo que la distribución es simétrica respecto al eje donde se encuentra la media.

Cabe destacar que, para la construcción del histograma, se empleó la librería matplotlib.pyplot (plt), dividiendo los datos en 50 intervalos o bins. La estimación de la densidad se realizó utilizando la función gaussian_kde de la biblioteca SciPy, lo que permitió suavizar la distribución y obtener una representación más clara de la tendencia subyacente de la señal.

 # RELACIÓN SEÑAL RUIDO (SNR):
# Ruido en la Señal y Relación Señal-Ruido (SNR)
En nuestro contexto del procesamiento digital de señales, el ruido es cualquier perturbación no deseada que se superpone a la señal de interés, afectando su calidad y precisión. Estas interferencias pueden tener diversas fuentes, como componentes electrónicos, interferencias ambientales, artefactos fisiológicos (en señales biomédicas), o errores en la adquisición y transmisión de datos.

El ruido en una señal puede clasificarse en diferentes tipos, dependiendo de su origen y características, pues en este caso se utilizaron tres tipos de ruidos, los cueles son:

# 1.Ruido Gaussiano
Es un tipo de ruido que sigue una distribución normal o gaussiana, caracterizada por una media de 0 y una desviación estándar que varía en función de la potencia del ruido. Se trata de un ruido aleatorio con propiedades estadísticas bien definidas, lo que lo hace ideal para simulaciones y análisis de sistemas en entornos controlados. Su presencia es común en dispositivos electrónicos y en la transmisión de señales debido a fenómenos térmicos y otras fuentes aleatorias de interferencia.

# 2.Ruido de Impulso
Se caracteriza por la aparición de valores atípicos o picos de alta amplitud en momentos aleatorios dentro de la señal. Estos impulsos pueden ser positivos o negativos y tienen una duración muy breve en comparación con la señal original. Su impacto puede ser significativo, ya que introduce distorsiones abruptas que pueden alterar la interpretación de los datos. Es común en interferencias electromagnéticas, errores en la transmisión de datos y perturbaciones externas en sensores.

# 3.Ruido de Artefacto
Se refiere a señales espurias o no deseadas que se introducen en un sistema de adquisición debido a factores externos. En el caso de señales biomédicas, este ruido puede originarse por movimientos del paciente, contracciones musculares involuntarias o fallas en los electrodos. En otros sistemas, puede deberse a interferencias mecánicas, acoplamientos eléctricos o problemas en los dispositivos de medición. Su presencia es particularmente problemática en análisis donde se requiere una alta precisión, ya que puede enmascarar información clave.

# Relación Señal-Ruido (SNR):
La SNR es una métrica que cuantifica la calidad de una señal en presencia de ruido. Se define como la relación entre la potencia de la señal útil y la potencia del ruido, expresada en decibeles (dB):
<img width="286" height="57" alt="image" src="https://github.com/user-attachments/assets/df17c3e4-3697-4eb9-9f37-2d3413625b49" />
|Ecu. 4: Ecuacion para calcular el SNR en una señal Bimedica.|

Por lo anterior, tenemos la siguiente parte de nuestro codigo, en donde implmentamos la parte de la contaminacion de la señal con los 3 tipos de Ruidos mencionados con anterioridad, por lo que:
```python
# Función para calcular SNR
def calcular_snr(señal, ruido):
    potencia_señal = np.mean(señal ** 2)
    potencia_ruido = np.mean(ruido ** 2)
    return 10 * np.log10(potencia_señal / potencia_ruido)

# a) Ruido Gaussiano
ruido_std = np.std(datos) * 0.3
ruido_gauss = np.random.normal(0, ruido_std, size=len(datos))
señal_gauss = datos + ruido_gauss
snr_gauss = calcular_snr(datos, ruido_gauss)
print(f"SNR con Ruido Gaussiano: {snr_gauss:.2f} dB")

# b) Ruido de Impulso
porcentaje_impulsos = 0.05
num_impulsos = int(len(datos) * porcentaje_impulsos)
ruido_impulso = np.zeros_like(datos)
indices_impulsos = np.random.choice(len(datos), size=num_impulsos, replace=False)
ruido_impulso[indices_impulsos] = np.random.uniform(-2.5, 2.5, size=num_impulsos)
señal_impulso = datos + ruido_impulso
snr_impulso = calcular_snr(datos, ruido_impulso)
print(f"SNR con Ruido de Impulso: {snr_impulso:.2f} dB")

# c) Ruido Tipo Artefacto (60 Hz)
fs = info['fs']
t = np.arange(0, len(datos)) / fs
frecuencia_red = 60
amplitud_artefacto = 0.8
ruido_artefacto = amplitud_artefacto * np.sin(2 * np.pi * frecuencia_red * t)
señal_artefacto = datos + ruido_artefacto
snr_artefacto = calcular_snr(datos, ruido_artefacto)
print(f"SNR con Ruido Tipo Artefacto (60 Hz): {snr_artefacto:.2f} dB")
```
Ahora bien, luego de ello Este código genera cuatro gráficas de señales electromiográficas (EMG) usando la librería matplotlib en Python, en un solo gráfico con cuatro subgráficas.

-Primera subgráfica (señal EMG original).
-Segunda subgráfica (señal EMG contaminada con ruido Gaussiano).
-Tercera subgráfica (señal EMG contaminada con ruido de impulso).
-Cuarta subgráfica (señal EMG contaminada con ruido Tipo artefacto).
Por ende, el código está generando un gráfico con tres subgráficas, cada una mostrando una señal EMG diferente: la original, una contaminada por Ruido de Artefacto y otra contaminada por Ruido de Impulso como se mostrara a continuacion:
```python
# Comparación de señales
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(datos, color='c')
plt.title("Señal Original")
plt.grid()

plt.subplot(4, 1, 2)
plt.plot(señal_gauss, color='red')
plt.title("Señal con Ruido Gaussiano")
plt.grid()

plt.subplot(4, 1, 3)
plt.plot(señal_impulso, color='orange')
plt.title("Señal con Ruido de Impulso")
plt.grid()

plt.subplot(4, 1, 4)
plt.plot(señal_artefacto, color='purple')
plt.title("Señal con Ruido Tipo Artefacto (60 Hz)")
plt.grid()

plt.tight_layout()
plt.show()
```
<img width="546" height="355" alt="image" src="https://github.com/user-attachments/assets/c508ea75-528f-49f3-949e-087ab23b3fe1" />
|Figura 4: Señal EMG original y contaminada con diferentes tipos de ruido|
En esta imagen (Figura 4) podemos decir que:

-Señal EMG Original (cian): Muestra variaciones de amplitud en un rango moderado, con picos característicos de la actividad muscular propia de una señal de electromiografía.

-Señal EMG con Ruido Gaussiano (rojo): Presenta una dispersión aleatoria sobre toda la señal, generando un aspecto más “rugoso” debido a la adición de ruido blanco gaussiano.

-Señal EMG con Ruido de Impulso (naranja): Se aprecian picos abruptos e irregulares en amplitud, simulando artefactos producidos por interferencias externas o fallos de adquisición.

-Señal EMG con Ruido Tipo Artefacto (60 Hz) (morado): Se evidencia una oscilación periódica superpuesta a la señal original, típica de la interferencia eléctrica de la red.

Este análisis comparativo permite identificar visualmente cómo cada tipo de ruido modifica la morfología de la señal EMG original, afectando su interpretación y potencial diagnóstico.

Esta parte del código tambien se encarga de calcular la SNR para evaluar la calidad de la señal de electromiografía (EMG) en presencia de distintos tipos de ruido, por lo que tenemos la implementacion de la Ecu. 4 para poder obtener la Relacion Señal-Ruido (SNR), en donde obtuvimos los siguientes resultados:
<img width="329" height="52" alt="image" src="https://github.com/user-attachments/assets/d6fc6dac-8afc-474d-bacc-848233238352" />
|Figura 5: Resultados obtenidos mediante la implementacion de la ecuacion de SNR.|
Resultados de SNR para la señal EMG contaminada con distintos tipos de ruido

A partir de los cálculos realizados, se obtuvieron los siguientes valores de relación señal-ruido (SNR) para cada tipo de ruido añadido a la señal EMG:

# Ruido Gaussiano:
Presenta el SNR más alto de los tres casos, con 10.73 dB, lo que indica que su efecto sobre la señal es el menos perjudicial. A pesar de la presencia de este ruido, la señal conserva una buena proporción de información útil frente al ruido.

# Ruido de Impulso:
Obtiene un SNR de 3.01 dB, lo que refleja un mayor impacto negativo sobre la calidad de la señal en comparación con el ruido gaussiano. Los picos abruptos generados por este tipo de ruido reducen notablemente la claridad de la señal.

# Ruido Tipo Artefacto (60 Hz):
Presenta un SNR de -2.37 dB, el valor más bajo y negativo, lo que indica que el ruido domina por completo la señal útil. Esta interferencia periódica de la red eléctrica es la más invasiva y afecta severamente la interpretabilidad de la señal EMG.

En conclusión, el ruido gaussiano fue el menos destructivo, mientras que el ruido de artefacto a 60 Hz resultó ser el más perjudicial, seguido del ruido de impulso. Estos resultados evidencian la importancia de aplicar técnicas de filtrado y acondicionamiento específicas según el tipo de ruido presente.

# Información Adicional:
Para finalizar es bueno que se tenga presenta optimizar el SNR en las señales biomedicas, teniendo en cuenta que el rango ideal según la literatura para una señal EMG de calidad aceotable debe estar entre 15 dB y 30 dB para poder garantizar mediciones precisas y presentaciones gráficas fieles de la señal capturada, puesto que un valor elevado de SNR implica que la señal sea más clara en comparación con el ruido y un SNR bajo dificulta la identificación de caracteristicas relevantes debido a la presencia dominante del ruido.
# Conclusión
Esta práctica permitió aplicar técnicas de análisis estadístico y procesamiento de señales sobre una señal EMG asociada a neuropatía, destacando la importancia de evaluar y mejorar la calidad de señales biomédicas para optimizar diagnósticos en el área de la salud.
Los resultados obtenidos muestran que el análisis de parámetros como la media, desviación estándar, coeficiente de variación, curtosis y la relación señal-ruido (SNR) permite identificar de forma precisa el impacto de distintos tipos de ruido en la señal. Además, se evidencia que algunos ruidos, como el de red (60 Hz), son más críticos y requieren estrategias específicas de filtrado y acondicionamiento.

# Librerías utilizadas
os → Ubicación y manejo de directorios.
wfdb → Carga y manejo de señales fisiológicas.
matplotlib.pyplot as plt → Gráficas y visualización.
numpy as np → Operaciones matemáticas y manejo de arreglos.
scipy.stats → norm, gaussian_kde para análisis estadístico y estimaciones de densidad.
statistics → Cálculos estadísticos adicionales.

# Bibliografía

[1] Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, PC, Mark, R., ... y Stanley, HE (2000). PhysioBank, PhysioToolkit y PhysioNet: componentes de un nuevo recurso de investigación para señales fisiológicas complejas. Circulation [En línea]. 101 (23), págs. e215–e220.

#Licencia
DOI (versión 1.0.0): https://doi.org/10.13026/C24S3D
Temas: neuropatía / electromiografía.





