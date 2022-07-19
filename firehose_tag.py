#!/usr/bin/env python3
# import the boto3 module
import boto3

# define client
client = boto3.client('firehose')

# set variable to list_delivery_streams
delivery_streams = client.list_delivery_streams(
    Limit=100
)

for tag in delivery_streams['DeliveryStreamNames']:
    delivery_tags = client.list_tags_for_delivery_stream(
        DeliveryStreamName=f'{tag}',
    )
    ar = 'ar'
    push = 'pushing'
    sms = 'sms'
    if ar in tag:
        ar_tagging = client.tag_delivery_stream(
            DeliveryStreamName=f'{tag}',
            Tags=[
                {
                    'Key': 'CostCenter',
                    'Value': 'email-rnd',
                    'Key': 'product',
                    'Value': 'ars'
                },
            ]
        )
    elif push in tag:
        push_tagging = client.tag_delivery_stream(
            DeliveryStreamName=f'{tag}',
            Tags=[
                {
                    'Key': 'CostCenter',
                    'Value': 'push',
                    'Key': 'product',
                    'Value': 'push'
                },
            ]
        )
    elif sms in tag:
        sms_tagging = client.tag_delivery_stream(
            DeliveryStreamName=f'{tag}',
            Tags=[
                {
                    'Key': 'CostCenter',
                    'Value': 'sms',
                    'Key': 'product',
                    'Value': 'sms'
                },
            ]
        )
    else:
        sending_tagging = client.tag_delivery_stream(
            DeliveryStreamName=f'{tag}',
            Tags=[
                {
                    'Key': 'CostCenter',
                    'Value': 'sending',

                },
            ]
        )
