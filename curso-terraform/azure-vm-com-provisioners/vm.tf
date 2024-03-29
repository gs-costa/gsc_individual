resource "azurerm_resource_group" "resource_group" {
  name     = "vm"
  location = var.location

  tags = local.common_tags
}

resource "azurerm_public_ip" "public_ip" {
  name                = "public-ip-terraform"
  resource_group_name = azurerm_resource_group.resource_group.name
  location            = var.location
  allocation_method   = "Dynamic"

  tags = local.common_tags
}

resource "azurerm_network_interface" "network_interface" {
  name                = "network-interface-terraform"
  location            = var.location
  resource_group_name = azurerm_resource_group.resource_group.name

  ip_configuration {
    name                          = "public-ip-terraform"
    subnet_id                     = data.terraform_remote_state.vnet.outputs.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.public_ip.id
  }

  tags = local.common_tags
}

resource "azurerm_network_interface_security_group_association" "nisga" {
  network_interface_id      = azurerm_network_interface.network_interface.id
  network_security_group_id = data.terraform_remote_state.vnet.outputs.security_group_id
}

resource "azurerm_linux_virtual_machine" "vm" {
  name                = "vm-terraform"
  resource_group_name = azurerm_resource_group.resource_group.name
  location            = var.location
  size                = "Standard_B1s"
  admin_username      = "terraform"
  network_interface_ids = [
    azurerm_network_interface.network_interface.id
  ]

  admin_ssh_key {
    username   = "terraform"
    public_key = file("./azure-key.pub") #comando para criar chave: ssh-keygen -f azure-key
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

  provisioner "local-exec" {
    command = "echo ${self.public_ip_address} >> public_ip.txt"
  }

  provisioner "file" {
    content     = "public_ip: ${self.public_ip_address}"
    destination = "/tmp/public_ip.txt"
  }

  provisioner "file" {
    source      = "./teste"
    destination = "/tmp"
  }

  connection {
    type        = "ssh"
    user        = "terraform"
    private_key = file("./azure-key")
    host        = self.public_ip_address
  }

  provisioner "remote-exec" {
    inline = [
      "echo location: ${var.location} >> /tmp/location.txt",
      "echo subnet_id: ${data.terraform_remote_state.vnet.outputs.subnet_id} >> /tmp/subnet_id.txt",
    ]
  }

  tags = local.common_tags
}