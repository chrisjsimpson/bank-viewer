from flask import Flask, request, render_template, url_for, redirect
from hsbc_csv_parse import (get_records, calculate, search, 
                    total_income, total_payments)
from subprocess import run



def create_app(test_config=None):
  app = Flask(__name__)

  @app.route("/")
  def home():
    return render_template('layout.html')

  @app.route("/", methods=["POST"])
  def route_transactions_request():
    year = request.form['year']
    month = request.form['month']
    return redirect(url_for('transactions_by_year_month', year=year, month=month))

  @app.route("/transactions/<year>/<month>", methods=["GET"])
  def transactions_by_year_month(year, month):
    return render_template('layout.html', body=calculate(year=year, month=month))
  
  @app.route("/scrape/<code>", methods=["GET"])
  def scrape(code):
    code = int(code)
    cmd = "printf '{}\n' | sudo /usr/bin/docker exec -i hsbc-scrape python3 main.py".format(code)
    print("Running subprocess: {}".format(cmd))
    run(cmd, shell=True) # Run as subprocess NOTE may need to edit sudoers (visudo)
    return "Done"
    

  return app
