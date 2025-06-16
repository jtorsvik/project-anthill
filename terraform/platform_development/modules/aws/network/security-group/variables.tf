variable "name" {
  description = "The name of the security group."
  type        = string
}

variable "description" {
  description = "A description of the security group."
  type        = string
}

variable "vpc_id" {
  description = "The ID of the VPC where the security group will be created."
  type        = string
}

variable "ingress_cidr_ipv4" {
  description = "The CIDR block for the security group ingress rule."
  type        = string
  default     = "0.0.0.0/0"
}

variable "tags" {
  description = "A map of tags to assign to the security group."
  type        = map(string)
  default     = {}
}

variable "ingress_to_port" {
  description = "The port number for the security group ingress rule."
  type        = number
  default     = 80
}

variable "ingress_from_port" {
  description = "The starting port number for the security group ingress rule."
  type        = number
  default     = 80
}

variable "ingress_ip_protocol" {
  description = "The IP protocol for the security group ingress rule."
  type        = string
  default     = "tcp"
}

variable "egress_cidr_ipv4" {
  description = "The CIDR block for the security group egress rule."
  type        = string
  default     = "0.0.0.0/0"
}

variable "egress_to_port" {
  description = "The port number for the security group egress rule."
  type        = number
  default     = 80
}

variable "egress_from_port" {
  description = "The starting port number for the security group egress rule."
  type        = number
  default     = 80
}

variable "egress_ip_protocol" {
  description = "The IP protocol for the security group egress rule."
  type        = string
  default     = "tcp"
}