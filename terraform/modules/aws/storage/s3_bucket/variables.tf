variable "bucket_name" {
    description = "The global name of the S3 bucket. Must be lowercase and less than or equal to 63 characters in length. Globally unique"
    type        = string
}

variable "region" {
    description = "The region of the S3 Bucket"
    type        = string
    default     = "eu-west-1"
}

# variable "bucket_prefix" {
#     description = "The local name of the S3 Bucket."
#     type = string
# }

variable "tags" {
    description = "A map of tags to assign the resource"
    type        = map(string)
    default     = {
        env     = "dev" # To be replaced with automatic env detector
        owner   = "jmtorsvik-admin"
        project = "project-anthill"
    }
}

variable "force_destroy" {
    description = "When the bucket is destroyed all objects in the bucket are destroyed"
    type        = bool
    default     = true
}

variable "object_lock_enabled" {
    description = "Write & Destroy protection on files"
    type        = bool
    default     = false
}