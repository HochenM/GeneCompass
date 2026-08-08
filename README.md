# 🌾 GeneCompass: Machine Learning for Wheat DON Prediction

![Python](https://img.shields.io/badge/Python-3.11-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

GeneCompass is a machine learning project that predicts **Deoxynivalenol (DON) concentration** in wheat using high-dimensional SNP genotype data.

The project compares multiple regression algorithms, performs hyperparameter optimization, evaluates predictive performance, and identifies the most influential genetic markers associated with DON prediction.

This project was developed as a practical Machine Learning and Bioinformatics portfolio project while studying modern ML workflows.

---

# 📌 Project Overview

Deoxynivalenol (DON) is one of the most important mycotoxins affecting wheat quality and food safety.

Traditional phenotyping for DON resistance is expensive and time-consuming. Machine Learning offers an alternative approach by learning relationships between genomic markers and DON concentration.

The objective of this project is to:

- Predict DON concentration from SNP genotype data
- Compare multiple regression models
- Optimize the best-performing model
- Identify important SNP markers using feature importance analysis
- Build a reproducible end-to-end machine learning workflow

---

# 🎯 Objectives

- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Multiple regression model comparison
- Hyperparameter tuning
- Model evaluation
- Feature importance analysis
- Marker discovery for wheat breeding

---

# 📊 Dataset

The dataset originates from the publication:

> **Ensembles of Genomic and Hyperspectral Imaging-Based Prediction Enable Selection for Reduced Deoxynivalenol Content in Wheat Grains**

Published on Dryad (2025)

Dataset includes:

- 15,456 SNP markers
- 558 wheat genotypes
- DON concentration values
- Hyperspectral imaging measurements (not used in the current version)

Only the genomic SNP dataset is used in this project.

---

# 📂 Repository Structure

```text
GeneCompass/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_Data_Preparation.ipynb
│   ├── 02_EDA.ipynb
│   └── 03_Model_and_Evaluation.ipynb
│
├── results/
│   ├── figures/
│   │   ├── prediction_vs_actual/
│   │   ├── residual_plots/
│   │   └── residual_histograms/
│   │
│   ├── metrics/
│   │   └── model_comparison.csv
│   │
│   └── best_markers/
│
├ 
│   
│
├── src/
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore

---

# 🔬 Machine Learning Workflow

```text
Raw SNP Data
        │
        ▼
Data Cleaning
        │
        ▼
Feature Preparation
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Train/Test Split
        │
        ▼
Feature Scaling (when required)
        │
        ▼
Model Training
        │
        ▼
Model Comparison
        │
        ▼
Hyperparameter Optimization
        │
        ▼
Best Model Selection
        │
        ▼
Feature Importance Analysis
```

---

# 📖 Exploratory Data Analysis

EDA includes:

- Missing value analysis
- Duplicate detection
- DON distribution
- Histogram
- Boxplot
- Outlier analysis (IQR)
- Skewness analysis
- SNP value distribution
- Zero variance feature removal
- Low variance feature removal
- Correlation heatmaps

---

# 🤖 Machine Learning Models

The following regression algorithms were evaluated:

- Linear Regression
- Lasso Regression (SGD)
- Ridge Regression (SGD)
- Random Forest Regressor
- XGBoost Regressor
- Multi-layer Perceptron (MLP)

---

# ⚙️ Hyperparameter Optimization

The best-performing model was optimized using:

- GridSearchCV
- 5-Fold Cross Validation

Optimized parameters include:

- Number of estimators
- Maximum tree depth
- Learning rate
- Subsample ratio

---

# 📈 Model Evaluation

Models are evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Coefficient of Determination (R²)

Additional evaluation includes:

- Prediction vs Actual visualization
- Residual Plot
- Residual Distribution
- Cross Validation scores
- Model comparison table

---

# 🧬 Feature Importance Analysis

After selecting the best model, feature importance scores are extracted to identify SNP markers contributing most strongly to DON prediction.

The project exports the most informative genetic markers for downstream biological interpretation.

---

# 📌 Results

**Best Model**

> XGBoost Regressor

Performance metrics will be updated after final model optimization.

| Metric | Value |
|---------|------|
| MAE | TBD |
| RMSE | TBD |
| R² | TBD |

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/HochenM/GeneCompass.git
```

Move into the project

```bash
cd GeneCompass
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Run notebooks in order:

```
01_Data_Preparation.ipynb

↓

02_EDA.ipynb

↓

03_Model_and_Evaluation.ipynb
```

---

# 🛠 Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Joblib
- Jupyter Notebook

---

#  Future Improvements

Planned future work includes:

- Classification of resistant vs susceptible wheat lines
- SHAP explainability
- Permutation Importance
- Integration of hyperspectral features
- Model deployment using FastAPI
- Docker support
- Complete `src/` package implementation
- CI/CD workflow
- Automated experiment tracking

---

#  References

Concepcion, J., & Olson, E.

Ensembles of Genomic and Hyperspectral Imaging-Based Prediction Enable Selection for Reduced Deoxynivalenol Content in Wheat Grains.

Dryad Digital Repository.

---

# 📄 License

This project is licensed under the MIT License.

---

#  Author

**Hossein Moein**

GitHub:

https://github.com/HochenM

LinkedIn:

https://www.linkedin.com/in/hossein-moein-276b28271/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BdxV%2FhdRESwONVJom7S46tw%3D%3D

---

If you found this project useful, consider giving it a ⭐.
