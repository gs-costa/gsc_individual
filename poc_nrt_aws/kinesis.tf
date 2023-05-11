resource "aws_kinesis_stream" "pocnrt_stream" {
  name             = "pocnrt-stream"
  shard_count      = 1
  retention_period = 24

  depends_on = [aws_iam_role_policy_attachment.poc_nrt_policy]
}

# resource "aws_kinesis_analytics_application" "nrtpoc_flink_application" {
#   name = "nrtpoc_flink_app"

#   inputs {
#     name_prefix = "input_prefix"

#     kinesis_stream {
#       resource_arn = aws_kinesis_stream.pocnrt_stream.arn
#       role_arn     = aws_iam_role.poc_nrt_role.arn
#     }

#     parallelism {
#       count = 2
#     }

#     schema {
#       record_columns {
#         mapping  = "$.test"
#         name     = "test"
#         sql_type = "VARCHAR(8)"
#       }

#       record_encoding = "UTF-8"

#       record_format {
#         mapping_parameters {
#           json {
#             record_row_path = "$"
#           }
#         }
#       }
#     }
#   }
# }
