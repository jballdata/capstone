from flask import Flask, render_template, request, redirect
import numpy as np
import pandas as pd
import bokeh as bk
import seaborn as sb

app = Flask(__name__)

app.vars={}

# Sample bins

#W	M	18 to 24 years
#		25 to 44 years
#		45 to 64 years
#		65 to 74 years
#		75 years and over
#	F	18 to 24 years
#		25 to 44 years
#		45 to 64 years
#		65 to 74 years
#		75 years and over
#N-W M	18 to 24 years
#		25 to 44 years
#		45 to 64 years
#		65 to 74 years
#		75 years and over
#	F	18 to 24 years
#		25 to 44 years
#		45 to 64 years
#		65 to 74 years
#		75 years and over

#bins = [7985.153739, 30942.13135, 40431.28589, 17310.02893, 11556.58055, 9833.670836, 36822.38836, 45621.44146, 18737.07186, 11450.19904, 2922.54554, 10413.43604, 15508.53926, 6836.858037, 4426.604508, 3886.007479, 14208.84671, 18116.89326, 7338.779096, 4621.278151]



#bk.layout([[plot_pred, plot_party], [plot_demog]], responsive = TRUE)

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
		
#@app.route('/Alabama')
#def alabama():
	#return render_template('index.html')
	
if __name__ == '__main__':
  app.run(port=33507, debug = True)
