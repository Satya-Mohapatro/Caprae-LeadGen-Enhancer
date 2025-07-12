import streamlit as st
import pandas as pd
from src.lead_scoring import score_leads
from src.email_verifier import verify_emails
from src.utils import clean_column_names

def main():
    st.title("Caprae LeadGen Enhancer")
    st.write("Upload your scraped leads CSV, verify emails, score leads, and export high-quality leads for outreach.")

    uploaded_file = st.file_uploader("Upload Leads CSV", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        df = clean_column_names(df)
        st.write("### Raw Data Preview", df.head())

        st.write("---")
        st.write("### Set Your Ideal Customer Profile (ICP)")
        industries = st.text_input("Preferred Industries (comma separated)", "SaaS, Fintech")
        min_funding_stage = st.selectbox("Minimum Funding Stage", ["Seed", "Series A", "Series B", "Series C", "Series D"])
        emp_min, emp_max = st.slider("Employee Count Range", 1, 1000, (10, 500))
        location = st.text_input("Preferred Location (optional)", "United States")

        if st.button("Verify Emails & Score Leads"):
            with st.spinner("Verifying emails..."):
                df = verify_emails(df)

            with st.spinner("Scoring leads..."):
                df = score_leads(
                    df,
                    preferred_industries=[i.strip() for i in industries.split(",")],
                    min_funding_stage=min_funding_stage,
                    emp_min=emp_min,
                    emp_max=emp_max,
                    preferred_location=location
                )

            st.success("Processing complete.")
            st.write("### Processed Leads Preview", df.head(30))

            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Processed Leads CSV",
                data=csv,
                file_name='processed_leads.csv',
                mime='text/csv'
            )

if __name__ == "__main__":
    main()