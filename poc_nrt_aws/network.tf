resource "aws_vpc" "vpc_poc" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "vpc_nrt_poc"
  }
}

resource "aws_subnet" "subnet" {
  count = 2

  vpc_id            = aws_vpc.vpc_poc.id
  cidr_block        = "10.0.${count.index}.0/24"
  availability_zone = var.location[count.index]

  tags = {
    Name = "subnet-terraform-${count.index}"
  }
}

resource "aws_security_group" "sc_poc_nrt" {
  name        = "sc_poc_nrt"
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_vpc.vpc_poc.id

  tags = {
    Name = "sc_poc_nrt"
  }
}
