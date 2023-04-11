variable "location" {
  description = "Variável que indica a região onde os recursos serão criados"
  type        = string
  default     = "Brazil South"
}

variable "aws_pub_key" {
  description = "public key para VM na AWS"
  type = string
}

variable "azure_pub_key" {
  description = "public key para VM na Azure"
  type = string
}