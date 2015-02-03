# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

from zope.interface import implements
from kotti.resources import Image
from kotti.interfaces import IImage
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode
from kotti_boxes.interfaces import IBannerBox
from kotti_boxes.interfaces import IBoxWorkflow


class BannerBox(Image):
    implements(IBoxWorkflow, IImage, IBannerBox)

    __tablename__ = 'banner_boxes'

    id = Column(Integer, ForeignKey('images.id'), primary_key=True)
    link = Column(Unicode(1000))

    type_info = Image.type_info.copy(
        name=u'BannerBox',
        title=u'BannerBox',
        add_view=u'add_banner_box',
        addable_to=[],  # updated at startup time
        )

    def __init__(self, link=u"", **kwargs):
        super(BannerBox, self).__init__(**kwargs)
        self.link = link
        self.in_navigation = False
