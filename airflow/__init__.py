"""
Authentication is implemented using flask_login and different environments can
implement their own login mechanisms by providing an `airflow_login` module
in their PYTHONPATH. airflow_login should be based off the
`airflow.www.login`
"""
__version__ = "1.1.0"

import logging
from airflow.configuration import conf
from airflow.models import DAG
from flask.ext.admin import BaseView


from airflow import default_login as login
if conf.getboolean('webserver', 'AUTHENTICATE'):
    try:
        # Environment specific login
        import airflow_login as login
    except ImportError:
        logging.error(
            "authenticate is set to True in airflow.cfg, "
            "but airflow_login failed to import")


class AirflowViewPlugin(BaseView):
    pass

class AirflowMacroPlugin(object):
    def __init__(self, namespace):
        self.namespace = namespace

from airflow import operators
from airflow import hooks
from airflow import executors
from airflow import macros

operators.integrate_plugins()
hooks.integrate_plugins()
macros.integrate_plugins()
