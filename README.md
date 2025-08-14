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



