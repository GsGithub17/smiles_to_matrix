# Tanimoto Similarity Matrix


## Overview


This repository contains a Python script for generating a Tanimoto similarity heatmap. The heatmap visually represents the pairwise similarity between molecular compounds, calculated using their SMILES (Simplified Molecular Input Line Entry System) representations. The script uses RDKit to compute molecular fingerprints and then calculates the Tanimoto similarity between these fingerprints.

## Features

* Calculation of ECFP (Extended-Connectivity Fingerprints) from SMILES strings.
* Computation of pairwise Tanimoto similarity for a set of molecular compounds.
* Generation of a heatmap with Seaborn and Matplotlib, displaying the similarity matrix.
* Inclusion of compound IDs as tick labels on the heatmap for easy identification.

## Prerequisites

* RDKit
* Pandas
* NumPy
* Seaborn
* Matplotlib

These can be installed via pip using the following command:

```bash 
pip install rdkit-pypi pandas numpy seaborn matplotlib
```
## Usage

1. Prepare a CSV file containing molecular compounds with the following columns:
  - ID: Unique identifier for each compound.
  - SMILES: SMILES representation of the compound.
2. Run the script, which reads the CSV file, computes the Tanimoto similarity matrix, and generates a heatmap.

## Example

To generate a heatmap, execute the script with your CSV file as input. Ensure that your file is formatted correctly and that the required columns (ID and SMILES) are present.

```python
#Example usage of the script
df = pd.read_csv("your_compounds_file.csv")  # Replace with your CSV file path
plot_tanimoto_heatmap(df)
```

This will produce a heatmap image showing the Tanimoto similarity between the compounds listed in the CSV file.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your enhancements.

## License

This project is licensed under the MIT License.
