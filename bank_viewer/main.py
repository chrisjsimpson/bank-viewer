from flask import Flask
from hsbc_csv_parse import (get_records, calculate, search, 
                    total_income, total_payments) 



def create_app(test_config=None):
  app = Flask(__name__)

  @app.route("/transactions/<year>/<month>", methods=["GET"])
  def transactions_by_year_month(year, month):
    
    return str(calculate(year=year, month=month))

  return app
