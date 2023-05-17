resource "aws_kinesis_stream" "pocnrt_stream" {
  name             = "pocnrt-stream"
  shard_count      = 1
  retention_period = 24

  depends_on = [aws_iam_role_policy_attachment.poc_nrt_policy]
}
