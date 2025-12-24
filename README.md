![Build](https://img.shields.io/badge/Build-Stable-brightgreen)
![Language](https://img.shields.io/badge/Python-3.x-blue)
![Domain](https://img.shields.io/badge/Domain-Generative%20Art-purple)
![Math](https://img.shields.io/badge/Math-Parametric%20Curves-indigo)
![Output](https://img.shields.io/badge/Output-High--Resolution%20PNG-orange)
![License](https://img.shields.io/badge/License-MIT-green)

# 🎨 Chromatic Spirograph Generator

A **mathematics-driven generative art engine** that creates high-resolution, rainbow-colored spirograph patterns using **NumPy**, **Matplotlib**, and **HSV color space interpolation**.

This project blends **geometry**, **parametric equations**, and **color theory** to generate visually striking digital artwork.

---

## ✨ What This Project Does

- Generates complex **Spirograph / Hypotrochoid** curves using parametric equations
- Applies a **smooth rainbow gradient** using HSV → RGB conversion
- Renders ultra-clean line art on a **black canvas**
- Exports high-resolution artwork suitable for wallpapers, prints, or NFTs

---

## 🧠 Mathematical Foundation

The curve is generated using the **hypotrochoid equation**:

\[
x(\theta) = (R - r)\cos(\theta) + d\cos\left(\frac{R - r}{r}\theta\right)
\]

\[
y(\theta) = (R - r)\sin(\theta) - d\sin\left(\frac{R - r}{r}\theta\right)
\]

Where:
- **R** = Radius of fixed circle  
- **r** = Radius of rolling circle  
- **d** = Distance from rolling circle center  
- **θ** = Angle parameter  

---

## 🌈 Color System

- Uses **HSV color space** for smooth perceptual gradients
- Hue is mapped linearly across curve length
- Converted to RGB for plotting via `colorsys`

This ensures **no banding** and perfect color continuity.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **NumPy** — numerical computation
- **Matplotlib** — rendering engine
- **colorsys** — HSV → RGB conversion

---

## 🚀 How to Run

### 1️⃣ Install dependencies
```bash
pip install numpy matplotlib
