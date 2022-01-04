#!/usr/bin/python3
import boto3

client = boto3.client('ec2')

volumes_to_delete = list()

volume_detail = client.describe_volumes()

if volume_detail['ResponseMetadata']['HTTPStatusCode'] == 200:
    for each_volume in volume_detail['Volumes']:
        # some logging to make things clear about the volumes in your existing system
        print("Working for volume with volume_id: ", each_volume['VolumeId'])
        print("Create Time: ", each_volume['CreateTime'])
        print("State of volume: ", each_volume['State'])
        print("Attachment state length: ", len(each_volume['Attachments']))
        print(each_volume['Attachments'])
        print("--------------------------------------------")
        # figuring out the unused volumes
        # the volumes which do not have 'Attachments' key and their state is 'available' is considered to be unused
        if len(each_volume['Attachments']) == 0 and each_volume['State'] == 'available':
            volumes_to_delete.append(each_volume['VolumeId'])
print(volumes_to_delete)