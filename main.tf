# Set AWS provider to the specified region
provider "aws" {
  region = var.region
}

# Create an SNS topic for CloudWatch alarms
resource "aws_sns_topic" "cloudwatch_alarm_topic" {
  name = var.sns_topic_name
}

# Create an SNS topic subscription for CloudWatch alarms
resource "aws_sns_topic_subscription" "teams_notifications_subscription" {
  topic_arn = aws_sns_topic.cloudwatch_alarm_topic.arn
  protocol  = "https"
  endpoint  = var.teams_webhook_url
}

# Create a CloudWatch metric alarm for CPU utilization
resource "aws_cloudwatch_metric_alarm" "alarm" {
  alarm_name          = var.alarm_name
  comparison_operator = var.cloudwatch_metric_operator
  evaluation_periods  = var.cloudwatch_metric_evaluation_periods
  metric_name         = var.cloudwatch_metric_name
  namespace           = var.cloudwatch_metric_namespace
  period              = var.cloudwatch_metric_period
  statistic           = "Average"
  threshold           = var.cloudwatch_metric_threshold
  alarm_description   = var.cloudwatch_metric_description
  alarm_actions       = [aws_sns_topic.sns_topic.arn]
  dimensions          = {
    "${var.cloudwatch_metric_dimension_name}" = var.cloudwatch_metric_dimension_value
  }
}

# Create a Lambda function to send notifications to Microsoft Teams
resource "aws_lambda_function" "sns_to_teams" {
  filename      = "lambda_function.zip"
  function_name = var.lambda_name
  role          = aws_iam_role.lambda_execution.arn
  handler       = var.lambda_handler_name
  runtime       = "python3.9"
  timeout       = "60"
  runtime       = var.lambda_runtime
  timeout       = var.lambda_timeout
  memory_size   = var.lambda_memory_size

  # Set environment variables for the Lambda function
  environment {
    variables = {
      MS_TEAMS_WEBHOOK_URL = var.ms_teams_webhook_url
    }
  }

  # Depend on the SNS topic and Lambda execution policy
  depends_on = [
    aws_sns_topic.cloudwatch_alarm_topic,
    aws_iam_role_policy.lambda_execution_policy,
  ]
}

# Create an IAM role for the Lambda function
resource "aws_iam_role" "lambda_execution" {
  name = "lambda_execution"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

# Create an IAM policy for the Lambda function execution
resource "aws_iam_role_policy" "lambda_execution_policy" {
  name   = "lambda_execution_policy"
  policy = data.aws_iam_policy_document.lambda_execution_policy.json

  # Depend on the IAM role
  depends_on = [
    aws_iam_role.lambda_execution,
  ]
}

# Define an IAM policy document for the Lambda function execution policy
data "aws_iam_policy_document" "lambda_execution_policy" {
  statement {
    effect = "Allow"
    actions = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]
    resources = ["arn:aws:logs:*:*:*"]
  }

  statement {
    effect = "Allow"
    actions = [
      "sns:Publish"
    ]
    resources = [aws_sns_topic.cloudwatch_alarm_topic.arn]
  }
}

# Define a local variable for the Lambda function zip file
locals {
  teams_lambda_zip_file = "sns_to_teams.zip"
}

# Define an IAM policy document for the SNS topic policy
data "aws_iam_policy_document" "cloudwatch_alarm_policy" {
  statement {
    effect = "Allow"
    actions = [
      "sns:Publish"
    ]
    resources = [aws_sns_topic.cloudwatch_alarm_topic.arn]
  }
}
