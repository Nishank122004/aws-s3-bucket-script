# S3 Bucket Creation Script using Boto3

This Python script creates an Amazon S3 bucket in the specified AWS region using the Boto3 SDK.

---

## Prerequisites

- Python installed (preferably 3.x)
- Boto3 library installed (`pip install boto3`)
- AWS CLI configured with your credentials and profile (`aws configure`)

---

## How to use

1. Clone or download this repository.

2. Update the `bucket_name` and `region_name` variables in the `create_s3_bucket.py` script as needed.

3. Make sure your AWS credentials are set up in the default profile or the profile you specify.

4. Run the script:

   ```bash
   python create_s3_bucket.py
