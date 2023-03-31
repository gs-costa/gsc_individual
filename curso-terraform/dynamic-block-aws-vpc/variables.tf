variable "portas" {
  description = "portas que serão abertas no Security Group"
  type = list(number)
  default = [22, 80, 443, 8080]
}