# Pingdom to Microsoft Teams - Alert Notifications

## Problem 
The Pingdom app on Microsoft Teams does not work, I contacted Pingdom and they confirmed the payload request that is sent to Microsoft Teams is not compatible.

If they have an actual app in the Microsoft Teams store, then why doesn't it work?
- Well the likely answer is that it needs updating, according to the reviews, the app suddenly stopped working. 

## Solution
Using AWS API Gateway and AWS Lambda, when the check is triggered in Pingdom, it will send the notification to the AWS api endpoint. 

- When a message is sent via HTTP it's identified as a payload. This is received in JSON format.  
- So the API receives the payload, we specify which data from the payload we're interested in.
- With the API Gateway set as a trigger to the AWS Lambda, this will have the python script which will send the payload to a Microsoft Teams channel incoming webhook url in a way that Microsoft accepts, a message card.  

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

## Costing?

Assuming that the Lambda function runs for a maximum of 50 invocations per day, and each invocation completes within 1 second,
the total monthly cost for AWS API Gateway and Lambda (EU Ireland region), can be estimated as follows:

### API Gateway
- Requests: 50 requests/day x 30 days = 1,500 requests/month
- Data transfer out: Assuming an average payload size of 1KB per request, the total data transfer out per month would be 1.5 MB.
- Cost = 1,500 requests * £0.0000004/request + 1.5 MB * £0.09/GB = £0.0006 + £0.0001 = £0.0007

### Lambda
- Execution: Assuming an average execution time of 200ms per request, the total compute time per month would be 50 requests * 200ms/request = 10 seconds.
- Memory: Assuming you use 128MB of memory for your Lambda function.
- Cost = 10 seconds * 128MB * £0.000000208/GB/second = £0.0000026

Therefore, the estimated monthly cost for the API Gateway and Lambda usage would be approximately £0.0007 + £0.0000026 = £0.0007026.

Also remember the 50 invocations is when a Pingdom check is activated, so this will be if the state changes, or if a test alert is sent. 

:fire: Please note that these are estimates and actual costs may vary depending on factors such as region the resources are provisioned in, traffic spikes and data transfer.

### AWS Caculator
You can estimate your AWS costs using the AWS Simple Monthly Calculator, which allows you to estimate the monthly costs of running your services based on your usage. 
You can access it here: https://calculator.aws/#/

### AWS Pricing
You can also view the AWS pricing page for a detailed breakdown of pricing for all AWS services. 
Here's the link: https://aws.amazon.com/pricing/

### Other Tools
- Request Bin and Postman is free
- I assume you already have an Pingdom and Microsoft Teams account. 

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

## AWS Lambda Files

In this repository you will find 4 files, these are what is required to run the lambda function. 

- 'domains.py': this is a list of domains that we want to use in our hostnames, this is optional
- 'regions.py': this is a list of AWS and azure regions to use in our hostnames, this is optional
- 'pingdom_hostnames.py': this is a list of hostnames that we want to check, these should be setup in Pingdom as checks, this is optional
- 'lambda_handler.py': this is the main part that will look at the HTTP POST request from the API Gateway and send the message to a Microsoft Teams channel. 

# Implementation

This is open-source and you may use my code for your implementation. 

Read my article here: :fire: to add

:fire: If you are using any documentation please credit my repo/article as source. 


Thank you!
