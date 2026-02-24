import os
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Ensuring the execution context is aligned with the local directory.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# --- 1. DATA ACQUISITION: Importing Validated Reference Waveforms ---
# These datasets represent high-fidelity signals synthesized in MATLAB.
def import_reference_data(filename):
    try:
        # Flattening multidimensional arrays for temporal consistency.
        return pd.read_csv(filename, header=None).values.flatten()
    except FileNotFoundError:
        print(f"CRITICAL ERROR: Resource {filename} unreachable. Verify local directory.")
        return None

# Loading reference classes generated through MATLAB-based modeling.
ref_sine = import_reference_data('sine_lab.csv')
ref_gaussian = import_reference_data('gaussian_lab.csv')
ref_exponential = import_reference_data('exponential_lab.csv')

# --- 2. FEATURE ENGINEERING: Statistical Descriptor Extraction ---
def compute_descriptors(signal):
    """
    Extracts statistical markers: Spectral Variance and Temporal Oscillation Rate.
    """
    if signal is None: return [0, 0]
    spectral_variance = np.std(signal)
    oscillation_rate = ((signal[:-1] * signal[1:]) < 0).sum()
    return [spectral_variance, oscillation_rate]

# Constructing the Training Feature Matrix (X) and Target Vector (y).
X = np.array([
    compute_descriptors(ref_sine), 
    compute_descriptors(ref_gaussian), 
    compute_descriptors(ref_exponential)
])
y = np.array(["Deterministic_Sine", "Stochastic_Gaussian", "Exponential_Decay"])

# --- 3. MODEL INITIALIZATION: Decision Tree Classifier Architecture ---
# Implementing a deterministic classifier for real-time waveform identification.
inference_engine = DecisionTreeClassifier()
inference_engine.fit(X, y)

print("--- CROSS-PLATFORM SIGNAL VALIDATION SYSTEM ---")
print(f"Inference Engine successfully initialized on {len(y)} reference classes.\n")

# --- 4. EXPERIMENTAL VALIDATION: Real-Time Inference on Unlabeled Data ---
# Simulating a real-world acquisition by adding noise to a reference signal.
unlabeled_input = ref_sine + np.random.normal(0, 0.05, len(ref_sine))

# Extracting descriptors for the test subject.
input_features = np.array([compute_descriptors(unlabeled_input)])

# Executing the prediction logic.
classification_result = inference_engine.predict(input_features)

print("--- REAL-TIME INFERENCE ENGINE OUTPUT ---")
print(f"Analyzed Waveform Profile Identified as: {classification_result[0]}")