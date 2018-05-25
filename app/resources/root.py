import os
import uuid
import mimetypes
import falcon
import cgi
import app.util.json as json
import requests

params = (
    ('recognize_vehicle', '1'),
    ('country', 'us'),
    ('secret_key', 'sk_02ecc708a736670ef7210224'),  # TODO secret key to parameters
)


def _recognize(image_file):
    files = {
        'image': (image_file, open(image_file, 'rb')),
    }

    response = requests.post('https://api.openalpr.com/v2/recognize', params=params, files=files)
    return json.dumps(response)


class RootResources(object):

    def on_get(self, req, resp):
        resp.body = json.dumps({
            "message": "GAF!",
        })


class Resource(object):  # TODO queue

    _CHUNK_SIZE_BYTES = 4096

    def __init__(self, storage_path):
        self._storage_path = storage_path

    def on_post(self, req, resp):
        image = req.get_param("image")
        ext = mimetypes.guess_extension(req.content_type)
        filename = "{uuid}{ext}".format(uuid=uuid.uuid4(), ext=ext)
        image_path = os.path.join(self._storage_path, filename)
        with open(image_path, "wb") as image_file:
            while True:
                chunk = image.file.read(4096)
                image_file.write(chunk)
                if not chunk:
                    break
        resp.status = falcon.HTTP_200
        resp.location = filename
        # resp.body = json.dumps("{name:" + image_path + "}")
        resp.body = json.dumps(_recognize(image_path))  # TODO try except and read from DB
