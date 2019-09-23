import requests
import json

# URL
url = 'http://localhost:5000/api'

# Change the value of experience that you want to test
r=requests.post(url,json={"LIMIT_BAL":310000,
                          "AGE":40,
                          "BILL_AMT1":25000,
                          "PAY_AMT1":23000,
                          "PAY_1_2":0,
                          "BILL_AMT2":55000,
                          "PAY_AMT2":45000,
                          "PAY_2_2":0,
                          "BILL_AMT3":12345,
                          "PAY_AMT3":34000,
                          "PAY_3_2":1,
                          "EDUCATION_2":1,
                          "EDUCATION_3":0
                         })
print(r.json())