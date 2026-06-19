"""Flask application factory and route definitions."""

import os
from flask import Flask, render_template
from dotenv import load_dotenv
from app.constants import NAV_LINKS, PAGE_TITLES, EXPERIENCES, EDUCATION

load_dotenv()
app = Flask(__name__)


@app.context_processor
def inject_globals():
    """Inject variables needed by every template (navbar links, site URL)."""
    return {
        "nav_links": NAV_LINKS,
        "url": os.getenv("URL"),
    }


@app.route("/")
def index():
    """Render the home page."""
    return render_template("components/home.html", title=PAGE_TITLES["home"], active_page="home")


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
    return render_template("components/projects.html", title=PAGE_TITLES["projects"], active_page="projects")


@app.route("/hobbies")
def hobbies():
    """Render the hobbies page."""
    return render_template("components/hobbies.html", title=PAGE_TITLES["hobbies"], active_page="hobbies")
