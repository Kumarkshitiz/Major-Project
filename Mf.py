
import pandas as pd
import numpy as np

file_path = 'Historical Returns.xlsx'
df = pd.read_excel(file_path, skiprows=1)
df.columns = ["Scheme_Name", "Plan", "Category", "Crisil_Rating", "AuM", "1W", "1M", "3M", "6M", "YTD", "1Y", "2Y", "3Y", "5Y", "10Y"]

# Cleaning and processing
df[['3Y', '5Y', '10Y']] = df[['3Y', '5Y', '10Y']].replace("-", np.nan)
df[['3Y', '5Y', '10Y']] = df[['3Y', '5Y', '10Y']].infer_objects(copy=False).astype(float)
df['3Y'] = df['3Y'].fillna(df['3Y'].median())
df['5Y'] = df['5Y'].fillna(df['5Y'].median())
df['10Y'] = df['10Y'].fillna(df['10Y'].median())

def select_top_mf_direct(df, tenure, risk_profile):
    return_col = '3Y' if tenure < 5 else '5Y'
    if risk_profile == 'High':
        categories = ['Small Cap Fund', 'Mid Cap Fund']
        small_cap_count = 4
        mid_cap_count = 1
    elif risk_profile == 'Moderate':
        categories = ['Small Cap Fund', 'Mid Cap Fund', 'Large & Mid Cap Fund']
        small_cap_count = 2
        mid_cap_count = 2
        large_cap_count = 1
    else:
        categories = ['Large Cap Fund', 'Mid Cap Fund']
        mid_cap_count = 2
        large_cap_count = 3
    
    selected_funds = []
    for category in categories:
        category_df = df[(df['Category'] == category) & (df['Plan'] == 'Direct Plan')]
        if category == 'Small Cap Fund' and risk_profile in ['High', 'Moderate']:
            top_small_caps = category_df.nlargest(small_cap_count, return_col)
            selected_funds.append(top_small_caps)
        elif category == 'Mid Cap Fund' and risk_profile in ['High', 'Moderate', 'Low']:
            top_mid_caps = category_df.nlargest(mid_cap_count, return_col)
            selected_funds.append(top_mid_caps)
        elif category == 'Large & Mid Cap Fund' and risk_profile == 'Moderate':
            top_large_and_mid_caps = category_df.nlargest(large_cap_count, return_col)
            selected_funds.append(top_large_and_mid_caps)
        elif category == 'Large Cap Fund' and risk_profile == 'Low':
            top_large_caps = category_df.nlargest(large_cap_count, return_col)
            selected_funds.append(top_large_caps)
    result_direct_df = pd.concat(selected_funds)
    return result_direct_df[['Scheme_Name', 'Category', return_col]]

def select_top_mf_regular(df, tenure, risk_profile):
    return_col = '3Y' if tenure < 5 else '5Y'
    if risk_profile == 'High':
        categories = ['Small Cap Fund', 'Mid Cap Fund']
        small_cap_count = 4
        mid_cap_count = 1
    elif risk_profile == 'Moderate':
        categories = ['Small Cap Fund', 'Mid Cap Fund', 'Large & Mid Cap Fund']
        small_cap_count = 2
        mid_cap_count = 2
        large_cap_count = 1
    else:
        categories = ['Large Cap Fund', 'Mid Cap Fund']
        mid_cap_count = 2
        large_cap_count = 3
    
    selected_funds = []
    for category in categories:
        category_df = df[(df['Category'] == category) & (df['Plan'] == 'Regular')]
        if category == 'Small Cap Fund' and risk_profile in ['High', 'Moderate']:
            top_small_caps = category_df.nlargest(small_cap_count, return_col)
            selected_funds.append(top_small_caps)
        elif category == 'Mid Cap Fund' and risk_profile in ['High', 'Moderate', 'Low']:
            top_mid_caps = category_df.nlargest(mid_cap_count, return_col)
            selected_funds.append(top_mid_caps)
        elif category == 'Large & Mid Cap Fund' and risk_profile == 'Moderate':
            top_large_and_mid_caps = category_df.nlargest(large_cap_count, return_col)
            selected_funds.append(top_large_and_mid_caps)
        elif category == 'Large Cap Fund' and risk_profile == 'Low':
            top_large_caps = category_df.nlargest(large_cap_count, return_col)
            selected_funds.append(top_large_caps)
    result_regular_df = pd.concat(selected_funds)
    return result_regular_df[['Scheme_Name', 'Category', return_col]]
