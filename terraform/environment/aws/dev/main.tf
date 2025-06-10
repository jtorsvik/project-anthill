# --------------------
# Storage
# --------------------
module "aws_s3_bucket" {
    source        = "../../../modules/aws/storage/s3_bucket/"
    # version     = "1.0.0"
    bucket_name   = "project-anthill-s3-bucket-tf-${var.env}"
}

module "aws_vpc_public_subnets" {
    source        = "../../../modules/aws/network/vpc/"
    # version     = "1.0.0"
    friendly_name_prefix = "project-anthill-vpc-tf-${var.env}"
    cidr_block           = "10.0.0.0/16"
    enable_dns_support   = false
    enable_dns_hostnames = false
    tags                 = var.tags
}

module "aws_public_subnets" {
    source        = "../../../modules/aws/network/subnet/public/"
    # version     = "1.0.0"
    vpc_id        = module.aws_vpc_public_subnets.vpc_id
    cidr_block    = "10.0.0.0/24"
    tags          = var.tags
}