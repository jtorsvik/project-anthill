variable "env" {
  description = "The environment for which the resources are being created (e.g., dev, staging, prod)"
  type        = string
  default     = "test"
}

variable "tags" {
  description = "A map of tags to assign to the resources"
  type        = map(string)
  default = {
    env     = "test"
    owner   = "jmtorsvik-admin"
    project = "project-anthill"
  }
}