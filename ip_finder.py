import requests

def my_public_ip():
	"""
	Get the public address details.
	"""
	map_values = {
		'YourFuckingCountryCode': 'Countrycode',
		'YourFuckingHostname': 'hostname',
		'YourFuckingIPAddress': 'ip address',
		'YourFuckingISP': 'isp',
		'YourFuckingLocation': 'location'}
	
	url = "https://wtfismyip.com/json"
	resp = requests.get(url)
	data = resp.json()

	final_result = {map_values[item]:str(data[item]) for item in data if item in map_values}
	return final_result

if __name__ == '__main__':
	print my_public_ip()
