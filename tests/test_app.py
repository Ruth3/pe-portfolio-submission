import unittest
import os
os.environ['TESTING'] = 'true'

from app import app, TimelinePost

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        # the in-memory SQLite db is shared across tests, so we start each test from a clean slate
        TimelinePost.delete().execute()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 302

        response = self.client.get("/", follow_redirects=True)
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "Hi, we're Ruth and Thrinayani!" in html # this test is subject to change if the porfolio is made to single person only later on the line

    def test_pages_render(self):
        # the base-template pages and their expected title in HTML
        for path, title in [
            ("/experience", "Experience"),
            ("/projects", "Projects"),
            ("/hobbies", "Hobbies"),
        ]:
            response = self.client.get(path)
            assert response.status_code == 200
            html = response.get_data(as_text=True)
            assert f"<title>{title}</title>" in html

    def test_timeline(self):
        # GET returns a JSON list this will be empty since no posts exist
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        posts = response.get_json()
        assert isinstance(posts, list)
        assert len(posts) == 0

    def test_timeline_post_create(self):
        # POST creates a timeline post and echoes it back
        response = self.client.post("/api/timeline_post", json={
            "name": "John Doe",
            "email": "john@example.com",
            "content": "Hello world, I'm John!",
        })
        assert response.status_code == 201
        assert response.is_json
        created = response.get_json()
        assert created["name"] == "John Doe"
        assert created["email"] == "john@example.com"
        assert created["content"] == "Hello world, I'm John!"
        assert "id" in created

        # created post now returned by the GET endpoint
        response = self.client.get("/api/timeline_post")
        posts = response.get_json()
        assert len(posts) == 1
        assert posts[0]["name"] == "John Doe"
        assert posts[0]["email"] == "john@example.com"
        assert posts[0]["content"] == "Hello world, I'm John!"

    #test to check if the posts come back ordered newest first
    def test_timeline_posts_ordered_newest_first(self):
        self.client.post("/api/timeline_post", json={
            "name": "First", "email": "first@example.com", "content": "first post",
        })
        self.client.post("/api/timeline_post", json={
            "name": "Second", "email": "second@example.com", "content": "second post",
        })

        posts = self.client.get("/api/timeline_post").get_json()
        assert len(posts) == 2
        assert posts[0]["content"] == "second post"
        assert posts[1]["content"] == "first post"

    # form render check in the timeline page
    def test_timeline_page(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert 'id="timeline-form"' in html
        assert 'name="name"' in html
        assert 'name="email"' in html
        assert 'name="content"' in html
