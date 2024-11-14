
import pandas as pd
import numpy as np

# FD Data
fd_data = {
    "Name": ["Bajaj Finance Ltd.", "SBI Bank", "ICICI Bank", "Axis Bank", "HDFC Bank", 
             "Bank of Baroda", "IDFC Bank", "Kotak Mahindra Bank", "Canara Bank", 
             "Yes Bank", "IndusInd Bank", "Punjab National Bank", "IDBI Bank", 
             "Union Bank", "Citibank", "RBL Bank", "Indian Bank"],
    "Type": ["NBFC", "Bank", "Bank", "Bank", "Bank", "Bank", "Bank", "Bank", "Bank", 
             "Bank", "Bank", "Bank", "Bank", "Bank", "Bank", "Bank", "Bank"],
    "Normal Rate": [8.4, 7.1, 7.25, 7.25, 7.4, 7.15, 7.75, 7.4, 7.25, 7.75, 
                    7.75, 7.25, 7.0, 7.3, 7.2, 8.1, 7.25],
    "Senior Citizen Rate": [8.65, 7.6, 7.8, 7.75, 7.9, 7.65, 8.25, 7.9, 7.75, 8.25,
                            8.25, 7.75, 7.5, 7.8, 7.85, 8.6, 7.75]
}

# Convert to DataFrame
df_fd = pd.DataFrame(fd_data)

def select_top_fds(age, risk_profile, df):
    rate_column = "Senior Citizen Rate" if age >= 60 else "Normal Rate"
    sorted_fds = df.sort_values(by=rate_column, ascending=False)
    if risk_profile == "low":
        top_fds = sorted_fds.head(3)
    elif risk_profile == "moderate":
        top_fds = sorted_fds.head(2)
    elif risk_profile == "high":
        top_fds = sorted_fds.head(1)
    return top_fds

# Gold ETF Data
data = pd.read_csv("GoldETFs.csv")
data.columns = data.columns.str.strip()

def select_top_gold_etf(age, risk_profile, df):
    rate_column = "NAV" if age >= 60 else "CHNG"
    sorted_gold_etfs = df.sort_values(by=rate_column, ascending=False)
    if risk_profile == "low":
        top_gold_etfs = sorted_gold_etfs.head(3)
    elif risk_profile == "moderate":
        top_gold_etfs = sorted_gold_etfs.head(2)
    elif risk_profile == "high":
        top_gold_etfs = sorted_gold_etfs.head(1)
    return top_gold_etfs
