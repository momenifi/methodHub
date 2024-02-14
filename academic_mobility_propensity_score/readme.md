# Propensity Score Matching Method

## Description

The propensity score matching method is used to estimate the causal effect of a treatment, intervention, or exposure by balancing covariates between treatment and control groups. It aims to reduce bias and confounding in observational studies by creating comparable groups based on propensity scores.

In this example, this method is employed to estimate the causal effect of academic mobility on research productivity and collaboration indicators among researchers. Academic mobility, represented by the treatment variable "mobile," distinguishes between researchers who have experienced academic mobility to other countries (mobile = 1) and those who have not (mobile = 0). The method aims to balance covariates such as region, main field of study, international co-authorship, gender, GDP per capita of the researcher's origin country, and age, between mobile and non-mobile researchers. By balancing covariates through propensity score matching, the method allows for a more accurate assessment of the impact of academic mobility on key research metrics, including CPP (citations per paper), PPY (number of papers per year), and COPP (co-authors per paper).

SMD quantifies the standardized difference in means between two groups, typically the treatment and control groups, by dividing the difference in means by the standard deviation of the outcome variable. It is commonly used in propensity score matching to assess balance between groups, with a lower SMD indicating better balance and greater comparability in terms of covariates. SMD facilitates comparing effect sizes across different studies or analyses, especially when outcome variables have different scales. In the context of this method, SMD is calculated for both unmatched and matched data to evaluate the balance achieved after matching. The treatment group consists of researchers who have experienced academic mobility to other countries (mobile = 1), while the control group consists of researchers who have not experienced academic mobility (mobile = 0).

The Mean Difference for each variable of interest (CPP, PPY, COPP) quantifies the average difference in these research productivity and collaboration indicators between mobile and non-mobile researchers. A positive Mean Difference indicates that mobile researchers, on average, have higher values of the respective metric compared to non-mobile researchers. For example, a positive Mean Difference in CPP suggests that mobile researchers receive more citations per paper than non-mobile researchers. Conversely, a negative Mean Difference indicates that mobile researchers, on average, have lower values of the respective metric compared to non-mobile researchers. Understanding the sign and magnitude of Mean Differences provides insights into the direction and magnitude of the impact of academic mobility on research productivity and collaboration indicators.

## Social Science Use Cases
- **Education Policy Evaluation**: Assessing the impact of educational interventions on student outcomes.
- **Healthcare Interventions**: Evaluating the effectiveness of medical treatments on patient outcomes.
- **Labor Market Studies**: Analyzing the effects of job training programs on employment outcomes.
- **Social Program Evaluations**: Assessing the outcomes of social interventions on poverty alleviation.

## Structure
The method consists of two main functions:
1. `perform_propensity_matching`: Conducts propensity score matching and calculates standardized mean differences (SMDs) for unmatched and matched data.
2. `calculate_mean_diff`: Calculates mean differences, t-values, and standard errors for variables of interest between treatment and control groups.

## Keywords
Propensity score matching, Causal inference, Observational studies, Social science research, Methodology.

## Setup
### Environment Setup
To run this method locally, ensure you have R installed on your system.

### Installing Dependencies
Install the required R packages:
- Matching
- tableone

## Usage
### Input Data (DBD datasets)
This method can work with any dataset containing variables of interest, a treatment indicator, and covariates.

### Sample Input Data
Sample input data can be provided in CSV format with columns representing variables of interest, treatment indicator, and covariates (data_sample.csv).
Here is a sample of input data:
![Image Alt Text](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/sample_data.PNG)

### Sample Output
Sample output includes standardized mean differences (SMD) for unmatched and matched data, as well as mean differences, t-values, and standard errors for variables of interest.

### How to Use
1. Load the input dataset into R.
2. Define the treatment variable and covariates.
3. Call the `perform_propensity_matching` function to conduct propensity score matching.
4. Call the `calculate_mean_diff` function to calculate mean differences for variables of interest.

## Specifics
### Contact Details
For questions or feedback, contact [fakhri.momeni@gesis.org](mailto:fakhri.momeni@gesis.org).

### Publication
This method was utilized in the following paper:
- [The many facets of academic mobility and its impact on scholars' career](https://doi.org/10.1016/j.joi.2022.101280)
- Propensity score matching results can be found in Table 6 and Table 7.
