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
                log_retention = names['retentionInDays']
            else:
                log_retention = None
            ar = 'ar'
            push = 'pushing'
            sms = 'sms'
            ccpa = ['CCPA', 'PrivacyRightsRequest', 'DoNotSell']
# if statement returning logs taged with 'product'
            if ar in log:
                ar_tagging = client.tag_log_group(
                    logGroupName=f'{log}',
                    tags={
                        'product': 'ars',
                        'CostCenter': 'email-rnd'
                    }
                )
                ar_retention = client.put_retention_policy(
                    logGroupName=f'{log}',
                    retentionInDays=30
                )
                print(log, log_retention, tag)
            elif push in log:
                push_tagging = client.tag_log_group(
                    logGroupName=f'{log}',
                    tags={
                        'product': 'push',
                        'CostCenter': 'push'
                    }
                )
                push_retention = client.put_retention_policy(
                    logGroupName=f'{log}',
                    retentionInDays=90
                )
                print(log, log_retention, tag)
            elif sms in log:
                sms_tagging = client.tag_log_group(
                    logGroupName=f'{log}',
                    tags={
                        'product': 'sms',
                        'CostCenter': 'sms'
                    }
                )
                sms_retention = client.put_retention_policy(
                    logGroupName=f'{log}',
                    retentionInDays=90
                )
                print(log, log_retention, tag)
            else:
                sending_tagging = client.tag_log_group(
                    logGroupName=f'{log}',
                    tags={
                        'CostCenter': 'sending'
                    }
                )
                for items in ccpa:
                    if items in log:
                        retention_policy = False
                        break
                    else:
                        retention_policy = True
                if retention_policy:
                    sending_retention = client.put_retention_policy(
                        logGroupName=f'{log}',
                        retentionInDays=90
                    )
                    print(log, log_retention, tag)
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
