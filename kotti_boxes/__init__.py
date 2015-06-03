# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

from pyramid.i18n import TranslationStringFactory
from kotti import FALSE_VALUES
from kotti_boxes.registry import box_manager_registry
from kotti_boxes.registry import box_registry
from kotti_boxes.util import get_managers
from kotti_boxes.util import get_boxes

_ = TranslationStringFactory('kotti_boxes')


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                kotti_boxes.kotti_configure

        to enable the ``kotti_boxes`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' '.join((
        ' kotti_boxes',
        ' kotti_boxes.views.edit.boxes',
        ' kotti_boxes.views.edit.managers',))

    # register addable types
    managers = get_managers(settings)
    boxes = get_boxes(settings)
    addable_types = managers + boxes
    addable_types_string = ''.join([' %s' % item for item in addable_types])
    settings['kotti.available_types'] += addable_types_string

    if not settings.get('kotti_boxes', None):
        settings['kotti_boxes.use_workflow'] = 'kotti_boxes:workflow.zcml'

    settings['kotti.fanstatic.view_needed'] += \
        ' kotti_boxes.fanstatic.css_and_js'


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    # register managers
    managers = get_managers(config.registry.settings)
    box_manager_registry.register_components(managers)
    # register boxes (updates addable_to)
    boxes = get_boxes(config.registry.settings)
    box_registry.register_components(boxes)

    workflow = config.registry.settings.get('kotti_boxes.use_workflow', None)
    if workflow and workflow.lower() not in FALSE_VALUES:
        config.begin()

        config.hook_zca()
        config.include('pyramid_zcml')
        config.load_zcml(workflow)
        config.commit()

    # translations
    config.add_translation_dirs('kotti_boxes:locale')

    # add static view
    config.add_static_view('static-kotti_boxes', 'kotti_boxes:static')

    # we want to provide the standard @@contents view as default view
    # for our box managers
    from kotti_boxes.resources import BaseBoxManager
    config.add_view('kotti.views.edit.actions.contents',
                    name=u'view',
                    context=BaseBoxManager,
                    permission=u'view',
                    renderer='kotti:templates/edit/contents.pt',
                    )
