import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 import data
df = pd.read_csv('medical_examination.csv')

# Step 2: Add 'overweight' column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# Step 3: Normalize data by making 0 good and 1 bad
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():   
# Step 5: Create DataFrame for cat plot using `pd.melt`
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

# Step 6: Group and reformat data to split by 'cardio' and show counts of each feature
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

# Step 7: Draw the catplot with 'sns.catplot()'
    plot = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar')
    
# Step 8: Get the figure object for the output
    fig = plot.fig

# Step 9: Save the figure
    fig.savefig('catplot.png')
    return fig
    
# 10
def draw_heat_map():

# Step 11: Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

# Step 12: Calculate the correlation matrix
    corr = df_heat.corr()

# Step 13: Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

# Step 14: Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))

# Step 15: Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, mask=mask, fmt='.1f', center=0, vmin=-0.1, vmax=0.3, square=True, cbar_kws={'shrink': 0.5}, ax=ax)

# Step 16: Save the figure
    fig.savefig('heatmap.png')
    return fig
