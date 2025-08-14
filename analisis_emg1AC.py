#------------PARTE A: Análisis Estadístico de la Señal Original---------------
"Laboratorio 1 - Análisis estadístico de señal EMG"

import os
import wfdb
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
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


# Cálculos estadísticos corregidos para CV
n = info['sig_len']

# Media y desviación estándar manual
media_manual = np.sum(datos) / n
desv_manual = np.sqrt(np.sum((datos - media_manual) ** 2) / (n - 1))

# CV usando la media absoluta
media_abs = np.mean(np.abs(datos))
cv_manual = (desv_manual / media_abs) * 100

# Media y desviación estándar con NumPy
media_numpy = np.mean(datos)
desv_numpy = np.std(datos, ddof=1)

# CV con NumPy usando media absoluta
cv_numpy = (desv_numpy / media_abs) * 100

#Curtosis
from scipy.stats import kurtosis
curtosis_valor = kurtosis(datos)

# Mostrar los datos estadisticos
print("--------------DATOS ESTADISTICOS:----------------")
print(f"Media (manual): {media_manual:.4f}")
print(f"Media (NumPy): {media_numpy:.4f}")
print(f"Desviación estándar (manual): {desv_manual:.4f}")
print(f"Desviación estándar (NumPy): {desv_numpy:.4f}")
print(f"Coeficiente de variación (manual): {cv_manual:.2f}%")
print(f"Coeficiente de variación (NumPy): {cv_numpy:.2f}%")
print(f"Curtosis: {curtosis_valor}")




# ------------PARTE C: Contaminación de señal y cálculo de SNR--------------

# Calculo del SNR
def calcular_snr(señal, ruido):
    potencia_señal = np.mean(señal ** 2)
    potencia_ruido = np.mean(ruido ** 2)
    return 10 * np.log10(potencia_señal / potencia_ruido)

# a. Calculo del SNR contaminado del Ruido Gaussiano
ruido_std = np.std(datos) * 0.3
ruido_gauss = np.random.normal(0, ruido_std, size=len(datos))
señal_gauss = datos + ruido_gauss
snr_gauss = calcular_snr(datos, ruido_gauss)
print(f"SNR con Ruido Gaussiano: {snr_gauss:.2f} dB")

# b. Calculo del SNR contaminado del Ruido de Impulso
porcentaje_impulsos = 0.05  # 5% de la señal
num_impulsos = int(len(datos) * porcentaje_impulsos)
ruido_impulso = np.zeros_like(datos)
indices_impulsos = np.random.choice(len(datos), size=num_impulsos, replace=False)
ruido_impulso[indices_impulsos] = np.random.uniform(-2.5, 2.5, size=num_impulsos)
señal_impulso = datos + ruido_impulso
snr_impulso = calcular_snr(datos, ruido_impulso)
print(f"SNR con Ruido de Impulso: {snr_impulso:.2f} dB")

# c. Calculo del SNR contaminado del Ruido tipo artefacto (ej. interferencia de red 60 Hz)
fs = info['fs']  # frecuencia de muestreo
t = np.arange(0, len(datos)) / fs
frecuencia_red = 60  # Hz
amplitud_artefacto = 0.8
ruido_artefacto = amplitud_artefacto * np.sin(2 * np.pi * frecuencia_red * t)
señal_artefacto = datos + ruido_artefacto
snr_artefacto = calcular_snr(datos, ruido_artefacto)
print(f"SNR con Ruido Tipo Artefacto (60 Hz): {snr_artefacto:.2f} dB")

# Comparacion de señal original con las contaminadas
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
