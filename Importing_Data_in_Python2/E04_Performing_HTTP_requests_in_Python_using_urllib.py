file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/Importing_Data_in_Python2/'
file = file+'winequality-red.csv'

# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# This packages the request: request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Print the datatype of response
print(type(response))

# Be polite and close the response!
response.close()
