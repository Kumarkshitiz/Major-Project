# equity_selection.py

import pandas as pd

nifty_100 = pd.read_csv("Large_Cap.csv")
nifty_midcap_100 = pd.read_csv("Mid_Cap.csv")
nifty_smallcap_100 = pd.read_csv("Small_Cap.csv") 

nifty_100.columns = nifty_100.columns.str.strip()
nifty_midcap_100.columns = nifty_midcap_100.columns.str.strip()
nifty_smallcap_100.columns = nifty_smallcap_100.columns.str.strip()

nifty_100 = nifty_100[['SYMBOL', '%CHNG']].dropna()
nifty_midcap_100 = nifty_midcap_100[['SYMBOL', '%CHNG']].dropna()
nifty_smallcap_100 = nifty_smallcap_100[['SYMBOL', '%CHNG']].dropna()

def get_top_stocks(risk_profile):
    top_large_cap = nifty_100.sort_values('%CHNG', ascending=False).head(4)
    top_mid_cap = nifty_midcap_100.sort_values('%CHNG', ascending=False).head(4)
    top_small_cap = nifty_smallcap_100.sort_values('%CHNG', ascending=False).head(4)

    if risk_profile == 'high':
        selected_stocks = pd.concat([top_small_cap.head(4), top_mid_cap.head(1)])
    elif risk_profile == 'moderate':
        selected_stocks = pd.concat([top_small_cap.head(2), top_mid_cap.head(2), top_large_cap.head(1)])
    elif risk_profile == 'low':
        selected_stocks = pd.concat([top_mid_cap.head(2), top_large_cap.head(3)])
    return selected_stocks[['SYMBOL', '%CHNG']]
