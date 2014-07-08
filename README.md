#Nagios-ElasticSearch

A few simple scripts for checking the state of your [ElasticSearch] cluster using Nagios the  endpoints of ElasticSearch

[![Build
Status](https://secure.travis-ci.org/opentable/nagios-elasticsearch.png)](https://secure.travis-ci.org/opentable/nagios-elasticsearch.png)

##How they work

These plugins work by submitting API requests to a local or remote
ElasticSearch server via the [cluster-health] and [node stats] endpoints

###Check Nodes in Cluster

This can be used to specify the nodes that are expected in the cluster. Currently, the check will return as **CRITICAL** if there are any unaccounted for nodes

```
Usage: check_es_nodes.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -v, --verbose
  -E NODES_IN_CLUSTER, --expected_nodes_in_cluster=NODES_IN_CLUSTER
                        This is the expected number of nodes in the cluster
  -H HOST, --host=HOST  The cluster to check
  -P PORT, --port=PORT  The ES port - defaults to 9200

python check_es_nodes.py --host=myescluster.com --expected_nodes_in_cluster=13
```

###Check Cluster Health Status

This plugin can be used to get the current cluster health. This will return OK for Green, Warning for Yellow and Critical for Red.


```
Usage: check_es_cluster_status.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -v, --verbose
  -H HOST, --host=HOST  The cluster to check
  -P PORT, --port=PORT  The ES port - defaults to 9200

python check_es_cluster_status.py --host=myescluster.com
```

###Check for Unassigned Nodes in Cluster

This plugin can be used to check for unassigned shards in the cluster. This can potentially indicate that a node is missing from the cluster. The alert will currently indicate a CRITICAL error if an unassigned shard is found

```
Usage: check_es_unassigned_shards.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -v, --verbose
  -H HOST, --host=HOST  The cluster to check
  -P PORT, --port=PORT  The ES port - defaults to 9200


python check_es_unassigned_shards.py --host=myescluster.com
```

###Check Node JVM Usage

This plugin can be used to ensure that the nodes in the cluster are not approaching, or exceeding, the thresholds that we determine that the JVM needs to run at. Currently, if any of the nodes exceed the critical limt, then the cluster will throw a CRITICAL error. If no nodes exceed the critical threshold but a node exceeds the warning threshold, then the cluster will throw a WARNING.

```
Usage: check_es_jvm_usage.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -v, --verbose
  -H HOST, --host=HOST  The cluster to check
  -P PORT, --port=PORT  The ES port - defaults to 9200
  -C CRITICAL_THRESHOLD, --critical_threshold=CRITICAL_THRESHOLD
                        The level at which we throw a CRITICAL alert -
                        defaults to 97% of the JVM setting
  -W WARNING_THRESHOLD, --warning_threshold=WARNING_THRESHOLD
                        The level at which we throw a WARNING alert - defaults
                        to 85% of the JVM setting


python check_es_unassigned_shards.py --host=myescluster.com
```

###Installation

###Development

###License
This project is licensed under MIT

 [cluster-health]: http://www.elasticsearch.org/guide/reference/api/admin-cluster-health.html
 [node stats]: http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/cluster-nodes-stats.html
 [ElasticSearch]: http://www.elasticsearch.org/
