import uuid
from io import BytesIO
from azure.storage.blob import BlobServiceClient

from app.core.config import settings
from app.clients.storage_client import StorageClient


class AzureBlobClient(StorageClient):

    def __init__(self):
        self.client = BlobServiceClient.from_connection_string(
            settings.AZURE_CONNECTION_STRING,
            api_version="2023-11-03"
        )
        self.container_name = settings.CONTAINER_NAME
        self._ensure_container()

    def _ensure_container(self):
        container = self.client.get_container_client(self.container_name)
        if not container.exists():
            container.create_container()

    def save(self, data: str) -> str:
        blob_id = str(uuid.uuid4())

        blob_client = self.client.get_blob_client(
            container=self.container_name,
            blob=blob_id
        )

        blob_client.upload_blob(BytesIO(data.encode()), overwrite=True)

        return blob_id

    def get(self, key: str) -> str:
        blob_client = self.client.get_blob_client(
            container=self.container_name,
            blob=key
        )

        stream = blob_client.download_blob()
        return stream.readall().decode()
    
    def list_ids(self) -> list[str]:
        container_client = self.client.get_container_client(self.container_name)
        return [blob.name for blob in container_client.list_blobs()]
