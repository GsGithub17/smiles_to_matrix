import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs

def plot_tanimoto_heatmap(df):
    def smiles_to_fp(smiles):
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return np.zeros(2048)  # Return a zero vector for invalid SMILES
        return AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)

    # Compute fingerprints
    fingerprints = df['SMILES'].apply(smiles_to_fp)

    # Calculate Tanimoto similarity matrix
    num_molecules = len(fingerprints)
    similarity_matrix = np.zeros((num_molecules, num_molecules))

    for i in range(num_molecules):
        for j in range(i + 1, num_molecules):
            similarity = DataStructs.FingerprintSimilarity(fingerprints[i], fingerprints[j])
            similarity_matrix[i, j] = similarity
            similarity_matrix[j, i] = similarity

    # Create a mask for the upper triangle
    mask = np.triu(np.ones_like(similarity_matrix, dtype=bool))

    # Plot the heatmap
    plt.figure(figsize=(15, 15))
    sns.heatmap(similarity_matrix, mask=mask, square=True, linewidths=.5, cmap='viridis',
                cbar_kws={'shrink': .4, 'ticks': [-1, -.5, 0, 0.5, 1]},
                vmin=0, vmax=1, annot=True, annot_kws={'size': 8})
    compound_ids = df['ID'].tolist()
    plt.yticks(np.arange(len(compound_ids)) + 0.5, labels=compound_ids, rotation=0)
    plt.xticks(np.arange(len(compound_ids)) + 0.5, labels=compound_ids, rotation=90)
    plt.title('Tanimoto Similarity Heatmap')
    plt.savefig("smilaritymatrix.png") 
    plt.show()

# Example usage
df = pd.read_csv("smilegraphxtest.csv")  # Replace with your CSV file path
plot_tanimoto_heatmap(df)
