output "sns_topic_arn" {
  value = aws_sns_topic.sns_topic.arn
}

output "lambda_function_name" {
  value = aws_lambda_function.lambda_function.function_name
}

output "lambda_function_arn" {
  value = aws_lambda_function.lambda_function.arn
}

output "lambda_function_role" {
  value = aws_iam_role.lambda_function_role.arn
}

output "cloudwatch_metric_alarm" {
  value = aws_cloudwatch_metric_alarm.alarm.arn
}
