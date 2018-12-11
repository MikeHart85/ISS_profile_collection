#!/usr/bin/env python3

"""\
Configure databroker-elasticsearch callback which inserts run-start
documents into Elasticsearch as they come off the RunEngine.

See the iss-elasticsearch.yml file for conversion specification
between the input databroker document and Elasticsearch entry.
"""

import os.path
import databroker_elasticsearch

# configuration is in 99-elasticsearch.yml
_esconfig = os.path.splitext(__file__)[0] + '.yml'
escb = databroker_elasticsearch.load_callback(_esconfig)

# activate the callback
#RE.subscribe(escb)

# define top-level function for ES query
def esqsearch(q, **kwargs):
    "Perform Elasticsearch query using Lucene string syntax."
    rv = escb.esindex.qsearch(q, **kwargs)
    return rv
