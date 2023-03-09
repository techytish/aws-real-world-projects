import os
import json
import urllib.request
from pingdom_hostnames import (
  list_of_hosts1, 
  list_of_hosts2, 
  list_of_hosts3, 
  list_of_hosts4, 
  list_of_hosts5,
  list_of_hosts6,
)

def lambda_handler(event, context):
  # Parse the Pingdom webhook request data
  data = event
  
  # Print the data object for debugging purposes
  print(data) #raw
  print("Received data: " + json.dumps(data, indent=2)) #pretty
  
  # Obtain the objects we want from Pingdom payload and any missing replace with "unknown"
  # This is because pingdom periodically update their payload and object names change
  check_name = data.get('check_name', 'unknown')
  check_id = data.get('check_id', 'unknown')
  check_type = data.get('check_type', 'unknown')
  long_description = data.get('long_description', 'unknown')
  hostname = data['check_params'].get('hostname', 'unknown')
  port = data['check_params'].get('port', 'unknown')
  state_changed_utc_time = data.get('state_changed_utc_time', 'unknown')
  current_state = data.get('current_state', 'unknown')
  previous_state = data.get('previous_state', 'unknown')
  
  # Check if the check port is 80 or 443 and update the hostname accordingly
  if data['check_params']['port'] == 80:
      hostname = data['check_params']['hostname'] + ':80'
  elif data['check_params']['port'] == 443:
      hostname = data['check_params']['hostname'] + ':443'

  # Construct the link to the Pingdom Alert in web application
  pingdom_alert_link = f"https://my.pingdom.com/app/reports/responsetime#check={check_id}"
  
  # Add url for where the documentation is
  alert_document = "https://example.com" #optional
  
  # Set colour of the message to green if current state is 'UP'
  colour = 'FF0000' # Red by default
  if current_state == 'UP':
      colour = '00FF00' # Green
      print(colour)
      
  # Construct the Microsoft Teams message payload
  teams_message = {
      "@type": "MessageCard",
      "@context": "http://schema.org/extensions",
      "themecolor": colour,
      "summary": f"{check_name} - {current_state}".replace('"', ''),
      "sections": [
          {
              "activityTitle": f"{current_state} - {check_name}".replace('"', ''),
              "activitySubtitle": f"State changed from: {previous_state} to {current_state}".replace('"', ''),
              "facts": [
                  {
                      "name": "Check ID:",
                      "value": check_id
                  },
                  {
                      "name": "Check:",
                      "value": f"{check_type}, {hostname}, {port}".replace('"', '')
                  },
                  {
                      "name": "Reason:",
                      "value": long_description.replace('"', '')
                  },
                  {
                      "name": "Timestamp UTC:",
                      "value": state_changed_utc_time.replace('"', '')
                  },
                  {
                      "name": "Alert Reference:",
                      "value": alert_document
                  }
              ],
              "markdown": True,
              "potentialAction": [
                  {
                      "@type": "OpenUri",
                      "name": "View details",
                      "targets": [
                          {
                              "os": "default",
                              "uri": f"{pingdom_alert_link}"
                          }
                      ]
                  }
              ]
          }
      ]
  }
  
  # Check if hostname in Pingdom alert exists in pingdom_hostnames.py
  # If it does, use the relevant webhook url to notify the correct Microsoft Teams channel
  # If it doesn't exist, we will get an error in the lambda logs
  if hostname in list_of_hosts1:
    teams_webhook_url = os.environ['TEAMS_WEBHOOK_URL_1']
  elif hostname in list_of_hosts2:
    teams_webhook_url = os.environ['TEAMS_WEBHOOK_URL_2']
  elif hostname in list_of_hosts3:
    teams_webhook_url = os.environ['TEAMS_WEBHOOK_URL_3']
  elif hostname in list_of_hosts4:
    teams_webhook_url = os.environ['TEAMS_WEBHOOK_URL_4']
  elif hostname in list_of_hosts5:
    teams_webhook_url = os.environ['TEAMS_WEBHOOK_URL_5']
  elif hostname in list_of_hosts6:
    teams_webhook_url = os.environ['TEAMS_WEBHOOK_URL_6']
  else:
    return {
      'statusCode': 200,
      'body': 'No matching webhook found for hostname'
    }
  
  headers = {
    "Content-Type": "application/json"
  }
  req = urllib.request.Request(
    teams_webhook_url, 
    data=json.dumps(teams_message).encode('utf-8'),
    headers=headers
  )
  response = urllib.request.urlopen(req)
  
  return {"statusCode": response.status}
