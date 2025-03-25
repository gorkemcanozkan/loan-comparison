import streamlit as st

st.title("Interactive Loan Product Comparison Calculator")

# --- Business Details ---
st.header("1. Business Details")
monthly_revenue = st.number_input(
    "Monthly Revenue (€)",
    min_value=10000.0,
    step=1000.0,
    value=10000.0,
    help="Minimum €10k"
)
business_type = st.selectbox("Business Type", options=["SaaS", "Ecommerce", "SME"])
time_in_business = st.number_input(
    "Time in Business (months)",
    min_value=6,
    step=1,
    value=6,
    help="Minimum 6 months"
)
location = st.selectbox("Location", options=["UK", "EU", "Switzerland"])

# --- Financing Needs ---
st.header("2. Financing Needs")
desired_amount = st.number_input(
    "Desired Financing Amount (€)",
    min_value=5000.0,
    step=5000.0,
    value=100000.0
)
repayment_period = st.number_input(
    "Preferred Repayment Period (months)",
    min_value=1,
    step=1,
    value=12
)
collateral = st.checkbox("Available Collateral")

# --- Financing Options Comparison ---
st.header("3. Financing Options Compared")

# Example calculations for two financing products:
# Option 1: Revenue-Based Financing (RBF)
# Assume the monthly payment is a fixed percentage of the monthly revenue.
rbf_rate = 0.05  # 5% of monthly revenue (example value)
rbf_monthly_payment = monthly_revenue * rbf_rate
rbf_total_cost = rbf_monthly_payment * repayment_period

# Option 2: Asset-Based Financing (ABF)
# Assume a fixed repayment where the rate adjusts slightly if collateral is provided.
base_rate = 0.07  # base rate
abf_rate = 0.06 if collateral else base_rate  # lower rate if collateral is available
# Calculate a fixed monthly payment (for demonstration, a simple amortization-like formula)
abf_monthly_payment = desired_amount / repayment_period + desired_amount * abf_rate
abf_total_cost = abf_monthly_payment * repayment_period

# Display Revenue-Based Financing details
st.subheader("Revenue-Based Financing")
st.write(f"**Monthly Payment:** €{rbf_monthly_payment:,.2f} (approx. {rbf_rate*100:.1f}% of revenue)")
st.write(f"**Estimated Total Cost:** €{rbf_total_cost:,.2f}")
st.write("**Flexibility:** High")
if business_type == "SaaS":
    best_for = "Growing SaaS companies"
elif business_type == "Ecommerce":
    best_for = "Expanding Ecommerce platforms"
else:
    best_for = "Diverse SMEs"
st.write(f"**Best for:** {best_for}")

# Display Asset-Based Financing details
st.subheader("Asset-Based Financing")
st.write(f"**Monthly Payment:** €{abf_monthly_payment:,.2f}")
st.write(f"**Estimated Total Cost:** €{abf_total_cost:,.2f}")
st.write("**Flexibility:** Medium")
if business_type == "Ecommerce":
    best_for_abf = "Inventory-rich businesses"
else:
    best_for_abf = "Asset-rich companies"
st.write(f"**Best for:** {best_for_abf}")

st.markdown("---")
st.info("This is a simplified example. In a real-world application, calculations would be based on more detailed financial models and criteria.")
