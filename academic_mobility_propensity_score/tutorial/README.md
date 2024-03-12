# Propensity Score Matching for Assessing the Impact of Job Training Programs on Employment Outcomes: A Step-by-Step Guide using R

## Learning Objectives

- Understand the concept of propensity score matching.
- Implement propensity score matching using R programming language.
- Interpret the results of propensity score matching.
- Apply the technique to assess the impact of job training programs on employment outcomes.

## Description

This tutorial provides a comprehensive guide on using propensity score matching techniques in R to assess the impact of job training programs on employment outcomes, specifically focusing on variables such as age, education level, years of experience, earnings before and after the training program, and participation in the training program (treatment variable). It includes step-by-step instructions, example code, and explanations to facilitate understanding and implementation.

In this example, the propensity score method is employed to estimate the causal effect of job training programs on employment outcomes. The treatment variable *"TREATED"* distinguishes between individuals who participated in the job training program *(TREATED = 1)* as the treatment group and those who did not *(TREATED = 0)* as a control group. The method aims to balance covariates such as age, education level, and years of experience between the treatment and control groups. By achieving covariate balance through propensity score matching, the method allows for a more accurate assessment of the impact of job training programs on employment outcomes.

Standardized Mean Difference (SMD) assesses the covariance balance between treatment and control groups before and after matching. SMD is commonly used in propensity score matching, with a lower SMD indicating better balance and greater comparability regarding covariates. Understanding the sign and magnitude of Mean Differences provides insights into the direction and magnitude of the impact of job training programs on employment outcomes.

## Target Audience

This tutorial is targeted towards researchers and practitioners interested in assessing the impact of job training programs on employment outcomes, particularly in the field of social science research.

## Prerequisites Required

Before starting this tutorial, you should have:
- Basic understanding of R programming language.
- Familiarity with statistical concepts such as regression analysis.
- Access to R environment with necessary packages mentioned below.

## Difficulty Level

Normal

## Duration

Approximately 30-45 minutes

## Setup

### Environment Setup (Installing dependencies)

Ensure you have R (version 3.6.0 or higher) environment on your local machine.

Install the required R packages by running the following commands:


```R
install.packages("Matching")
install.packages("tableone")
```

## Input Data ([Digital behavior Data](https://www.gesis.org/en/institute/digital-behavioral-data))

This method can work with any dataset containing variables of interest, a treatment indicator, and covariates. For example:
- [The 'Call me sexist but' Dataset (CMSB)](https://search.gesis.org/research_data/SDN-10.7802-2251?doi=10.7802/2251) to Assessing the Impact of Gender Bias in Social Media Posts. 
Propensity score matching can be used to determine if an author's gender influences bias in social media posts by creating comparable groups based on observable characteristics. This method allows researchers to assess gender's causal impact on bias while controlling for potential confounding factors, providing insights into online discourse dynamics.

## Step-wise Guide

To utilize the propensity score matching technique for assessing the impact of job training programs on employment outcomes, follow these steps:

### 1. Download Files:
   - Download the following files into a single folder:
     - ["job_training_data.csv"](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/tutorial/job_training_data.csv): Input dataset containing the relevant variables for analysis.
     - ["propensity_matching_functions.R"](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/tutorial/propensity_matching_functions.R): R script containing functions for propensity score matching.
     - ["main_script.R"](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/tutorial/main_script.R): R script for executing the analysis.

### 2. Run Commands in "main_script.R":
   - Open ["main_script.R"](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/tutorial/main_script.R) in your R environment.
   - Run the commands sequentially to execute the analysis.

### 3. Load Input Dataset:
   - Execute the following lines to load the input dataset into R as `job_training_data`:
     ```R
      # Get the directory path of the main_script.R
      script_dir <- dirname(rstudioapi::getActiveDocumentContext()$path)
      
      # Example usage:
      job_training_data <- read.csv(file.path(script_dir, "job_training_data.csv"))
      ```
 **Sample Input Data**
   Sample input data can be provided in CSV format with columns representing variables of interest (EARNINGS_PRE, EARNINGS_POST), a treatment indicator (TREATED), and covariates (AGE, EDUCATION, EXPERIENCE).
Here is a screenshot of the sample input data:
   ![Image Alt Text](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/tutorial/job_training_data.PNG)
### 4. Define Functions:
   - Execute this line to define the necessary functions from "propensity_matching_functions.R":
     ```R
     source(file.path(script_dir, "propensity_matching_functions.R"))
     ```

### 5. Define Treatment Variable and Covariates:
   - Define the treatment variable (`treatment_var`) as "TREATED" and covariates (`covariates`) as relevant variables such as age, education level, and years of experience.
     ```R
        # Define variables
         treatment_var <- "TREATED"  # Specify your treatment variable
         covariates <- c("AGE", "EDUCATION", "EXPERIENCE")  # Specify relevant covariates
     ```

### 6. Perform Propensity Score Matching:
   - Call the `perform_propensity_matching` function with parameters `job_training_data`, `treatment_var`, and `covariates` to conduct propensity score matching:
     ```R
        # Perform propensity score matching
         matching_results <- perform_propensity_matching(data = job_training_data,
                                                   treatment_var = treatment_var,
                                                   covariates = covariates)
     ```
   - The output includes standardized mean differences (SMDs) of unmatched/matched data (`unmatched_smd` and `matched_smd`) and the matched data (`matched_data`).

### 7. Define Variables of Interest:
   - Define the variables of interest (`vars_of_interest`) based on the employment outcomes you want to assess.
     ```R
      vars_of_interest <- c("EARNINGS_PRE", "EARNINGS_POST")  # Specify variables for mean difference calculation
     ```
### 8. Perform Propensity Score Matching and Get the Matched Data:
   - Perform propensity score matching
     ```R
      matching_results <- perform_propensity_matching(data = job_training_data,
                                                   treatment_var = treatment_var,
                                                   covariates = covariates)
     # Matched data
      matched_data <- matching_results$matched_data
     ```

### 9. Compare the SMD in Unmatched and Matched Data:
      ```R
      # Print SMDs
      print(unmatched_smd)
      print(matched_smd)
      ```
      **Standard Mean Deviation:**
      By examining the SMD for unmatched and matched data under different covariances, we assess the effectiveness of the matching process in achieving balance between the treatment and control groups. A lower SMD indicates a smaller       difference between the two groups. For instance, in this example, the SMD for the variable "AGE" is 0.76 for unmatched data and 0.06 for matched data. This suggests that the treatment group in the matched data is more similar to the control group compared to the unmatched data.
      ![Image Alt Text](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/tutorial/output_SMD.PNG)
     
### 8. Calculate Mean Differences:
   - Call the `calculate_mean_diff` function with parameters `matched_data`, `treatment_var`, and `vars_of_interest` to calculate mean differences for the variables of interest.
     ```R
     # Calculate mean differences
      mean_diff <- calculate_mean_diff(data = matched_data, treatment_var = treatment_var, vars_of_interest = vars_of_interest)
     ```
   - The output provides the mean differences of `vars_of_interest`.
     ```R
      # Print mean differences
      print(mean_diff)
     ```
      **Mean difference:**
      Example for the interpretation: A mean difference of -666.6 for the variable EARNINGS_PRE indicates that, on average, individuals who participated in the training program had earnings that were $666.6 less before the training program compared to those who did not participate in the training program. 
Additionally, their earnings after the training program are, on average, $3000 more than those who did not participate in the training program, as indicated by the mean difference of 3000 for the variable EARNINGS_POST.
      ![Image Alt Text](https://github.com/momenifi/methodHub/blob/main/academic_mobility_propensity_score/tutorial/output_mainDiff.PNG)
      
      
      
 By following these steps, you can successfully conduct propensity score matching analysis to assess the impact of academic mobility on research productivity and collaboration indicators, focusing on the variables of interest "PPY", "CPP", and "COPP".
## Conclusion

In conclusion, this tutorial provides a detailed overview of propensity score matching techniques and their application in assessing the impact of job training programs on employment outcomes. By following the step-by-step guide and sample code provided, learners gain a comprehensive understanding of how to implement propensity score matching in R and interpret the results effectively.

## Conclusion

In conclusion, this tutorial provides a detailed overview of propensity score matching techniques and their application in assessing the impact of academic mobility on research productivity, received citations, and collaboration indicators. By following the step-by-step guide and sample code provided, learners gain a comprehensive understanding of how to implement propensity score matching in R and interpret the results effectively.

**How the Learning Goal is Achieved**

The learning goal of understanding and implementing propensity score matching techniques to assess the impact of academic mobility has been achieved through:

- Introduction to the concept of propensity score matching.
- Step-by-step instructions on data preparation, propensity score estimation, matching, and outcome analysis.
- Hands-on experience with example code and explanations.
- Interpretation of results and assessment of balance after matching.

**Skills Acquired with this Tutorial**

Upon completing this tutorial, learners have acquired the following skills:

- Understanding of propensity score matching and its relevance in social science research.
- Proficiency in using R programming language for propensity score matching analysis.
- Ability to interpret standardized mean differences (SMDs) and mean differences in matched data.
- Competence in assessing the impact of academic mobility on research productivity, received citations, and collaboration indicators using propensity score matching.

**Concluding Remarks**

Propensity score matching is a powerful technique for estimating causal effects in observational studies, particularly in the context of social science research. By mastering this technique, researchers can overcome challenges associated with selection bias and confounding variables, leading to more robust and reliable research findings. We encourage learners to further explore advanced topics in propensity score matching and apply these skills to their own research endeavors.

## References
- [The many facets of academic mobility and its impact on scholars' career](https://doi.org/10.1016/j.joi.2022.101280)
