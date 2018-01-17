from flask import Flask, render_template, request, redirect
import numpy as np
import pandas as pd
from bokeh.plotting import figure, output_file
import quandl

app = Flask(__name__)

app.vars={}

@app.route('/milestone',methods=['GET','POST'])
def index():
	if request.method == 'GET':
		return render_template('input.html')
	else:
		app.vars['ticker'] = request.form['input_ticker']
		app.vars['start'] = request.form['input_start']
		app.vars['end'] = request.form['input_end']

		data = quandl.get('WIKI/', returns = "pandas", ticker = app.vars['ticker'], start_date = app.vars['start'], end_date = app.vars['end'])
		
		output_file("lines.html",title='stockdata')
		p = figure(title="Stock Information", x_axis_label = "Date", x_axis_type = 'datetime', y_axis_label = "Value")
		p.line(data.index.values.tolist(),data['Open'].values.tolist(),legend = "line",line_width = 2,line_color = "blue")
		p.line(data.index.values.tolist(),data['Close'].values.tolist(),legend = "line",line_width = 2,line_color = "red")

if __name__ == '__main__':
  app.run(port=33507, debug = True)
