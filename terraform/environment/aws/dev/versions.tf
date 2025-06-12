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
    databricks = {
      source = "databricks/databricks"
      version = "~> 1.0.0"
    }
  }
}

provider "aws" {
  region = "eu-west-1"
}

provider "databricks" {
  # Config options
}