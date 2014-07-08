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
    version="0.1.0",
    packages=find_packages(),
    author='Paul Stack',
    author_email='pstack@opentable.com',
    url="https://github.com/opentable/nagios-elasticsearch",
    scripts=["check_es_nodes.py"],
    license="MIT",
    install_requires=[str(req.req) for req in
                      parse_requirements("requirements.txt")],
    include_package_data=True
)
