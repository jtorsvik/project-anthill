#############################################
# Storage
#############################################
module "aws_s3_bucket" {
    source = "../../../modules/aws/storage/s3_bucket/"
    # version     = "1.0.0"
    bucket_name = "project-anthill-s3-bucket-tf-${var.env}"
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
#     region                   = var.region
#     tags                     = local.tags
# }