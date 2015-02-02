# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

from pyramid.util import DottedNameResolver
from kotti import DBSession
from kotti.resources import Content
from kotti.resources import TypeInfo
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from zope.interface import implements

from kotti_boxes.interfaces import IBoxManager
from kotti_boxes.interfaces import IBoxWorkflow


class BoxManagerTypeInfo(TypeInfo):

    def addable(self, context, request):
        resolver = DottedNameResolver()
        if hasattr(self, 'dotted_class'):
            resource_class = resolver.maybe_resolve(self.dotted_class)

            if resource_class:
                already_exists_box = DBSession.query(resource_class).\
                    filter(resource_class.parent_id == context.id).first()
                if already_exists_box is not None:
                    return False
            else:
                return False
        else:
            return False

        return super(BoxManagerTypeInfo, self).addable(context, request)

    def copy(self, **kwargs):
        """

        :result: a copy of the current TypeInfo instance
        :rtype: :class:`~kotti.resources.TypeInfo`
        """

        d = self.__dict__.copy()
        d.update(kwargs)
        # the parent's .copy don't preserve the addable method
        # (it returns the original TypeInfo class)
        return self.__class__(**d)

data = dict(addable_to=[u'Document'],)
box_manager_type_info_data = Content.type_info.copy(
    **data
    ).__dict__.copy()
box_manager_type_info = BoxManagerTypeInfo(**box_manager_type_info_data)


class BaseBoxManager(Content):
    """ """
    implements(IBoxWorkflow, IBoxManager)

    id = Column(Integer, ForeignKey('contents.id'), primary_key=True)

    type_info = box_manager_type_info
