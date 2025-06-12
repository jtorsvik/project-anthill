# ----------------------------------------
# Environment Variables for AWS Resources
# ----------------------------------------

variable "env" {
  description = "The environment for which the resources are being created (e.g., dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "owner" {
  description = "The owner of the resources"
  type        = string
  default     = "joakimmt-admin"
}

variable "project" {
  description = "The project name for which the resources are being created"
  type        = string
  default     = "project-anthill"
}

# ----------------------------------------
# Variables for the AWS VPC
# ----------------------------------------



# ----------------------------------------
# Variables for the Databricks Workspace configuration
# ----------------------------------------

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

# ----------------------------------------
# Variables for the Databricks Cluster configuration
# ----------------------------------------

variable "databricks_cluster_name" {
  description = "The name of the Databricks cluster"
  type        = string
  default     = "dbrix-cluster-dev"
}

variable "databricks_cluster_node_type" {
  description = "The node type for the Databricks cluster"
  type        = string
  default     = "i3.xlarge"
}