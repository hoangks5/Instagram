from instapy import InstaPy



user_name = 'hoangks5'
password = 'Hoang22041999'
session = InstaPy(username=user_name, password=password,headless_browser=False,want_check_browser=False)
session.login()
session.set_do_like(enabled=True, percentage=70)
