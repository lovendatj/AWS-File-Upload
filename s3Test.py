import StandardLibrary.AWS.S3 as s3

with open('./File 1.pdf', 'rb') as file:
    url = s3.upload_file(file=file,
                         bucket_alias='notion')
    print(url)
