terraform {
  backend "s3" {
    bucket       = "project-anthill-s3-tfstate-dev"
    key          = "state/terraform.tfstate"
    region       = "eu-west-1"
    use_lockfile = true
  }
}