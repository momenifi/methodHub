import pandas as pd
import numpy as np




df = pd.DataFrame(pd.read_csv("domain_visibility_datasetsNumber_hindex.csv", sep=";"))
df_economic = df[df['category']=='economic']
df_social = df[df['category']=='social']


# Get top ten domains with highest number of dois from both DataFrames
top_ten_df_economic_doi = df_economic.nlargest(10, 'dois_number')[['domain', 'dois_number', 'mean_visibility_index', 'h_index']]
top_ten_df_social_doi = df_social.nlargest(10, 'dois_number')[['domain', 'dois_number', 'mean_visibility_index', 'h_index']]


# Get top ten domains with highest mean_visibility_index from both DataFrames
top_ten_df_economic_mean_visibility = df_economic.nlargest(10, 'mean_visibility_index')[['domain', 'dois_number', 'mean_visibility_index', 'h_index']]
top_ten_df_social_mean_visibility = df_social.nlargest(10, 'mean_visibility_index')[['domain', 'dois_number', 'mean_visibility_index', 'h_index']]

# Get top ten domains with highest h_index from both DataFrames
top_ten_df_economic_h_index = df_economic.nlargest(10, 'h_index')[['domain', 'dois_number', 'mean_visibility_index', 'h_index']]
top_ten_df_social_h_index = df_social.nlargest(10, 'h_index')[['domain', 'dois_number', 'mean_visibility_index', 'h_index']]


# Generate LaTeX tables for dois from both DataFrames
latex_table_df_economic_doi = top_ten_df_economic_doi.to_latex(index=False)
latex_table_df_social_doi = top_ten_df_social_doi.to_latex(index=False)

# Generate LaTeX tables for mean_visibility_index for both Economic and Social data
latex_table_df_economic_mean_visibility = top_ten_df_economic_mean_visibility.to_latex(index=False)
latex_table_df_social_mean_visibility = top_ten_df_social_mean_visibility.to_latex(index=False)

# Generate LaTeX tables for h_index for both Economic and Social data
latex_table_df_economic_h_index = top_ten_df_economic_h_index.to_latex(index=False)
latex_table_df_social_h_index = top_ten_df_social_h_index.to_latex(index=False)


# Writing LaTeX tables to separate .tex files
with open('10_top_domains/table_economic_doi.tex', 'w') as file1:
    file1.write(latex_table_df_economic_doi)

with open('10_top_domains/table_social_doi.tex', 'w') as file2:
    file2.write(latex_table_df_social_doi)
    
    # Writing LaTeX tables for mean_visibility_index to separate .tex files
with open('10_top_domains/table_economic_mean_visibility.tex', 'w') as file1:
    file1.write(latex_table_df_economic_mean_visibility)

with open('10_top_domains/table_social_mean_visibility.tex', 'w') as file2:
    file2.write(latex_table_df_social_mean_visibility)

# Writing LaTeX tables for h_index to separate .tex files
with open('10_top_domains/table_economic_h_index.tex', 'w') as file3:
    file3.write(latex_table_df_economic_h_index)

with open('10_top_domains/table_social_h_index.tex', 'w') as file4:
    file4.write(latex_table_df_social_h_index)