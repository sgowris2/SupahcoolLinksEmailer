__author__ = 'sudeep'

from apiclient import errors
from apiclient import discovery
import httplib2

def get_service(service_name, version, api_key):
    http_instance = httplib2.Http()
    service = discovery.build(service_name, version, http=http_instance, developerKey=api_key)
    return service

def get_file(service, file_id):
    my_file = service.files().get(fileId=file_id).execute()
    return my_file

def download_file(service, drive_file):
  """Download a file's content.

  Args:
    service: Drive API service instance.
    drive_file: Drive File instance.

  Returns:
    File's content if successful, None otherwise.
  """
  download_url = drive_file.get('exportLinks').get('text/csv')
  if download_url:
    resp, content = service._http.request(download_url)
    if resp.status == 200:
      print 'Status: %s' % resp
      return content
    else:
      print 'An error occurred: %s' % resp
      return None
  else:
    # The file doesn't have any content stored on Drive.
    return None

def get_api_key():
    """Get the stored Drive API Key

    Args:
        None
    Returns:
        The API Key as a string
    """
    with open('../DriveAPI.key', 'r') as key_file:
        return key_file.read().replace('\n', '')