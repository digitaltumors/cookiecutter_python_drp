#! /usr/bin/env python

import os
import time
import logging
from cellmaps_utils import logutils
from cellmaps_utils.provenance import ProvenanceUtil
from aixport.basecmdtool import BaseCommandLineTool

from {{ cookiecutter.project_slug }}.exceptions import {{ cookiecutter.__error_class_name }}

import {{ cookiecutter.project_slug }}

logger = logging.getLogger(__name__)


class {{ cookiecutter.__runner_class_name }}(BaseCommandLineTool):
    """
    Class to run algorithm
    """
    def __init__(self, theargs, provenance_utils=None):
        """
        Constructor

        :param theargs: Arguments for constructor
        :type theargs: dict
        :param skip_logging: If ``True`` skip logging, if ``None`` or ``False`` do NOT skip logging
        :type skip_logging: bool
        :param exitcode: value to return via :py:meth:`.{{ cookiecutter.__runner_class_name }}.run` method
        :type int:
        :param input_data_dict: Command line arguments used to invoke this
        :type input_data_dict: dict
        :param provenance_utils: Wrapper for `fairscape-cli <https://pypi.org/project/fairscape-cli>`__
                                 which is used for
                                 `RO-Crate <https://www.researchobject.org/ro-crate>`__ creation and population
        :type provenance_utils: :py:class:`~cellmaps_utils.provenance.ProvenanceUtil`
        """
        super().__init__(theargs,
                         provenance_utils=provenance_utils)
        logger.debug('In constructor')

    def run(self):
        """
        Runs {{ cookiecutter.project_name }}


        :return:
        """
        exitcode = 99
        try:
            logger.debug('In run method')
            self._initialize_rocrate()

            # Perform processing here

            # set exit code to value passed in via constructor
            exitcode = self._theargs['exitcode']
            return exitcode
        finally:
            self._write_task_finish(exitcode)
