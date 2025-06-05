# --------------------
# Storage
# --------------------
module "aws_s3_bucket" {
    source        = "../../../modules/aws/storage/s3_bucket"
    # version     = "1.0.0"
    bucket_name   = "project-anthill-s3-bucket-tf-dev"
}