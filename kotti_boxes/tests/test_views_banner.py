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
            link='',
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
        file_obj = view.add(
            title=u'A title',
            description=u'A description',
            tags=[],
            file=dict(
                fp=StringIO('filecontents'),
                filename=u'myfile.png',
                mimetype=u'image/png',
                ),
            )

        assert file_obj.title == u'A title'
        assert file_obj.description == u'A description'
        assert file_obj.tags == []
        assert file_obj.data
        assert file_obj.filename == u'myfile.png'
        assert file_obj.mimetype == u'image/png'
        assert file_obj.size == len('filecontents')

    def test_add2(self, config):
        """ The added item should be a BannerBox instance """
        view = self.make_one()
        file = view.add(
            title=u'A title',
            description=u'A description',
            tags=[],
            link=u'http://google.com',
            file=dict(
                fp=StringIO('filecontents'),
                filename=u'myfile.png',
                mimetype=u'image/png',
                ),
            )

        assert file.title == u'A title'
        assert file.link == u'http://google.com'
        from kotti_boxes.resources import BannerBox
        assert isinstance(file, BannerBox)
