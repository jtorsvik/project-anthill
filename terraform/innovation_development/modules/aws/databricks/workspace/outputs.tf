output "databricks_workspace_id" {
    description = "Databricks workspace ID"
    value       = databricks_mws_workspace.this.id
}

output "databricks_workspace_url" {
    description = "Databricks workspace URL"
    value       = databricks_mws_workspace.this.workspace_url
}

output "databricks_workspace_name" {
    description = "Databricks workspace name"
    value       = databricks_mws_workspace.this.workspace_name
}

output "databricks_workspace_region" {
    description = "Databricks workspace region"
    value       = databricks_mws_workspace.this.region
}

output "databricks_workspace_credentials_id" {
    description = "Databricks workspace credentials ID"
    value       = databricks_mws_credentials.this.credentials_id
}

output "databricks_workspace_storage_configuration_id" {
    description = "Databricks workspace storage configuration ID"
    value       = databricks_mws_storage_configurations.this.storage_configuration_id
}

output "databricks_workspace_network_id" {
    description = "Databricks workspace network ID"
    value       = databricks_mws_networks.this.network_id
}

output "databricks_workspace_cidr_block" {
    description = "Databricks workspace CIDR block"
    value       = databricks_mws_workspace.this.cidr_block
}

output "databricks_workspace_tags" {
    description = "Databricks workspace tags"
    value       = databricks_mws_workspace.this.tags
}

output "databricks_workspace_credentials_role_arn" {
    description = "Databricks workspace credentials role ARN"
    value       = databricks_mws_credentials.this.role_arn
}

output "databricks_workspace_storage_location" {
    description = "Databricks workspace storage location"
    value       = databricks_mws_storage_configurations.this.storage_location
}

output "databricks_workspace_network_name" {
    description = "Databricks workspace network name"
    value       = databricks_mws_networks.this.network_name
}

output "databricks_workspace_vpc_id" {
    description = "Databricks workspace VPC ID"
    value       = databricks_mws_networks.this.vpc_id
}

output "databricks_workspace_subnet_ids" {
    description = "Databricks workspace subnet IDs"
    value       = databricks_mws_networks.this.subnet_ids
}

output "databricks_workspace_security_group_ids" {
    description = "Databricks workspace security group IDs"
    value       = databricks_mws_networks.this.security_group_ids
}

output "databricks_token" {
    description = "Databricks workspace token"
    value       = databricks_mws_credentials.this.token[0].token_value
    sensitive   = true
}