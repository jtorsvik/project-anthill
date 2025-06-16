output "name" {
  description = "The name of the EC2 instance."
  value       = aws_ec2_instance.this.tags["Name"]
}

output "id" {
  description = "The ID of the EC2 instance."
  value       = aws_ec2_instance.this.id
}

output "public_ip" {
  description = "The public IP address of the EC2 instance."
  value       = aws_ec2_instance.this.public_ip
}

output "private_ip" {
  description = "The private IP address of the EC2 instance."
  value       = aws_ec2_instance.this.private_ip
}

output "security_group_id" {
  description = "The ID of the security group associated with the EC2 instance."
  value       = aws_ec2_instance.this.vpc_security_group_ids[0]
}

output "subnet_id" {
  description = "The ID of the subnet where the EC2 instance is launched."
  value       = aws_ec2_instance.this.subnet_id
}

output "ami" {
  description = "The AMI ID used for the EC2 instance."
  value       = aws_ec2_instance.this.ami
}

output "instance_type" {
  description = "The type of EC2 instance."
  value       = aws_ec2_instance.this.instance_type
}

output "key_name" {
  description = "The name of the key pair used for SSH access to the EC2 instance."
  value       = aws_ec2_instance.this.key_name
}