from flask import Flask, jsonify, request
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Load sales data
sales_data = pd.read_csv('data/sales_data.csv', parse_dates=['Date'], index_col='Date')

# Verify the columns and ensure they match
print(sales_data.columns)

def forecast_sales(data, steps=30):
    model = ARIMA(data, order=(5, 1, 0))  # Customize parameters as needed
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=steps)
    return forecast

@app.route('/forecast', methods=['GET'])
def get_forecast():
    steps = int(request.args.get('steps', 30))  # Number of days to forecast
    forecast_data = forecast_sales(sales_data['Total Amount'], steps=steps)  # Forecasting Total Amount
    return jsonify({'forecast': forecast_data.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
