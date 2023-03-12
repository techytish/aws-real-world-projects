import json   # Importing json library for parsing JSON data
import requests   # Importing requests library for sending HTTP requests
import os   # Importing os library for accessing environment variables

def lambda_handler(event, context):
    # Accessing the message from the SNS event passed as input to the Lambda function
    message = event['Records'][0]['Sns']['Message']
    
    # Parsing the JSON message to extract various details about the CloudWatch alarm triggered
    message = event['Records'][0]['Sns']['Message']
    alarm_name = json.loads(message)['AlarmName']
    alarm_desc = json.loads(message)['AlarmDescription']
    new_state = json.loads(message)['NewStateValue']
    alarm_time = json.loads(message)['StateChangeTime']
    instance_id = json.loads(message)['Trigger']['Dimensions'][0]['value']
    region = json.loads(message)['Region']
    account_id = context.invoked_function_arn.split(':')[4]
    
    # Create url link to view alarm
    alarm_url = f"https://console.aws.amazon.com/cloudwatch/home?region={region}#s=Alarms&alarm={alarm_name}"
    
    # Setting the theme color for the Teams message based on the new state of the alarm
     if new_state == "ALARM":
        colour = "FF0000"
    elif new_state == "OK":
        colour = "00FF00"
    else:
        colour = "0000FF"
    
    # Constructing the Teams message payload for an alarm
    message_card = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": color,
        "title": f"{alarm_name} {new_state} on {instance_id}",
        "text": f"Alarm description: {alarm_desc}\nCurrent state: {new_state}\nTriggered time: {alarm_time}",
        "potentialAction": [
            {
                "@type": "OpenUri",
                "name": "View Alarm",
                "targets": [
                    {
                        "os": "default",
                        "uri": alarm_url
                    }
                ]
            }
        ]
    }
    
    # Sending the Teams message to the specified webhook URL
    webhook_url = os.environ['TEAMS_WEBHOOK_URL']
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.post(webhook_url, json=message_card, headers=headers)
    print(response.text)
