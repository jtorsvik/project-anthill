variable "vpc_id" {
    description = "The ID of the VPC where the public subnet will be created."
    type        = string
}

variable "cidr_block" {
    description = "The CIDR block for the public subnet."
    type        = string
}

variable "tags" {
    description = "A map of tags to assign to the public subnet."
    type        = map(string)
    default     = {
        env     = "dev" # To be replaced with automatic env detector
        owner   = "jmtorsvik-admin"
        project = "project-anthill"
    }
}