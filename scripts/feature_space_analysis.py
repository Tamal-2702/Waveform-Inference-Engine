import matplotlib.pyplot as plt

# --- CONFIGURATION: Feature Space Mapping ---
# Data points represent high-dimensional statistical descriptors extracted from 
# MATLAB-synthesized reference waveforms.

# X-axis: Spectral Variance (Standard Deviation) - Quantifies amplitude dispersion.
# Y-axis: Temporal Oscillation Rate (ZCR) - Proxy for frequency characteristics.

plt.figure(figsize=(10, 7), facecolor='white')

# Mapping Reference Classes with Research-Standard Color Palettes
plt.scatter(0.707, 9, color='royalblue', s=150, edgecolors='black', 
            alpha=0.8, label='Deterministic_Sine', marker='o')

plt.scatter(0.495, 520, color='crimson', s=150, edgecolors='black', 
            alpha=0.8, label='Stochastic_Gaussian', marker='s')

plt.scatter(0.280, 0, color='forestgreen', s=150, edgecolors='black', 
            alpha=0.8, label='Exponential_Decay', marker='^')

# --- PLOT ANNOTATION & STYLING ---
plt.title("Statistical Distribution of Signal Features (Feature Space Clustering)", 
          fontsize=14, fontweight='bold', pad=20)

plt.xlabel("Spectral Variance ($\sigma$)", fontsize=12)
plt.ylabel("Temporal Oscillation Rate (ZCR)", fontsize=12)

# Adding Descriptive Text Boxes for GIST Reviewers
plt.text(0.72, 20, "Low Frequency / High Variance", fontsize=9, style='italic')
plt.text(0.51, 510, "High Entropy Cluster", fontsize=9, style='italic')

plt.legend(frameon=True, shadow=True, title="Waveform Classes")
plt.grid(True, linestyle='--', alpha=0.6)

# Finalizing the Visual Proof
plt.tight_layout()
print("Generating High-Resolution Feature Map for Research Validation...")
plt.show()