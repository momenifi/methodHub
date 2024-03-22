import requests
from urllib.parse import urlparse
import pandas as pd
import sys
import json
import xml.etree.ElementTree as ET
import numpy as np
from scipy import stats
from tabulate import tabulate
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_h_index(group):
    return sum(x >= i + 1 for i, x in enumerate(sorted(list(group['cit_all_years']), reverse=True)))


if __name__ == "__main__":
    categories = ["social", "economic"]
    
    #number of dois in social, economic and overlap between both categories
    all_dois_info = pd.read_csv(f"dois_info.csv", sep=";")
    economic_dois = all_dois_info[all_dois_info['category'] == 'economic']['doi'].unique()
    social_dois = all_dois_info[all_dois_info['category'] == 'social']['doi'].unique()
    # Count the number of unique DOIs that appear in both categories
    unique_dois_count = len(set(economic_dois) & set(social_dois))
    
    
    
    dois_info = all_dois_info[lambda x: (x['pubyear'] > 2015) & (x['pubyear'] < 2022)].copy()
  
    #dois = dois_info['doi'].unique()
    #get_domain(dois).to_csv(f"dois_domains.csv", index=False)
    dois_domains = pd.read_csv(f"dois_domains.csv", sep=";",dtype={'status': 'object'})

    domains = dois_domains['domain'].unique()
    
    visibility = pd.read_csv(f"visibility.csv", sep=";") 
    average_visibility = visibility.groupby('domain')['visibility_index'].mean().reset_index()#Get the average visibility index of each domain among countries
    std_dev_cite_norm = {}
    mean_cite_norm = {}
    std_dev_h_index = {}
    mean_h_index = {}
    std_dev_visibility = {}
    mean_visibility = {}
    
    correlation_values = {}
    
    for category in categories:    
        filtered_dois = dois_domains[(dois_domains['status'] == str(1)) ] # filter dois that we found domain for them
        
        filtered_dois_cat = filtered_dois.merge(dois_info, on='doi', how='inner')
        
        filtered_dois_cat = filtered_dois_cat[['doi', 'domain', 'category']]
        filtered_dois_cat = filtered_dois_cat.drop_duplicates(subset=['doi', 'domain', 'category'])
        
        # Merge DOI and domain data with visibility index
        doi_domain_visibility = filtered_dois_cat.merge(average_visibility, on='domain', how='inner')
        
        # Get the visibility index and number of dataset for each domain
        domains_doi_counts_visibility_index = doi_domain_visibility.groupby(['domain', 'category']).agg({'doi': 'count', 'visibility_index': 'mean'}).reset_index()
        domains_doi_counts_visibility_index.columns = ['domain' ,'category', 'dois_number', 'mean_visibility_index']
        
        # Read DOI metadata
        dois_info.loc[:,'cite_norm'] = (dois_info['cit_all_years'] / (2024 - dois_info['pubyear'])) 
        
        dois_citation = dois_info[['doi', 'cite_norm', 'cit_all_years', 'pubyear']].drop_duplicates()

        # Merge DOI, domain, and visibility with other DOI metadata
        dois_all_info = doi_domain_visibility.merge(dois_citation, on='doi', how='inner').drop_duplicates()
        ######print(f"dois in {category}:",dois_info[dois_info['category'] == category]['doi'].nunique()  ) 
        
        # Calculate h-index 
        filtered_dois_all_info = dois_all_info[(dois_all_info['pubyear'] > 2015) & (dois_all_info['pubyear'] < 2022)]
        #print(len(filtered_dois_all_info))
        ttt = dois_domains.merge(all_dois_info[(all_dois_info['pubyear'] < 2015) & (all_dois_info['pubyear'] < 2022)],on='doi',how='inner')
        print(len(ttt[ttt['domain']=='https://www.icpsr.umich.edu/'])) 
        dois_all_info[dois_all_info['domain'] == 'https://www.icpsr.umich.edu/'].sort_values(by='cit_all_years', ascending=False).to_csv("aaaacitation_icpsr.csv", index=False)
        filtered_df = filtered_dois_all_info[(filtered_dois_all_info['category'] == category) & (filtered_dois_all_info['domain'] == 'https://www.icpsr.umich.edu/')][['doi', 'cit_all_years']]
        df_sorted = filtered_df.sort_values(by='cit_all_years', ascending=False)
        df_sorted.to_csv("citation_icpsr.csv", index=False)
        # Plotting the 'cite_norm' values as a line plot
        df_sorted['cit_all_years'] = pd.to_numeric(df_sorted['cit_all_years'])

        # Create density plot using Seaborn
        plt.figure(figsize=(10, 6))
        sns.kdeplot(data=df_sorted, x='cit_all_years', fill=True)
        plt.xlabel('Number of Citations ')
        plt.ylabel('Density')
        plt.title('Density Plot of Number of Citations for Articles')
        # Save the figure as a PNG file
        plt.savefig('icpsr.png')

