# Calculating Propensity Score Matching in R

## Description

The propensity score matching method is used to estimate the causal effect of a treatment, intervention, or exposure by balancing covariates between treatment and control groups. It aims to reduce bias and confounding in observational studies by creating comparable groups based on propensity scores.

It is used to construct control/treatment groups in scientific studies, in such a way that individuals in the control group are as similar as possible to individuals in the treatment group. 
![Image Alt Text](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/PS_explanation.jpg)

## Social Science Use Cases
- **Education Policy Evaluation**: [Assessing the impact of educational interventions on student outcomes](https://telearn.hal.science/hal-00190019/document)
- **Healthcare Interventions**: [Evaluating the effectiveness of medical treatments on patient outcomes](https://www.tandfonline.com/doi/pdf/10.1080/00273171.2011.568786)
- **Labor Market Studies**: [Analyzing the effects of job training programs on employment outcomes](https://www.nber.org/system/files/working_papers/w6829/w6829.pdf)
- **At-Risk Youth: Mentoring Program Impact**: [examine the impact of a mentoring program on academic achievement outcomes among at-risk youth](https://books.google.de/books?hl=de&lr=&id=5Y_MAwAAQBAJ&oi=fnd&pg=PP1&dq=Propensity+Score+Analysis:+Statistical+Methods+and+Applications.+Sage+Publications.&ots=WY57gK_A9w&sig=h8usM9tYzJGz-RRhnca-iyx0cnA#v=onepage&q=Propensity%20Score%20Analysis%3A%20Statistical%20Methods%20and%20Applications.%20Sage%20Publications.&f=false)
- **Academic Mobility of Researchers**: [Assessing the impact of academic mobility on scientific outcomes](https://doi.org/10.1016/j.joi.2022.101280)

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

### How to Use
1. Download  ["mydata_sample.csv"](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/mydata_sample.csv), ["propensity_matching_functions.R"](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/propensity_matching_functions.R), and ["main_script.R"](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/main_script.R) in a folder.
2. Run the commands in "main_script.R"
    - Load the input dataset into R (data_sample) (lines 1 to 5)
    - Define the functions (line 8)
    - Define the treatment variable (treatment_var) and covariates (covariates)(lines 11 and 12)
    - Call the `perform_propensity_matching` function to conduct propensity score matching (line 15) with parameters data_sample, treatment_var, and covariates.  
      The output contains SMDs of unmatched/matched data (unmatched_smd in line 20)/matched_smd in line 21) and 
    - Define the variables of interest (vars_of_interest) (line 29) and Matched data (matched_data in line 24)
    - Call the `calculate_mean_diff` function to calculate mean differences for variables of interest (line 33) with parameteres matched_data, treatment_var, and vars_of_interest. The output gets the mean differences of vars_of_interest. 


## Usage
### Input Data (DBD datasets)
This method can work with any dataset containing variables of interest, a treatment indicator, and covariates.

### Sample Input Data
Sample input data can be provided in CSV format with columns representing variables of interest (PPY, COPP, CPP), a treatment indicator (MOBILE), and covariates (REGION, MAIN_FIELD, INTERNATIONAL_COAUTHOR, GENDER, GDP_PC_ORIGIN, AGE). (mydata_sample.csv).
Here is a screenshot of sample input data:
![Image Alt Text](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/sample_data.PNG)

### Sample Output

The output includes standardized mean differences (SMD) for both unmatched and matched data, along with mean differences, t-values, and standard errors for the variables of interest.

By examining the SMD for unmatched and matched data under different covariances, we assess the effectiveness of the matching process in achieving balance between the treatment and control groups. A lower SMD indicates a smaller difference between the two groups. For instance, in this example, the SMD for the variable "AGE" is 0.34 for unmatched data and 0.03 for matched data. This suggests that the treatment group in the matched data is more similar to the control group compared to the unmatched data.
**SMD:**

![Image Alt Text](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/output_SMD.PNG)


**Main difference:**

A mean difference of 3.04 for the variable CPP indicates that, on average, the treatment group's CPP value is 3.04 units higher than that of the control group.
![Image Alt Text](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/output_mainDiff.PNG)


## Specifics
### Contact Details
For questions or feedback, contact [fakhri.momeni@gesis.org](mailto:fakhri.momeni@gesis.org).

### Publication
This method was utilized in the following paper:
- [The many facets of academic mobility and its impact on scholars' career](https://doi.org/10.1016/j.joi.2022.101280)
- Propensity score matching results can be found in Table 6 and Table 7.
