variable "env" {
  description = "The environment for which the resources are being created (e.g., dev, staging, prod)"
  type        = string
  default     = "prod"
}

variable "tags" {
  description = "A map of tags to assign to the resources"
  type        = map(string)
  default = {
    env     = "prod"
    owner   = "jmtorsvik-admin"
    project = "project-anthill"
  }
}