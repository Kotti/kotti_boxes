# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

import colander
from deform.widget import RichTextWidget
from kotti.views.edit import DocumentSchema
from kotti.views.edit.content import DocumentEditForm
from kotti.views.edit.content import DocumentAddForm
from pyramid.view import view_config

from kotti_boxes import _
from kotti_boxes.resources import TextBox
from kotti_boxes.interfaces import ITextBox


class TextBoxSchema(DocumentSchema):

    body = colander.SchemaNode(
        colander.String(),
        title=_(u'Body'),
        widget=RichTextWidget(
            # theme='advanced', width=790, height=500
            height=500
        ),
        missing=u"",
        )

    def after_bind(self, node, kw):
        del node['tags']


@view_config(name='edit', permission='edit',
             context=ITextBox,
             renderer='kotti:templates/edit/node.pt')
class TextBoxEditForm(DocumentEditForm):
    schema_factory = TextBoxSchema


@view_config(name=TextBox.type_info.add_view, permission='add',
             renderer='kotti:templates/edit/node.pt')
class TextBoxAddForm(DocumentAddForm):
    item_type = _(u"Text Box")
    item_class = TextBox
    schema_factory = TextBoxSchema
