# ⚡ Steel Industry Energy Consumption Prediction using PCA & Random Forest

## 📖 Project Overview

Energy consumption prediction is one of the most important tasks in modern industries because electricity is one of the highest operational costs in manufacturing. Accurate prediction helps industries optimize production schedules, reduce unnecessary energy usage, lower operational expenses, and improve sustainability.

This project focuses on predicting the **electricity consumption (Usage_kWh)** of a steel manufacturing industry using Machine Learning. The dataset contains electrical measurements, operational parameters, and production information collected from industrial equipment.

A complete end-to-end Machine Learning pipeline has been implemented, including data preprocessing, feature engineering, dimensionality reduction using Principal Component Analysis (PCA), model training, performance evaluation, visualization, and deployment-ready model saving.

The main objective is to compare the prediction performance of Random Forest Regression using the original dataset and PCA-transformed datasets to understand the impact of dimensionality reduction on model accuracy and computational efficiency.

---

# 🎯 Objectives

The primary objectives of this project are:

- Predict industrial energy consumption accurately.
- Understand the relationship between industrial electrical parameters and energy usage.
- Remove unnecessary and highly correlated features using PCA.
- Reduce model complexity while maintaining high prediction accuracy.
- Compare machine learning performance before and after dimensionality reduction.
- Build a deployment-ready machine learning pipeline.
- Visualize the most important patterns in the industrial dataset.
- Save the trained model for future real-time prediction systems.

---

# 📂 Dataset Description

The project uses the **Steel Industry Energy Consumption Dataset**.

The dataset contains information about industrial energy usage measured over different operating conditions.

Some important features include:

- Usage_kWh (Target Variable)
- Lagging Current Reactive Power
- Leading Current Reactive Power
- CO2 Emissions
- Lagging Current Power Factor
- Leading Current Power Factor
- NSM (Number of Seconds from Midnight)
- Week Status
- Day Type
- Load Type
- Month
- Day of Week

Each row represents the operational condition of the steel industry at a specific time.

---

# 🎯 Target Variable

The target variable is:

**Usage_kWh**

This variable represents the amount of electrical energy consumed by the steel industry.

The machine learning model learns patterns from all input features and predicts future energy consumption.

---

# 🧹 Data Preprocessing

Before training the machine learning model, several preprocessing techniques were applied to improve data quality.

## Missing Value Handling

The dataset contained missing values in the Power Factor Ratio column.

Instead of removing those rows, the missing values were replaced with the column mean to preserve data consistency and avoid losing useful information.

---

## Data Leakage Removal

Columns that could introduce data leakage or were unnecessary for prediction were removed.

Removing leakage features ensures that the model learns genuine relationships instead of memorizing hidden information.

---

## Categorical Encoding

Machine learning algorithms cannot process text values directly.

Categorical features such as:

- Load Type
- Day Type
- Week Status
- Day of Week
- Month

were converted into numerical values using One-Hot Encoding.

This transformation enables the model to understand categorical information correctly.

---

# ⚙ Feature Scaling

Since PCA is sensitive to feature magnitude, StandardScaler was applied before PCA.

Standardization transforms every feature so that:

- Mean becomes 0
- Standard deviation becomes 1

This prevents features with larger values from dominating the principal components.

---

# 📉 Principal Component Analysis (PCA)

Principal Component Analysis (PCA) is a dimensionality reduction technique.

Instead of using every original feature, PCA creates a smaller number of new features called **Principal Components**.

These components preserve most of the information available in the original dataset while removing redundancy.

Benefits of PCA include:

- Reduced feature dimensions
- Faster model training
- Reduced computational cost
- Lower memory usage
- Less noise
- Better generalization

---

# 📊 Explained Variance

After applying PCA, the explained variance ratio was calculated.

This metric indicates how much information each principal component retains from the original dataset.

For example:

- PC1 captures the largest amount of variance.
- PC2 captures the second largest variance.
- Additional components gradually contribute less information.

A cumulative variance plot was used to determine the minimum number of components required to preserve approximately 95% of the original information.

---

# 📈 Data Visualization

Several visualizations were created to better understand the dataset.

These include:

## Correlation Heatmap

Shows the relationship between all numerical variables.

---

## Scree Plot

Displays the variance explained by every principal component.

---

## Cumulative Variance Plot

Shows how much total information is preserved as additional components are included.

---

## PCA Loading Heatmap

Illustrates the contribution of every original feature to each principal component.

---

## Energy Consumption Charts

Visualizations showing:

- Energy Consumption by Hour
- Energy Consumption by Load Type
- Feature Relationships

These graphs provide useful business insights regarding industrial energy usage.

---

# 🤖 Machine Learning Model

Random Forest Regression was selected because it provides:

- High prediction accuracy
- Strong resistance to overfitting
- Ability to capture nonlinear relationships
- Excellent performance on structured datasets

Three experiments were performed:

1. Random Forest using Original Features
2. Random Forest using PCA (3 Components)
3. Random Forest using PCA (95% Variance)

The performance of all models was compared.

---

# 📏 Model Evaluation

The trained models were evaluated using:

## Root Mean Squared Error (RMSE)

Measures prediction error.

Lower RMSE indicates better performance.

---

## R² Score

Measures how well the model explains the target variable.

Values closer to **1** indicate excellent predictive performance.

---

# 📊 Workflow

The complete workflow followed in this project is:

1. Import Required Libraries
2. Load Dataset
3. Data Inspection
4. Missing Value Handling
5. Remove Leakage Features
6. Encode Categorical Variables
7. Split Features and Target
8. Train-Test Split
9. Feature Scaling
10. Apply PCA
11. Train Random Forest Model
12. Evaluate Model Performance
13. Compare PCA and Original Models
14. Generate Visualizations
15. Save Deployment Pipeline

---

# 💾 Model Saving

The final trained pipeline was saved using Joblib.

Saving the model allows it to be directly integrated into:

- Flask Applications
- FastAPI Applications
- Streamlit Applications
- Production Systems

without retraining the model every time.


# 🚀 Future Improvements

The project can be enhanced further by implementing:

- Hyperparameter Tuning
- Cross Validation
- Grid Search
- Random Search
- XGBoost Regression
- LightGBM Regression
- CatBoost Regression
- SHAP Explainability
- Feature Importance Analysis
- Real-Time Prediction API
- Docker Deployment


# 📚 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

---

# 📌 Conclusion

This project demonstrates a complete industrial machine learning workflow for predicting electricity consumption in the steel industry. PCA successfully reduces the dimensionality of the dataset while preserving most of its useful information. Random Forest Regression provides highly accurate predictions, making the solution suitable for industrial energy forecasting, optimization, and future deployment.

