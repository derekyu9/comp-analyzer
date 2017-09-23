import requests
import xml.etree.ElementTree as ET

getSearchResultsURL = 'http://www.zillow.com/webservice/GetSearchResults.htm'
getDeepCompsURL = 'http://www.zillow.com/webservice/GetDeepComps.htm'
zwsid = "X1-ZWz1928oa47v2j_305s0"

getSearchResultsParameters = {"zws-id": zwsid, "address": "2165 Somerset Ave", "citystatezip": "94578"}
searchResultsResponse = requests.get(getSearchResultsURL, params=getSearchResultsParameters)

with open('data.xml', 'w') as f:
    f.write(searchResultsResponse.text)

root = ET.fromstring(searchResultsResponse.text)
print(root.find('response').find('results').find('result').find('zpid').text);
zpid = root.find('response').find('results').find('result').find('zpid').text

getDeepCompsParameters = {"zws-id": zwsid, "zpid": zpid, "count": 10, "rentzestimate": True}
deepCompsResponse = requests.get(getDeepCompsURL, params=getDeepCompsParameters)

with open('comps.xml', 'w') as f:
    f.write(deepCompsResponse.text)

compString = ET.fromstring(deepCompsResponse.text)
for comparable in compString.iter('comp'):
	address = comparable.find('address').find('street').text
	sellPrice = comparable.find('lastSoldPrice').text
	print "Address: ", address, "Selling Price: ", sellPrice
