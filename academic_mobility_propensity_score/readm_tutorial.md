# Tutorial Title
Propensity Score Matching for Assessing Academic Mobility Impact: A Step-by-Step Guide using R


##Learning Goal  
- By the end of this tutorial, you will be able to understand and implement propensity score matching techniques to assess the impact of academic mobility on research productivity, recieved citations and collaboration indicators among researchers.

## Learning Objectives

- Understand the concept of propensity score matching.
- Implement propensity score matching using R programming language.
- Interpret the results of propensity score matching analysis.
- Apply the technique to assess the impact of academic mobility on key research metrics.

## Description

This tutorial provides a comprehensive guide on using propensity score matching techniques in R to assess the impact of academic mobility on research productivity and collaboration indicators among researchers. It includes step-by-step instructions, example code, and explanations to facilitate understanding and implementation.

## Target Audience

This tutorial is targeted towards social science researchers, particularly those interested in assessing the impact of academic mobility on research outcomes. Basic knowledge of R programming and statistical concepts is recommended.

## Prerequisites Required

Before starting this tutorial, you should have:
- Basic understanding of R programming language.
- Familiarity with statistical concepts such as regression analysis.
- Access to R environment with necessary packages installed.

## Difficulty Level

Normal

## Duration

Approximately 30-45 minutes

## Social Science Relevance

**Social Science Usecase(s):**  
This tutorial addresses the technical challenge in social science research of assessing the impact of academic mobility, a topic of growing importance in the context of globalization and international collaboration in academia.

Setup

## Environment Setup 
Ensure you have R environment set up on your local machine.

## Installing Dependencies
Install the required R packages by running the following commands:

```R
install.packages("Matching")
install.packages("tableone")
```
## Flow Diagram

[Include a flow diagram here if applicable]

## Content Sections and Subsections

- Introduction to Propensity Score Matching
- Data Preparation
- Propensity Score Estimation
- Propensity Score Matching
- Assessing Balance after Matching
- Outcome Analysis
- Interpretation of Results


## Input Data (DBD datasets)
This method can work with any dataset containing variables of interest, a treatment indicator, and covariates.

## Sample Input Data
Sample input data can be provided in CSV format with columns representing variables of interest, treatment indicator, and covariates (data_sample.csv).
Here is a screenshot of sample input data:
![Image Alt Text](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/sample_data.PNG)

## Sample Output
Sample output includes standardized mean differences (SMD) for unmatched and matched data, as well as mean differences, t-values, and standard errors for variables of interest. 

**SMD:**

![Image Alt Text](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/output_SMD.PNG)


**Main difference:**

![Image Alt Text](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/output_mainDiff.PNG)



## How to Use

To utilize the propensity score matching technique for assessing the impact of academic mobility on research productivity and collaboration indicators, follow these steps:
In this example, this method is employed to estimate the causal effect of academic mobility on research productivity, recieved citations and collaboration indicators among researchers. Academic mobility, represented by the treatment variable "mobile," distinguishes between researchers who have experienced academic mobility to other countries (mobile = 1) and those who have not (mobile = 0). The method aims to balance covariates such as region, main field of study, international co-authorship, gender, GDP per capita of the researcher's origin country, and age, between mobile and non-mobile researchers. By balancing covariates through propensity score matching, the method allows for a more accurate assessment of the impact of academic mobility on key research metrics, including CPP (citations per paper), PPY (number of papers per year), and COPP (co-authors per paper).

SMD quantifies the standardized difference in means between two groups, typically the treatment and control groups, by dividing the difference in means by the standard deviation of the outcome variable. It is commonly used in propensity score matching to assess balance between groups, with a lower SMD indicating better balance and greater comparability in terms of covariates. SMD facilitates comparing effect sizes across different studies or analyses, especially when outcome variables have different scales. In the context of this method, SMD is calculated for both unmatched and matched data to evaluate the balance achieved after matching. The treatment group consists of researchers who have experienced academic mobility to other countries (mobile = 1), while the control group consists of researchers who have not experienced academic mobility (mobile = 0).

The Mean Difference for each variable of interest (CPP, PPY, COPP) quantifies the average difference in these research productivity, recieved citations and collaboration indicators between mobile and non-mobile researchers. A positive Mean Difference indicates that mobile researchers, on average, have higher values of the respective metric compared to non-mobile researchers. For example, a positive Mean Difference in CPP suggests that mobile researchers receive more citations per paper than non-mobile researchers. Conversely, a negative Mean Difference indicates that mobile researchers, on average, have lower values of the respective metric compared to non-mobile researchers. Understanding the sign and magnitude of Mean Differences provides insights into the direction and magnitude of the impact of academic mobility on research productivity and collaboration indicators.

1. **Download Files:**
   - Download the following files into a single folder:
     - "mydata_sample.csv": Input dataset containing the relevant variables for analysis.
     - "propensity_matching_functions.R": R script containing functions for propensity score matching.
     - "main_script.R": R script for executing the analysis.

2. **Run Commands in "main_script.R":**
   - Open "main_script.R" in your R environment.
   - Run the commands sequentially to execute the analysis.

3. **Load Input Dataset:**
   - Execute lines 1 to 5 in "main_script.R" to load the input dataset into R as `data_sample`.

4. **Define Functions:**
   - Execute line 8 in "main_script.R" to define the necessary functions from "propensity_matching_functions.R".

5. **Define Treatment Variable and Covariates:**
   - Define the treatment variable (`treatment_var`) as "MOBILE" and covariates (`covariates`) as "REGION", "MAIN_FIELD", "INTERNATIONAL_COAUTHOR", "GENDER", "GDP_PC_ORIGIN", and "AGE" in lines 11 and 12 of "main_script.R".

6. **Perform Propensity Score Matching:**
   - Call the `perform_propensity_matching` function in line 15 of "main_script.R" with parameters `data_sample`, `treatment_var`, and `covariates` to conduct propensity score matching.
   - The output includes standardized mean differences (SMDs) of unmatched/matched data (`unmatched_smd` in line 20 and `matched_smd` in line 21) and the matched data (`matched_data` in line 24).

7. **Define Variables of Interest:**
   - Define the variables of interest (`vars_of_interest`) as "PPY", "CPP", and "COPP" in line 29 of "main_script.R".

8. **Calculate Mean Differences:**
   - Call the `calculate_mean_diff` function in line 33 of "main_script.R" with parameters `matched_data`, `treatment_var`, and `vars_of_interest` to calculate mean differences for the variables of interest.
   - The output provides the mean differences of `vars_of_interest`.

By following these steps, you can successfully conduct propensity score matching analysis to assess the impact of academic mobility on research productivity and collaboration indicators, focusing on the variables of interest "PPY", "CPP", and "COPP".



## Conclusion

In conclusion, this tutorial has provided a detailed overview of propensity score matching techniques and their application in assessing the impact of academic mobility on research productivity and collaboration indicators. By following the step-by-step guide and example code provided, learners have gained a comprehensive understanding of how to implement propensity score matching in R and interpret the results effectively.

#### How the Learning Goal is Achieved

The learning goal of understanding and implementing propensity score matching techniques to assess the impact of academic mobility has been achieved through:

- Introduction to the concept of propensity score matching.
- Step-by-step instructions on data preparation, propensity score estimation, matching, and outcome analysis.
- Hands-on experience with example code and explanations.
- Interpretation of results and assessment of balance after matching.

#### Skills Acquired with this Tutorial

Upon completing this tutorial, learners have acquired the following skills:

- Understanding of propensity score matching and its relevance in social science research.
- Proficiency in using R programming language for propensity score matching analysis.
- Ability to interpret standardized mean differences (SMDs) and mean differences in matched data.
- Competence in assessing the impact of academic mobility on research productivity and collaboration indicators using propensity score matching.

#### Concluding Remarks

Propensity score matching is a powerful technique for estimating causal effects in observational studies, particularly in the context of social science research. By mastering this technique, researchers can overcome challenges associated with selection bias and confounding variables, leading to more robust and reliable research findings. We encourage learners to further explore advanced topics in propensity score matching and apply these skills to their own research endeavors.

## References
- [The many facets of academic mobility and its impact on scholars' career](https://doi.org/10.1016/j.joi.2022.101280)