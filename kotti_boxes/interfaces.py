from zope.interface import Interface
from kotti.interfaces import IDefaultWorkflow


class IBoxWorkflow(IDefaultWorkflow):
    """ Custom workflow for box related types """


class IBoxCommon(Interface):
    """ Base interface for box-related interfaces """


class IBoxManager(IBoxCommon):
    """ Marker interface """


class IBox(IBoxCommon):
    """ Marker interface for
        box elements addable to a
        box manager container
    """


class ITextBox(IBox):
    """ """


class IBannerBox(IBox):
    """ """


class IBaseRegistry(Interface):
    """ This is the base related box components registry.
        When you define a new box manager or box, you
        should register it calling the register.

       If you provide the kotti_boxes.managers and
       kotti_boxes.boxes settings, no need to use this
       registry. kotti_boxes will register your components
       for you.
    """

    def register_component(component):
        """ Adds a box component to the registry
            Accepts a class or a string like
            plugin.resource.Something)
        """

    def register_components(components):
        """ Adds a box component list to the registry.
            Accepts a list of classes or strings like
            plugin.resource.Something
        """

    def get_components():
        """ Returns a list of box component classes """

    def get_dotted_components():
        """ Returns a list of box component dotted
            strings (eg: 'kotti_your.resources.YourBox')
        """

    def get_component_names():
        """ Returns a list of box component names
            from type_info
        """


class IBoxManagerRegistry(IBaseRegistry):
    """ Box Manager registry"""


class IBoxRegistry(IBaseRegistry):
    """ Box registry """
