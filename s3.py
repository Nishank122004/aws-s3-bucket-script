import boto3

session = boto3.session.Session(profile_name="default")
s3 = session.client(service_name='s3', region_name="ap-south-1")

bucket_name = "my-unique-s3-bucket-nishank-2025"
result = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': "ap-south-1"}
)

print(f"Created Bucket '{bucket_name}' successfully!")
