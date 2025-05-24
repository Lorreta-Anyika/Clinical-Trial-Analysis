# 💊 Drug Safety Analysis: Ceutix Clinical Trial (Python & Streamlit Project)

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Key Questions Addressed](#key-questions-addressed)  
3. [Key Findings](#key-findings)  
4. [Data Sources](#data-sources)  
5. [Analysis Workflow](#analysis-workflow)  
6. [Statistical Methods & Code](#statistical-methods--code)  
7. [Dashboard Features](#dashboard-features)  
8. [Conclusion](#conclusion)  
9. [About the Analyst](#about-the-analyst)  
10. [Try the Dashboard & Connect](#try-the-dashboard--connect)  

---

## Project Overview

**Role Fit:** Healthcare Data Analyst | Pharmaceuticals | Clinical Trials  
**Tools:** Python (pandas, statsmodels, scipy), Streamlit  
**Demo:** [Live Streamlit Dashboard](https://lorreta-anyikatabrepositories-ekfr7ql8bchjr6atacbwts.streamlit.app/)  
**Read our Newsletter:** [The ALU DATATOK Brief](https://www.linkedin.com/pulse/issue-002-pharmaceutical-drug-trial-statistical-analysis-anyika-z2jkf/?trackingId=qRfoXwJTREKB2N8ITQPgqQ%3D%3D)

This project evaluates the safety of a new drug by Ceutix using real clinical trial data. The analysis aims to determine if the drug causes more side effects than a placebo, and whether age or other factors confound the results. All insights are brought to life in an interactive Streamlit dashboard for healthcare analysts and researchers.

> 💡 **Background**  
> Pharmaceutical companies must prove their drugs are safe compared to a placebo before approval. This analysis answers the question: “Does the Ceutix drug cause more adverse effects than a sugar pill?”—using robust statistical tests and clear data storytelling.

---

![image](https://github.com/user-attachments/assets/977b5f5d-3882-42de-860c-677f9367875c)
-can you identify the drug vs placebo?

## Key Questions Addressed

- **Is the proportion of patients experiencing adverse effects significantly higher in the Drug group compared to the Placebo group?**  
- **Is the number of different side effects a person experiences independent of whether they received the drug or placebo?**  
- **Are the Drug and Placebo groups similar in age, or could age be a confounding factor?**

---

## Key Findings

- **No significant difference in side effect rates:**  
  The Z-test showed the proportion of adverse effects is statistically similar between Drug and Placebo groups (p = 0.847).
- **No link between treatment and number of side effects:**  
  The Chi-Square test of independence found no association between group and number of side effects (p = 0.303).
- **Age is not a confounder:**  
  Both groups have statistically similar age distributions (Mann-Whitney U test, p = 0.64).
- **Result:**  
  The Ceutix drug is as safe as placebo, with no evidence of increased side effects or age bias.

---

## Data Sources

- **Trial Dataset:** 16,475 records, 61 fields from a randomized, double-blind clinical trial (Ceutix, fictional)
- **Fields Used:**  
  - `trx` (Drug/Placebo group)  
  - 5 adverse effects: `headache`, `ab.pain`, `dyspepsia`, `upper.resp.infect`, `coad`  
  - `id` (unique patient ID)  
  - `age`  

---

## Analysis Workflow

1. **Data Cleaning:**  
   - Subset data to relevant fields.
   - Remove duplicates by summarizing side effects per patient (one row per patient).
   - Feature engineering:  
     - `adverse_effects` (1 if any side effect, else 0)  
     - `num_effects` (count of unique side effects per patient)

2. **Statistical Analysis:**  
   - **Proportion Z-Test:** Compare adverse effect rates between groups.
   - **Chi-Square Test:** Test independence between group and number of side effects.
   - **Normality Check (Shapiro-Wilk):** Assess if age is normally distributed.
   - **Mann-Whitney U Test:** Compare age distributions between groups.

3. **Visualization:**  
   - Histograms of age distributions.
   - Bar/column charts for adverse effect proportions.

---

## Statistical Methods & Code

- **Proportion Z-Test:**
  ```python
  from statsmodels.stats.proportion import proportions_ztest
count = [num_with_effect_drug, num_with_effect_placebo]
nobs = [total_drug, total_placebo]
stat, pval = proportions_ztest(count, nobs)```

![image](https://github.com/user-attachments/assets/e8e4d2cb-5859-455a-9ecb-b1215fe83701)

- **Chi-Square Test:**  
from scipy.stats import chi2_contingency
chi2, pval, dof, expected = chi2_contingency(contingency_table)

- **Shapiro-Wilk Test:**  
``python
from scipy.stats import shapiro
stat, pval = shapiro(age_group)
```

- **Mann-Whitney U Test:**  
```python
from scipy.stats import mannwhitneyu
stat, pval = mannwhitneyu(age_drug, age_placebo)
```

![image](https://github.com/user-attachments/assets/f13e8739-c096-4c5d-a4c9-538fc9c72bd3)

---

## Dashboard Features

- 📊 **Adverse Effect Proportions:** Interactive bar charts comparing Drug vs Placebo.
- 📈 **Side Effect Counts:** Visual breakdown of number of side effects per group.
- 🧑‍⚕️ **Age Distribution:** Histograms and statistical summaries.
- 📑 **Statistical Test Results:** Z-test, Chi-Square, Shapiro-Wilk, and Mann-Whitney U outputs.
- 🖥️ **Live Demo:** Explore the data and results interactively via Streamlit.

---

## Conclusion

Despite initial concerns, the Ceutix drug does **not** cause significantly more side effects than placebo. Both the frequency and number of side effects are statistically similar across groups, and age does not confound the analysis. This project demonstrates a transparent, reproducible approach to clinical trial safety analytics—empowering healthcare analysts and decision-makers.

---

## About the Analyst

**Lorreta Anyika**  
Founder @ **ALU Datatok** | Healthcare Data & Policy Analyst | Python | Streamlit | Clinical Trials

📌 Specializes in data-driven safety analysis for pharma and healthcare  
📌 Experienced in clinical data cleaning, statistical testing, and dashboarding  
📌 Passionate about making complex results accessible to all stakeholders

- 🔗 [LinkedIn](https://www.linkedin.com/in/uchechukwu-lorreta-anyika-7b5b4a253/)  
- 📹 [YouTube Channel – ALU Datatok](https://www.youtube.com/channel/UCQL3Wg_j3D5TWtn6ticnTsg)  
- 💬 [Join our WhatsApp Community](https://chat.whatsapp.com/LhAFCcplWbf0MYfyShJTgf)  

---

## Try the Dashboard & Connect

- **Live Streamlit Demo:** [Click here to explore](https://lorreta-anyikatabrepositories-ekfr7ql8bchjr6atacbwts.streamlit.app/)


> *At ALU DATATOK, we use data not just to code, but to clarify, communicate, and create impact. Subscribe and share if you want more high-quality healthcare and data analysis projects!*
