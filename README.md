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


1) Investigación: ¿Qué es la Relación Señal‑Ruido ?
   
La relación señal‑ruido  cuantifica cuánta energía útil de la señal está presente respecto a la energía del ruido que la contamina. Se expresa típicamente en decibelios (dB):
SNR(dB) = 10·log10(Pseñal / Pruido) = 20·log10(Aseñal_rms / A_ruido_rms)
• P es la potencia media (RMS²)
• SNR alto ⇒ señal clara; SNR bajo o negativo ⇒ el ruido domina.
Cómo estimar SNR en biomédicas (EMG):
• Con referencia limpia (caso ideal): x = s + n. Si conozco s (limpia) y el ruido inyectado n, calculo Ps y Pn directamente.
• Sin referencia (registro real): aproximamos Pn con tramos de reposo, filtrado pasa‑banda o residual (señal contaminada − señal filtrada).
En EMG de superficie, SNRs típicos pueden ir de ~0–20 dB dependiendo de electrodos, movimiento, impedancia de piel y tipo de contracción. En neuropatías, la amplitud útil puede ser menor, lo que tiende a reducir el SNR.


2) Método  aplicado a EMG de neuropatía
Trabajamos  con una señal EMG tipo neuropatía y se  contaminarion con tres clases de ruido. El cálculo de este se hizo con la fórmula de potencia (conociendo el ruido inyectado en cada caso).
Notas prácticas:
– Implementado en Python (Spyder) 
– EMG sintética tipo neuropatía (bandpass 20–150 Hz + ráfagas).– Frecuencia de muestreo: 1000 Hz, duración: 10 s.
(a) Ruido gaussiano:
• Modelo: ruido blanco normal de media 0 con σ=0.35·σEMG.
• Motivación: modela ruido térmico/electrónico y parte del ruido ambiental.
• SNR medido: ≈ 9.10 dB.
(b) Ruido de impulso:
• Modelo: picos esporádicos de gran amplitud (prob.=0.004 por muestra, factor=9·σ).
• Motivación: simula falsos contactos/descargas breves.
• SNR medido: ≈ 4.89 dB.
(c) Ruido tipo artefacto:
• Modelo compuesto: deriva de línea base (0.3 Hz)
• Motivación: reproduce perturbaciones reales comunes en EMG clínica.
• SNR medido: ≈ −0.99 dB (el ruido domina a la señal).



