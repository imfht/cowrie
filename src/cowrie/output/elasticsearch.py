# Simple elasticsearch logger

from __future__ import absolute_import, division

from elasticsearch import Elasticsearch

import cowrie.core.output
from cowrie.core.config import CowrieConfig


class Output(cowrie.core.output.Output):
    """
    elasticsearch output
    """

    def start(self):
        self.endpoint = CowrieConfig().get('output_elasticsearch', 'endpoint')
        self.index = CowrieConfig().get('output_elasticsearch', 'index')
        self.type = CowrieConfig().get('output_elasticsearch', 'type')
        self.pipeline = CowrieConfig().get('output_elasticsearch', 'pipeline')
        #self.es = Elasticsearch(["https://like:you@es.1db.tech:443/"])
        self.es = Elasticsearch([self.endpoint,])

    def stop(self):
        pass

    def write(self, logentry):
        for i in list(logentry.keys()):
            # remove twisted 15 legacy keys
            if i.startswith('log_'):
                del logentry[i]

        self.es.index(index=self.index, doc_type=self.type, body=logentry, pipeline=self.pipeline)
