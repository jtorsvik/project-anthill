data "databicks_node_type" "smallest" {
    local_disk = true
}

# Use the latest Databricks Runtime Version
data "databricks_runtime_version" "latest_lts" {
  # This data source retrieves the latest Databricks Runtime Version
    long_term_support = true
}