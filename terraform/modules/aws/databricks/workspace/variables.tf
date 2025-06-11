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