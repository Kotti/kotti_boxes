from StringIO import StringIO

from mock import MagicMock

from kotti.testing import DummyRequest


class TestBannerBoxEditForm:
    def make_one(self):
        from kotti_boxes.views.edit.boxes.banner import BannerBoxEditForm
        return BannerBoxEditForm(MagicMock(), DummyRequest())

    def test_edit_with_file(self):
        view = self.make_one()
        view.edit(
            title=u'A title',
            description=u'A description',
            tags=[],
            file=dict(
                fp=StringIO('filecontents'),
                filename=u'myfile.png',
                mimetype=u'image/png',
                ),
            )
        assert view.context.title == u'A title'
        assert view.context.description == u'A description'
        assert view.context.data == 'filecontents'
        assert view.context.filename == u'myfile.png'
        assert view.context.mimetype == u'image/png'
        assert view.context.size == len('filecontents')


class TestBannerBoxAddForm:
    def make_one(self):
        from kotti_boxes.views.edit.boxes.banner import BannerBoxAddForm
        return BannerBoxAddForm(MagicMock(), DummyRequest())

    def test_add(self, config):
        view = self.make_one()
        file = view.add(
            title=u'A title',
            description=u'A description',
            tags=[],
            file=dict(
                fp=StringIO('filecontents'),
                filename=u'myfile.png',
                mimetype=u'image/png',
                ),
            )

        assert file.title == u'A title'
        assert file.description == u'A description'
        assert file.tags == []
        assert file.data == 'filecontents'
        assert file.filename == u'myfile.png'
        assert file.mimetype == u'image/png'
        assert file.size == len('filecontents')