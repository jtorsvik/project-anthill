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

variable "cidr_block" {
  type        = string
  description = "(Required) The CIDR block for the Databricks workspace."
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