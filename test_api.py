import json
import requests
from json2table import convert
import logging

logger = logging.basicConfig(
    filename='app.log',
    filemode='w',
    level='DEBUG',
    format='%(asctime)s - %(levelname)s %(message)s'
)

api_key = '579b464db66ec23bdd000001e40dd21c2746437d667c36225001b9cd'
base_urls = [
    'https://api.data.gov.in/resource/794c42c2-8120-4fdc-8773-ec366dd0ac5a',
    'https://api.data.gov.in/resource/d1ac29db-549d-44b2-9bea-28d6e449ff85',
]
params = {
    'api-key': api_key,
    'format': 'json',
}
for url in base_urls:
    api_url = url
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        logger.info("access of %s is successful" % api_url)
    else:
        logger.info("access of %s is failed" % api_url)
#
# api_url = base_url
# response = requests.get(api_url, params=params)
#
# if response.status_code == 200:
#     print(response.status_code)
#
# json_data = json.loads(response.content)
#
# json_object = json_data['records']
# build_direction = "LEFT_TO_RIGHT"
# table_attributes = {
# 'style': 'border: 1px solid black',
# }
#
# company = input("Enter company name \n")
# result_set = []
# for record in json_object:
#     if company in record['company_name']:
#         result_set.append(record)
#
# print(len(result_set))
# # print("something went wrong")
#
# with open('json_data.html', 'w+') as f:
#     for record in result_set:
#         html = convert(
#             record,
#             build_direction=build_direction,
#             table_attributes=table_attributes
#         )
#         f.write(html)
