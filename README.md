# About this Repo
* Download the data
* Understand the problem statement
* Analysis Questions
* Further readings  
  
## Downloading the data
The data for this project is provided with the souce code under file name Project_1.zip. Incase you decided to download the data  and try your own will be much beneficial to you.  

## Understanding the problem statement
it's a supervised learning beacause it's already predefined for us the target value for pridiction. it's a regression problem because the output variable is a real or continuous value, to predict hc_mortgage_mean. Many different models can be used, but we use the simplest, linear regression. It tries to fit data with the best hyper-plane which goes through the points.  
it is a very straightforward simple linear approach for predicting a quantitative response Y in our case "household mortgage mean" on the basis of  predictor variables.  
 
    Y = β0 + β1X1 + β2X2 + ··· + βpXp + e,
    Y  = output "Household mortgage mean"
    β0 = intercept
    β1.. = slope
    X1.. = Variables
    e  = bias
    
<img width="429" alt="Screenshot 2021-12-09 164545" src="https://user-images.githubusercontent.com/85021780/145407846-a817349f-3b28-421d-ba99-5cc3dc7c3376.png">  

## Questions Answered in this Project
> * Figure out the primary key and look for the requirement of indexing?
> * Gauge the fill rate of the variables and devise plans for missing value treatment. Please explain explicitly the reason for the treatment chosen for each variable?
> * Explore the top 2,500 locations where the percentage of households with a second mortgage is the highest and percent ownership is above 10 percent? Visualize using geo-map? You may keep the upper limit for the percent of households with a second mortgage to 50 percent?
> * Create pie charts to show overall debt and bad debt?
> * Create Box and whisker plot and analyze the distribution for 2nd mortgage, home equity, good debt, and bad debt for different cities?
> * Create a collated income distribution chart for family income, house hold income, and remaining income?
> * Use pop and ALand variables to create a new field called population density?
> * Use male_age_median, female_age_median, male_pop, and female_pop to create a new field called median age?
> * Visualize the findings using appropriate chart type?
> * Create bins for population into a new variable by selecting appropriate class interval so that the number of categories don’t exceed 5 for the ease of analysis.
     a) Analyze the married, separated, and divorced population for these population brackets?
     b) Visualize using appropriate chart type?
> * Please detail your observations for rent as a percentage of income at an overall level, and for different states?
> * Perform correlation analysis for all the relevant variables by creating a heatmap. Describe your findings?
> * Use factor analysis to find latent variables in our dataset and gain insight into the linear relationships in the data?
> * Build a linear Regression model to predict the total monthly expenditure for home mortgages loan. Please refer ‘deplotment_RE.xlsx’. Column hc_mortgage_mean is predicted variable. This is the mean monthly mortgage and owner costs of specified geographical location. Note: Exclude loans from prediction model which have NaN (Not a Number) values for hc_mortgage_mean.  

## Further Reading
[An Introduction to Statistical Learning] (https://hastie.su.domains/ISLR2/ISLRv2_website.pdf)
[Supervised Machine Learning] (https://www.geeksforgeeks.org/regression-classification-supervised-machine-learning/)  
[A Quick Overview of Regression Algorithms in Machine Learning ] ( https://www.analyticsvidhya.com/blog/2021/01/a-quick-overview-of-regression-algorithms-in-machine-learning/)

  
