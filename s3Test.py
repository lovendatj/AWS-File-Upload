import StandardLibrary.AWS.S3 as s3

with open('2011-DataWrangling-IVJ.pdf', 'rb') as file:
    s3.upload_file(file=file,
                   bucket_alias='notion')
