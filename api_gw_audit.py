#!/usr/bin/env python3
import boto3
# Define client
client = boto3.client('apigateway')
# main function for collecting current API gateways specifically restful type apis
def api_gw():
    print('API Gateway Audit')
    groups = client.get_rest_apis(limit=500)
    for api in groups['items']:
        api_name = api['name']
        print(api_name)
        if "tags" in api:
            api_tag = api['tags']
            print(api_tag)
        else:
            continue
api_gw()
print('end of apis')