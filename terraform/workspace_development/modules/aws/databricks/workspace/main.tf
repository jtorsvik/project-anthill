resource "databricks_mws_credentials" "this" {
    provider       = databricks.mws
    account_id     = var.databricks_account_id
    credentials_id = var.credentials_id
    role_arn       = var.role_arn
}

resource "databricks_mws_storage_configurations" "this" {
    provider                 = databricks.mws
    account_id               = var.databricks_account_id
    storage_configuration_id = var.storage_configuration_id
    storage_location         = var.storage_location
}

resource "databricks_mws_networks" "this" {
    provider           = databricks.mws
    account_id         = var.databricks_account_id
    network_name       = var.network_name
    vpc_id             = var.vpc_id
    subnet_ids         = var.subnet_ids
    security_group_ids = var.security_group_ids
}

resource "databricks_mws_workspace" "this" {
    provider                 = databricks.mws
    account_id               = var.databricks_account_id
    workspace_name           = var.workspace_name
    aws_region               = var.region
    
    credentials_id           = databricks_mws_credentials.this.credentials_id
    storage_configuration_id = databricks_mws_storage_configurations.this.storage_configuration_id
    network_id               = databricks_mws_networks.this.network_id

    tags = var.tags

    token {}
}