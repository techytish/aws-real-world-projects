# AWS Lambda Deprecation Checker 🚀

## Table of Contents

<!-- TOC start -->
  * [Overview](#overview)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Contributing](#contributing)
<!-- TOC end -->

## Overview

This project automates checking for deprecated runtime versions in AWS Lambda functions using Azure DevOps pipelines. 🔍

📌 This project uses Python scripts and AWS CLI to search through AWS accounts and list all Lambda functions, as well as checking for deprecated runtime versions.

## Prerequisites
- An AWS account with Lambda functions
- An Azure DevOps account with pipelines
- Git installed on your local machine
- Python 3.x installed on your local machine

## Installation
1. Clone the repository:

```bash
git clone https://github.com/TechyTish/aws-real-world-projects.git
```

2. Navigate to the `aws-lambda-deprecation-checker` directory:

```bash
cd aws-real-world-projects/aws-lambda-deprecation-checker
```

3. Create a virtual environment:

```bash
python -m venv env
source env/bin/activate  # for Linux/Mac
env\Scripts\activate  # for Windows
```

4. Install the required packages:

```bash
pip install -r requirements.txt
```

5. Set up the AWS CLI on your local machine:

- Follow the instructions in the AWS documentation to install and configure the AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
- Make sure that you have permissions to access the Lambda functions in your AWS account.

6. Create an AWS IAM user with programmatic access and the necessary permissions:

- In the AWS Management Console, go to "Services" > "IAM".
- Click "Users" > "Add User".
- Give the user a name and select "Programmatic access" as the access type.
- Attach the "AWSLambdaReadOnlyAccess" and "CloudWatchLogsReadOnlyAccess" policies to the user.
- Click "Create User" and note down the access key ID and secret access key.

7. Set up the Azure DevOps pipeline:

- In your Azure DevOps project, go to "Pipelines" > "Pipelines".
- Click "New Pipeline" and select the repository you cloned earlier.
- Choose "Existing Azure Pipelines YAML file" and select the `aws_lambda.yml` file in the root of your repository.
- Click "Continue" and then "Save and run".

8. Connect your AWS account to the pipeline:

- In your Azure DevOps project, go to "Pipelines" > "Library".
- Click on "New Variable Group" and give it a name, like "AWS Credentials".
- In the "Variables" tab, add the following variables:
  - `AWS_ACCESS_KEY_ID`: your AWS access key ID
  - `AWS_SECRET_ACCESS_KEY`: your AWS secret access key
  - `AWS_DEFAULT_REGION`: the default AWS region you want to use, like "us-east-1"
- Click "Save" to create the variable group.
- In your pipeline YAML file, add a variables section at the top, like this:
```yaml
variables:
  - group: AWS Credentials
```

9. Run the pipeline:
- Click "Save and run" to start the pipeline.
- The pipeline will run the Python scripts to get information about the Lambda functions in your AWS account.
- The results will be published as test results and pipeline artifacts.
- You can view the results in the "Tests" and "Artifacts" tabs in the pipeline summary.

# Contributing

Check out the article for implementation here :arrow_right:: https://medium.com/@techytish/automating-aws-lambda-deprecation-checks-with-azure-devops-f98dfcb1c9b6

If you have any suggestions or would like to contribute to this project, please feel free to open an issue or pull request.

👨‍💻 Let's work together to improve AWS Lambda function optimisation and automation!
