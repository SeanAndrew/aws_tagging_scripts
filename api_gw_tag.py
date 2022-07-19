#!/usr/bin/env python3
import boto3
client = boto3.client('apigateway')
def api_gw_tag():
    print('API Gateway Tagging')
    api_list = client.get_rest_apis(limit=500)
    for api in api_list['items']:
        api_name = api['name']
        api_id = api['id']
        api_arn = 'arn:aws:apigateway:us-east-1::/restapis/'f'{api_id}'
        ar = 'ar By TypeID'
        ar2 = 'ar2'
        push = 'push'
        sms = 'sms'
        sms2 = 'SMS'
        if ar in api_name:
            ar_tag = client.tag_resource(
                resourceArn=f'{api_arn}',
                tags={
                    'product': 'ar',
                    'CostCenter': 'email-rnd'
                }
            )
            print(api_name)
        elif ar2 in api_name:
            ar2_tag = client.tag_resource(
                resourceArn=f'{api_arn}',
                tags={
                    'product': 'ar',
                    'CostCenter': 'email-rnd'
                }
            )
            print(api_name)
        elif push in api_name:
            push_tag = client.tag_resource(
                resourceArn=f'{api_arn}',
                tags={
                    'product': 'push',
                    'CostCenter': 'push'
                }
            )
            print(api_name)
        elif sms in api_name:
            sms_tag = client.tag_resource(
                resourceArn=f'{api_arn}',
                tags={
                    'product': 'sms',
                    'CostCenter': 'sms'
                }
            )
            print(api_name)
        elif sms2 in api_name:
            sms2_tag = client.tag_resource(
                resourceArn=f'{api_arn}',
                tags={
                    'product': 'sms',
                    'CostCenter': 'sms'
                }
            )
            print(api_name)
        else:
            sending_tag = client.tag_resource(
                resourceArn=f'{api_arn}',
                tags={
                    'CostCenter': 'sending'
                }
            )
            print(api_name)
api_gw_tag()
print('end of tagging')
