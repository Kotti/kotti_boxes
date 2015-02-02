# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""


def test_add_text(root, db_session):
    from kotti_boxes.resources import RightBoxManager

    cc = RightBoxManager()

    root['cc'] = cc

    from kotti_boxes.resources import TextBox
    text = TextBox()
    cc['text'] = text
    assert cc['text'].name == 'text'


def test_base_not_addable_in_root(root, db_session, config):
    """ The base box object should not be addable """
    from kotti.testing import DummyRequest
    from kotti_boxes.resources import TextBox

    config.include('kotti_boxes')
    box = TextBox()
    # box is addable, ok
    assert not box.type_info.addable(root, DummyRequest())
