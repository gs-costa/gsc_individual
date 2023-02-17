terraform {
    #required_version = ">= 1.0.0, < 1.2.0" #versoes entre 1.0.0 e 1.2.0
    required_version = "~>= 1.0.0" #1.0.0 até 1.1.n

    required_providers {
      aws = {
        version = ">= 3.50.0"
        source = "hashicorp/aws"
      }
      azurerm = {
        version = "2.70.0"
        source = "hashicorp/azurerm"
      }
    }

    backend "s3" {
      
    }
}

provider "aws" {
  
}

resource "aws_instance" "vm1" {
  
}

data "aws_ami" "ami" {
  
} #busca informações de itens de fora do terraform

module "vpc" {
  
}

variable "ip" {
  
}

output "vm1_ip" {
  
} #pega informação de dentro do terraform e envia para recurso

locals {
  
} #pega funções ou extensões que são usadas várias vezes no terraform para poder usá-las em outros locais