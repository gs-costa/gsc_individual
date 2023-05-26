resource "aws_vpc" "vpc_poc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true

  tags = {
    Name = "vpc_poc"
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

  ingress {
    description = "internet"
    from_port   = 0
    to_port     = 0
    protocol    = "all"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "internet"
    from_port   = 0
    to_port     = 0
    protocol    = "all"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.vpc_poc.id

  tags = {
    Name = "vpc_poc"
  }
}

resource "aws_route_table" "rt_poc" {
  vpc_id = aws_vpc.vpc_poc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
  # route {
  #   cidr_block = "172.31.0.0/16"
  # }


  tags = {
    name = "rt_poc"
  }
}

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.subnet[0].id
  route_table_id = aws_route_table.rt_poc.id
}