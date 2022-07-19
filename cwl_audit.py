#!/usr/bin/env python3
# import boto3 python3 module
import boto3

# define client
client = boto3.client('logs')

# define cwl function
def cwl():
    logs = True
# set boolean to pull first 50 logs and generate first 'nextToken'
# to finish the rest of the script
    first_group = True
    while logs:
# if statement for first 50 log pull
        if first_group:
            print('CWL Log collection')
            groups = client.describe_log_groups()
# else statement reused throughout the below for loop with 'nextToken' variable
# pulling the latest token for each page
        else:
            groups = client.describe_log_groups(nextToken=f'{token}')
        for names in groups['logGroups']:
            names_formatted = names['logGroupName']
# variable for pulling each individual log group name
            name_tag = client.list_tags_log_group(
                logGroupName=f'{names_formatted}'
            )
            log = names_formatted
            tag = name_tag['tags']
            if 'retentionInDays' in names:
                retention_policy = names['retentionInDays']
                print(log, retention_policy, tag)
            else:
                print(log, tag)
# if statement determining if there is a 'nextToken' to be found
# this ends the first if statement above
        if 'nextToken' in groups:
            first_group = False
            token = groups['nextToken']
# when there is no longer a 'nextToken' this ends the while loop
        else:
            logs = False
            print('end of logs')
cwl()