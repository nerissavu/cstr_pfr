# Chemical reactors are central to chemical engineering processes, where chemical reactions occur under controlled conditions. Develop a Python-based calculator for designing an isothermal Continuous Stirred Tank Reactor (CSTR) and a Plug Flow Reactor (PFR) for a first-order irreversible reaction. This app will calculate the reactor volume required to achieve a specified conversion and compare the performance of CSTR and PFR reactors.
# The app will:
# •	Calculate the reactor volume (V) for both CSTR and PFR given the feed rate, rate constant, and target conversion.
# •	Compare the performance of CSTR and PFR, showing the volume required to achieve the same conversion in both reactors.
# •	Plot the conversion profile for a PFR along the reactor length and the conversion as a function of reactor volume for the CSTR.
# •	Allow the user to input reaction rate constants, flow rates, and initial concentrations, and dynamically adjust the conversion and reactor volumes.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import streamlit as st

def cstr_volume(F, k, CAi, X):
    """Calculate CSTR volume."""
    return F * X / (k * CAi * (1 - X))

def pfr_volume(F, k, CAi, X):
    """Calculate PFR volume."""
    return -F / (k * CAi) * np.log(1 - X)

def pfr_conversion_profile(V, F, k, CAi):
    """Calculate PFR conversion profile."""
    return 1 - np.exp(-k * CAi * V / F)

def cstr_conversion_profile(V, F, k, CAi):
    """Calculate CSTR conversion profile."""
    return k * CAi * V / (F + k * CAi * V)

def main():
    st.title("CSTR and PFR Reactor Design Calculator")
    
    # User inputs
    F = st.number_input("Volumetric flow rate (L/min)", min_value=0.1, value=10.0, step=0.1)
    k = st.number_input("Reaction rate constant (1/min)", min_value=0.001, value=0.1, step=0.001)
    CAi = st.number_input("Initial concentration (mol/L)", min_value=0.1, value=1.0, step=0.1)
    X_target = st.slider("Target conversion", min_value=0.0, max_value=0.99, value=0.8, step=0.01)

    # Calculate reactor volumes
    V_cstr = cstr_volume(F, k, CAi, X_target)
    V_pfr = pfr_volume(F, k, CAi, X_target)

    # Display results
    st.subheader("Reactor Volumes")
    st.write(f"CSTR Volume: {V_cstr:.2f} L")
    st.write(f"PFR Volume: {V_pfr:.2f} L")
    st.write(f"Volume Ratio (PFR/CSTR): {V_pfr/V_cstr:.2f}")

    # Plot conversion profiles
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # PFR conversion profile
    V_range = np.linspace(0, V_pfr * 1.2, 100)
    X_pfr = pfr_conversion_profile(V_range, F, k, CAi)
    ax1.plot(V_range, X_pfr)
    ax1.set_xlabel("Reactor Volume (L)")
    ax1.set_ylabel("Conversion")
    ax1.set_title("PFR Conversion Profile")
    ax1.grid(True)

    # CSTR conversion profile
    V_range = np.linspace(0, V_cstr * 1.2, 100)
    X_cstr = cstr_conversion_profile(V_range, F, k, CAi)
    ax2.plot(V_range, X_cstr)
    ax2.set_xlabel("Reactor Volume (L)")
    ax2.set_ylabel("Conversion")
    ax2.set_title("CSTR Conversion Profile")
    ax2.grid(True)

    st.pyplot(fig)

if __name__ == "__main__":
    main()