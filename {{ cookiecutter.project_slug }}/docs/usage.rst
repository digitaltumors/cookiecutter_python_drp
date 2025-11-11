=====
Usage
=====

This page should provide information on how to use {{ cookiecutter.project_slug }}

In a project
--------------

To use {{ cookiecutter.project_name }} in a project:

.. code-block:: python

    from {{ cookiecutter.project_slug }}.runner import {{ cookiecutter.__runner_class_name }}

    # assumes /tmp/inputcrate directory is a training RO-Crate and
    # /tmp directory exists and is writeable
    mymodel = {{ cookiecutter.__runner_class_name }}({'mode': 'train', 'outdir': '/tmp/foo', 'input_crate': '/tmp/inputcrate'})

    # run the train and print exit code
    print(mymodel.run())

On the command line
---------------------

For information invoke :code:`{{ cookiecutter.__runner_name }}.py -h`

**Example usage**

.. code-block:: console

    {{ cookiecutter.__runner_name }}.py <OUTPUT> --mode <MODE> --input_crate <TRAIN RO-CRATE> --config_file <CONFIG FILE>

``<OUTPUT>``
    Destination directory where output is written asn RO-Crate

``--mode {train, test, predict, optimizetrain}``
    Selects the execution flow. ``train`` is responsible for training the model,
    ``test`` and ``predict`` are synonyms and are responsible for making prediction.
    ``optimizetrain`` triggers hyperparameter optimization prior to training.

``--input_crate`` ``</path/to/input_rocrate>``
    Absolute or relative path to the input RO-Crate.  For ``train`` and
    ``optimizetrain`` this is a training crate; for ``test``/``predict`` it is
    a testing crate.  The flag name is fixed to ``--input_crate`` so the
    benchmark launcher can invoke all models uniformly.

``--model`` ``</path/to/trained_model_rocrate>``
    Path to a trained model RO-Crate. Used by ``test``/``predict`` modes.
    The RO-Crate MUST contain:

    - a model (``model.pkl``, ``model.pt``, or similar)
    - a ``config.yml`` file capturing the hyperparameters used to produce the
      model


    ``--model`` is mandatory for ``test``/``predict`` and optional for
    ``train``/``optimizetrain`` when training from scratch.

``--config_file`` ``</path/to/configuration>``
    Path to an algorithm-specific configuration file. Implementations
    MAY ignore the flag when they do not support external configuration and
    MUST preserve existing defaults when the flag is omitted.


Via Docker
---------------

**Example usage**

**TODO:** Add information about example usage


.. code-block::

   Coming soon ...


