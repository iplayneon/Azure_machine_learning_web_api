import urllib.request
import json

sl, sw, pl, pw = map(float, input("Enter sepal length and width and also petal length and width, all separated by a comma: ").split(', '))

data = {
  "Inputs": {
    "input1": {
      "ColumnNames": [
        "sepal-length",
        "sepal-width",
        "petal-length",
        "petal-width"
      ],
      "Values": [
        [
          "1.2",
          "3.2",
          "2.1",
          "1.3"
        ]
      ]
    }
  },
  "GlobalParameters": {}
}

body = str.encode(json.dumps(data))

# Replace this with the URI and API Key for your web service
url = 'https://ussouthcentral.services.azureml.net/workspaces/1166b63e9429415ba0c7dc38efd94658/services/28525146540b4fa1a57691c4eef3e2f7/execute?api-version=2.0&details=true '
api_key = 'PXrjFua0CQPxDPT7jPdtY00GhHNFJ1JbHJp5nXPHt+mJVEPODMnZWEkM3BKNo841EzSRzFaQhTe8D+ZBQ1vzLw=='
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)

except urllib.error.HTTPError as error: 
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the request ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read())) 