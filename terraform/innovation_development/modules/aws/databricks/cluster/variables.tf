variable "cluster_name" {
  description = "The name of the Databricks cluster"
  type        = string
}

variable "spark_version" {
  description = "The Databricks Runtime version for the cluster"
  type        = string
  default     = data.databricks_runtime_version.latest_lts.id
}

variable "node_type_id" {
  description = "The node type for the Databricks cluster"
  type        = string
  default     = data.databicks_node_type.smallest.id
}

variable "autotermination_minutes" {
  description = "The number of minutes after which the cluster will automatically terminate if not in use"
  type        = number
  default     = 60
}

variable "num_workers" {
  description = "The number of worker nodes in the cluster"
  type        = number
  default     = 2
}