#
# Copyright (C) 2014 MTA SZTAKI
#
# Key-Value store abstraction for the OCCO InfoBroker
#

__all__ = ['KeyValueStore',
           'KeyValueStoreProvider',
           'DictKVStore']

import occo.infobroker as ib
import occo.util.factory as factory
import yaml
import logging
import redis

log = logging.getLogger('occo.infobroker.kvstore.redis')_(self, **kwargs):
        pass

@factory.register(ib.KeyValueStore, 'redis')
class RedisKVStore(ib.KeyValueStore):
    def __init__(self, host='localhost', port='6379', db=0,  **kwargs):
	self.backend = redis.StrictRedis(host, port, db)
    def query_item(self, key):
        return self.backend.get(key)
    def set_item(self, key, value):
        self.backend.set(key, value)
    def has_key(self, key):
        return self.backend.exists(key)
