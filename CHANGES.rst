History
=======

0.1.5 (2015-06-08)
------------------

- Move to modular ``config.include`` strategy for view registrations (it should help overriding views)
  [davidemoro]

- Update README file (funding)
  [davidemoro]


0.1.4 (2015-05-25)
------------------

- If you provide a non empty ``addable_to`` property to your box ``type_info`` you
  can decide where your box will be addable. Otherwise it will be addable in
  all box registered box managers.
  [davidemoro]

- Updated test (broken test on TravisCI build with the latest Kotti version based on ``filedepot``, false positive)
  [davidemoro]

0.1.3 (2015-03-16)
------------------

- No more ``selectable_default_views`` inheritance for box related types.
  Initialized to [] on our resources'type_info.
  [davidemoro]

- Fixed bug with BannerBox edit form.
  [davidemoro]

0.1.2 (2015-03-03)
------------------

- Fixed Travis CI build
  [davidemoro]

- Fixed problem with edit form on BannerBox (no context
  discriminator)
  [davidemoro]


0.1.1 (2015-02-26)
------------------

- Updated development version (from 0.2 to 0.1.1)
  [davidemoro]

- Fixed a bug in TextBox addform (the saved item
  wasn't a a TextBox instance)
  [davidemoro]

- Fixed a bug in BannerBox addform (the link
  attribute wasn't saved)
  [davidemoro]

- The BannerBox's link now accepts also internal
  urls (eg: /en/about)
  [davidemoro]


0.1 (2015-02-24)
----------------

- Prerelease tag.
  [davidemoro]
