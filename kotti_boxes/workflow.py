from kotti_boxes.interfaces import IBoxWorkflow


def elector(context):
    return IBoxWorkflow.providedBy(context)
