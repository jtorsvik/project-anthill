variable "vpc_id" {
  description = "The ID of the VPC to attach the Internet Gateway to."
  type        = string
}

variable "tags" {
  description = "A map of tags to assign to the resource."
  type        = map(string)
  default     = {
        env     = "dev" # To be replaced with automatic env detector
        owner   = "jmtorsvik-admin"
        project = "project-anthill"
    }
}
variable "cidr_block" {
  description = "The CIDR block for the public subnet."
  type        = string
}

variable "gateway_id" {
  description = "The ID of the Internet Gateway to use for the route table."
  type        = string
}

variable "subnet_id" {
  description = "The ID of the subnet to associate with the route table."
  type        = string
}