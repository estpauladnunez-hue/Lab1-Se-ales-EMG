#------------PARTE A: Análisis Estadístico de la Señal Original---------------
"Laboratorio 1 - Análisis estadístico de señal EMG"

import os
import wfdb
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde, kurtosis
plt.close('all') 

# Vincular la carpeta como directorio
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

# ====================== CÁLCULOS ESTADÍSTICOS ======================

# MEDIA MANUAL
sumatoriadatos = 0
for i in datos:
    sumatoriadatos += i
media = sumatoriadatos / info['sig_len']
print(f"Media: {media}")

# MEDIA NUMPY
mean = np.mean(datos)
print(f"Media Numpy: {mean}")

# DESVIACIÓN ESTÁNDAR MANUAL
resta = datos - media
resta2 = resta ** 2
sumatoriaresta = 0
for i in resta2:
    sumatoriaresta += i
S = np.sqrt(sumatoriaresta / (info['sig_len'] - 1))
print(f"Desviación estándar: {S}")

# DESVIACIÓN ESTÁNDAR NUMPY
desviacion_muestral = np.std(datos, ddof=1)  # ddof=1 para muestra
print(f"Desviación estándar Numpy: {desviacion_muestral:.4f}")

# COEFICIENTE DE VARIACIÓN MANUAL
CV = (S / media) * 100
print(f"Coeficiente de Variación: {CV}%")

# COEFICIENTE DE VARIACIÓN NUMPY
cv = (desviacion_muestral / mean) * 100
print(f"Coeficiente de Variación Numpy: {cv:.2f}%")

# Curtosis
curtosis_valor = kurtosis(datos)
print(f"Curtosis: {curtosis_valor}")

# ------------PARTE C: Contaminación de señal y cálculo de SNR--------------

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