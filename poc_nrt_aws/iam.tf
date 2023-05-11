# resource "aws_iam_role" "kinesis_role" {
#   name               = "kinesis-role"
#   assume_role_policy = file("./permissions/policy_kinesis.json")
# }