resource "aws_security_group" "this" {
  name        = var.name
  description = var.description
  vpc_id      = var.vpc_id

  tags = var.tags

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_vpc_security_group_ingress_rule" "this" {
  security_group_id = aws_security_group.this.id
  cidr_ipv4         = var.ingress_cidr_ipv4
  to_port           = var.ingress_to_port
  from_port         = var.ingress_from_port
  ip_protocol       = var.ingress_ip_protocol
}

resource "aws_vpc_security_group_egress_rule" "this" {
  security_group_id = aws_security_group.this.id
  cidr_ipv4         = var.egress_cidr_ipv4
  to_port           = var.egress_to_port
  from_port         = var.egress_from_port
  ip_protocol       = var.egress_ip_protocol
}