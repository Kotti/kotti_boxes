# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

from kotti.views.edit import ContentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from pyramid.view import view_config

from kotti_boxes import _
from kotti_boxes.resources import RightBoxManager
from kotti_boxes.resources import LeftBoxManager
from kotti_boxes.resources import AboveFooterBoxManager
from kotti_boxes.resources import AboveContentBoxManager
from kotti_boxes.resources import BelowContentBoxManager


class BoxManagerSchema(ContentSchema):
    """ Schema for BoxManager. """

    def after_bind(self, node, kw):
        del node['tags']
        del node['description']


class RightBoxManagerSchema(BoxManagerSchema):
    """ Schema for BoxManager. """

    def after_bind(self, node, kw):
        super(RightBoxManagerSchema, self).after_bind(node, kw)
        node['title'].default = _('RightBoxManager')


class LeftBoxManagerSchema(BoxManagerSchema):
    """ Schema for BoxManager. """

    def after_bind(self, node, kw):
        super(LeftBoxManagerSchema, self).after_bind(node, kw)
        node['title'].default = _('LeftBoxManager')


class AboveFooterBoxManagerSchema(BoxManagerSchema):
    """ Schema for BoxManager. """

    def after_bind(self, node, kw):
        super(AboveFooterBoxManagerSchema, self).after_bind(node, kw)
        node['title'].default = _('AboveFooterBoxManager')


class AboveContentBoxManagerSchema(BoxManagerSchema):
    """ Schema for BoxManager. """

    def after_bind(self, node, kw):
        super(AboveContentBoxManagerSchema, self).after_bind(node, kw)
        node['title'].default = _('AboveContentBoxManager')


class BelowContentBoxManagerSchema(BoxManagerSchema):
    """ Schema for BoxManager. """

    def after_bind(self, node, kw):
        super(BelowContentBoxManagerSchema, self).after_bind(node, kw)
        node['title'].default = _('BelowContentBoxManager')


@view_config(name=RightBoxManager.type_info.add_view, permission='add',
             renderer='kotti:templates/edit/node.pt')
class BoxManagerAddForm(AddFormView):
    """ Form to add a new instance of BoxManager. """

    schema_factory = RightBoxManagerSchema
    add = RightBoxManager
    item_type = _(u"RightBoxManager")


@view_config(name='edit', context=RightBoxManager, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class BoxManagerEditForm(EditFormView):
    """ Form to edit existing calendars. """

    schema_factory = RightBoxManagerSchema


@view_config(name=LeftBoxManager.type_info.add_view, permission='add',
             renderer='kotti:templates/edit/node.pt')
class LeftBoxManagerAddForm(AddFormView):
    """ Form to add a new instance of BoxManager. """

    schema_factory = LeftBoxManagerSchema
    add = LeftBoxManager
    item_type = _(u"LeftBoxManager")


@view_config(name='edit', context=LeftBoxManager, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class LeftBoxManagerEditForm(EditFormView):
    """ Form to edit existing calendars. """

    schema_factory = LeftBoxManagerSchema


@view_config(name=AboveFooterBoxManager.type_info.add_view, permission='add',
             renderer='kotti:templates/edit/node.pt')
class AboveFooterBoxManagerAddForm(AddFormView):
    """ Form to add a new instance of BoxManager. """

    schema_factory = AboveFooterBoxManagerSchema
    add = AboveFooterBoxManager
    item_type = _(u"AboveFooterBoxManager")


@view_config(name='edit', context=AboveFooterBoxManager, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class AboveFooterBoxManagerEditForm(EditFormView):
    """ Form to edit existing calendars. """

    schema_factory = AboveFooterBoxManagerSchema


@view_config(name=AboveContentBoxManager.type_info.add_view, permission='add',
             renderer='kotti:templates/edit/node.pt')
class AboveContentBoxManagerAddForm(AddFormView):
    """ Form to add a new instance of BoxManager. """

    schema_factory = AboveContentBoxManagerSchema
    add = AboveContentBoxManager
    item_type = _(u"AboveContentBoxManager")


@view_config(name='edit', context=AboveContentBoxManager, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class AboveContentBoxManagerEditForm(EditFormView):
    """ Form to edit existing calendars. """

    schema_factory = AboveContentBoxManagerSchema


@view_config(name=BelowContentBoxManager.type_info.add_view, permission='add',
             renderer='kotti:templates/edit/node.pt')
class BelowContentBoxManagerAddForm(AddFormView):
    """ Form to add a new instance of BoxManager. """

    schema_factory = BelowContentBoxManagerSchema
    add = BelowContentBoxManager
    item_type = _(u"BelowContentBoxManager")


@view_config(name='edit', context=BelowContentBoxManager, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class BelowContentBoxManagerEditForm(EditFormView):
    """ Form to edit existing calendars. """

    schema_factory = BelowContentBoxManagerSchema


def includeme(config):
    config.scan(__name__)
