output "cluster_url" {
  description = "The URL of the Databricks cluster"
  value       = databricks_cluster.this.cluster_url
}