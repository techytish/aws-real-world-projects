from regions import (
  aws_regions, 
  azure_regions,
)

# AWS
aws_api_domain = f"execute-api.{'.'.join(aws_regions)}.amazonaws.com" # restapi domain
  
# Azure
azure_regions = f"environment.{'.'.join(azure_regions)}.amazonaws.com"
