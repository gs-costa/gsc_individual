resource "aws_db_subnet_group" "dsg_poc_nrt" {
  name       = "main"
  subnet_ids = [aws_subnet.subnet[0].id, aws_subnet.subnet[1].id]

  tags = {
    Name = "DB subnet group"
  }
}

resource "aws_db_instance" "db_instance_poc_nrt" {
  allocated_storage      = 10
  identifier             = "db-instance-poc-nrt"
  db_name                = local.rds_dbname
  engine                 = "postgres"    #aurora-postgresql
  instance_class         = "db.t2.micro" #"db.serverless"
  engine_version         = "12.14"
  username               = local.rds_username
  password               = local.rds_password
  publicly_accessible    = true
  db_subnet_group_name   = aws_db_subnet_group.dsg_poc_nrt.id
  vpc_security_group_ids = [aws_security_group.sc_poc_nrt.id]
  skip_final_snapshot    = true
  # monitoring_role_arn    = aws_iam_role.poc_nrt_role.arn
}
