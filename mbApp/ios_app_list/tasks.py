from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from .models import AppResource
import boto3
import botocore

#from photos.utils import save_latest_flickr_image

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="iterate_bucket",
    ignore_result=True
)
def iterate_bucket():
    a_r = AppResource(resource_key = 'yoyoyoy ')
    a_r.save()
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('mb-appstore')
    exists = True
    try:
        s3.meta.client.head_bucket(Bucket='mb-appstore')
    except botocore.exceptions.ClientError as e:
        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            exists = False
    if exists:
        for key in bucket.objects.all():
            a_r = AppResource(resource_key = '%s' %key.key)
            a_r.save()


