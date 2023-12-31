resource "aws_sns_topic" "notification_topic" {
  name = "error_notification"
}
resource "aws_sns_topic_subscription" "user_updates_sqs_target" {
  topic_arn = aws_sns_topic.notification_topic.arn
  protocol  = "email"
  endpoint  = "de.project.banana@gmail.com"
}