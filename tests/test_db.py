import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

# using inmemory SQLite for tests
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # we bind model classes to test db. since we have a complete list of all models
        # we do not need to recursively bind dependencies
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # not really necessary sicne SQLite databases only live for the duration of connectioon
        # and in the next step we close the connect but this is a good practise
        test_db.drop_tables(MODELS)

        # connection close
        test_db.close()

    def test_timeline_post(self):
        # create 2 timeline posts
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2

        # get all timeline posts, ordered by insertion
        posts = list(TimelinePost.select().order_by(TimelinePost.id))
        assert len(posts) == 2

        # assert the first post has the correct values
        assert posts[0].id == first_post.id
        assert posts[0].name == 'John Doe'
        assert posts[0].email == 'john@example.com'
        assert posts[0].content == 'Hello world, I\'m John!'

        # assert the second post has the correct values
        assert posts[1].id == second_post.id
        assert posts[1].name == 'Jane Doe'
        assert posts[1].email == 'jane@example.com'
        assert posts[1].content == 'Hello world, I\'m Jane!'