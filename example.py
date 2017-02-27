from pytrends.request import TrendReq

def mytrends():
	google_username = <Your GMAIL address>
	google_password = <Your PASSWORD>

	# connect to Google
	pytrend = TrendReq(google_username, google_password, custom_useragent='My Pytrends Script')

	trend_payload = {'q': 'the lego batman movie', 'date':'01/2017 2m',  'geo': 'US'}
	trend = pytrend.trend(trend_payload)
	return pytrend.trend(trend_payload, return_type='dataframe')


data= mytrends()
if data is None:
	print "error: no data found"
else:
	print data

