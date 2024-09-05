# Exploratory Data Analysis (EDA)

This Jupyter Notebook contains an **Exploratory Data Analysis (EDA)** of a dataset, focusing on various aspects of the data, such as distribution, relationships between features, and basic summary statistics. The EDA was conducted using Python with popular data science libraries such as `pandas`, `matplotlib`, and `seaborn`.

## Key Features
- **Data Preprocessing**: Loading and cleaning the dataset, handling missing values, and performing necessary transformations.
- **Univariate Analysis**: Analyzing individual features using summary statistics, histograms, and box plots to understand the distribution and outliers.
- **Bivariate Analysis**: Studying relationships between pairs of variables using correlation matrices, scatter plots, and other visualizations.
- **Insights**: Key takeaways and observations from the analysis.

## Libraries Used
- **pandas**: For data manipulation and preprocessing.
- **matplotlib**: For creating static, animated, and interactive visualizations.
- **seaborn**: For making statistical graphics, building on top of `matplotlib`.

## Analysis Overview

1. **Data Loading**:
   - The dataset is loaded and inspected for initial exploration.
   
2. **Data Cleaning**:
   - Handling missing values.
   - Checking for inconsistencies and ensuring proper data types.

3. **Univariate Analysis**:
   - **Numeric Features**: Histograms and box plots were used to visualize the distribution of numeric features such as `mileage`, `engine_capacity`, and `price`.
   - **Categorical Features**: Bar plots and value counts were used to explore the distribution of categorical variables like `fuel_type` and `transmission_type`.

4. **Bivariate Analysis**:
    - **Fuel vs. Mileage**: Analyzed the relationship between fuel type and mileage using box plots. 
    - **Key Observation:** CNG yields the highest mileage, followed by diesel, while diesel engines show a relatively low average mileage in the dataset.
    - **Other relationships**: Scatter plots and correlation heatmaps were used to explore potential correlations between other variables.

## Visualizations

- Histograms: To explore the distribution of continuous variables like mileage and engine capacity.
- Box Plots: To identify outliers and compare distributions across different categories.
- Correlation Matrix: A heatmap was generated to study the relationships between different numerical features.
- Scatter Plots: To visualize relationships between pairs of numeric variables.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/iampraveens/SNS-iHub-Assignment.git
    ```

2. Navigate to the project directory:
    ```bash
    cd your-repository
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Open the Jupyter Notebook:
    ```bash
    jupyter notebook "Problem Statement 4 - Data Analysis.ipynb"
    ```
    
## Results and Insights
- **Fuel Efficiency:** CNG offers the best mileage, followed by diesel. However, diesel engines also exhibit low efficiency on average.
- **Correlation:** Features such as engine capacity and price were studied for potential correlations.

## Conclusion
The EDA provided important insights into the dataset, helping to uncover patterns and relationships between different features. These findings will assist in future modeling and decision-making processes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.