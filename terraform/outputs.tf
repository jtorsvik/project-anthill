# Network
output "network_id" {
  value       = local.network_id
  description = "The identity of the VPC in which resources are deployed."
  # This output is marked as sensitive to work around a bug in Terraform 0.14
  sensitive = true
}

output "private_subnet_ids" {
  value       = local.network_private_subnets
  description = "The identities of the private subnetworks deployed within the VPC."
  # This output is marked as sensitive to work around a bug in Terraform 0.14
  sensitive = true
}

output "public_subnet_ids" {
  value       = local.network_public_subnets
  description = "The identities of the public subnetworks deployed within the VPC."
  # This output is marked as sensitive to work around a bug in Terraform 0.14
  sensitive = true
}

output "network_private_subnet_cidrs" {
  value       = local.network_private_subnet_cidrs
  description = "The CIDR blocks of the private subnetworks deployed within the VPC."
  # This output is marked as sensitive to work around a bug in Terraform 0.14
  sensitive = true
}