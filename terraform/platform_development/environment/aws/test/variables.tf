# ----------------------------------------
# Variables for the AWS VPC
# ----------------------------------------



# # ----------------------------------------
# # Variables for the Databricks Workspace configuration
# # ----------------------------------------

variable "databricks_workspace_name" {
  description = "The name of the Databricks workspace"
  type        = string
  default     = "dbrix-project-anthill-dev"
}

variable "databricks_workspace_region" {
  description = "The AWS region for the Databricks workspace"
  type        = string
  default     = "eu-west-1"
}

# # ----------------------------------------
# # Variables for the Databricks Cluster configuration
# # ----------------------------------------

# variable "databricks_cluster_name" {
#   description = "The name of the Databricks cluster"
#   type        = string
#   default     = "dbrix-cluster-dev"
# }

# variable "databricks_cluster_node_type" {
#   description = "The node type for the Databricks cluster"
#   type        = string
#   default     = "i3.xlarge"
# }

# # ----------------------------------------
# # Variables for the Databricks Credentials
# # ----------------------------------------

# variable "databricks_account_id" {
#   description = "The Databricks account ID"
#   type        = string
# }

# variable "credentials_id" {
#   description = "The credentials ID for the Databricks workspace"
#   type        = string
# }

# variable "role_arn" {
#   description = "The IAM role ARN for the Databricks workspace"
#   type        = string
# }

# variable "storage_configuration_id" {
#   description = "The storage configuration ID for the Databricks workspace"
#   type        = string
# }

# variable "storage_location" {
#   description = "The storage location for the Databricks workspace"
#   type        = string
# }

# variable "network_name" {
#   description = "The name of the network for the Databricks workspace"
#   type        = string
#   default     = "dbrix-network-dev"
# }

# variable "vpc_id" {
#   description = "The VPC ID for the Databricks workspace"
#   type        = string
# }

# variable "subnet_ids" {
#   description = "The subnet IDs for the Databricks workspace"
#   type        = list(string)
# }

# variable "security_group_ids" {
#   description = "The security group IDs for the Databricks workspace"
#   type        = list(string)
# }

# variable "workspace_name" {
#   description = "The name of the Databricks workspace"
#   type        = string
#   default     = "dbrix-workspace-dev"
# }

# variable "client_id" {
#   description = "The client ID for the Databricks workspace"
#   type        = string
# }

# variable "client_secret" {
#   description = "The client secret for the Databricks workspace"
#   type        = string
# }

# variable "network_id" {
#   description = "The network ID for the Databricks workspace"
#   type        = string
# }
