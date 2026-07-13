"""Flask application factory and route definitions."""

import os
import datetime
from flask import Flask, render_template, redirect, url_for, request, jsonify
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict
from app.constants import NAV_LINKS, PAGE_TITLES, HOBBIES, PROJECTS, EXPERIENCES, EDUCATION

load_dotenv()
app = Flask(__name__)

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306,
)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database


database.connect()
database.create_tables([TimelinePost])

@app.context_processor
def inject_globals():
    """Inject variables needed by every template (navbar links, site URL)."""
    return {
        "nav_links": NAV_LINKS,
        "url": os.getenv("URL"),
    }


@app.route("/")
def index():
    return redirect(url_for("about"))


@app.route("/about")
def about():
    """Render the about page."""
    return render_template("components/about.html", title=PAGE_TITLES["about"], active_page="about")


@app.route("/experience")
def experience():
    """Render the experience page."""
    return render_template(
        "components/experience.html",
        title=PAGE_TITLES["experience"],
        active_page="experience",
        experiences=EXPERIENCES,
        education=EDUCATION,
    )


@app.route("/projects")
def projects():
    """Render the projects page."""
    return render_template(
        "components/projects.html",
        title=PAGE_TITLES["projects"],
        active_page="projects",
        projects=PROJECTS,
    )


@app.route("/hobbies")
def hobbies():
    """Render the hobbies page."""
    return render_template(
        "components/hobbies.html",
        title=PAGE_TITLES["hobbies"],
        active_page="hobbies",
        hobbies=HOBBIES,
    )

@app.route("/timeline")
def timeline():
    """Render the timeline page."""
    return render_template("timeline.html", title="Timeline", active_page="timeline")

@app.route("/api/timeline_post", methods=["POST"])
def create_timeline_post():
    data = request.get_json()
    post = TimelinePost.create(
        name=data.get("name"),
        email=data.get("email"),
        content=data.get("content"),
    )
    return jsonify(model_to_dict(post)), 201


@app.route("/api/timeline_post", methods=["GET"])
def get_timeline_posts():
    posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
    return jsonify([model_to_dict(post) for post in posts])


@app.route("/api/timeline_post/<int:post_id>", methods=["DELETE"])
def delete_timeline_post(post_id):
    post = TimelinePost.get_or_none(TimelinePost.id == post_id)
    if post is None:
        return jsonify({"error": "Timeline post not found"}), 404
    post.delete_instance()
    return jsonify({"success": True}), 200
