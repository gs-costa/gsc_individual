terraform {

  required_version = ">= 1.0.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.44.1"
    }
  }

  backend "azurerm" {
    resource_group_name  = "storage_account_resource_group"
    storage_account_name = "gustavocostaremotestate"
    container_name       = "remote-state"
    key                  = "azure-vm-modulo-remoto/terraform.tfstate"
  }
}

provider "azurerm" {
  # Configuration options
  features {}
}

module "network" {
  source  = "Azure/network/azurerm"
  version = "3.5.0"

  # insert the 1 required variable here
  resource_group_name = azurerm_resource_group.resource_group.name
}