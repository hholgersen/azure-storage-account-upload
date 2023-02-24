# first run "pip install azure-storage-blob"

from azure.storage.blob import BlobServiceClient


# Add details here:
file_to_upload = "<my_folder/data.csv>"
destination_file_name = "<data_2022_01_01.csv>"
storage_account_name = "<name of storage account>"
container_name = "<container-name-to-upload-to>"
sas_token = "<secret-sas-token>"


def write_to_azure_blob(sas_token, container_name, blob_name, file_path):
  """ upload file to azure blob storage """

  blob_service_client = BlobServiceClient.from_connection_string(sas_token)
  container_client = blob_service_client.get_container_client(container_name)
  blob_client = container_client.get_blob_client(blob_name)

  with open(file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)


def main():

  connection_string = f"BlobEndpoint=https://{storage_account_name}.blob.core.windows.net/;SharedAccessSignature={sas_token}"
  
  
  write_to_azure_blob(connection_string, container_name, destination_file_name, file_to_upload)

if __name__ == '__main__':
  main()

