import boto3

# Set the region (avoid NoRegionError)
region = "ap-south-1"

# Initialize AWS clients (no credentials needed if using EC2 instance with IAM role)
ec2 = boto3.client('ec2', region_name=region)
s3 = boto3.client('s3', region_name=region)
cf = boto3.client('cloudformation', region_name=region)

# Optional: Fetch stack resources
def list_stack_resources(stack_name):
    resources = cf.describe_stack_resources(StackName=stack_name)
    print(f"\nResources in stack '{stack_name}':")
    for res in resources['StackResources']:
        print(f"- {res['ResourceType']}: {res['PhysicalResourceId']}")

# List EC2 instances
def list_ec2_instances():
    print("\nEC2 Instances:")
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")

# List S3 buckets
def list_s3_buckets():
    print("\nS3 Buckets:")
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(f"- {bucket['Name']}")

if __name__ == "__main__":
    # Replace with your actual stack name
    stack_name = "ReadOnlyRoleStack"
    list_stack_resources(stack_name)
    list_ec2_instances()
    list_s3_buckets()
