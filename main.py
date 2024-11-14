# main.py
from diversify import diversify_funds
from Equity import get_top_stocks
from Mf import select_top_mf_direct
from Mf import select_top_mf_regular
from FD_ETf import select_top_fds
from FD_ETf import select_top_gold_etf
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/investment', methods=['POST'])
def process_investment():
    data = request.json
    age = data['age']
    tenure = data['tenure']
    investment_type = data['investment_type']
    amount = data['amount']
    risk_profile = data['risk_profile']
    
    # Step 1: Diversify Funds
    allocation = diversify_funds(age, tenure, investment_type, amount, risk_profile)
    
    # Step 2: Get Top Performers
    top_equities = get_top_stocks(risk_profile)
    Direct_mutual_funds = select_top_mf_direct(tenure, risk_profile)
    Regular_mutual_funds = select_top_mf_regular(tenure, risk_profile)
    top_fds = select_top_fds(age, risk_profile)
    top_gold_etfs = select_top_gold_etf(age, risk_profile)
    
    # Step 3: Return Data in JSON format
    result = {
        "allocation": allocation,
        "top_equities": top_equities.to_dict(orient='records'),
        "Direct_mutual_funds": Direct_mutual_funds.to_dict(orient='records'),
        "Regular_mutual_funds": Regular_mutual_funds.to_dict(orient='records'),
        "Top_FDs": top_fds.to_dict(orient='records'),
        "Top_gold_etfs ": top_gold_etfs.to_dict(orient='records')
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
