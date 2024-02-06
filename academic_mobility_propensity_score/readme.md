# Propensity Score Matching Method

## Description
The propensity score matching method is used to estimate the causal effect of a treatment, intervention, or exposure by balancing covariates between treatment and control groups. It aims to reduce bias and confounding in observational studies by creating comparable groups based on propensity scores.

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

### Sample Output
Sample output includes standardized mean differences for unmatched and matched data, as well as mean differences, t-values, and standard errors for variables of interest.

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
