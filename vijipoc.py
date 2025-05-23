# -*- coding: utf-8 -*-
"""Vijipoc.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iDJoJCqkR7xat9GOf5-879k3gRdRF3-s
"""

!pip install streamlit

import matplotlib.pyplot as plt
import pandas as pd

# Create sample data
data = {
    "Drug": ["Drug A", "Drug B", "Drug C", "Drug D", "Drug E"],
    "Effectiveness (%)": [80, 70, 90, 60, 85],
}

df = pd.DataFrame(data)

# Plot bar chart
plt.figure(figsize=(8, 5))
plt.bar(df["Drug"], df["Effectiveness (%)"], color='skyblue')
plt.title("Effectiveness of Drugs", fontsize=16)
plt.xlabel("Drugs", fontsize=14)
plt.ylabel("Effectiveness (%)", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

