# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

pytest_plugins = "kotti"

from pytest import fixture


@fixture(scope='session')
def custom_settings():
    import kotti_boxes.resources
    kotti_boxes.resources  # make pyflakes happy
    return {
        'kotti.configurators': 'kotti_tinymce.kotti_configure '
                               'kotti_boxes.kotti_configure',
        'kotti_boxes.managers': 'kotti_boxes.resources.RightBoxManager '
                                'kotti_boxes.resources.LeftBoxManager '
                                'kotti_boxes.resources.AboveFooterBoxManager ',
        'kotti_boxes.boxes': 'kotti_boxes.resources.BannerBox '
                             'kotti_boxes.resources.TextBox',
        'kotti.use_workflow': 'kotti:workflow.zcml',
        'kotti_boxes.use_workflow': 'kotti_boxes:workflow.zcml',
        }
