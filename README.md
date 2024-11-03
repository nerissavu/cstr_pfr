# 🧪 Chemical Reactor Design Calculator

A [Streamlit](https://streamlit.io)-based calculator for designing and comparing Continuous Stirred Tank Reactor (CSTR) and Plug Flow Reactor (PFR) systems for first-order irreversible reactions.

## 🎯 Key Features

* Calculate reactor volumes for specified conversions
* Compare CSTR and PFR performance
* Plot conversion profiles along reactor length
* Interactive parameter adjustment
* Real-time calculation updates
* Performance comparison visualizations

## 🧮 Calculations

The calculator performs the following analyses:
* CSTR Volume: V = FX/(k*CAi*(1-X))
* PFR Volume: V = -F/(k*CAi)*ln(1-X)
* Conversion profiles for both reactor types
* Volume ratio comparisons

## 📊 Input Parameters

* Operating Conditions:
  * Volumetric flow rate (F)
  * Reaction rate constant (k)
  * Initial concentration (CAi)
  * Target conversion (X)

## 💻 How to Use

1. Enter the required parameters:
   * Flow rate (L/min)
   * Rate constant (1/min)
   * Initial concentration (mol/L)
   * Target conversion

2. The calculator will automatically:
   * Compute required reactor volumes
   * Generate conversion profiles
   * Display comparative analysis
   * Plot performance curves

## 📈 Output

The calculator provides:
* Required reactor volumes
* Volume ratio comparison
* Conversion profiles for both reactors
* Performance visualization graphs
* Numerical results summary

## 🔬 Theory

The calculations are based on:
* Mass balance equations
* First-order reaction kinetics
* Ideal reactor assumptions
* Design equations for:
  * CSTR: Perfect mixing
  * PFR: Plug flow behavior
