from __future__ import absolute_import

import os

from etcd3._client import Client

ENV_ETCD3_CA = 'ETCD3_CA'
ENV_ETCD3_ENDPOINT = 'ETCD3_ENDPOINT'
ENV_ETCD3_PASSWORD = 'ETCD3_PASSWORD'
ENV_ETCD3_USER = 'ETCD3_USER'


__all__ = [
    'Client'
]

_clt = None


def client():
    global _clt
    if _clt:
        return _clt

    endpoint = os.getenv(ENV_ETCD3_ENDPOINT, '127.0.0.1:2379')
    user = os.getenv(ENV_ETCD3_USER)
    password = os.getenv(ENV_ETCD3_PASSWORD)
    cert_ca = os.getenv(ENV_ETCD3_CA)
    _clt = Client(endpoint, user, password, cert_ca=cert_ca)
    return _clt