#!/usr/bin/env python3

import connexion

from openapi_server.config.default import *

from openapi_server import encoder

app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml', arguments={'title': 'Legitimate People API'})
app.app.config.from_object(DevelopmentConfig)


if __name__ == "__main__":
    app.run(threaded=True, port=5000)

