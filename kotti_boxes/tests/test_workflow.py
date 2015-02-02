def test_workflow_elector_document():
    from kotti_boxes.workflow import elector
    from kotti.resources import Document
    assert elector(Document()) is False


def test_workflow_elector_manager():
    from kotti_boxes.workflow import elector
    from kotti_boxes.resources import RightBoxManager
    assert elector(RightBoxManager()) is True


def test_workflow_elector_box():
    from kotti_boxes.workflow import elector
    from kotti_boxes.resources import TextBox
    assert elector(TextBox()) is True


def test_workflow_permission(config):
    from repoze.workflow import get_workflow
    from kotti_boxes.resources import TextBox

    config.include('pyramid_zcml')
    config.include('kotti_boxes')
    context = TextBox()
    wf = get_workflow(context, 'security', context=context)
    assert wf.__dict__['_state_data']['public']['system.Everyone'] == \
        u'viewbox'
