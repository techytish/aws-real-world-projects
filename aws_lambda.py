import boto3
import os
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

# Get the environment variables for AWS access
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
aws_region = os.environ.get('AWS_DEFAULT_REGION')

# This function uses the AWS Organisations API to list all accounts in your AWS organisation.
def list_accounts():
    client = boto3.client('organizations')
    response = client.list_accounts()
    accounts = response['Accounts']
    return accounts

# This function uses the AWS Lambda API to list all Lambda functions, 
# and then filters the list to include only those that have been invoked in the last 30 days.
def list_invoked_lambdas():
    # Create an empty list to store the names of invoked Lambda functions
    invoked_functions = []
    # Set the time range for filtering invoked Lambda functions (last 30 days)
    end_time = datetime.now()
    start_time = end_time - timedelta(days=30)
    # Loop through all available regions for Lambda functions
    for region in boto3.session.Session().get_available_regions('lambda'):
        # Create a client for Lambda in the current region
        client = boto3.client('lambda', region_name=region)
        # Call the list_functions API to get a list of all Lambda functions in the current region
        response = client.list_functions()
        functions = response['Functions']
        # Loop through each Lambda function in the current region
        for function in functions:
            name = function['FunctionName']
            last_invocation_time = function['LastInvocationTime']
            # Check if the Lambda function was invoked within the last 30 days
            if last_invocation_time is not None and last_invocation_time >= start_time and last_invocation_time <= end_time:
                # If the Lambda function was invoked within the last 30 days, add its name to the list of invoked functions
                invoked_functions.append(name)
    # Write list of invoked functions to JUnit XML file
    root = ET.Element("testsuite", name="invoked_lambdas")
    for func in invoked_functions:
        testcase = ET.SubElement(root, "testcase", name=func)
    tree = ET.ElementTree(root)
    tree.write("lambda_invoked_results.xml")
    # Return the list of invoked functions
    return invoked_functions

# This function uses the AWS Lambda API to list all Lambda functions, and then filters the list to include only those that 
# are using an old or deprecated runtime version.
def list_deprecated_lambdas():
    # Create an empty list to store the names of deprecated Lambda functions
    deprecated_functions = []
    # Loop through all available regions for Lambda functions
    for region in boto3.session.Session().get_available_regions('lambda'):
        # Create a client for Lambda in the current region
        client = boto3.client('lambda', region_name=region)
        # Call the list_functions API to get a list of all Lambda functions in the current region
        response = client.list_functions()
        functions = response['Functions']
        # Loop through each Lambda function in the current region
        for function in functions:
            name = function['FunctionName']
            runtime = function['Runtime']
            # Check if the Lambda function is using an old or deprecated runtime version
            if runtime.startswith('python2.') or runtime.startswith('nodejs') or runtime.startswith('java') or runtime.startswith('go'):
                # If the Lambda function is using an old or deprecated runtime version, add its name to the list of deprecated functions
                deprecated_functions.append(name)
    # Write list of deprecated functions to JUnit XML file
    root = ET.Element("testsuite", name="deprecated_lambdas")
    for func in deprecated_functions:
        testcase = ET.SubElement(root, "testcase", name=func)
    tree = ET.ElementTree(root)
    tree.write("lambda_deprecated_results.xml")
    # Return the list of deprecated functions
    return deprecated_functions
