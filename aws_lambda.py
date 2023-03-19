import boto3
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

# This function uses the AWS Organisations API to list all accounts in your AWS organisation.
def list_accounts():
    client = boto3.client('organizations')
    response = client.list_accounts()
    accounts = response['Accounts']
    return accounts

# This function uses the AWS Lambda API to list all Lambda functions, 
# and then filters the list to include only those that have been invoked in the last 30 days.
def list_invoked_lambdas():
    client = boto3.client('lambda')
    end_time = datetime.now()
    start_time = end_time - timedelta(days=30)
    response = client.list_functions()
    functions = response['Functions']
    invoked_functions = []
    for function in functions:
        name = function['FunctionName']
        last_invocation_time = function['LastInvocationTime']
        # Check if the function was invoked within the last 30 days
        if last_invocation_time is not None and last_invocation_time >= start_time and last_invocation_time <= end_time:
            invoked_functions.append(name)
    # Write list of invoked functions to junit xml file
    root = ET.Element("testsuite", name="invoked_lambdas")
    for func in invoked_functions:
        testcase = ET.SubElement(root, "testcase", name=func)
    tree = ET.ElementTree(root)
    tree.write("lambda_invoked_results.xml")
    return invoked_functions

# This function uses the AWS Lambda API to list all Lambda functions, and then filters the list to include only those that 
# are using an old or deprecated runtime version.
def list_deprecated_lambdas():
    client = boto3.client('lambda')
    response = client.list_functions()
    functions = response['Functions']
    deprecated_functions = []
    for function in functions:
        name = function['FunctionName']
        runtime = function['Runtime']
        # Check if the function is using an old or deprecated runtime version
        if runtime.startswith('python2.') or runtime.startswith('nodejs') or runtime.startswith('java') or runtime.startswith('go'):
            deprecated_functions.append(name)
    # Write list of deprecated functions to junit xml file
    root = ET.Element("testsuite", name="deprecated_lambdas")
    for func in deprecated_functions:
        testcase = ET.SubElement(root, "testcase", name=func)
    tree = ET.ElementTree(root)
    tree.write("lambda_deprecated_results.xml")
    return deprecated_functions
