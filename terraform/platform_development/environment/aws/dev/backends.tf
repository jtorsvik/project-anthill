terraform {
  backend "s3" {
    bucket       = "project-anthill-s3-tfstate-dev"
    key          = "platform/state/terraform.tfstate"
    region       = "eu-west-1"
    # use_lockfile = true
  }
}