"""
======================================================================
HC3 Robust Standard Errors for Regression Models
======================================================================

Author: Binyam Heyi

Purpose:
--------
This script reads survey/regression data from a CSV file and fits
ordinary least squares (OLS) regression models with HC3
heteroscedasticity-consistent standard errors.

HC3 robust standard errors adjust the estimated uncertainty of the
regression coefficients when residual variance is not constant. The
script prints the regression summaries and compares conventional OLS
standard errors with HC3 robust standard errors.

Models:
-------
1. Job Demands -> Well-Being
2. Job Demands + Job Resources -> Well-Being

How to Run:
-----------
1. Open Command Prompt or PowerShell.

2. Navigate to the folder containing this Python script.

3. Run the script and provide the complete path to the CSV file:

      python hc3_regression.py "C:\\path\\to\\your_data.csv"

4. Required packages can be installed using:

      pip install pandas statsmodels

Note:
-----
A CSV file path must be supplied when running this script.
The CSV file must contain Well_Being, Job_Demands, and Job_Resources
columns.

======================================================================
"""

import sys
from pathlib import Path

import pandas as pd
import statsmodels.formula.api as smf

def run_hc3_regression(df, formula, label):
    print(f"\n{'='*70}\n{label}\n{'='*70}")

    ols_model = smf.ols(formula, data=df).fit()
    hc3_model = ols_model.get_robustcov_results(cov_type="HC3")
    print("\n-- OLS Regression with HC3 Robust Standard Errors --")
    print(hc3_model.summary())

    ci = hc3_model.conf_int()
    print("\n-- OLS vs. HC3 Standard Error Comparison --")
    for i, name in enumerate(ols_model.params.index):
        b = ols_model.params[name]
        se_ols = ols_model.bse[name]
        se_hc3 = hc3_model.bse[i]
        t = hc3_model.tvalues[i]
        p = hc3_model.pvalues[i]
        lower, upper = ci[i]
        print(f"{name:<15} B={b:.4f}  OLS SE={se_ols:.4f}  HC3 SE={se_hc3:.4f}  "
              f"t={t:.2f}  p={p:.4g}  95% CI=[{lower:.3f}, {upper:.3f}]")

def main():
    if len(sys.argv) != 2:
        print("Error: No CSV file path was provided.")
        print()
        print("Usage:")
        print(
            r'  python "path to your python file" '
            r'"path to your csv"'
        )
        sys.exit(1)

    data_path = Path(sys.argv[1])
    if not data_path.is_file():
        print(f"Error: CSV file not found at:\n{data_path}")
        print("\nPlease verify that the file path is correct.")
        sys.exit(1)

    df = pd.read_csv(data_path)

    run_hc3_regression(df, 'Well_Being ~ Job_Demands', 'Job Demands alone -> Well-Being')
    run_hc3_regression(df, 'Well_Being ~ Job_Demands + Job_Resources', 'Combined (RQ3) -> Well-Being')

if __name__ == "__main__":
    main()
