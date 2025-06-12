variable "client_id" {
  type        = string
  description = "(Required) The client ID for the Databricks workspace."
}

variable "client_secret" {
  type        = string
  description = "(Required) The client secret for the Databricks workspace."
}

variable "databricks_account_id" {
  type        = string
  description = "(Required) The Databricks account ID."
}

variable "role_arn" {
  type        = string
  description = "(Required) The AWS IAM role ARN that Databricks will assume for the workspace."
}

variable "storage_location" {
  type        = string
  description = "(Required) The S3 bucket location for the Databricks workspace storage."
}

variable "network_name" {
  type        = string
  description = "(Required) The name of the network for the Databricks workspace."
}

variable "vpc_id" {
  type        = string
  description = "(Required) The VPC ID where the Databricks workspace will be created."
}

variable "subnet_ids" {
  type        = list(string)
  description = "(Required) A list of subnet IDs for the Databricks workspace."
}

variable "security_group_ids" {
  type        = list(string)
  description = "(Required) A list of security group IDs for the Databricks workspace."
}

variable "workspace_name" {
  type        = string
  description = "(Required) The name of the Databricks workspace."
}

variable "region" {
  type        = string
  description = "(Required) The AWS region where the Databricks workspace will be created."
}

variable "credentials_id" {
  type        = string
  description = "(Required) The credentials ID for the Databricks workspace."
}

variable "storage_configuration_id" {
  type        = string
  description = "(Required) The storage configuration ID for the Databricks workspace."
}

variable "network_id" {
  type        = string
  description = "(Required) The network ID for the Databricks workspace."
}

variable "tags" {
  type        = map(string)
  description = "(Optional) A map of tags to assign to the Databricks workspace."
  default     = {}
}