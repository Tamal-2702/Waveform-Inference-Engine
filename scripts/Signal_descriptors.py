import numpy as np
import pandas as pd

def compute_signal_descriptors(signal, class_label):
    """
    Extracts high-dimensional statistical descriptors from raw temporal data.
    """
    # Descriptor 1: Spectral Variance / Standard Deviation
    # Quantifies the dispersion of signal amplitudes from the mean.
    variance_metric = np.std(signal)
    
    # Descriptor 2: Temporal Oscillation Rate (Zero-Crossing Rate)
    # Measures the rate of sign-changes, serving as a proxy for fundamental frequency.
    oscillation_rate = ((signal[:-1] * signal[1:]) < 0).sum()
    
    return {
        'Spectral_Variance': variance_metric, 
        'Oscillation_Rate': oscillation_rate, 
        'Target_Class': class_label
    }

# --- Data Acquisition Simulation ---
t = np.linspace(0, 1, 1000)
deterministic_sine = np.sin(2 * np.pi * 5 * t)
rectangular_pulse = np.sign(np.sin(2 * np.pi * 5 * t))
stochastic_noise = np.random.normal(0, 0.5, 1000)

# --- Feature Space Construction ---
# Aggregating descriptors into a structured analytical framework.
dataset_registry = []
dataset_registry.append(compute_signal_descriptors(deterministic_sine, "Deterministic_Sine"))
dataset_registry.append(compute_signal_descriptors(rectangular_pulse, "Rectangular_Pulse"))
dataset_registry.append(compute_signal_descriptors(stochastic_noise, "Stochastic_Noise"))

# Output formalization using DataFrames
feature_matrix = pd.DataFrame(dataset_registry)

print("--- SIGNAL ATTRIBUTE CHARACTERIZATION MATRIX ---")
print(feature_matrix)