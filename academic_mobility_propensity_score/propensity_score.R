library(Matching)
library(tableone)


perform_propensity_matching <- function(data, treatment_var, covariates, caliper = 0.2, replace = FALSE) {
  # Check to determine if log transformation is needed for each covariate
  for (col in covariates) {
    data[[col]] <- if (is.numeric(data[[col]]) && max(data[[col]]) - min(data[[col]]) > 10) log(data[[col]]) else data[[col]]
  }
  # Fit propensity score model
  ps_formula <- as.formula(paste(treatment_var, "~", paste(covariates, collapse = " + ")))
  ps_model <- glm(ps_formula, family = binomial(link = "logit"), data = data)
  
  # Predict propensity scores
  data$p_ps <- predict(ps_model, type = "response")
  data$p_ps_no <- 1 - data$p_ps
  
  # Perform matching
  listMatch <- Match(Tr = (data[[treatment_var]] == 1),
                     X = log(data$p_ps / data$p_ps_no),
                     M = 1,
                     caliper = caliper,
                     replace = replace,
                     ties = FALSE,
                     version = "fast")
  
  # Extract matched data
  matched_indices <- unlist(listMatch[c("index.treated", "index.control")])
  matched_data <- data[matched_indices, ]
  
  # Calculate standardized mean differences for unmatched data
  tabUnmatched <- CreateTableOne(vars = covariates, strata = treatment_var, data = data, test = FALSE)
  unmatched_smd <- ExtractSmd(tabUnmatched)
  
  # Calculate standardized mean differences for matched data
  tabMatched <- CreateTableOne(vars = covariates, strata = treatment_var, data = matched_data, test = FALSE)
  matched_smd <- ExtractSmd(tabMatched)
  
  # Return SMDs and matched data
  return(list(unmatched_smd = unmatched_smd, matched_smd = matched_smd, matched_data = matched_data))
}



calculate_mean_diff <- function(data, treatment_var, vars_of_interest) {
  # Subset data for treatment groups
  treated_data <- data[data[[treatment_var]] == 1, ]
  control_data <- data[data[[treatment_var]] == 0, ]
  
  # Calculate mean difference, t-value, and SE for each variable
  results <- lapply(vars_of_interest, function(var) {
    treated_var <- treated_data[[var]]
    control_var <- control_data[[var]]
    if (length(treated_var) > 0 & length(control_var) > 0) {
      t_test_result <- t.test(treated_var, control_var, paired = TRUE)
      mean_diff <- t_test_result$estimate
      t_value <- t_test_result$statistic
      se <- t_test_result$stderr
      return(data.frame(Variable = var, Mean_Difference = mean_diff, T_Value = t_value, SE = se))
    } else {
      return(data.frame(Variable = var, Mean_Difference = NA, T_Value = NA, SE = NA))
    }
  })
  
  # Combine results into a data frame
  result_df <- do.call(rbind, results)
  
  # Return data frame with mean difference, t-value, and SE
  return(result_df)
}


# Example usage:
# Assuming 'data_sample' is your dataset containing relevant variables
data_sample<-read.table("C:/Users/momenifi/Desktop/gitMethodHub/methodHub/academic_mobility_propensity_score/mydata_sample.csv",header=TRUE,sep=",",quote="\r",dec = ".")


# Define variables
treatment_var <- "mobile"  # Specify your treatment variable
covariates <- c("REGION", "MAIN_FIELD", "INTERNATIONAL_COAUTHOR", "GENDER", "GDP_PC_ORIGIN", "age")

# Perform propensity score matching
matching_results <- perform_propensity_matching(data = data_sample,
                                                treatment_var = treatment_var,
                                                covariates = covariates)


# Access SMDs of unmatched and matched data
unmatched_smd <- matching_results$unmatched_smd
matched_smd <- matching_results$matched_smd
matched_data <- matching_results$matched_data

# Print SMDs
print(unmatched_smd)
print(matched_smd)


vars_of_interest <- c("PPY", "CPP", "COPP")  # Specify variables for mean difference calculation

# Calculate mean differences
mean_diff <- calculate_mean_diff(data = matched_data, treatment_var = treatment_var, vars_of_interest = vars_of_interest)

# Print mean differences
print(mean_diff)

