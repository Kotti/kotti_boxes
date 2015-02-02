from pyramid.view import view_config
from kotti_boxes.interfaces import IBox


@view_config(context=IBox, name='portlet', permission='viewbox',
             renderer='kotti_boxes:views/templates/box.pt')
def banner_view(context):
    return {}
