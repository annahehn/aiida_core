# -*- coding: utf-8 -*-
###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida_core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from six.moves import range
from aiida.plugins.entry_point import ENTRYPOINT_MANAGER
from aiida.backends.profile import BACKEND_SQLA, BACKEND_DJANGO

db_test_list = {
    BACKEND_DJANGO: {
        'generic': ['aiida.backends.djsite.db.subtests.generic'],
        'nodes': ['aiida.backends.djsite.db.subtests.nodes'],
        'migrations': ['aiida.backends.djsite.db.subtests.migrations'],
        'query': ['aiida.backends.djsite.db.subtests.query'],
    },
    BACKEND_SQLA: {
        'generic': ['aiida.backends.sqlalchemy.tests.generic'],
        'nodes': ['aiida.backends.sqlalchemy.tests.nodes'],
        'query': ['aiida.backends.sqlalchemy.tests.query'],
        'session': ['aiida.backends.sqlalchemy.tests.session'],
        'schema': ['aiida.backends.sqlalchemy.tests.schema'],
        'migrations': ['aiida.backends.sqlalchemy.tests.migrations'],
    },
    # Must be always defined (in the worst case, an empty dict)
    'common': {
        'generic': ['aiida.backends.tests.generic'],
        'nodes': ['aiida.backends.tests.nodes'],
        'base_dataclasses': ['aiida.backends.tests.base_dataclasses'],
        'dataclasses': ['aiida.backends.tests.dataclasses'],
        'dbimporters': ['aiida.backends.tests.dbimporters'],
        'export_and_import': ['aiida.backends.tests.export_and_import'],
        'parsers': ['aiida.backends.tests.parsers'],
        'tcodexporter': ['aiida.backends.tests.tcodexporter'],
        'query': ['aiida.backends.tests.query'],
        'calculation_node': ['aiida.backends.tests.calculation_node'],
        'backup_script': ['aiida.backends.tests.backup_script'],
        'backup_setup_script': ['aiida.backends.tests.backup_setup_script'],
        'restapi': ['aiida.backends.tests.restapi'],
        'cmdline.commands.calcjob': ['aiida.backends.tests.cmdline.commands.test_calcjob'],
        'cmdline.commands.calculation': ['aiida.backends.tests.cmdline.commands.test_calculation'],
        'cmdline.commands.code': ['aiida.backends.tests.cmdline.commands.test_code'],
        'cmdline.commands.comment': ['aiida.backends.tests.cmdline.commands.test_comment'],
        'cmdline.commands.computer': ['aiida.backends.tests.cmdline.commands.test_computer'],
        'cmdline.commands.config': ['aiida.backends.tests.cmdline.commands.test_config'],
        'cmdline.commands.data': ['aiida.backends.tests.cmdline.commands.test_data'],
        'cmdline.commands.database': ['aiida.backends.tests.cmdline.commands.test_database'],
        'cmdline.commands.export': ['aiida.backends.tests.cmdline.commands.test_export'],
        'cmdline.commands.graph': ['aiida.backends.tests.cmdline.commands.test_graph'],
        'cmdline.commands.group': ['aiida.backends.tests.cmdline.commands.test_group'],
        'cmdline.commands.import': ['aiida.backends.tests.cmdline.commands.test_import'],
        'cmdline.commands.node': ['aiida.backends.tests.cmdline.commands.test_node'],
        'cmdline.commands.process': ['aiida.backends.tests.cmdline.commands.test_process'],
        'cmdline.commands.profile': ['aiida.backends.tests.cmdline.commands.test_profile'],
        'cmdline.commands.rehash': ['aiida.backends.tests.cmdline.commands.test_rehash'],
        'cmdline.commands.run': ['aiida.backends.tests.cmdline.commands.test_run'],
        'cmdline.commands.setup': ['aiida.backends.tests.cmdline.commands.test_setup'],
        'cmdline.commands.user': ['aiida.backends.tests.cmdline.commands.test_user'],
        'cmdline.commands.verdi': ['aiida.backends.tests.cmdline.commands.test_verdi'],
        'cmdline.commands.work': ['aiida.backends.tests.cmdline.commands.test_work'],
        'cmdline.params.types.calculation': ['aiida.backends.tests.cmdline.params.types.test_calculation'],
        'cmdline.params.types.code': ['aiida.backends.tests.cmdline.params.types.test_code'],
        'cmdline.params.types.computer': ['aiida.backends.tests.cmdline.params.types.test_computer'],
        'cmdline.params.types.data': ['aiida.backends.tests.cmdline.params.types.test_data'],
        'cmdline.params.types.group': ['aiida.backends.tests.cmdline.params.types.test_group'],
        'cmdline.params.types.identifier': ['aiida.backends.tests.cmdline.params.types.test_identifier'],
        'cmdline.params.types.node': ['aiida.backends.tests.cmdline.params.types.test_node'],
        'cmdline.params.types.plugin': ['aiida.backends.tests.cmdline.params.types.test_plugin'],
        'common.archive': ['aiida.backends.tests.common.test_archive'],
        'common.datastructures': ['aiida.backends.tests.common.test_datastructures'],
        'common.extendeddicts': ['aiida.backends.tests.common.test_extendeddicts'],
        'common.folders': ['aiida.backends.tests.common.test_folders'],
        'common.hashing': ['aiida.backends.tests.common.test_hashing'],
        'common.logging': ['aiida.backends.tests.common.test_logging'],
        'common.serialize': ['aiida.backends.tests.common.test_serialize'],
        'common.timezone': ['aiida.backends.tests.common.test_timezone'],
        'common.utils': ['aiida.backends.tests.common.test_utils'],
        'daemon.client': ['aiida.backends.tests.daemon.test_client'],
        'manage.configuration.config.': ['aiida.backends.tests.manage.configuration.test_config'],
        'manage.configuration.migrations.': ['aiida.backends.tests.manage.configuration.migrations.test_migrations'],
        'manage.configuration.options.': ['aiida.backends.tests.manage.configuration.test_options'],
        'manage.configuration.profile.': ['aiida.backends.tests.manage.configuration.test_profile'],
        'manage.external.postgres.': ['aiida.backends.tests.manage.external.test_postgres'],
        'orm.authinfo': ['aiida.backends.tests.orm.authinfo'],
        'orm.comments': ['aiida.backends.tests.orm.comments'],
        'orm.computer': ['aiida.backends.tests.computer'],
        'orm.data.frozendict': ['aiida.backends.tests.orm.data.frozendict'],
        'orm.data.remote': ['aiida.backends.tests.orm.data.remote'],
        'orm.data.upf': ['aiida.backends.tests.orm.data.upf'],
        'orm.entities': ['aiida.backends.tests.orm.entities'],
        'orm.groups': ['aiida.backends.tests.orm.groups'],
        'orm.logs': ['aiida.backends.tests.orm.logs'],
        'orm.mixins': ['aiida.backends.tests.orm.mixins'],
        'orm.node': ['aiida.backends.tests.orm.node.test_node'],
        'orm.utils.loaders': ['aiida.backends.tests.orm.utils.loaders'],
        'work.calcfunctions': ['aiida.backends.tests.work.test_calcfunctions'],
        'work.class_loader': ['aiida.backends.tests.work.class_loader'],
        'work.daemon': ['aiida.backends.tests.work.daemon'],
        'work.futures': ['aiida.backends.tests.work.test_futures'],
        'work.launch': ['aiida.backends.tests.work.test_launch'],
        'work.persistence': ['aiida.backends.tests.work.persistence'],
        'work.process': ['aiida.backends.tests.work.process'],
        'work.process_builder': ['aiida.backends.tests.work.test_process_builder'],
        'work.process_function': ['aiida.backends.tests.work.test_process_function'],
        'work.process_spec': ['aiida.backends.tests.work.test_process_spec'],
        'work.rmq': ['aiida.backends.tests.work.test_rmq'],
        'work.run': ['aiida.backends.tests.work.run'],
        'work.runners': ['aiida.backends.tests.work.test_runners'],
        'work.transport': ['aiida.backends.tests.work.test_transport'],
        'work.utils': ['aiida.backends.tests.work.test_utils'],
        'work.work_chain': ['aiida.backends.tests.work.work_chain'],
        'work.workfunctions': ['aiida.backends.tests.work.test_workfunctions'],
        'work.job_processes': ['aiida.backends.tests.work.job_processes'],
        'plugin_loader': ['aiida.backends.tests.test_plugin_loader'],
        'caching_config': ['aiida.backends.tests.test_caching_config'],
    }
}


def get_db_test_names():
    retlist = []
    for backend in db_test_list:
        for name in db_test_list[backend]:
            retlist.append(name)

    # This is a temporary solution to be able to run tests in plugins. Once the plugin fixtures
    # have been made working and are released, we can replace this logic with them
    for ep in [ep for ep in ENTRYPOINT_MANAGER.iter_entry_points(group='aiida.tests')]:
        retlist.append(ep.name)

    # Explode the list so that if I have a.b.c,
    # I can run it also just with 'a' or with 'a.b'
    final_list = [_ for _ in retlist]
    for k in retlist:
        if '.' in k:
            parts = k.split('.')
            for last_idx in range(1, len(parts)):
                parentkey = ".".join(parts[:last_idx])
                final_list.append(parentkey)

    # return the list of possible names, without duplicates
    return sorted(set(final_list))


def get_db_test_list():
    """
    This function returns the db_test_list for the current backend,
    merged with the 'common' tests.

    :note: This function should be called only after setting the
      backend, and then it returns only the tests for this backend, and the common ones.
    """
    from aiida.backends import settings
    from aiida.common.exceptions import ConfigurationError
    from collections import defaultdict

    current_backend = settings.BACKEND
    try:
        be_tests = db_test_list[current_backend]
    except KeyError:
        raise ConfigurationError("No backend configured yet")

    # Could be undefined, so put to empty dict by default
    try:
        common_tests = db_test_list["common"]
    except KeyError:
        raise ConfigurationError("A 'common' key must always be defined!")

    retdict = defaultdict(list)
    for k, tests in common_tests.items():
        for t in tests:
            retdict[k].append(t)
    for k, tests in be_tests.items():
        for t in tests:
            retdict[k].append(t)

    # This is a temporary solution to be able to run tests in plugins. Once the plugin fixtures
    # have been made working and are released, we can replace this logic with them
    for ep in [ep for ep in ENTRYPOINT_MANAGER.iter_entry_points(group='aiida.tests')]:
        retdict[ep.name].append(ep.module_name)

    # Explode the dictionary so that if I have a.b.c,
    # I can run it also just with 'a' or with 'a.b'
    final_retdict = defaultdict(list)
    for k, v in retdict.items():
        final_retdict[k] = v
    for k, v in retdict.items():
        if '.' in k:
            parts = k.split('.')
            for last_idx in range(1, len(parts)):
                parentkey = ".".join(parts[:last_idx])
                final_retdict[parentkey].extend(v)

    return dict(final_retdict)
