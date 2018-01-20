from flask import Flask, render_template, request, redirect
import numpy as np
import pandas as pd

app = Flask(__name__)

app.vars={}
#test

@app.route('/')
def index():
	return render_template('index_two.html')
# 	else:
# 		app.vars['ticker'] = request.form['input_ticker']
# 		app.vars['start'] = request.form['input_start']
# 		app.vars['end'] = request.form['input_end']

# 		data = quandl.get('WIKI/', returns = "pandas", ticker = app.vars['ticker'], start_date = app.vars['start'], end_date = app.vars['end'])

# 		output_file("lines.html",title='stockdata')
# 		p = figure(title="Stock Information", x_axis_label = "Date", x_axis_type = 'datetime', y_axis_label = "Value")
# 		p.line(data.index.values.tolist(),data['Open'].values.tolist(),legend = "line",line_width = 2,line_color = "blue")
# 		p.line(data.index.values.tolist(),data['Close'].values.tolist(),legend = "line",line_width = 2,line_color = "red")
		
@app.route('/Alabama')
def alabama():
	return render_template('index.html')
		
if __name__ == '__main__':
  app.run(port=33507, debug = True)
