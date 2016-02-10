#!/usr/bin/python
import urllib2
import base64
import json

username="CHARTMOGUL_API_TOKEN"
password="CHARTMOGUL_SECRET_KEY"

base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')

headers = {"Authorization" : "Basic %s" % base64string}

request = urllib2.Request("https://api.chartmogul.com/v1/metrics/all?start-date=2016-01-01&interval=month&end-date=2016-01-31", headers=headers)

contents = urllib2.urlopen(request).read()

jsonResponse=contents

jsonData = json.loads(jsonResponse)

for item in jsonData["entries"]:
    mrr = item.get("mrr")
    arpa = item.get("arpa")
    ltv = item.get("arpa")
    customers = item.get("customers")
    arr = item.get("arr")
    asp = item.get("asp")

def monetize( data ):
	if data:
		a = str(data)
		b = a.replace(' ', '')[:-3].upper()
		c = int(b)
		d = '${:,.2f}'.format(c).replace(' ', '')[:-3].upper()
		return d
	else:
		return data


print "ChartMogul"
print "---"
print "MRR: ", monetize(mrr)
print "LTV: ", monetize(ltv)
print "Customers: ", customers
print "ARR: ", monetize(arr)
print "ASP: ", monetize(asp)