import requests
from urllib.parse import urlparse
import pandas as pd
import sys
import json
import xml.etree.ElementTree as ET
import numpy as np
from scipy import stats
from tabulate import tabulate


def calculate_h_index(group):
    return sum(x >= i + 1 for i, x in enumerate(sorted(list(group['cit_all_years']), reverse=True)))

def get_domain(dois):
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
                result = {'doi': doi, 'domain': 'NG', 'status': h}
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
                try:
                    root= ET.fromstring(response.content)
                    for child in root.iter('*'):
                        if child.tag == 'answer': 
                            for tag in child:
                                h_value = tag.get('value')
                                if h_value is not None:
                                    visibility = {'domain':domain,'country':country_code,'visibility_index':float(h_value)}
                                    visibilities.append(visibility)
                except:
                    return pd.DataFrame()
    return pd.DataFrame(visibilities, columns=['domain', 'country', 'visibility_index'])
                
if __name__ == "__main__":
    categories = ["social", "economic"]
    
    #number of dois in social, economic and overlap between both categories
    all_dois_info = pd.read_csv(f"dois_info.csv", sep=";")
    economic_dois = all_dois_info[all_dois_info['category'] == 'economic']['doi'].unique()
    social_dois = all_dois_info[all_dois_info['category'] == 'social']['doi'].unique()
    # Count the number of unique DOIs that appear in both categories
    unique_dois_count = len(set(economic_dois) & set(social_dois))
    print("all dois in social:",all_dois_info[all_dois_info['category'] == 'social']['doi'].nunique())
    print("all dois in economic:",all_dois_info[all_dois_info['category'] == 'economic']['doi'].nunique())
    print("overlap:",unique_dois_count)
    
    
    dois_info = all_dois_info[lambda x: (x['pubyear'] > 2015) & (x['pubyear'] < 2022)].copy()
  
    #dois = dois_info['doi'].unique()
    #get_domain(dois).to_csv(f"dois_domains.csv", index=False)
    dois_domains = pd.read_csv(f"dois_domains.csv", sep=";",dtype={'status': 'object'})

    domains = dois_domains['domain'].unique()
    
    
    '''visibility = get_visibility_index(domains)
    if visibility.empty: #if no access to sistrix api use the file  
        visibility = pd.read_csv(f"visibility.csv") 
    else:
        visibility.to_csv(f"visibility.csv", index=False)#Get the visibility index for wach domain among different countries
    '''
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
        filtered_dois = dois_domains[(dois_domains['status'] == str(1))] # filter dois that we found domain for them
        
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
        #&(dois_all_info['domain']!='https://primarysources.brillonline.com/') & (dois_all_info['domain']!='https://referenceworks.brillonline.com/')]
        

        domain_h_index = filtered_dois_all_info.groupby(['domain', 'category']).apply(calculate_h_index).reset_index()
        domain_h_index.columns = ['domain', 'category','h_index']
        domain_h_index.to_csv(f"domain_h_index.csv", index=False)
        #domain_h_index = pd.read_csv(f"domain_h_index.csv")

        visibility_hindex = average_visibility.merge(domain_h_index, on='domain', how='inner')
        
        domain_doi_count_visibility_hindex = domains_doi_counts_visibility_index.merge(visibility_hindex, on = ['domain', 'category'], how = 'outer')
        
        domain_doi_count_visibility_hindex['h_index'] = domain_doi_count_visibility_hindex['h_index'].fillna(0)
        domain_doi_count_visibility_hindex = domain_doi_count_visibility_hindex.sort_values(by=['dois_number','mean_visibility_index'], ascending=False)
        columns_to_keep =  ['domain', 'dois_number', 'mean_visibility_index',  'h_index', 'category']
        domain_doi_count_visibility_hindex=domain_doi_count_visibility_hindex[columns_to_keep]
        domain_doi_count_visibility_hindex.to_csv(f'domain_visibility_datasetsNumber_hindex.csv', index=False, sep=';')
        
        
        # Calculate standard deviation and mean for 'cite_norm' 
        std_dev_cite_norm[category] = filtered_dois_all_info[filtered_dois_all_info['category'] == category]['cite_norm'].std()
        mean_cite_norm[category] = filtered_dois_all_info[filtered_dois_all_info['category'] == category]['cite_norm'].mean()
        
        # Calculate standard deviation and mean for 'h_index' and 'visibility_index'
        visibility_hindex_cat = visibility_hindex[visibility_hindex['category'] == category]
        std_dev_h_index[category] = visibility_hindex_cat['h_index'].std()
        mean_h_index[category] = visibility_hindex_cat['h_index'].mean()

        std_dev_visibility[category] = visibility_hindex_cat['visibility_index'].std()
        mean_visibility[category] = visibility_hindex_cat['visibility_index'].mean()
        '''
        # Display standard deviation and mean for 'h_index' and 'visibility_index'
        print(f"Mean of h_index: {mean_h_index[category]}")
        print(f"Standard Deviation of h_index: {std_dev_h_index[category]}")
        print(f"Mean of visibility_index: {mean_visibility[category]}")
        print(f"Standard Deviation of visibility_index: {std_dev_visibility[category]}")
        print(f"Mean of normalized citation in {category}: {mean_cite_norm[category]}")
        print(f"Standard Deviation of normalized citation in {category}: {std_dev_cite_norm[category]}") 
        '
        '''

        spearman_corr_cite_visibility = stats.spearmanr(filtered_dois_all_info['visibility_index'], filtered_dois_all_info['cite_norm'])
        
        
        
        
        # Calculate the correlation for different thresholds
        thresholds = [-1, 0, 1]
        spearman_corr = {}
        for threshold in thresholds:
            filtered_dois_all_info_hindex = filtered_dois_all_info.merge(domain_h_index,on = 
            ['domain', 'category'], how = 'inner')[['doi','domain','category','cit_all_years','visibility_index','cite_norm','h_index']].drop_duplicates()
            #filtered_dois_all_info_hindex = filtered_dois_all_info_hindex[(filtered_dois_all_info_hindex['domain']!='https://referenceworks.brillonline.com/') & 
            #(filtered_dois_all_info_hindex['domain']!='https://www.oecd-ilibrary.org/')].reset_index()
            filtered_dois_all_info_cat = filtered_dois_all_info_hindex[filtered_dois_all_info_hindex['category'] == category]
            filtered_dois_all_info_filtered_cat = filtered_dois_all_info_cat[filtered_dois_all_info_cat['cite_norm'] > threshold]
            spearman_corr = stats.spearmanr(filtered_dois_all_info_filtered_cat['visibility_index'], filtered_dois_all_info_filtered_cat['cite_norm'])
            
            #print(f"Threshold {threshold} Spearman correlation for {category}, number:{len(visibility_hindex_filtered)}")
            #print(spearman_corr)
            #visibility_hindex.to_csv(f'visibility_h-index_{category}_threshold_{threshold}.csv', index=False)
            
            
            num_domains = len(filtered_dois_all_info_filtered_cat)
            correlation_values[(category, threshold)] = {'correlation': spearman_corr, 'num_domains': num_domains}

        
        '''
        # Calculate the correlation for different thresholds
        thresholds = [-1, 0, 1]
        spearman_corr = {}
        for threshold in thresholds:
            visibility_hindex_filtered = visibility_hindex_cat[visibility_hindex_cat['h_index'] > threshold]
            spearman_corr = stats.spearmanr(visibility_hindex_filtered['visibility_index'], visibility_hindex_filtered['h_index'])
            
            #print(f"Threshold {threshold} Spearman correlation for {category}, number:{len(visibility_hindex_filtered)}")
            #print(spearman_corr)
            #visibility_hindex.to_csv(f'visibility_h-index_{category}_threshold_{threshold}.csv', index=False)
            
            
            spearman_corr = stats.spearmanr(visibility_hindex_filtered['visibility_index'], visibility_hindex_filtered['h_index'])
            num_domains = len(visibility_hindex_filtered)
            correlation_values[(category, threshold)] = {'correlation': spearman_corr, 'num_domains': num_domains}
        '''
    
    # Create LaTeX tables for each category

    for category in categories:
        print(f"\\begin{{table}}[htbp]")
        print(f"\\centering")
        print(f"\\caption{{Correlation between h-index of domains in \\textbf{{\\textit{{{category}}}}} and visibility index of domain captured by Sistrix}}")
        print(f"\\label{{tab-hindex-{category.lower().replace(' ', '_')}}}")
        print(f"\\begin{{tabular}}{{|c|c|c|}}")
        print(f"\\hline")
        print(f"\\textbf{{h-Index Threshold}} & \\textbf{{Number of Domains}} & \\textbf{{Spearman Correlation (P-Value)}}  \\\\")
        print(f"\\hline")

        for threshold in thresholds:
            correlation_data = correlation_values[(category, threshold)]
            num_domains = correlation_data['num_domains']
            spearman_corr = round(correlation_data['correlation'].correlation, 2)
            p_value = round(correlation_data['correlation'].pvalue, 3)
            '''
            # Define descriptive labels for different categories of domains
            if threshold == -1:
                threshold_label = "All domains"
            elif threshold == 0:
                threshold_label = "Domains with h-index $>$ 0"
            elif threshold == 1:
                threshold_label = "Domains with h-index $>$ 1"
            '''
            #citation correlation
            # Define descriptive labels for different categories of domains
            if threshold == -1:
                threshold_label = "All datasets"
            elif threshold == 0:
                threshold_label = "Domains with number of citations $>$ 0"
            elif threshold == 1:
                threshold_label = "Domains with number od citations $>$ 1"

            print(f"{threshold_label} & {num_domains} & {spearman_corr} ({p_value}) \\\\")
            print(f"\\hline")
        
        print(f"\\end{{tabular}}")
        print(f"\\end{{table}}")
        print("\n")
    
    
    #creating data for descriptive satatistics in the table 1
    data = [
    ["h-Index", round(mean_h_index['social'], 2), round(std_dev_h_index['social'], 2), round(mean_h_index['economic'], 2), round(std_dev_h_index['economic'], 2)],
    ["Visibility Index", round(mean_visibility['social'], 2), round(std_dev_visibility['social'], 2), round(mean_visibility['economic'], 2), round(std_dev_visibility['economic'], 2)],
    ["Normalized citation", round(mean_cite_norm['social'], 2), round(std_dev_cite_norm['social'], 2), round(mean_cite_norm['economic'], 2), round(std_dev_cite_norm['economic'], 2)]
    ]
    
    # Generate LaTeX table
    # Constructing the LaTeX table string
    latex_table = "\\begin{table}[htbp]\n\\centering\n\\caption{Mean and Standard Deviation (SD) for H-Index and Visibility Index}\n\\label{tab:statistics}\n\\begin{tabular}{|c|c|c|c|c|}\n\\hline\n"

    # Adding column headers to the LaTeX table string
    latex_table += "\\multirow{2}{*}{\\textbf{Variable}} & \\multicolumn{2}{c|}{\\textbf{Social Sciences}} & \\multicolumn{2}{c|}{\\textbf{Economic}} \\\\\n\\cline{2-5}\n"
    latex_table += " & \\textbf{Mean} & \\textbf{SD} & \\textbf{Mean} & \\textbf{SD} \\\\\n\\hline\n"

    # Adding data rows to the LaTeX table string
    for row in data:
        latex_table += " & ".join(map(str, row)) + " \\\\\n"

    # Completing the LaTeX table string
    latex_table += "\\hline\n\\end{tabular}\n\\end{table}"

    
    #print(latex_table)

            
        
        