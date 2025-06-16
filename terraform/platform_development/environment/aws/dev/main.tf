#############################################
# Network & Security
#############################################

module "aws_vpc_public_subnets" {
    source = "../../../modules/aws/network/vpc/"
    # version     = "1.0.0"
    friendly_name_prefix = "project-anthill-vpc-tf-${local.env}"
    cidr_block           = "10.0.0.0/16"
    enable_dns_support   = false
    enable_dns_hostnames = false
    tags                 = var.tags
}

module "aws_public_subnets" {
    source = "../../../modules/aws/network/subnet/public/"
    # version     = "1.0.0"
    vpc_id     = module.aws_vpc_public_subnets.vpc_id
    cidr_block = "10.0.0.0/24"
    tags       = var.tags
}

module "aws_internet_gateway" {
    source = "../../../modules/aws/network/internet-gateway/"
    # version     = "1.0.0"
    vpc_id = module.aws_vpc_public_subnets.vpc_id
    tags   = var.tags
}

module "aws_route_table" {
    source = "../../../modules/aws/network/route-table/"
    # version           = "1.0.0"
    gateway_id = module.aws_internet_gateway.internet_gateway_id
    cidr_block = "0.0.0.0/0"
    subnet_id  = module.aws_public_subnets.public_subnet_id
    vpc_id     = module.aws_vpc_public_subnets.vpc_id
}

module "security_group" {
    source = "../../../modules/aws/network/security-group/"
    # version     = "1.0.0"
    name        = "project-anthill-sg-tf-${local.env}"
    description = "Security group for project Anthill"
    vpc_id      = module.aws_vpc_public_subnets.vpc_id
}

#############################################
# Databricks Workspace
#############################################

# module "aws_databricks_workspace" {
#     source = "../../../modules/aws/databricks/workspace/"
#     # version = "1.0.0"
#     workspace_name           = var.workspace_name
#     databricks_account_id    = var.databricks_account_id
#     client_id                = var.client_id
#     client_secret            = var.client_secret
#     network_id               = var.network_id
#     credentials_id           = var.credentials_id
#     role_arn                 = var.role_arn
#     storage_configuration_id = var.storage_configuration_id
#     storage_location         = var.storage_location
#     network_name             = var.network_name
#     vpc_id                   = module.aws_vpc_public_subnets.vpc_id
#     subnet_ids               = module.aws_public_subnets.public_subnet_ids
#     security_group_ids       = var.security_group_ids
#     region                   = var.databricks_workspace_region
#     tags                     = var.tags
# }