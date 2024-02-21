### Tutorial Title
Propensity Score Matching for Assessing Academic Mobility Impact: A Step-by-Step Guide using R

#### Upfront Information

**Learning Goal:**  
By the end of this tutorial, you will be able to understand and implement propensity score matching techniques to assess the impact of academic mobility on research productivity and collaboration indicators among researchers.

#### Learning Objectives:

- Understand the concept of propensity score matching.
- Implement propensity score matching using R programming language.
- Interpret the results of propensity score matching analysis.
- Apply the technique to assess the impact of academic mobility on key research metrics.

#### Description

This tutorial provides a comprehensive guide on using propensity score matching techniques in R to assess the impact of academic mobility on research productivity and collaboration indicators among researchers. It includes step-by-step instructions, example code, and explanations to facilitate understanding and implementation.

#### Target Audience

This tutorial is targeted towards social science researchers, particularly those interested in assessing the impact of academic mobility on research outcomes. Basic knowledge of R programming and statistical concepts is recommended.

#### Prerequisites Required

Before starting this tutorial, you should have:
- Basic understanding of R programming language.
- Familiarity with statistical concepts such as regression analysis.
- Access to R environment with necessary packages installed.

#### Difficulty Level

Normal

#### Duration

Approximately 30-45 minutes

#### Social Science Relevance

**Social Science Usecase(s):**  
This tutorial addresses the technical challenge in social science research of assessing the impact of academic mobility, a topic of growing importance in the context of globalization and international collaboration in academia.

#### Setup

**Environment Setup:**  
Ensure you have R environment set up on your local machine.

**Installing Dependencies:**  
Install the required R packages by running the following commands:

```R
install.packages("Matching")
install.packages("tableone")
...
#### Flow Diagram

[Include a flow diagram here if applicable]

#### Content Sections and Subsections

- Introduction to Propensity Score Matching
- Data Preparation
- Propensity Score Estimation
- Propensity Score Matching
- Assessing Balance after Matching
- Outcome Analysis
- Interpretation of Results

#### Usage

**How to Use**

To utilize the propensity score matching technique for assessing the impact of academic mobility on research productivity and collaboration indicators, follow these steps:

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
