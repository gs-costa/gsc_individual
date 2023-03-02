resource "azurerm_resource_group" "resource_group" {
  name     = "modulo-remoto"
  location = var.location

  tags = local.common_tags
}
