output "bucket_name" {
    value = aws_s3_bucket.this.bucket
}

output "region" {
    value = aws_s3_bucket.this.region
}