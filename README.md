# HC3 Robust Regression

This Python script fits ordinary least squares (OLS) regression models for
Well-Being and calculates HC3 heteroscedasticity-consistent standard errors.
It prints each model's regression summary and compares conventional OLS
standard errors with HC3 robust standard errors.

The script runs these models:

| Model | Predictors | Outcome |
| --- | --- | --- |
| 1 | `Job_Demands` | `Well_Being` |
| 2 | `Job_Demands`, `Job_Resources` | `Well_Being` |

## Requirements

- Python 3
- pandas
- statsmodels

Install the required packages:

```bash
python -m pip install pandas statsmodels
```

## How to run

Pass the path to your CSV file as the script's only argument:

```bash
python hc3_regression.py "path/to/your_data.csv"
```

For example, in Windows PowerShell, from this folder:

```powershell
python .\hc3_regression.py "C:\path\to\your_data.csv"
```

Or, from the repository root:

```powershell
python .\Living\hc3_regression.py "C:\path\to\your_data.csv"
```

The CSV file must contain the `Well_Being`, `Job_Demands`, and
`Job_Resources` columns. Provide the path to the CSV file when running the
script; no default dataset is specified.

## Interpreting the output

For each model, the script prints coefficient estimates, conventional OLS
standard errors, HC3 robust standard errors, t-statistics, p-values, and 95%
confidence intervals. HC3 adjusts standard errors for heteroscedasticity; it
does not change the OLS coefficient estimates.

- **p-value < 0.05:** evidence of an association between the predictor and
  Well-Being at the 0.05 significance level.
- **p-value >= 0.05:** insufficient evidence of an association at the 0.05
  significance level.

A p-value does not measure the size or practical importance of an effect.
