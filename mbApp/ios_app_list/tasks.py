from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from .models import AppResource
#from photos.utils import save_latest_flickr_image

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="fetch_contents",
    ignore_result=True
)
def fetch_contents():
    """
    Fetches content from aws server
    """
    all_app_resources = AppResource.objects.all()
    count = len(all_app_resources)
    a_r = AppResource(resource_key = 'resource num %d' %count)
    a_r.save()
    logger.info("Content from aws")
