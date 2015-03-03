# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

from pytest import mark
from pytest import fixture


@fixture
def dummy_manager(root):

    from kotti_boxes.resources import RightBoxManager

    root['right'] = cc = RightBoxManager()

    return cc


@mark.user('admin')
def test_edit_box(webtest, dummy_manager):
    """ Box should be editable"""

    from kotti_boxes.resources import BannerBox

    dummy_manager['cc'] = BannerBox(title=u'Box Title',
                                    link=u'http://google.it')

    resp = webtest.get('/right/cc/@@edit')
    form = resp.forms['deform']
    assert form['link'].value == u'http://google.it'
