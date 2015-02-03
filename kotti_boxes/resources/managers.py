# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from kotti_boxes.resources import BaseBoxManager


class RightBoxManager(BaseBoxManager):
    """ """

    id = Column(Integer, ForeignKey('base_box_managers.id'), primary_key=True)

    type_info = BaseBoxManager.type_info.copy(
        name=u'RightBoxManager',
        title=u'RightBoxManager',
        add_view=u'add_box_manager_right',
        dotted_class='kotti_boxes.resources.RightBoxManager',
        )


class LeftBoxManager(BaseBoxManager):
    """ """

    id = Column(Integer, ForeignKey('base_box_managers.id'), primary_key=True)

    type_info = BaseBoxManager.type_info.copy(
        name=u'LeftBoxManager',
        title=u'LeftBoxManager',
        add_view=u'add_box_manager_left',
        dotted_class='kotti_boxes.resources.LeftBoxManager',
        )


class AboveFooterBoxManager(BaseBoxManager):
    """ """

    id = Column(Integer, ForeignKey('base_box_managers.id'), primary_key=True)

    type_info = BaseBoxManager.type_info.copy(
        name=u'AboveFooterBoxManager',
        title=u'AboveFooterBoxManager',
        add_view=u'add_box_manager_above_footer',
        dotted_class='kotti_boxes.resources.AboveFooterBoxManager',
        )


class AboveContentBoxManager(BaseBoxManager):
    """ """

    id = Column(Integer, ForeignKey('base_box_managers.id'), primary_key=True)

    type_info = BaseBoxManager.type_info.copy(
        name=u'AboveContentBoxManager',
        title=u'AboveContentBoxManager',
        add_view=u'add_box_manager_above_content',
        dotted_class='kotti_boxes.resources.AboveContentBoxManager',
        )


class BelowContentBoxManager(BaseBoxManager):
    """ """

    id = Column(Integer, ForeignKey('base_box_managers.id'), primary_key=True)

    type_info = BaseBoxManager.type_info.copy(
        name=u'BelowContentBoxManager',
        title=u'BelowContentBoxManager',
        add_view=u'add_box_manager_below_content',
        dotted_class='kotti_boxes.resources.BelowContentBoxManager',
        )
