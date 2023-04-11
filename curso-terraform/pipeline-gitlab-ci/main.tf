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
    key                  = "pipeline-gitlab-ci/terraform.tfstate"
  }
}

provider "azurerm" {
  # Configuration options
  features {}
}

data "terraform_remote_state" "vpc" {
  backend = "azurerm"
  config = {
    resource_group_name  = "storage_account_resource_group"
    storage_account_name = "gustavocostaremotestate"
    container_name       = "remote-state"
    key                  = "azure-vm-modulo-remoto/terraform.tfstate"
  }
}

provider "aws" {
  # Configuration options
  region = "us-east-1"
  default_tags {
    tags = {
      owner      = "gustavocosta"
      managed-by = "terraform"
    }
  }
}

data "terraform_remote_state" "vpc" {
  backend = "s3"
  config = {
    bucket = "gsantosaero-terraform-remote-state"
    key    = "aws-vpc/terraform.tfstate"
    region = "us-east-1"
  }
}