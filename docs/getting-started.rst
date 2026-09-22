Getting started
===============

You need **Python 3.11 or newer** and **Machinome 0.7 or newer**. Mechanics
is an optional package; installing the framework alone does not install it.

Install the released package
----------------------------

Machinome Mechanics 0.1.0 is released with Machinome 0.7.0. In a virtual
environment, the framework's ``mechanics`` extra installs both:

.. code-block:: console

   python -m venv .venv
   source .venv/bin/activate
   python -m pip install 'machinome[mechanics]'

On Windows, activate with ``.venv\Scripts\activate``. If Machinome is
already installed, ``pip install machinome-mechanics`` adds the helpers.
For the browser viewer as well, install ``'machinome[viewer,mechanics]'``.
The framework's `installation guide
<https://machinome.readthedocs.io/en/latest/start/install.html>`_ covers
CAD backend requirements and the viewer.

Build from source
-----------------

To work on the helpers themselves, clone both repositories and install
them editable together, so pip resolves the framework dependency from
your checkout:

.. code-block:: console

   git clone https://github.com/machinome/machinome.git
   git clone https://github.com/machinome/machinome-mechanics.git
   python -m pip install -e './machinome[mechanics]' -e ./machinome-mechanics

Calculate a pose
----------------

The distribution name has a hyphen, ``machinome-mechanics``. The Python
import uses an underscore, ``machinome_mechanics``. All helpers are
available from that package:

.. doctest::

   >>> from machinome_mechanics import screw_travel, screw_angle
   >>> lead = 4.0  # A four-start screw with a 1 mm pitch
   >>> screw_travel(90, lead)
   1.0
   >>> screw_angle(1, lead)
   90.0

Here the screw advances 1 mm relative to its nut for a quarter turn.
Lengths use the units you supply, and angles are always degrees. Read
:doc:`reference/screws` when converting this to a moving nut or a
left-hand thread, because the sign depends on what your machine moves.

Family imports are equivalent:

.. doctest::

   >>> from machinome_mechanics.screws import screw_travel
   >>> screw_travel(720, 4)
   8.0

Use a changing input
--------------------

A helper called with a symbolic input produces a deferred expression.
There is no second formula to write for animation. :doc:`using-with-machinome`
walks through a complete driver-to-piston relation and shows numeric and
symbolic use of the same helper.

Migrating earlier imports
-------------------------

Before 0.7 the framework's development versions carried these formulas
as ``machinome.mechanisms``. After installing mechanics, update the
import, keeping your arguments and conventions:

.. code-block:: python

   # Before: from machinome.mechanisms import delta_carriage
   from machinome_mechanics import delta_carriage

The framework does not re-export these functions, and solid-node 0.6 does
not satisfy this package's Machinome 0.7 dependency. The framework's
`upgrading guide
<https://machinome.readthedocs.io/en/latest/project/upgrading.html>`_
covers the rest of the rename.
