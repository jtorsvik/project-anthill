terraform {
  required_version = ">= 1.7.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
  backend "s3" {
      bucket         = "project-anthill-s3-tfstate-dev"
      key            = "state/terraform.tfstate"
      region         = "eu-west-1"
      use_lockfile   = true
  }
}

provider "aws" {
    region = "eu-west-1"   
}