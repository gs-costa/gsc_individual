variable "location" {
  description = "variável que indica região onde recursos serão criados"
  default     = ["us-east-1a", "us-east-1b"]
  type        = list(any)
}
