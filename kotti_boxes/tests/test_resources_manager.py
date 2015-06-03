# -*- coding: utf-8 -*-

"""
Created on 2015-01-27
:author: Davide Moro (d.moro@truelab.eu)
"""


def test_add_rightboxmanager(root, db_session):
    from kotti_boxes.resources import RightBoxManager

    cc = RightBoxManager()

    root['cc'] = cc
    assert cc.name == 'cc'


def test_add_leftboxmanager(root, db_session):
    from kotti_boxes.resources import LeftBoxManager

    cc = LeftBoxManager()

    root['cc'] = cc
    assert cc.name == 'cc'


def test_custom_type_info(root, config):
    """ We test if our object type info is our custom
        implementation
    """
    from kotti_boxes.resources import RightBoxManager
    from kotti_boxes.resources import BoxManagerTypeInfo

    box = RightBoxManager()
    assert isinstance(box.type_info, BoxManagerTypeInfo)


def test_custom_type_info_copy(root, config):
    """ When you copy our custom type info you should
        obtain an instance of our custom class (and not
        the original TypeInfo class)
    """
    from kotti_boxes.resources import BoxManagerTypeInfo
    type_info = BoxManagerTypeInfo()
    assert isinstance(type_info, BoxManagerTypeInfo)

    copied_type_info = type_info.copy()
    assert isinstance(copied_type_info, BoxManagerTypeInfo)


def test_basebox_not_addable(root, db_session, config):
    """ The base box object should not be addable """
    from kotti.testing import DummyRequest
    from kotti_boxes.resources import BaseBoxManager

    config.include('kotti_boxes')
    box = BaseBoxManager()
    # base box is addable, ok
    assert not box.type_info.addable(root, DummyRequest())


def test_rightbox_addable_in_root_one_time(root, db_session, config):
    """ The rightbox object should be addable in root
        just one time
    """
    from kotti.testing import DummyRequest
    from kotti_boxes.resources import RightBoxManager

    config.include('kotti_boxes')
    box = RightBoxManager()
    # right box is addable, ok
    from kotti_boxes.views.edit import boxes
    from kotti_boxes.views.edit import managers
    config.include(managers)
    config.include(boxes)
    assert box.type_info.addable(root, DummyRequest())

    # ok, let's add it
    root['box'] = box

    # right box is no addable anymore (on root)
    another_box = RightBoxManager()
    assert not another_box.type_info.addable(root, DummyRequest())


def test_leftbox_addable_in_root_one_time(root, db_session, config):
    """ The leftbox object should be addable in root
        just one time
    """
    from kotti.testing import DummyRequest
    from kotti_boxes.resources import LeftBoxManager

    config.include('kotti_boxes')
    box = LeftBoxManager()

    from kotti_boxes.views.edit import boxes
    from kotti_boxes.views.edit import managers
    config.include(managers)
    config.include(boxes)
    # left box is addable, ok
    assert box.type_info.addable(root, DummyRequest())

    # ok, let's add it
    root['box'] = box

    # left box is no addable anymore (on root)
    another_box = LeftBoxManager()
    assert not another_box.type_info.addable(root, DummyRequest())
