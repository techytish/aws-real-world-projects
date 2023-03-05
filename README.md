# Pingdom to Microsoft Teams

The Pingdom app on Microsoft Teams does not work, I contacted Pingdom and they confirmed the payload request that is sent to Microsoft Teams is not compatible.

If they have an actual app in the Microsoft Teams store, then why doesn't it work?

Well the likely answer is that it needs updating, according to the reviews the app stopped working. 

So here comes my solution, assuming you have the following:
- AWS account
  - permissions to create resources in AWS
  - permissions to access AWS CloudWatch
- Pingdom account with checks configured, and permissions to add integration webhook urls
- Microsoft Teams account with permissions to add Incomming Webhook connector and create teams/channels
