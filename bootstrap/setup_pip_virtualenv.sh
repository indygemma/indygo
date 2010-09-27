#!/bin/sh
#########
# Optional script to download pip, virtualenv, and fabric
# and upgrade those packages to the latest version
# used on a deployment server in order to make bootstrapping work
#########
# RUN AS SUDO!
CUR_DIR=`pwd`
PYTHON_LIB_DIR=`python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()"`
echo "--- Deleting pip ---"
cd $PYTHON_LIB_DIR && rm -rf pip*
cd $CUR_DIR
wget http://pypi.python.org/packages/source/p/pip/pip-0.6.2.tar.gz#md5=9a43e0a2ce8833069f41c347932bdb25
tar zxvf pip-0.6.2.tar.gz
cd pip-0.6.2 && python setup.py install && cd ..
wget http://pypi.python.org/packages/source/s/setuptools/setuptools-0.6c11.tar.gz#md5=7df2a529a074f613b509fb44feefe74e
tar zxvf setuptools-0.6c11.tar.gz
cd setuptools-0.6c11 && python setup.py install && cd ..
pip install virtualenv --upgrade
pip install fabric --upgrade
rm -rf pip-0.6.2*
rm -rf setuptools-0.6c11*
rm -rf build
