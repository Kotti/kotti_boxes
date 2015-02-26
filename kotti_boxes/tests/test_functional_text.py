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


def test_login_required_add_text(webtest, root):
    """ Add view requires login """
    resp = webtest.get('/add_text_box')
    assert resp.status_code == 302


def test_login_required_add_left(webtest, dummy_manager):
    """ Add view requires login """
    resp = webtest.get('/right/add_text_box')
    assert resp.status_code == 302


@mark.user('admin')
def test_add_right_box(webtest, dummy_manager):

    resp = webtest.get('/right/add_text_box')

    # submit empty form
    form = resp.forms['deform']
    form['title'] = u'new box'
    resp = form.submit('save')
    assert resp.status_code == 302
    resp = resp.follow()
    assert 'Item was added.' in resp.body


@mark.user('admin')
def test_add_right_box2(webtest, dummy_manager, root):
    """ We should check if the added item is an instance
        of TextBox instead of Document
    """

    resp = webtest.get('/right/add_text_box')

    # submit empty form
    form = resp.forms['deform']
    form['title'] = u'new box'
    resp = form.submit('save')
    assert resp.status_code == 302
    resp = resp.follow()
    assert 'Item was added.' in resp.body

    # Content added, let's check if it isn't a document
    # instance (it should be a TextBoxInstance)
    from kotti_boxes.resources import TextBox
    assert isinstance(root['right']['new-box'], TextBox)


@mark.user('admin')
def test_edit_box(webtest, dummy_manager):
    """ Box should be editable"""

    from kotti_boxes.resources import TextBox

    dummy_manager['cc'] = TextBox(title=u'Box Title')

    resp = webtest.get('/right/cc/@@edit')
    form = resp.forms['deform']
    assert form['title'].value == u'Box Title'
    form['title'] = u'Bazinga'
    form['description'] = u'This is the description'
    form['body'] = u'This is the text'
    resp = form.submit('save').maybe_follow()
    assert u'Your changes have been saved.' in resp.body
    assert u'Bazinga' in resp.body
    assert u'This is the description' in resp.body
    assert u'This is the text' in resp.body
