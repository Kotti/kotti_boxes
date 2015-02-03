def test_manager_registry_names():
    """ Default managers should be registered (name)"""
    from kotti_boxes.registry import box_manager_registry

    assert 'RightBoxManager' in box_manager_registry.get_component_names()
    assert 'LeftBoxManager' in box_manager_registry.get_component_names()
    assert 'AboveFooterBoxManager' in \
           box_manager_registry.get_component_names()


def test_box_registry_names():
    """ Default boxes should be registered (name)"""
    from kotti_boxes.registry import box_registry

    assert 'BannerBox' in box_registry.get_component_names()
    assert 'TextBox' in box_registry.get_component_names()


def test_manager_registry_names_count():
    """ Default boxes should be registered (unique list)"""
    from kotti_boxes.registry import box_manager_registry

    assert box_manager_registry.get_component_names().\
        count('RightBoxManager') == 1
    assert box_manager_registry.get_component_names().\
        count('LeftBoxManager') == 1


def test_common_registry_names_count():
    """ Default boxes should be registered (unique list)"""
    from kotti_boxes.registry import box_registry

    assert box_registry.get_component_names().count('BannerBox') == 1
    assert box_registry.get_component_names().count('TextBox') == 1


def test_manager_registry_dotted():
    """ Default managers should be registered (dotted)"""
    from kotti_boxes.registry import box_manager_registry

    assert 'kotti_boxes.resources.managers.RightBoxManager' in \
        box_manager_registry.get_dotted_components()
    assert 'kotti_boxes.resources.managers.LeftBoxManager' in \
        box_manager_registry.get_dotted_components()


def test_box_registry_dotted():
    """ Default managers should be registered (dotted)"""
    from kotti_boxes.registry import box_registry

    assert 'kotti_boxes.resources.boxes.banner.BannerBox' in \
        box_registry.get_dotted_components()
    assert 'kotti_boxes.resources.boxes.text.TextBox' in \
        box_registry.get_dotted_components()


def test_manager_registry_components():
    """ Default managers should be registered (components)"""
    from kotti_boxes.registry import box_manager_registry

    import kotti_boxes
    assert kotti_boxes.resources.RightBoxManager in \
        box_manager_registry.get_components()
    assert kotti_boxes.resources.LeftBoxManager in \
        box_manager_registry.get_components()


def test_box_registry_components():
    """ Default managers should be registered (components)"""
    from kotti_boxes.registry import box_registry

    import kotti_boxes
    assert kotti_boxes.resources.BannerBox in \
        box_registry.get_components()
    assert kotti_boxes.resources.TextBox in \
        box_registry.get_components()


def test_manager_register_component():
    """ Register a new component """
    from kotti_boxes.registry import box_manager_registry
    from kotti_boxes.interfaces import IBoxManager
    from kotti_boxes.resources import RightBoxManager
    from zope.interface import implements

    class FakeBoxManager:
        implements(IBoxManager)
        type_info = RightBoxManager.type_info.copy(
            name='FakeBoxManager',
            dotted_class='kotti_boxes.resources.FakeBoxManager',
            )

    assert FakeBoxManager not in box_manager_registry.get_components()

    box_manager_registry.register_component(FakeBoxManager)
    assert FakeBoxManager in box_manager_registry.get_components()
    assert 'FakeBoxManager' in box_manager_registry.get_component_names()


def test_box_register_component():
    """ Register a new component """
    from kotti_boxes.registry import box_registry
    from kotti_boxes.interfaces import IBox
    from kotti_boxes.resources import TextBox
    from zope.interface import implements

    class FakeBox:
        implements(IBox)
        type_info = TextBox.type_info.copy(
            name='FakeBox',
            addable_to=[],
            )

    assert FakeBox not in box_registry.get_components()

    box_registry.register_component(FakeBox)
    assert FakeBox in box_registry.get_components()
    assert 'FakeBox' in box_registry.get_component_names()
    assert 'RightBoxManager' in FakeBox.type_info.addable_to
