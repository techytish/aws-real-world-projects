# Microsoft Teams Notifications for CloudWatch Alarms

## Table of Contents

<!-- TOC start -->
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Technologies & Pre-Requisites](#technologies--pre-requisites)
- [Setup Instructions](#setup-instructions)
- [Implementation](#implementation)
- [Conclusion](#conclusion)
<!-- TOC end -->

## Overview

This project sets up an AWS CloudWatch alarm to monitor an EC2 instance's CPU usage and sends a notification to a Microsoft Teams channel when the CPU utilization exceeds a certain threshold. The notifications are sent via an AWS Lambda function written in Python 3.9 and using the AWS SNS service.

The project is implemented using Terraform, an infrastructure as code (IaC) tool, to provision all the necessary AWS resources, including the EC2 instance, CloudWatch alarm, SNS topic, and Lambda function. The project also includes instructions on how to create a webhook in Microsoft Teams to receive the notifications.

## Project Structure

The project's file structure is as follows:

```python
.
├── README.md
├── lambda_function.py
├── lambda_test.json
├── main.tf
├── outputs.tf
└── variables.tf

```

- `README.md`: This file, providing an overview of the project and its components.
- `lambda_function.py`: The Python code for the Lambda function that sends notifications to Microsoft Teams.
- `lambda_test.json`: The JSON code for testing the lambda in the AWS console.
- `main.tf`: The main Terraform file that declares all the resources and their configurations.
- `outputs.tf`: The Terraform file that declares the outputs of the project, such as the SNS topic ARN.
- `variables.tf`: The Terraform file that declares the input variables used by the project, such as the AWS region and instance type.

## Technologies & Pre-Requisites

<img width="672" alt="image" src="https://user-images.githubusercontent.com/27959256/224549300-c0501a9d-b923-4cf9-a10a-dc29cc807995.png">

Before getting started with this project, you will need to have the following:

- An AWS account with appropriate permissions to create the necessary resources
- Terraform installed on your local machine
- Python 3.9 or later installed on your local machine
- Basic knowledge of Python and AWS services
- Microsoft Teams account with permissions to create a team or channel for the incoming webhook.

Make sure to set up your AWS credentials with appropriate permissions to create the required resources. Additionally, make sure to have a basic understanding of Python and AWS services such as Lambda, SNS, and CloudWatch alarms.

:exclamation: Note: The AWS CLI and Terraform should be installed and configured according to their respective documentation.

## Setup Instructions

To set up the project, follow these steps:

1. Clone this repository to your local machine.
2. Install Terraform on your local machine if you haven't already.
3. Configure your AWS credentials on your local machine if you haven't already.
4. Create a Microsoft Teams channel and a webhook to receive the notifications.
5. Set the input variables in variables.tf to your desired values.
6. Run terraform init to initialize the Terraform project.
7. Run terraform apply to create the AWS resources.
8. Copy the SNS topic ARN from the Terraform output and use it to create a CloudWatch alarm.
9. Verify that the alarm triggers by generating high CPU usage on the EC2 instance.
10. Check the Microsoft Teams channel for the notifications.

## Implementation

This is open-source and you may use my code for your implementation.

- Read the article here ➡️ https://medium.com/@techytish/creating-an-alert-notification-in-microsoft-teams-for-aws-cloudwatch-alarms-d21ffd28e90e

🔥 If you are using any documentation please credit my repo/article as source.

Here is an example of the Microsoft Teams notification:

<img width="859" alt="image" src="https://user-images.githubusercontent.com/27959256/224553058-18b126e4-c2a0-41ac-8cf4-8f0d79dc1e90.png">

## Conclusion

This project demonstrates how to set up a CloudWatch alarm to monitor an EC2 instance's CPU utilization and send notifications to a Microsoft Teams channel via an AWS Lambda function and SNS topic. By using Terraform to provision the resources, the project provides a scalable and repeatable way to set up the notification system.

You can use this repository and setup any type of AWS CLoudWatch alarm.
