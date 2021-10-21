import StandardLibrary.AWS.Dynamo as dynamo
import StandardLibrary.AWS.S3 as s3
import sys
import glob
import os
from datetime import datetime
print(sys.argv)
readPath = sys.argv[1]
bucketAlias = sys.argv[2]
cleanUp = sys.argv[3]
try:
    filterFile = sys.argv[4]
except:
    filterFile = None
if filterFile is not None:
    files = glob.glob(f'../{readPath}/{filterFile}')
else:
    files = glob.glob(f'../{readPath}/*.*')

for f in files:
    with open(f, 'rb') as file:
        print(f'Processing {file.name}')
        file_name, url = s3.upload_file(file=file,
                                        bucket_alias='notion')
        dynamo.insert_row('reading', {
            'Name': file_name,
            'Read': False,
            'URL': url,
            'Date Added': datetime.now().strftime('%m-%d-%Y')
        })
    try:
        if cleanUp:
            os.remove(f)
    except:
        continue
