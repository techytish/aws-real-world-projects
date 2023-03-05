# Pingdom to Microsoft Teams - Alert Notifications

## Problem 
The Pingdom app on Microsoft Teams does not work, I contacted Pingdom and they confirmed the payload request that is sent to Microsoft Teams is not compatible.

If they have an actual app in the Microsoft Teams store, then why doesn't it work?

Well the likely answer is that it needs updating, according to the reviews the app stopped working. 

## Technologies
- AWS account
  - permissions to create resources in AWS
  - permissions to access AWS CloudWatch
- Pingdom account with checks configured, and permissions to add integration webhook urls
- Microsoft Teams account with permissions to add Incomming Webhook connector and create teams/channels
- Knowledge of Python as the AWS Lambda is written in python
- Some understanding of REST APIs as that's where the pingdom alert will go to
- Request Bin account - to see how a payload is received
- Postman Account - test HTTP requests

## Solution
When the check is triggered in Pingdom, it will send the notification to the AWS api endpoint. 

When a message is sent via HTTP it's identified as a payload. This is received in JSON format.  

So the api receives the payload, we specify which data from the payload we're interested in. 

Remember there is a lot of information on a payload, but not all of the fields are relevant
With the api gateway set as a trigger for the AWS Lambda, 
this will have the python script send the payload to Microsoft Teams channel incoming webhook url in a way that Microsoft accepts, a message card.  

## Architecture Diagram

This architecture diagram provides a high level overview of how the notification from the pingdom check goes to a Microsoft Teams channel. 

:fire: to do

## Pingdom Payload

Example of Pingdom payload 

:fire: to add

Use requestbin, to identify exactly how the payload looks. 

## Microsoft Teams Message Card

This screenshot shows how the alert will appear in Microsoft Teams 

:fire: to add
