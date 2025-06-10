variable "friendly_name_prefix" {
  type        = string
  description = "(Required) Friendly name prefix used for tagging and naming AWS resources."
}

variable "cidr_block" {
  type        = string
  description = "(Optional) CIDR block for the VPC."
}
variable "network_cidr" {
  type        = string
  description = "(Optional) CIDR block for VPC."
  default     = "10.0.0.0/16"
}

variable "network_private_subnet_cidrs" {
  type        = list(string)
  description = "(Optional) List of private subnet CIDR ranges to create in VPC."
  default     = ["10.0.32.0/24", "10.0.48.0/24"]
}

variable "network_public_subnet_cidrs" {
  type        = list(string)
  description = "(Optional) List of public subnet CIDR ranges to create in VPC."
  default     = ["10.0.0.0/24", "10.0.16.0/24"]
}

variable "project" { 
  type        = string
  description = "(Required) Project name used for tagging and naming AWS resources."
  default     = "project-anthill"
}

variable "tags" {
    description = "A map of tags to assign the resource"
    type        = map(string)
    default     = {
        env     = "dev" # To be replaced with automatic env detector
        owner   = "jmtorsvik-admin"
        project = "project-anthill"
    }
}

variable "enable_dns_support" {
  type        = bool
  description = "(Optional) Whether to enable DNS support in the VPC."
  default     = true
}
variable "enable_dns_hostnames" {
  type        = bool
  description = "(Optional) Whether to enable DNS hostnames in the VPC."
  default     = true
}