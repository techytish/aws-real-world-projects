from regions import (
  aws_regions, 
  azure_regions,
)

# AWS
domain1 = f"api-gateway.{aws_regions}.amazonaws.com"  # api-gateway.us-east-1.amazonaws.com
domain2 = f"prod.{aws_regions}.amazonaws.com"         # lambda.us-east-1.amazonaws.com
domain3 = f"dev.{aws_regions}.amazonaws.com"          # s3.us-east-1.amazonaws.com
  
# Azure
domain4 = f"prod.{azure_regions}.azure.com"        # prod.ukwest.azure.com
domain5 = f"dev.{azure_regions}.azure.com"         # dev.ukwest.azure.com
domain6 = f"staging.{azure_regions}.azure.net"     # staging.ukwest.azure.net
