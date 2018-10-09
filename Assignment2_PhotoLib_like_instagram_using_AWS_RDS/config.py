#Name : Virti Bipin Sanghavi
#Student Id : 1001504428
#Assignment 2 - CSE 6331 Cloud Computing
#Reference to the code used from some online blogs, websites and repositories
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:test1234@vbsdbinstance.cgntbdpkzpds.us-east-2.rds.amazonaws.com:3306/vbsdatabase'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'qODT9oasBUJVHu5B8I4sV73rY3M6nZdRpD+d'


#Connection to S3 bucket

#AWS - Secret Key and access key from security credentials
access_key='AKIAJ25JNQVTNSDYLWKQ'
secret_key= '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'
#Bucket Name
my_bucket = 'vbsbucket'

s3Client = boto3.client('s3',aws_access_key_id=access_key,
  aws_secret_access_key=secret_key,
  config=Config(signature_version='s3v4'))

s3resource = boto3.resource('s3')
bucket = s3resource.Bucket(my_bucket)