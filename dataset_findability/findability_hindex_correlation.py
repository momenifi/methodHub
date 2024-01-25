import requests
from urllib.parse import urlparse
import pandas as pd
import sys
import json
import xml.etree.ElementTree as ET
import numpy as np
from scipy import stats

def calculate_h_index(group):
    return sum(x >= i + 1 for i, x in enumerate(sorted(list(group['cit_all_years']), reverse=True)))

def get_domain(category,dois):
    #data = pd.read_csv("dois_"+category+".csv",sep=";")
    #data = pd.read_csv("dois_"+category+"_sample.csv",sep=";")
    #dois = data.loc[:,'doi']
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    
    results = []
    for doi in dois:
        URL = "https://doi.org/" + str(doi)
        try:
            r = requests.head(URL, allow_redirects=True, headers=headers)
            h = '1'
            parsed_uri = urlparse(r.url)
            result = {'doi': doi, 'domain': '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri), 'status': h}
            results.append(result)
        except:
            try:
                r = requests.head(URL, allow_redirects=True)
                h = '2'
                parsed_uri = urlparse(r.url)
                result = result = {'doi': doi, 'domain': 'NG', 'status': h}
                results.append(result)
            except:
                h = '3'
                result = doi + ";" + "NG" + ";" + h
                results.append(result)
    return pd.DataFrame(results, columns=['doi', 'domain', 'status'])

def get_visibility_index(domains):
    sistrix_api_key="jKXrKrwSXp5D4u68jv6Z4sAEYMpIFbqdQhv"
    country_codes = ['de', 'at', 'ch', 'it', 'es', 'fr', 'pl', 'nl', 'uk', 'us', 'se', 'br', 'tr', 'be', 'ie', 'pt', 'dk', 'no', 'fi', 'gr', 'hu', 'sk', 'cz', 'au', 'jp', 'ca', 'ro', 'hr', 'bg', 'si']
    visibilities = []
    for domain in domains:
        for country_code in country_codes:
            request="https://api.sistrix.com/domain.sichtbarkeitsindex?api_key="+sistrix_api_key+"&host="+domain+"&country="+country_code
            response = requests.get(request)
            if response.status_code == 403:
                return pd.DataFrame()
            else:
                root= ET.fromstring(response.content)
                for child in root.iter('*'):
                    if child.tag == 'answer': 
                        for tag in child:
                            h_value = tag.get('value')
                            if h_value is not None:
                                visibility = {'domain':domain,'country':country_code,'visibility_index':float(h_value)}
                                visibilities.append(visibility)
    return pd.DataFrame(visibilities, columns=['domain', 'country', 'visibility_index'])
                
if __name__ == "__main__":
    categories = ["social", "economic"]
    for category in categories:
        dois_info = pd.read_csv(f"dois_info_{category}_sample.csv", sep="$")[lambda x: (x['pubyear'] > 2015) & (x['pubyear'] < 2022)]
        dois = dois_info['doi'].unique()
        get_domain(category,dois).to_csv(f"dois_domains_{category}.csv", index=False)
        dois_domains = pd.read_csv(f"dois_domains_{category}.csv",dtype={'status': 'object'})

        domains = dois_domains['domain'].unique()
        visibility = get_visibility_index(domains)
        visibility.to_csv(f"visibility_{category}.csv", index=False)#Get the visibility index for wach domain among different countries
        if visibility.empty: #if no access to sistrix api use the file  
            visibility = pd.read_csv(f"visibility_{category}.csv") 
        
        average_visibility = visibility.groupby('domain')['visibility_index'].mean().reset_index()#Get the average visibility index of each domain among countries
        filtered_dois = dois_domains[dois_domains['status'] == str(1)] # filter dois that we found domain for them
        
        # Merge DOI and domain data with visibility index
        doi_domain_visibility = filtered_dois.merge(average_visibility, on='domain', how='inner')
        
        # Get the visibility index and number of dataset for each domain
        domains_doi_counts_visibility_index = doi_domain_visibility.groupby('domain').agg({'doi': 'count', 'visibility_index': 'mean'}).reset_index()
        domains_doi_counts_visibility_index.columns = ['domain', 'dois_number', 'mean_visibility_index']
        
        # Read DOI metadata
        dois_info['cite_norm'] = (dois_info['cit_all_years'] / (2024 - dois_info['pubyear']))
        dois_info['oa_status'] = np.where(dois_info['oa_status'] == 'closed', 0, 1)
        print(f"close in {category}:",dois_info.loc[dois_info['oa_status'] == 1 , 'doi'].nunique()) 
        
        dois_citation = dois_info[['doi', 'cite_norm', 'cit_all_years', 'oa_status', 'pubyear']]

        # Merge DOI, domain, and visibility with other DOI metadata
        dois_all_info = doi_domain_visibility.merge(dois_citation, on='doi', how='inner')
        print(f"dois in {category}:",dois_info['doi'].nunique()) 
         
        # Calculate h-index 
        filtered_dois_all_info = dois_all_info[(dois_all_info['pubyear'] > 2015) & (dois_all_info['pubyear'] < 2022)]
        filtered_dois_all_info.groupby('domain').apply(calculate_h_index).reset_index().to_csv(f"domain_h_index_{category}.csv", index=False)
        domain_h_index = pd.read_csv(f"domain_h_index_{category}.csv")
        
        #domain_h_index = filtered_dois_all_info.groupby('domain').apply(calculate_h_index).reset_index()
        domain_h_index.columns = ['domain', 'h_index']
        visibility_hindex = average_visibility.merge(domain_h_index, on='domain', how='inner')

        domain_doi_count_visibility_hindex = domains_doi_counts_visibility_index.merge(visibility_hindex, on = 'domain', how = 'outer')
        domain_doi_count_visibility_hindex['h_index'] = domain_doi_count_visibility_hindex['h_index'].fillna(0)
        domain_doi_count_visibility_hindex = domain_doi_count_visibility_hindex.sort_values(by=['dois_number','mean_visibility_index'], ascending=False)
        columns_to_keep =  ['domain', 'dois_number', 'mean_visibility_index',  'h_index']
        domain_doi_count_visibility_hindex=domain_doi_count_visibility_hindex[columns_to_keep]
        domain_doi_count_visibility_hindex.to_csv(f'domain_visibility_datasetsNumber_hindex_{category}.csv', index=False, sep=';')
        
        
        # Calculate standard deviation and mean for 'cite_norm' 
        std_dev_cite_norm = np.std(filtered_dois_all_info['cite_norm'])
        mean_cite_norm = np.mean(filtered_dois_all_info['cite_norm'])
        
        # Calculate standard deviation and mean for 'h_index' and 'visibility_index'
        std_dev_h_index = np.std(visibility_hindex['h_index'])
        mean_h_index = np.mean(visibility_hindex['h_index'])

        std_dev_visibility = np.std(visibility_hindex['visibility_index'])
        mean_visibility = np.mean(visibility_hindex['visibility_index'])

        # Display standard deviation and mean for 'h_index' and 'visibility_index'
        print(f"Standard Deviation of h_index: {std_dev_h_index}")
        print(f"Mean of h_index: {mean_h_index}")
        print(f"Standard Deviation of visibility_index: {std_dev_visibility}")
        print(f"Mean of visibility_index: {mean_visibility}")
        
        '''
        print(f"Mean of normalized citation in {category}: {np.mean(filtered_dois_all_info['cite_norm'])}")
        print(f"Standard Deviation of normalized citation in {category}: {np.std(filtered_dois_all_info['cite_norm'])}") 
        '''
        
        # Calculate the correlation for different thresholds
        thresholds = [-1, 0, 1]
        for threshold in thresholds:
            visibility_hindex = visibility_hindex[visibility_hindex['h_index'] > threshold]
            spearman_corr = stats.spearmanr(visibility_hindex['visibility_index'], visibility_hindex['h_index'])
            print(f"Threshold {threshold} Spearman correlation for {category}:")
            print(spearman_corr)
            #visibility_hindex.to_csv(f'visibility_h-index_{category}_threshold_{threshold}.csv', index=False)
            
        # Calculate the correlation with OA status
        filtered_dois_all_info['cite_norm'] = pd.to_numeric(filtered_dois_all_info['cite_norm'])
        filtered_dois_all_info['oa_status'] = pd.to_numeric(filtered_dois_all_info['oa_status'])
        filtered_dois_all_info.dropna(inplace=True)
        #print(f"dois with  zero citations for in  {category}:",dois_info.loc[(dois_info['cite_norm'] < 1) , 'doi'].nunique()/dois_info.loc[(dois_info['cite_norm'] > -1) , 'doi'].nunique()) 
        spearman_corrOA = stats.spearmanr(filtered_dois_all_info['oa_status'], filtered_dois_all_info['cite_norm'])
        print(f"correlation cite_norm with OA for {category}:")
        print(spearman_corrOA)