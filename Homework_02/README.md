# 📘 Homework 2: Descriptive Statistics, Correlation, and Regression Analysis

This assignment introduces students to data summarization and regression analysis using Python. 
We will learn how economists and researchers explore datasets, identify relationships, and estimate demand models.

The focus is not just coding—it’s understanding what the numbers are telling you.

## 📊 What You Will Learn

By completing this homework, we will:

* Create professional descriptive statistics tables
* Analyze relationships using a correlation matrix
* Visualize correlations with a heatmap
* Estimate a multiple linear regression model
* Transform variables using logarithms
* Interpret coefficients as elasticities

## 🧠 Economic Concepts

This assignment builds directly on economic theory:

* Demand Function → Consumption depends on prices and income
* Substitutes → Tea may influence coffee demand
* Complements → Sugar may influence coffee demand
* Multivariate Analysis → Multiple factors affect behavior simultaneously
* Elasticity → Log models measure percentage responses

## 📂 Files Included

* data/ Coffee_demand.csv – Dataset used in the analysis
* figures/ – Generated plots (e.g., correlation heatmap)
* notebooks/ – Jupyter notebook version
* scripts/ Homework_02.py – Main Python script

## 🚀 Getting Started (Recommended: Google Colab)

The easiest way to complete this assignment is with
👉 Google Colab

* Option 1: Run in Google Colab (Recommended)
* Open Colab
* Click "New Notebook"
Upload:
* Homework_02.py (or copy/paste the code)
* Coffee_demand.csv
* Run each section step-by-step

## 🧪 Assignment Structure

Part 1: Descriptive Statistics

* Generate a clean summary table
* Examine: Mean vs median
* Spread (standard deviation)
* Skewness

👉 Focus: Understanding the shape and distribution of the data

Part 2: Correlation Analysis

* Compute the correlation matrix
* Visualize relationships using a heatmap

👉 Focus: Identifying relationships between variables

Part 3: Linear Regression (Levels Model)

Estimate the demand function:

Coffee Consumption = f(Coffee price, Sugar price, Tea price, Income)

👉 Focus: Understanding how multiple variables affect demand

Part 4: Log-Log Regression (Elasticities)

* Transform all variables using natural logs
* Estimate a new model where:

👉 Coefficients = Elasticities

Example:
A coefficient of -0.5 → A 1% increase in price reduces demand by 0.5%

👉 Focus: Interpreting economic sensitivity

## 📈 Example Visualizations

💡 Key Takeaways

* Always understand your data before modeling
* Correlation helps identify relationships—but not causation
* Regression allows you to control for multiple variables
* Log transformations turn models into powerful economic tools

## 🎯 Submission Guidelines

* Run all code successfully
Generate:
* Descriptive statistics table
* Correlation heatmap
* Regression outputs
Be prepared to explain:
* What the coefficients mean
* Whether results support economic theory

This assignment is designed to bridge the gap between data analysis and economic reasoning.
Focus on interpreting results—not just running the code.
