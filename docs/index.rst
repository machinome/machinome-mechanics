Machinome Mechanics
===================

**Mechanics helpers for the Machinome framework.**

Turn a gear and find its neighbour's angle. Rotate a lead screw and find
its travel. Move a delta printer's effector and find the carriage heights.
Machinome Mechanics supplies the formulas that connect those movements.

The package provides small Python functions for gears, screws, rolling travel,
slider-cranks, linear deltas and planar linkages. Use them to calculate a
single pose, or put them inside a `Machinome relation law
<https://machinome.readthedocs.io/en/latest/concepts/relations.html>`_ so the same
formula follows a driver through an animation. Numeric and symbolic inputs
share one definition through ``machinome.math``.

Your project supplies dimensions, coordinate frames and assembly geometry.
Machinome supplies the machine model and motion evaluation. Mechanics
supplies reusable kinematic relationships between them.

.. doctest::

   >>> from machinome_mechanics import screw_travel, piston_height, meshed_angle
   >>> screw_travel(360, 2)     # One turn of a 2 mm lead screw
   2.0
   >>> piston_height(0, 15, 60) # Piston at top dead centre, in mm
   75.0
   >>> meshed_angle(0, 12, 24, driver_gap=15)
   172.5

Start with :doc:`getting-started`, learn the :doc:`conventions`, or go
straight to the :doc:`helper reference <reference/index>`.

.. note::

   This manual describes Machinome Mechanics **0.1.0**, released on
   23 September 2026 with Machinome 0.7.0 and requiring Machinome 0.7 or
   newer. :doc:`getting-started` installs both packages at once.

Find the formula you need
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Mechanism
     - What you can calculate
   * - :doc:`Gears <reference/gears>`
     - External registration, internal mesh increments and cycloidal ratios.
   * - :doc:`Lead screws <reference/screws>`
     - Linear travel from rotation, or the rotation needed for a travel.
   * - :doc:`Slider-cranks <reference/cranks>`
     - Crank-pin position, connecting-rod angle and piston height.
   * - :doc:`Cam followers <reference/cams>`
     - Periodic half-cosine lift, return and base dwell.
   * - :doc:`Indexed advance <reference/indexing>`
     - Signed completed-turn accumulation around a mechanical stroke.
   * - :doc:`Linear deltas <reference/deltas>`
     - Carriage heights and rod orientations for an effector position.
   * - :doc:`Linkages <reference/linkages>`
     - Circle/triangle geometry, link rise, two-link angles and four-bar poses.
   * - :doc:`Rolling motion <reference/rolling>`
     - Rack, belt or drum travel from rotation, and its inverse.
   * - :doc:`Belt geometry <reference/belts>`
     - Pulley pitch radius, tangent contacts, closed path metrics and contact-referenced angle.

These helpers describe geometry and movement. They do not generate gear
teeth or threads, solve forces, or check collisions. Use the `Machinome
manual <https://machinome.readthedocs.io/en/latest/>`_ for building,
operating and testing the resulting machine.

.. toctree::
   :maxdepth: 1
   :caption: Getting started

   getting-started
   conventions
   using-with-machinome

.. toctree::
   :maxdepth: 2
   :caption: Helper reference

   reference/index

.. toctree::
   :maxdepth: 1
   :caption: Project

   Machinome framework <https://machinome.readthedocs.io/en/latest/>
   Source code <https://github.com/machinome/machinome-mechanics>

Machinome Mechanics is licensed under Apache-2.0.
