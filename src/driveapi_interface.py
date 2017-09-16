__author__ = 'sudeep'

from apiclient import discovery
import httplib2


def get_service(service_name, version, api_key):
    """
    Gets the Drive API's service instance.
    :param service_name: Name of the service
    :param version: Version of the API interface
    :param api_key: Developer's API key.
    :return: Drive API's service instance
    """
    http_instance = httplib2.Http()
    service = discovery.build(service_name, version, http=http_instance, developerKey=api_key)
    return service


def get_file(service, file_id):
    """
    Gets a file instance from file_id
    :param service: Drive API's service instance
    :param file_id: The ID of the file on Drive
    :return: Drive File instance
    """
    my_file = service.files().get(fileId=file_id).execute()
    return my_file


def download_file(service, drive_file):
    """
    Downloads a drive file's content.

    :param service: Drive API's service instance
    :param drive_file: Drive File instance
    :return: Content of File if successful, otherwise None.
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
    """
    Gets the stored Drive API secret key.
    :return: Drive API key.
    """
    with open('../resources/.drive_api_key', 'r') as key_file:
        return key_file.read().replace('\n', '')