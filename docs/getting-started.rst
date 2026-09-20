Getting started
===============

You need **Python 3.11 or newer** and **Machinome 0.7 or newer**. Mechanics
is an optional package; installing the framework alone does not install it.

Install the source version
--------------------------

Machinome Mechanics 0.1.0 and Machinome 0.7 are awaiting publication.
Until they are available on the package index, clone both repositories
and install them together in a virtual environment:

.. code-block:: console

   git clone https://github.com/machinome/machinome.git
   git clone https://github.com/machinome/machinome-mechanics.git
   python -m venv .venv
   source .venv/bin/activate
   python -m pip install -e './machinome[mechanics]' -e ./machinome-mechanics

On Windows, activate with ``.venv\Scripts\activate``. If you already have
the two checkouts, use their paths in the installation command. The
framework's `installation guide
<https://machinome.readthedocs.io/en/latest/quickstart.html>`_ covers CAD
backend requirements and the optional browser viewer.

Once both packages are published, a fresh installation will be:

.. code-block:: console

   python -m pip install 'machinome[mechanics]'

If Machinome is already installed, ``pip install machinome-mechanics``
will add the helpers. For a browser viewer as well, use
``pip install 'machinome[viewer,mechanics]'`` after publication.

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

The helpers were extracted from the unreleased
``machinome.mechanisms`` package. After installing mechanics, update the
import, keeping your arguments and conventions:

.. code-block:: python

   # Before: from machinome.mechanisms import delta_carriage
   from machinome_mechanics import delta_carriage

The earlier unpublished name ``solid_node_mechanics`` also becomes
``machinome_mechanics``. The framework does not re-export these functions.
The older solid-node 0.6 distribution does not satisfy this package's
Machinome 0.7 dependency.
