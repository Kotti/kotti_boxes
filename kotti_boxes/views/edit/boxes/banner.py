# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

import colander
from deform import FileData
from deform.widget import FileUploadWidget
from kotti.views.edit import ContentSchema
from kotti.views.edit.content import ImageEditForm
from kotti.views.edit.content import ImageAddForm
from kotti.views.form import validate_file_size_limit
from kotti.views.form import FileUploadTempStore
from kotti.views.form import AddFormView
from pyramid.view import view_config

from kotti_boxes import _
from kotti_boxes.resources import BannerBox
from kotti_boxes.validators import link_validator


def BannerBoxSchema(tmpstore):
    """ File schema with no set title missing binding """
    class BannerBoxSchema(ContentSchema):
        file = colander.SchemaNode(
            FileData(),
            title=_(u'File'),
            widget=FileUploadWidget(tmpstore),
            validator=validate_file_size_limit,
            )
        link = colander.SchemaNode(
            colander.String(),
            title=_('Link'),
            validator=link_validator,
            missing=u'',
            )

    def after_bind(node, kw):
        del node['tags']

    return BannerBoxSchema(after_bind=after_bind)


@view_config(name='edit', permission='edit',
             context=BannerBox,
             renderer='kotti:templates/edit/node.pt')
class BannerBoxEditForm(ImageEditForm):
    def schema_factory(self):
        tmpstore = FileUploadTempStore(self.request)
        return BannerBoxSchema(tmpstore)


@view_config(name=BannerBox.type_info.add_view, permission='add',
             renderer='kotti:templates/edit/node.pt')
class BannerBoxAddForm(ImageAddForm):
    item_type = _(u"Banner Box")
    item_class = BannerBox

    def schema_factory(self):
        tmpstore = FileUploadTempStore(self.request)
        return BannerBoxSchema(tmpstore)

    def save_success(self, appstruct):
        # overried this method (no filename as title
        # like images)
        return AddFormView.save_success(self, appstruct)

    def add(self, **appstruct):
        # override (no tags in our form)
        buf = appstruct['file']['fp'].read()
        filename = appstruct['file']['filename']
        return self.item_class(
            title=appstruct['title'] or filename,
            description=appstruct['description'],
            data=buf,
            filename=filename,
            link=appstruct.get('link', u''),
            mimetype=appstruct['file']['mimetype'],
            size=len(buf),
            )
