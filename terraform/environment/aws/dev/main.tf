# --------------------
# Storage
# --------------------
module "aws_s3_bucket" {
  source = "../../../modules/aws/storage/s3_bucket/"
  # version     = "1.0.0"
  bucket_name = "project-anthill-s3-bucket-tf-${var.env}"
}

module "aws_vpc_public_subnets" {
  source = "../../../modules/aws/network/vpc/"
  # version     = "1.0.0"
  friendly_name_prefix = "project-anthill-vpc-tf-${var.env}"
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = false
  enable_dns_hostnames = false
  tags                 = local.tags
}

module "aws_public_subnets" {
  source = "../../../modules/aws/network/subnet/public/"
  # version     = "1.0.0"
  vpc_id     = module.aws_vpc_public_subnets.vpc_id
  cidr_block = "10.0.0.0/24"
  tags       = local.tags
}

module "aws_internet_gateway" {
  source = "../../../modules/aws/network/internet-gateway/"
  # version     = "1.0.0"
  vpc_id = module.aws_vpc_public_subnets.vpc_id
  tags   = local.tags
}

module "aws_route_table" {
  source = "../../../modules/aws/network/route-table/"
  # version           = "1.0.0"
  gateway_id = module.aws_internet_gateway.internet_gateway_id
  cidr_block = "0.0.0.0/0"
  subnet_id  = module.aws_public_subnets.public_subnet_id
  vpc_id     = module.aws_vpc_public_subnets.vpc_id
}