from setuptools import setup, find_packages


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

setup(
    name="nagios-elasticsearch",
    description="A selection of Nagios plugins to monitor ElasticSearch.",
    long_description=open('README.rst').read(),
    version="0.1.3",
    packages=find_packages(),
    author='Paul Stack',
    author_email='public@paulstack.co.uk',
    url="https://github.com/stack72/nagios-elasticsearch",
    download_url='http://github.com/stack72/nagios-elasticsearch/tarball/0.1.3',
    scripts=["check_es_nodes.py",
             "check_es_cluster_status.py",
             "check_es_jvm_usage.py",
             "check_es_unassigned_shards.py",
             "check_es_split_brain.py"],
    license="MIT",
    install_requires=parse_requirements("requirements.txt"),
    include_package_data=True,
    keywords=['monitoring', 'nagios', 'elasticsearch'],
    classifiers=[],

)
