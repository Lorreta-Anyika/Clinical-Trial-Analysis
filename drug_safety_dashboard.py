
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency, mannwhitneyu, shapiro
from statsmodels.stats.proportion import proportions_ztest

st.set_page_config(layout="wide")
st.title("💊 Drug Safety Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv("safety_data.csv")
    side_effects = ['headache', 'ab.pain', 'dyspepsia', 'upper.resp.infect', 'coad']
    df = df[['id', 'trx', 'age'] + side_effects]
    df = df.groupby('id').agg({
        'trx': 'first',
        'age': 'first',
        'headache': 'max',
        'ab.pain': 'max',
        'dyspepsia': 'max',
        'upper.resp.infect': 'max',
        'coad': 'max'
    }).reset_index()
    df['adverse_effects'] = df[side_effects].sum(axis=1).apply(lambda x: 1 if x > 0 else 0)
    df['num_effects'] = df[side_effects].sum(axis=1)
    return df

df = load_data()

overview, side_effects, age_analysis = st.tabs(["📋 Overview", "⚠️ Side Effects", "👥 Age Analysis"])

with overview:
    st.subheader("Trial Summary")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Participants", len(df))
    with col2:
        st.metric("Drug Group (%)", round(100 * (df['trx'] == 'Drug').mean(), 1))
    with col3:
        st.metric("Overall Side Effects (%)", round(100 * df['adverse_effects'].mean(), 1))

with side_effects:
    st.subheader("1. Proportion with Side Effects")
    adverse_counts = df.groupby('trx')['adverse_effects'].sum()
    sample_sizes = df['trx'].value_counts()
    count = [adverse_counts['Drug'], adverse_counts['Placebo']]
    nobs = [sample_sizes['Drug'], sample_sizes['Placebo']]
    z_stat, two_sample_p_value = proportions_ztest(count, nobs)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Z-Test P-value", f"{two_sample_p_value:.4f}")
        st.write("Significant" if two_sample_p_value < 0.05 else "Not significant")
    with col2:
        side_effect_rate = df.groupby('trx')['adverse_effects'].mean().reset_index()
        fig1, ax1 = plt.subplots()
        ax1.bar(side_effect_rate['trx'], side_effect_rate['adverse_effects'], color=['#4CAF50', '#F44336'])
        ax1.set_ylabel('% with Side Effects')
        ax1.set_title('Proportion with Adverse Effects')
        st.pyplot(fig1)

    st.subheader("2. Number of Side Effects per Person")
    contingency = pd.crosstab(df['trx'], df['num_effects'])
    chi2_stat, num_effects_p_value, dof, expected = chi2_contingency(contingency)

    col3, col4 = st.columns(2)
    with col3:
        st.metric("Chi-Square P-value", f"{num_effects_p_value:.4f}")
        st.write("Dependent" if num_effects_p_value < 0.05 else "No association")
    with col4:
        st.dataframe(contingency)

with age_analysis:
    st.subheader("3. Age Distribution")
    age_drug = df[df['trx'] == 'Drug']['age']
    age_placebo = df[df['trx'] == 'Placebo']['age']
    shapiro_p_drug = shapiro(age_drug).pvalue
    shapiro_p_placebo = shapiro(age_placebo).pvalue
    stat, age_group_effects_p_value = mannwhitneyu(age_drug, age_placebo)

    col5, col6, col7 = st.columns(3)
    with col5:
        st.metric("Shapiro (Drug)", f"{shapiro_p_drug:.4f}")
    with col6:
        st.metric("Shapiro (Placebo)", f"{shapiro_p_placebo:.4f}")
    with col7:
        st.metric("Mann-Whitney P", f"{age_group_effects_p_value:.4f}")

    fig2, ax2 = plt.subplots()
    ax2.hist(age_drug, bins=20, alpha=0.6, label='Drug')
    ax2.hist(age_placebo, bins=20, alpha=0.6, label='Placebo')
    ax2.set_title('Age Distribution by Group')
    ax2.set_xlabel('Age')
    ax2.set_ylabel('Frequency')
    ax2.legend()
    st.pyplot(fig2)

with st.expander("📝 Final Conclusion"):
    st.markdown("""
    - **No significant difference** in the proportion of participants with side effects.
    - **No evidence** that the number of side effects depends on treatment.
    - **Age distributions are similar** — age is not a confounder.
    """)
