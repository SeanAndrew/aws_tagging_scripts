#!/usr/bin/env python3
# import the boto3 module
import boto3

# define client
client = boto3.client('firehose')

# set variable to list_delivery_streams
delivery_streams = client.list_delivery_streams(
    Limit=100
)

# for loop to pull DeliveryStreamNames into a variable
# set a variable to list_tags_for_delivery_stream

for tag in delivery_streams['DeliveryStreamNames']:
    delivery_tags = client.list_tags_for_delivery_stream(
        DeliveryStreamName=f'{tag}',
        Limit=15
    )
# if loop to determine delivery_streams without any tags
    if delivery_tags['Tags'] == []:
        print(tag)
    else:
# for loop to determine Delivery streams with tags
        for tag_formated in delivery_tags['Tags']:
            key = tag_formated['Key']
            value = tag_formated['Value']
# those tags with key value 'product'
            if key == 'product':
                print(tag, key, value)
            elif key == 'CostCenter':
                print(tag, key, value)
            else:
                pass