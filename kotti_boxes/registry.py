import inspect
from zope.interface import implements
from pyramid.util import DottedNameResolver
from kotti_boxes.interfaces import IBoxManagerRegistry
from kotti_boxes.interfaces import IBoxRegistry


class BaseBoxRegistry(object):

    def __init__(self):
        self.components = []

    def _convert_component(self, component):
        """ Return the component class """
        if inspect.isclass(component):
            return component
        else:
            resolver = DottedNameResolver()
            return resolver.resolve(component)

    def register_components(self, components):
        for component in components:
            self.register_component(component)

    def get_components(self):
        return self.components

    def get_dotted_components(self):
        return ["%s.%s" % (item.__module__,
                           item.__name__) for item in self.get_components()]

    def get_component_names(self):
        return [item.type_info.name for item in self.get_components()]

    def register_component(self, component):
        component_class = self._convert_component(component)
        if component_class not in self.components:
            self.components.append(component_class)


class BoxManagerRegistry(BaseBoxRegistry):
    """ This is the box manager registry.
        When you define a new box manager, you
        should register it calling the register.

        See interfaces.py for further details.
    """
    implements(IBoxManagerRegistry)

box_manager_registry = BoxManagerRegistry()


class BoxRegistry(BaseBoxRegistry):
    """ This is the box registry.

        See interfaces.py for further details.
    """
    implements(IBoxRegistry)

    def _update_addable_to(self, component_class):
        component_class.type_info.addable_to += \
            box_manager_registry.get_component_names()

    def register_component(self, component):
        component_class = self._convert_component(component)
        if component_class not in self.components:
            self.components.append(component_class)
            self._update_addable_to(component_class)

box_registry = BoxRegistry()
