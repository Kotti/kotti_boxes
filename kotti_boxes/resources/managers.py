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
