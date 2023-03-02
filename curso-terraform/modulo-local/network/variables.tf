variable "cidr_vpc" {
  description = "Cidr block para VPC"
  type        = string
}

variable "cidr_subnet" {
  description = "Cidr block para subnet"
  type        = string
}

variable "environment" {
  description = "Ambiente onde o recurso será utilizado"
  type        = string
}