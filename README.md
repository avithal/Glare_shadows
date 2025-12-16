# Shadow & Sun-Glare Augmentation (OpenCV)

This repository contains **preliminary, research-oriented code** for generating **synthetic shadow and sun-glare artifacts** in images using **classical computer vision techniques (OpenCV)**.

The goal is to improve **model robustness** to real-world imaging conditions such as harsh illumination, partial occlusions, and overexposure.

This work is intentionally lightweight and interpretable, focusing on **controllable augmentations** rather than learned generative models.

---
![input](Data/Input/original.png)
____
![output](DATA/Output/20251216_125749_aug.png)

## 🎯 Motivation

Many real-world vision systems suffer performance degradation due to:
- Strong directional lighting
- Shadows cast by objects or environment
- Sun glare and overexposed regions

This project explores **deterministic augmentations** that can be:
- Easily integrated into training pipelines
- Controlled by parameters
- Debugged and visualized

---

## 🧠 Implemented Augmentations

### ☁️ Shadow Augmentation
- Random polygon shadow masks
- Smooth alpha blending
- Variable intensity and softness
- Partial image coverage

**Key ideas**
- Simulate occlusion and uneven illumination
- Preserve image structure while reducing local contrast

---

### ☀️ Sun-Glare / Overexposure Augmentation
- Radial brightness increase
- Gaussian falloff from a random light source

**Key ideas**
- Simulate sensor saturation
- Stress-test robustness to highlights and glare

---

## 🛠️ Tech Stack

- Python 3.9+
- OpenCV
- NumPy

---

## 📂 Repository Structure

```text
.
├── Data/
│   ├── Input/       
│   └── output/
├── DATA/
│   └── demo.py            
├── AugmentationsShadowGlare.md # Visualization examples
├── README.md
├── requirements.txt
