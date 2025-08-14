# Laboratorio señal 1 

RESUMEN




INTRODUCION 







1) Investigación: ¿Qué es la Relación Señal‑Ruido ?
   
La relación señal‑ruido  cuantifica cuánta energía útil de la señal está presente respecto a la energía del ruido que la contamina. Se expresa típicamente en decibelios (dB):
SNR(dB) = 10·log10(Pseñal / Pruido) = 20·log10(Aseñal_rms / A_ruido_rms)
• P es la potencia media (RMS²)
• SNR alto ⇒ señal clara; SNR bajo o negativo ⇒ el ruido domina.
Cómo estimar SNR en biomédicas (EMG):
• Con referencia limpia (caso ideal): x = s + n. Si conozco s (limpia) y el ruido inyectado n, calculo Ps y Pn directamente.
• Sin referencia (registro real): aproximamos Pn con tramos de reposo, filtrado pasa‑banda o residual (señal contaminada − señal filtrada).
En EMG de superficie, SNRs típicos pueden ir de ~0–20 dB dependiendo de electrodos, movimiento, impedancia de piel y tipo de contracción. En neuropatías, la amplitud útil puede ser menor, lo que tiende a reducir el SNR.
