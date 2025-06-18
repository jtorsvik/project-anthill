# ----------------------------------------
# Environment Variables for AWS Resources
# ----------------------------------------

variable "env" {
  description = "The environment for which the resources are being created (e.g., dev, staging, prod)"
  type        = string
  default     = "test"
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

variable "region" {
  description = "The AWS region where the resources will be created"
  type        = string
  default     = "eu-west-1"
}
