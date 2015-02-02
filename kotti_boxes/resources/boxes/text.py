# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

from zope.interface import implements
from kotti.resources import Document
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from kotti_boxes.interfaces import ITextBox
from kotti_boxes.interfaces import IBoxWorkflow


class TextBox(Document):
    implements(IBoxWorkflow, ITextBox)

    __tablename__ = 'text_boxes'

    id = Column(Integer, ForeignKey('documents.id'), primary_key=True)

    type_info = Document.type_info.copy(
        name=u'TextBox',
        title=u'TextBox',
        add_view=u'add_text_box',
        addable_to=[]  # updated at startup time
        )
