# 📡 Automated Waveform Characterization & Inference Pipeline
> **A Hybrid MATLAB-Python Framework for Signal Integrity & Pattern Recognition**

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![MATLAB](https://img.shields.io/badge/MATLAB-R2023-orange?style=for-the-badge&logo=mathworks)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-green?style=for-the-badge&logo=scikit-learn)

---

## 🔬 Research Abstract
This project addresses the challenge of autonomous signal identification in complex electronic environments. By bridging **MATLAB-based mathematical synthesis** with **Python-driven Machine Learning**, I developed a pipeline that extracts deterministic features from raw temporal data to classify unlabeled waveforms. The system is designed to distinguish between periodic analog signals, digital pulse trains, and stochastic interference, providing a scalable solution for signal integrity monitoring.

---

## 📐 System Architecture
The framework is divided into three core functional layers:

1.  **Synthesis Layer (`waveform_engine.py`):** Generates high-fidelity reference classes—Deterministic Sinusoidal, Rectangular Pulse, and Stochastic Gaussian models.
2.  **Descriptor Layer (`signal_descriptors.py`):** A feature engineering engine that computes **Spectral Variance ($\sigma$)** and **Temporal Oscillation Rates (ZCR)**.
3.  **Inference Layer (`automated_inference_system.py`):** Implements a Decision Tree Classifier trained on validated reference datasets to perform real-time waveform profiling.

---

## 📈 Experimental Results & Validation

### 1. High-Fidelity Waveform Synthesis
The pipeline generates three distinct classes of signals for characterization. This provides the mathematical ground truth for training the inference engine.
![Waveform Engine Output](results/Figure_1(WE).png)

### 2. Statistical Feature Space Mapping
By extracting spectral and temporal markers, the system creates deterministic clusters in the feature space. This visualization confirms 100% separation between the reference signal morphologies.
![Feature Space Mapping](results/Figure_2(FSA).png)

### 3. Real-Time Inference Performance
The trained engine successfully identifies unlabeled, noisy inputs by mapping them to the high-precision reference clusters. 
![Inference Engine Output](results/image_5e147a.png)

---

## 📂 Repository Structure
```text
├── data/               # Validated CSV datasets exported from MATLAB
├── scripts/            # Core Python inference and descriptor scripts
├── results/            # High-resolution visualization and shell outputs
└── docs/               # Academic references and laboratory documentation'
```

---

## 🚀 Installation & Usage
### 1. Dependencies: Ensure numpy, pandas, matplotlib, and scikit-learn are installed.

### 2. Execution: Run scripts/automated_inference_system.py to initialize the model and validate against test inputs.

### 3. Visualization: Run scripts/feature_space_analysis.py to generate the statistical distribution map.

---

## 🎓 Academic Profile

Institution: Gauhati University

Department: Electronics and Communication Engineering

Researcher: Tamal Ghosh (Roll: 240101045)

Core Competencies: Signal Processing, Machine Learning, MATLAB-Python Integration.

----
