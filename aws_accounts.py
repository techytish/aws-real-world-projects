import boto3
from datetime import datetime, timedelta

# this function uses the AWS Organisations API to list all accounts in your AWS organisation.
def list_accounts():
    client = boto3.client('organizations')
    response = client.list_accounts()
    accounts = response['Accounts']
    return accounts

# this function uses the AWS Lambda API to list all Lambda functions, 
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
        if last_invocation_time is not None and last_invocation_time >= start_time and last_invocation_time <= end_time:
            invoked_functions.append(name)
    return invoked_functions

  # this function uses the AWS Lambda API to list all Lambda functions, and then filters the list to include only those that 
  # are using an old or deprecated runtime version.
  def list_deprecated_lambdas():
    client = boto3.client('lambda')
    response = client.list_functions()
    functions = response['Functions']
    deprecated_functions = []
    for function in functions:
        name = function['FunctionName']
        runtime = function['Runtime']
        if runtime.startswith('python2.') or runtime.startswith('nodejs') or runtime.startswith('java') or runtime.startswith('go'):
            deprecated_functions.append(name)
    return deprecated_functions
