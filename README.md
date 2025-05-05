# AWS Inventory Fetcher using CloudFormation and Boto3

## 📘 Project Overview

This project demonstrates how to:
- Provision a read-only IAM role using AWS CloudFormation.
- Generate a Stack Launch URL to easily deploy the stack.
- Use a Python script to fetch inventory details (EC2 instances, S3 buckets, etc.) securely **without using access keys**, leveraging **EC2 instance profile roles** instead.

## 🛠️ Technologies Used

- AWS CloudFormation (YAML)
- IAM Roles and Policies
- Amazon EC2
- Amazon S3
- Python 3
- Boto3 (AWS SDK for Python)

## 🔧 CloudFormation Stack Details

The CloudFormation template:
- Creates an IAM Role `ReadOnlyAccessRole`
- Attaches the following AWS managed policies:
  - `AmazonEC2ReadOnlyAccess`
  - `AmazonS3ReadOnlyAccess`
  - `ReadOnlyAccess`
- Assumes the role for EC2 using the appropriate trust policy

### 🚀 Stack Launch URL

> Replace `<your-bucket-url>` with the actual S3 URL if hosting the template:
