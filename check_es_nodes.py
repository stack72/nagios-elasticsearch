#!/usr/bin/python
from nagioscheck import NagiosCheck, UsageError
from nagioscheck import PerformanceMetric, Status
import urllib2
import optparse

try:
    import json
except ImportError:
    import simplejson as json

parser = optparse.OptionParser()
parser.add_option('-E','--expected_nodes_in_cluster', dest='nodes_in_cluster')
parser.add_option('-H','--host', dest='host')
parser.add_option('-P','--port', dest='port')
(opts, args) = parser.parse_args()

mandatories = ['nodes_in_cluster', 'host']
for m in mandatories:
  if not opts.__dict__[m]:
    print "mandatory parameter is missing\n"
    exit(-1)

def get_json(uri):
    try:
        response = urllib2.urlopen(uri)
    except urllib2.HTTPError, e:
        raise Status('unknown', ("API failure", None, "API failure:\n\n%s" % str(e)))
    except urllib2.URLError, e:
        raise Status('critical', (e.reason))

    response_body = response.read()

    try:
        json_rep = json.loads(response_body)
    except ValueError:
        raise Status('unknown', ("API returned nonsense",))

    return json_rep

def main():
  host = opts.host
  port = int(opts.port or '9200')
  nodes_in_cluster = int(opts.nodes_in_cluster)

  es_cluster_health = get_json(r'http://%s:%d/_cluster/health' %(host, port))

  active_cluster_nodes = es_cluster_health['number_of_nodes']

  if active_cluster_nodes != nodes_in_cluster:
    raise Status('CRITICAL', "The number of nodes in the cluster is not '%s'" %es_cluster_health['number_of_nodes'])
  else:
    raise Status('OK', "The number of nodes in the clust is good")

if __name__ == "__main__":main()
