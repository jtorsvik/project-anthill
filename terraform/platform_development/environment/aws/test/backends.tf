terraform {
  backend "s3" {
    bucket       = "project-anthill-s3-tfstate-${var.env}"
    key          = "platform/state/terraform.tfstate"
    region       = "eu-west-1"
  }
}