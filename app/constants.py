"""Static strings and configuration values used across the app."""

APP_NAME = "MLH Fellow"
APP_DESCRIPTION = "My Personal Portfolio"

# Each entry drives both the navbar rendering and the route's page title.
# 'key' must match the active_page value passed from the route.
NAV_LINKS = [
    {"label": "Home",       "href": "/",           "key": "home"},
    {"label": "About",      "href": "/about",       "key": "about"},
    {"label": "Experience", "href": "/experience",  "key": "experience"},
    {"label": "Projects",   "href": "/projects",    "key": "projects"},
    {"label": "Hobbies",    "href": "/hobbies",     "key": "hobbies"},
]

PAGE_TITLES = {
    "home":       APP_NAME,
    "about":      "About",
    "experience": "Experience",
    "projects":   "Projects",
    "hobbies":    "Hobbies",
}

EXPERIENCES = [
    {
        "company": "Company Name",
        "role": "Your Job Title",
        "dates": "Month Year – Month Year",
        "bullets": [
            "Describe a key accomplishment or responsibility here.",
            "Another impact you had — quantify it if you can.",
            "One more highlight from this role.",
        ],
    },
    {
        "company": "Another Company",
        "role": "Your Role",
        "dates": "Month Year – Month Year",
        "bullets": [
            "What you built, shipped, or improved.",
            "A skill or tool you used heavily.",
        ],
    },
]

EDUCATION = [
    {
        "school": "University Name",
        "degree": "Bachelor of Science in Computer Science",
        "dates": "Year – Year",
        "highlights": [
            "Relevant coursework, honor, or activity worth mentioning.",
        ],
    },
]
