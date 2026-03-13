import streamlit as st
import os

# --- PADI Bureau Liaison Node ---
st.set_page_config(page_title="PADI Bureau", page_icon="🏦")

# This pulls the key you saved in Hugging Face Settings
STRIPE_KEY = os.getenv("STRIPE_SECRET_KEY")

st.title("🤖 PADI Agent Liaison")
st.subheader("High-Value Settlement Portal")

with st.container(border=True):
    st.markdown("### 🛠️ Enterprise Tier: 1,300,000 KES")
    st.write("Target: EU AI Act Annex IV Compliance")
    
    if st.button("💳 Initialize Secure Checkout"):
        if STRIPE_KEY:
            st.success("Secure Handshake Initialized.")
            st.link_button("Proceed to Stripe/Paystack", "https://checkout.stripe.com/test_demo")
        else:
            st.error("Bureau Offline: Secret Key missing in Space Settings.")

st.divider()
st.caption("Protocol: A2A | Node: Nairobi N-1")
