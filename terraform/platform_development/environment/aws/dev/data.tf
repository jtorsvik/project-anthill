# ----------------------------------
# This file is part of the Anthill project.
# ------------------------------------

# ----------------------------------------
# Data Sources for AWS Resources
# ----------------------------------------

data "aws_region" "current" {
  # This data source retrieves the current AWS region
}

# ----------------------------------------
# Databricks Cluster Data Source
# ----------------------------------------

# # Create a cluster with the smallest node type available in Databricks
# data "databricks_node_type" "smallest" {
#     local_disk = true
# }

# # Use the latest Databricks Runtime Version
# data "databricks_runtime_version" "latest_lts" {
#   # This data source retrieves the latest Databricks Runtime Version
#     long_term_support = true
# }