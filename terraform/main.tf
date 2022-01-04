provider "aws" {
  region                  = "us-east-1"
  shared_credentials_file = "/home/tgray/.aws/credentials"
  profile                 = "tgray"
}
resource "aws_instance" "ec2_1" {
    ami = "ami-0ed9277fb7eb570c9"  
    instance_type = "t2.small" 
    subnet_id = "subnet-0efc11ba19a17a66e"
    key_name = "awskey"
    tags = {
        Name = "Terraform EC2 1"
    }
}
resource "aws_instance" "ec2_2" {
    ami = "ami-0ed9277fb7eb570c9"  
    instance_type = "t2.small" 
    subnet_id = "subnet-0eb2543f6c0074127"
    key_name = "awskey"
    tags = {
        Name = "Terraform EC2 2"
    }
}