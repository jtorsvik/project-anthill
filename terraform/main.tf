data "aws_region" "current" {}

data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

data "aws_kms_key" "main" {
  key_id = var.kms_key_arn
}

# KMS & Secrets Manager
# ---------------------
variable "kms_key_arn" {
  type        = string
  description = "KMS key arn for AWS KMS Customer managed key."
}