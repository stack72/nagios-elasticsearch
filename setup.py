from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name="nagios-elasticsearch",
    description="A selection of Nagios plugins to monitor ElasticSearch.",
    long_description="""
nagios-elasticsearch is a selection of nagios plugins that will monitor
a selection of ElasticSearch cluster metrics like Unassigned Shards, Cluster
health, that all nodes in the cluster are accounted for and also the Cluster
JVM settings
    """,
    version="0.1",
    packages=find_packages(),
    author='Paul Stack',
    author_email='public@paulstack.co.uk',
    url="https://github.com/opentable/nagios-elasticsearch",
    download_url = 'https://github.com/stack72/nagios-elasticsearch/tarball/0.1',
    scripts=["check_es_nodes.py","check_es_cluster_status.py","check_es_jvm_usage.py", "check_es_unassigned_shards.py","check_es_split_brain.py"],
    license="MIT",
    install_requires=[str(req.req) for req in
                      parse_requirements("requirements.txt")],
    include_package_data=True,
    keywords = ['monitoring','nagios','elasticsearch'],
    classifiers=[],

)
