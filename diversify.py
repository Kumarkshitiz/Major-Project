# fund_diversification.py
def diversify_funds(age, tenure, investment_type, amount, risk_profile):
    allocation = {
        "FDs": 0,
        "Mutual Funds": 0,
        "Gold ETFs": 0,
        "Equity Large Cap": 0,
        "Equity Mid Cap": 0,
        "Equity Small Cap": 0
    }
    # Diversification based on risk profile and tenure
    if risk_profile == "low":
        if tenure <= 3:
            allocation.update({"FDs": 0.50, "Mutual Funds": 0.20, "Gold ETFs": 0.20, "Equity Large Cap": 0.10})
        else:
            allocation.update({"FDs": 0.40, "Mutual Funds": 0.25, "Gold ETFs": 0.15, "Equity Large Cap": 0.20})
    elif risk_profile == "moderate":
        allocation.update({
            "FDs": 0.25, "Mutual Funds": 0.25, "Gold ETFs": 0.10, 
            "Equity Large Cap": 0.20, "Equity Mid Cap": 0.15, "Equity Small Cap": 0.05 if tenure >= 7 else 0
        })
    elif risk_profile == "high":
        allocation.update({
            "FDs": 0.10, "Mutual Funds": 0.15, "Gold ETFs": 0.05,
            "Equity Large Cap": 0.15, "Equity Mid Cap": 0.25, "Equity Small Cap": 0.20
        })
    if age <= 30 and risk_profile == "high":
        allocation["Equity Mid Cap"] += 0.05
        allocation["Equity Small Cap"] += 0.05
        allocation["FDs"] -= 0.05
    if investment_type == "Monthly":
        allocation["FDs"] -= 0.05
        allocation["Mutual Funds"] += 0.05
    
    return {k: v * amount for k, v in allocation.items()}
