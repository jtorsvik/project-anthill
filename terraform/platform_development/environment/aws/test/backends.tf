terraform {
  backend "s3" {
    bucket       = "project-anthill-s3-tfstate-test"
    key          = "platform/state/terraform.tfstate"
    region       = "eu-west-1"
  }
}