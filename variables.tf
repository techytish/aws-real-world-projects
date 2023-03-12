variable "aws_region" {
  default = "eu-west-1"
}

variable "sns_topic_name" {
  default = "my-sns-topic"
}

variable "lambda_function_name" {
  default = "my-lambda-function"
}

variable "lambda_handler_name" {
  default = "lambda_function.lambda_handler"
}

variable "lambda_runtime" {
  default = "python3.9"
}

variable "lambda_timeout" {
  default = 30
}

variable "lambda_memory_size" {
  default = 128
}

variable "cloudwatch_metric_namespace" {
  default = "AWS/EC2"
}

variable "cloudwatch_metric_name" {
  default = "CPUUtilization"
}

variable "cloudwatch_metric_dimension_name" {
  default = "InstanceId"
}

variable "cloudwatch_metric_dimension_value" {
  default = "i-0123456789abcdefg"
}

variable "cloudwatch_metric_threshold" {
  default = 80
}

variable "cloudwatch_metric_evaluation_periods" {
  default = 1
}

variable "cloudwatch_metric_period" {
  default = 60
}

variable "cloudwatch_metric_operator" {
  default = "GreaterThanOrEqualToThreshold"
}
