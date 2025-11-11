#! /usr/bin/env python

import argparse
import sys
import logging
import logging.config
from cellmaps_utils import logutils
from cellmaps_utils import constants
import aixport.constants

import {{ cookiecutter.project_slug }}
from {{ cookiecutter.project_slug }}.runner import {{ cookiecutter.__runner_class_name }}

logger = logging.getLogger(__name__)


def _parse_arguments(desc, args):
    """
    Parses command line arguments

    :param desc: description to display on command line
    :type desc: str
    :param args: command line arguments usually :py:func:`sys.argv[1:]`
    :type args: list
    :return: arguments parsed by :py:mod:`argparse`
    :rtype: :py:class:`argparse.Namespace`
    """
    parser = argparse.ArgumentParser(description=desc,
                                     formatter_class=constants.ArgParseFormatter)
    parser.add_argument('outdir',
                        help='Directory to write results to as an RO-Crate')
    # RO-Crate input directory (optional to satisfy unit tests;
    # validated at runtime)
    parser.add_argument('--input_rocrate', '--input_crate',
                        required=False, default=None,
                        help='Absolute or relative path to the input RO-Crate. '
                             'For ' + aixport.constants.TRAIN_MODE + ' and ' +
                             aixport.constants.OPTIMIZETRAIN_MODE + ' this is a training '
                             'crate; for ' + aixport.constants.TEST_MODE +
                             '/' + aixport.constants.PREDICT_MODE +
                             ' it is a testing crate. '
                             'The flag name is fixed to --input_crate so the '
                             'benchmark launcher can invoke all models '
                             'uniformly')
    parser.add_argument('--mode', default='test', choices=[
                        aixport.constants.TRAIN_MODE,
                        aixport.constants.TEST_MODE,
                        aixport.constants.PREDICT_MODE,
                        aixport.constants.OPTIMIZETRAIN_MODE],
                        help='Selects the execution flow. ' +
                             aixport.constants.TRAIN_MODE +
                             ' is responsible '
                             'for training the model, ' +
                             aixport.constants.TEST_MODE +
                             '/' + aixport.constants.PREDICT_MODE + ' are '
                             'synonyms and are responsible for making '
                             'prediction. ' +
                             aixport.constants.OPTIMIZETRAIN_MODE +
                             ' triggers hyperparameter optimization prior to '
                             'training')
    parser.add_argument('--model', help="Path to model file or model RO-Crate")
    parser.add_argument('--config_file',
                        help='Path to an algorithm-specific configuration file. '
                             'Implementations MAY ignore the flag when they do not '
                             'support external configuration and MUST preserve '
                             'existing defaults when the flag is omitted')
    parser.add_argument('--logconf', default=None,
                        help='Path to python logging configuration file in '
                             'this format: https://docs.python.org/3/library/'
                             'logging.config.html#logging-config-fileformat '
                             'Setting this overrides -v parameter which uses '
                             ' default logger. (default None)')
    parser.add_argument('--skip_logging', action='store_true',
                        help='If set, output.log, error.log '
                             'files will not be created')
    parser.add_argument('--verbose', '-v', action='count', default=1,
                        help='Increases verbosity of logger to standard '
                             'error for log messages in this module. Messages are '
                             'output at these python logging levels '
                             '-v = WARNING, -vv = INFO, '
                             '-vvv = DEBUG, -vvvv = NOTSET (default ERROR '
                             'logging)')
    parser.add_argument('--version', action='version',
                        version=('%(prog)s ' +
                                 {{ cookiecutter.project_slug }}.__version__))

    return parser.parse_args(args)


def main(args):
    """
    Main entry point for program

    :param args: arguments passed to command line usually :py:func:`sys.argv[1:]`
    :type args: list

    :return: return value of :py:meth:`{{ cookiecutter.project_slug }}.runner.{{ cookiecutter.__runner_class_name }}.run`
             or ``2`` if an exception is raised
    :rtype: int
    """
    desc = """
    Version {version}

    Invokes run() method on {{ cookiecutter.__runner_class_name }}

    """.format(version={{ cookiecutter.project_slug }}.__version__)
    theargs = _parse_arguments(desc, args[1:])
    theargs.program = args[0]
    theargs.version = {{ cookiecutter.project_slug }}.__version__

    try:
        logutils.setup_cmd_logging(theargs)
        return {{ cookiecutter.__runner_class_name }}(vars(theargs)).run()
    except Exception as e:
        logger.exception('Caught exception: ' + str(e))
        return 2
    finally:
        logging.shutdown()


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main(sys.argv))
