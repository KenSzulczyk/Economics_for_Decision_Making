# 📘 Homework 3: Estimating a Cubic Cost Function

This assignment introduces students to cost modeling and nonlinear regression using Python. 
We will analyze production data and estimate a cubic cost function, a common model in economics used to capture increasing marginal costs.

The goal is to move beyond simple linear relationships and understand how costs behave as production scales.

## 📊 What We Will Learn

By completing this homework, we will:

* Work with real production and cost data
* Create polynomial variables (Q2, Q3)
* Generate descriptive statistics for key variables
* Analyze relationships between polynomial terms
* Estimate a cubic cost function using regression
* Visualize total cost and fitted cost curves
* Interpret economic meaning from regression results

## 🧠 Economic Concepts

This assignment connects directly to core microeconomic theory:

* Cost Functions → Relationship between output and total cost
* Fixed Costs → Costs when output is zero
* Marginal Cost → Cost of producing one more unit
* Nonlinear Production → Costs often increase at an increasing rate
* Multicollinearity → Polynomial terms can be highly correlated

## 📂 Files Included

* data/ Cubic_cost_function.csv – Dataset containing output and cost data
* figures/ – Generated plots (cost curves, correlation heatmap)
* notebooks/ – Jupyter notebook version
* scripts/ Homework_03.py – Main Python script

## 🚀 Getting Started (Recommended: Google Colab)

The easiest way to complete this assignment is with
👉 Google Colab

* Option 1: Run in Google Colab (Recommended)
* Open Colab
* Click "New Notebook"
Upload:
* Homework_03.py (or copy/paste the code)
* Cubic_cost_function.csv
* Run each section step-by-step

## 🧪 Assignment Structure

Part 1: Data Preparation

* Load the dataset
* Create polynomial variables: Q2 (Quantity squared) and Q3 (Quantity cubed)

👉 Focus: Preparing data for nonlinear modeling

Part 2: Descriptive Statistics

* Generate summary statistics for:
* Quantity
* Total Cost

👉 Focus: Understanding the scale and variation of production

Part 3: Correlation Analysis

* Examine correlation between: Total cost, Q, Q2, and Q3

👉 Focus: Recognizing multicollinearity in polynomial models

Part 4: Cubic Cost Function

* Estimate the model: Cost = β0 + β1 Q + β2 Q2 + β3 Q3

👉 Focus: Modeling nonlinear cost behavior

Part 5: Visualization

* Plot:
* Actual cost data (scatter plot)
* Fitted cubic cost curve

👉 Focus: Seeing how well the model fits the data

## 📈 Example Visualization

💡 Key Takeaways

* Real-world cost functions are often nonlinear
* Polynomial models help capture complex relationships
* Fixed costs come from the intercept
* Marginal cost can be derived from the slope of the function
* Visualization helps connect equations to economic intuition

## 🎯 Assignment Questions

Be prepared to answer:

* Report regression estimates and statistical significance
* Identify the firm’s fixed costs
* Compute average total cost at Q = 140
* Compute marginal cost at Q = 140

## 📌 Final Thoughts

This assignment bridges data analysis, regression modeling, and economic theory.
Focus on understanding how costs behave—not just estimating equations.

More advanced tools build on this foundation, so take time to understand each step.
