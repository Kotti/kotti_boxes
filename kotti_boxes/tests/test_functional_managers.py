# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""

from pytest import mark


def test_login_required_add_right(webtest, root):
    """ Add view requires login """
    resp = webtest.get('/add_box_manager_right')
    assert resp.status_code == 302


def test_login_required_add_left(webtest, root):
    """ Add view requires login """
    resp = webtest.get('/add_box_manager_left')
    assert resp.status_code == 302


@mark.user('admin')
def test_add_right_box(webtest, root):

    resp = webtest.get('/add_box_manager_right')

    # submit empty form
    form = resp.forms['deform']
    assert form['title'].value
    resp = form.submit('save')
    assert resp.status_code == 302
    resp = resp.follow()
    assert 'Item was added.' in resp.body


@mark.user('admin')
def test_add_left_box(webtest, root):

    resp = webtest.get('/add_box_manager_left')

    # submit empty form
    form = resp.forms['deform']
    assert form['title'].value
    resp = form.submit('save')
    assert resp.status_code == 302
    resp = resp.follow()
    assert 'Item was added.' in resp.body


@mark.user('admin')
def test_add_right_box_one_time(webtest, root):
    """ portlet manager can be added just one time """

    assert '/add_box_manager_right' in webtest.get('/').body

    resp = webtest.get('/add_box_manager_right')

    # submit empty form
    form = resp.forms['deform']
    assert form['title'].value
    resp = form.submit('save')
    assert resp.status_code == 302
    resp = resp.follow()
    assert 'Item was added.' in resp.body

    assert '/add_box_manager_right' not in webtest.get('/').body


@mark.user('admin')
def test_add_left_box_one_time(webtest, root):
    """ portlet manager can be added just one time """

    assert '/add_box_manager_left' in webtest.get('/').body

    resp = webtest.get('/add_box_manager_left')

    # submit empty form
    form = resp.forms['deform']
    assert form['title'].value
    resp = form.submit('save')
    assert resp.status_code == 302
    resp = resp.follow()
    assert 'Item was added.' in resp.body

    assert '/add_box_manager_left' not in webtest.get('/').body


@mark.user('admin')
def test_edit_right_box(webtest, root):
    """ Box managers should be editable"""

    from kotti_boxes.resources import RightBoxManager

    root['cc'] = RightBoxManager(title=u'Box Title')

    resp = webtest.get('/cc/@@edit')
    form = resp.forms['deform']
    assert form['title'].value == u'Box Title'
    form['title'] = u'Bazinga'
    resp = form.submit('save').maybe_follow()
    assert u'Your changes have been saved.' in resp.body
    assert u'Bazinga' in resp.body


@mark.user('admin')
def test_edit_left_box(webtest, root):
    """ Box managers should be editable"""

    from kotti_boxes.resources import RightBoxManager

    root['cc'] = RightBoxManager(title=u'Box Title')

    resp = webtest.get('/cc/@@edit')
    form = resp.forms['deform']
    assert form['title'].value == u'Box Title'
    form['title'] = u'Bazinga'
    resp = form.submit('save').maybe_follow()
    assert u'Your changes have been saved.' in resp.body
    assert u'Bazinga' in resp.body


@mark.user('admin')
def test_edit_right_default_view(webtest, root):
    """ standard default contents as default view (already tested) """

    from kotti_boxes.resources import RightBoxManager

    root['cc'] = RightBoxManager(title=u'Box Title')

    resp = webtest.get('/cc')
    assert 'No content items are contained here.' in resp.body


@mark.user('admin')
def test_edit_left_default_view(webtest, root):
    """ standard default contents as default view (already tested) """

    from kotti_boxes.resources import RightBoxManager

    root['cc'] = RightBoxManager(title=u'Box Title')

    resp = webtest.get('/cc')
    assert 'No content items are contained here.' in resp.body