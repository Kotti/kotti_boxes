kotti_boxes
***********

This is a backend only extension that allows to add one or more
box manager groups.

It provides Right and Left BoxManager types, you can add just one
instance of the same type to the current node (it won't be possible
to add two instances of right box manager on the same node).

A subnode will inherit block managers from its ancestors. If on a 
particular subsection you want to disable a block or view other
boxes you can create a new instance of BoxManager (leave it empty
if you want to leave the area empty)

We want to keep things simple, so we avoid to add other block
inheritance options like Plone.

This is a box management plugin for Kotti developed by Truelab.
You can add one or more "box managers" in your sections. There are 
several types of box managers:

* left
* right
* other positions will be added in next releases

Depending on the type of the manager, boxes will displayed on the left, right side
and so on.

In this release you can add just one type of box manager in one folder (eg:
only a left instance on a particular node /mysection). Probably in next 
releases we can avoid this constraint and let the users to group boxes into
different box managers, inherit box managers from the ancestor nodes and override
or hide just one box manager.

Box managers are folderish objects that will contain box items. You can add
several box object types in your managers, for example:

* banner box, a box with title, description and and image field. It will display
  the given image in the assigned slot. Title and description will be used to 
  decorate the image html attributes

* text box, a box with title, description and a rich text field. In next releases
  we'll add more metadata fields like show_border and show_title. This box
  will display the text provided in the rich text field

* other box types will be added in next releases (configurable dynamic queries, tags, 
  configurable navigation boxes and so on)

Workflows. It provides a custom workflow for box types with the following states:

* private. The box won't be displayed

* public. The box data will displayed the instance box resource url will be
  visible just for users with a role >= viewer.
  When the box state is public, the view named portlet will be used to fill
  the kotti's right, left side or other managed slots (to be implemented).

Boxes and box managers are regular content types. This choice has advantages and
disavantages.

In next releases boxes and box managers will be inherited by parent nodes (or 
not inherited using a boolean control).

Advantages:

* regular content types allowed me to speed up the development of this prototype

* easy way to create new box and box managers

* you can copy and paste single box or box manager instances

* workflow, you can decide to show a box instance **only** to users with
  a particular role

* add permissions and security in general, you can delegate the box management
  using the standard sharing view

* you can add more than one custom view to your box instances

Disadvantages:

* box instances should not be searchable

* box instances should not be added shown in folder contents view. We can add
  a new management link manage boxes (a customized folder content view) and a 
  menu with the active box managers on the current node

* box managers will be placed as persistent items in the node hierarchy used for
  regular contents

* box managers and box instances should be not be accessible by non box manager
  users.

This plugin is under heavy development and it provides only the model definitions
and tests. No inheritance or front-end work on Kotti side. At this moment we are
using Kotti just as a backend content manager and data persisted on the database
will be shown to the end users by another component with other integrations.

Probably this package will be rebranded under kotti_boxes.


|build status|_

`Find out more about Kotti`_

Development happens at https://github.com/truelab/kotti_boxes

.. |build status| image:: https://secure.travis-ci.org/truelab/kotti_boxes.png?branch=master
.. _build status: http://travis-ci.org/truelab/kotti_boxes
.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti

Setup
=====

To enable the extension in your Kotti site, activate the configurator::

    kotti.configurators =
        kotti_boxes.kotti_configure

    kotti_boxes.managers =
        kotti_boxes.resources.RightBoxManager
        kotti_boxes.resources.LeftBoxManager

    kotti_boxes.boxes =
        kotti_boxes.resources.BannerBox
        kotti_boxes.resources.TextBox

Database upgrade
================

If you are upgrading from a previous version you might have to migrate your
database.  The migration is performed with `alembic`_ and Kotti's console script
``kotti-migrate``. To migrate, run
``kotti-migrate upgrade_all --scripts=kotti_boxes:alembic``.

For integration of alembic in your environment please refer to the
`alembic documentation`_. If you have problems with the upgrade,
please create a new issue in the `tracker`_.

Development
===========

Contributions to kotti_boxes are highly welcome.
Just clone its `Github repository`_ and submit your contributions as pull requests.

.. _alembic: http://pypi.python.org/pypi/alembic
.. _alembic documentation: http://alembic.readthedocs.org/en/latest/index.html
.. _tracker: https://github.com/davidemoro/kotti_boxes/issues
.. _Github repository: https://github.com/davidemoro/kotti_boxes
