#! /usr/bin/env python

import os
import time
import logging
from cellmaps_utils import logutils
from cellmaps_utils.provenance import ProvenanceUtil
from aixport.basecmdtool import BaseCommandLineTool
import aixport.constants

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
        :param provenance_utils: Wrapper for `fairscape-cli <https://pypi.org/project/fairscape-cli>`__
                                 which is used for
                                 `RO-Crate <https://www.researchobject.org/ro-crate>`__ creation and population
        :type provenance_utils: :py:class:`~cellmaps_utils.provenance.ProvenanceUtil`
        """
        super().__init__(theargs,
                         provenance_utils=provenance_utils)
        logger.debug('In constructor')

    def train(self):
        """
        Runs train mode

        :return: exit code
        :rtype: int
        """
        logger.info('In train')
        return 0

    def optimizetrain(self):
        """
        Runs optimizetrain mode

        :return: exit code
        :rtype: int
        """
        logger.info('In optimizetrain')
        return 0

    def predict(self):
        """
        Runs predict/test mode

        :return: exit code
        :rtype: int
        """
        logger.info('In predict/test')
        return 0


    def run(self):
        """
        Entry point for {{ cookiecutter.project_name }}


        :return: exit code, 0 means success otherwise failure
        :rtype: int
        """
        exitcode = 99
        try:
            logger.debug('In run method')
            self._initialize_rocrate()

            if self._theargs['mode'] == aixport.constants.TRAIN_MODE:
                exitcode = self.train()
            elif self._theargs['mode'] == aixport.constants.OPTIMIZETRAIN_MODE:
                exitcode = self.optimizetrain()
            elif self._theargs['mode'] == aixport.constants.TEST_MODE or\
                self._theargs['mode'] == aixport.constants.PREDICT_MODE:
                 exitcode = self.predict()
            else:
                raise {{ cookiecutter.__error_class_name }}('Unsupported mode: ' +
                                                            str(self._theargs['mode']))
            return exitcode
        finally:
            self._write_task_finish_json(exitcode)
