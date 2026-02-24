import numpy as np
import matplotlib.pyplot as plt

# --- 1. CONFIGURATION: Temporal Domain Specification ---
# Sampling Frequency: 1000 Hz | Duration: 1.0 Second
# Defining a discrete time vector for digital signal processing.
t = np.linspace(0, 1, 1000) 

# --- 2. SYNTHESIS: Generating Reference Signal Classes ---

# Class A: Deterministic Sinusoidal Waveform (Analog Modeling)
# Represents periodic periodic signals found in communication systems.
sine_wave = np.sin(2 * np.pi * 5 * t)

# Class B: Rectangular Pulse Train (Digital Switching Logic)
# Modeling idealized bit-stream transitions using signum functions.
square_wave = np.sign(np.sin(2 * np.pi * 5 * t))

# Class C: Stochastic Gaussian Noise (Spectral Interference)
# Simulating thermal electronic interference using a Normal Distribution.
noise = np.random.normal(0, 0.5, 1000)

# --- 3. ANALYSIS: Multi-Panel Temporal Visualization ---
# Generating high-resolution plots for signal characterization.
plt.figure(figsize=(10, 8))

# Subplot: Sinusoidal Analysis
plt.subplot(3, 1, 1)
plt.plot(t, sine_wave, color='royalblue', linewidth=1.5)
plt.title("Class A: Deterministic Sinusoidal Waveform (Reference)")
plt.ylabel("Amplitude")
plt.grid(True, alpha=0.3)

# Subplot: Square Waveform Analysis
plt.subplot(3, 1, 2)
plt.plot(t, square_wave, color='forestgreen', linewidth=1.5)
plt.title("Class B: Rectangular Pulse Train (Digital Pulse)")
plt.ylabel("Amplitude")
plt.grid(True, alpha=0.3)

# Subplot: Gaussian Noise Analysis
plt.subplot(3, 1, 3)
plt.plot(t, noise, color='crimson', linewidth=0.8)
plt.title("Class C: Stochastic Gaussian Noise (Interference)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True, alpha=0.3)

plt.tight_layout()
print("Waveform synthesis complete. Visualizing results...")
plt.show()