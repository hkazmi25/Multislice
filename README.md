# Multislice Simulation – Atomic Potential of Polonium

This repository contains a Python script that implements key concepts from **Chapter 5 of _Advanced Computing in Electron Microscopy_ by Earl J. Kirkland**. The code serves as a foundational tool for understanding atomic potentials, projected potentials, scattering factors, and transmission functions — all essential to building advanced multislice simulations in transmission electron microscopy (TEM).

## 🧪 Objective

The main purpose of this code is to:

- Illustrate the computation of atomic and projected potentials for the Polonium (Po) atom.
- Compute interaction parameters, scattering factors, and transmission functions.
- Provide a stepping stone for further development of advanced-level multislice electron microscopy simulation tools.

## 📘 Book Reference

**Advanced Computing in Electron Microscopy**  
Earl J. Kirkland  
Chapter 5 – Atomic Potentials and Multislice Formalism

## 📂 Features of the Script

- **Atomic Potential Calculation** using parameterized exponential sums.
- **Interaction Parameter (σ)** vs. Electron Energy plot.
- **Projected Atomic Potential** computation (integrated along the z-axis).
- **Scattering Factors** computation and plotting.
- **Transmission Function** for a single Po atom based on the calculated potentials.

## 📊 Output

The script uses `matplotlib` to generate multiple plots:

1. Interaction parameter vs. electron energy.
2. Atomic potential vs. radial distance.
3. Projected atomic potential.
4. Scattering factor vs. scattering angle.
5. Transmission function (visual representation).

## 📦 Dependencies

Make sure the following Python libraries are installed:

```bash
numpy
matplotlib
scipy
```

## ▶️ How to Run

Simply run the Python script using:

```bash
python multislice_po_atom.py
```

## 🧠 Future Extensions
1. The code is adapted for educational purposes and provides clarity on the basic building blocks of multislice simulations.
2. The Po atom parameters are directly taken from Kirkland's tables.
3. Integrate this into a full multislice simulation framework.
4. Extend support to other atomic species.
5. Implement FFT-based convolution for wave propagation.

## 📄 License
This project is intended for academic and educational purposes. Please cite the original book by Earl J. Kirkland if you build upon this work.

