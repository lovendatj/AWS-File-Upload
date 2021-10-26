<!--
title: 'AWS Python File Upload'
description: 'This is intended as a quick file upload to an S3 Bucket and record management with DynamoDB'
layout: Doc
framework: v1
platform: AWS
language: Python
priority: 2
authorLink: 'https://github.com/lovendatj'
authorName: 'John Murray'
-->

# AWS Python File Upload

This is intended as a quick file upload to an S3 Bucket and record management with DynamoDB.

## Before starting

This example uses the [Serverless Framework](https://www.serverless.com/) for deploying AWS Services. In order to use this example, you will need to (1) install serverless and the aws-sdk using NPM, install python dependancies, and(3) configurate AWS CLI.

```bash
# (1) Installing Serverless with NPM.
npm install serverless aws-sdk
# (2) Install python libraries 
pip install -r requirements.txt
# (3) Configure AWS CLI
aws configure
```

### Creating the stack
To setup dependencies on AWS, run the following command:
```
serverless deploy
```

