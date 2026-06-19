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

HOBBIES = {
    "ruth": [
        {
            "name": "Photography",
            "description": "I love doing event and portrait photography and love meeting new people!",
            "image": "img/hobbies/ruth/photography.jpg",
        },
        {
            "name": "Hiking",
            "description": "I love to explore new trails and go to different states!",
            "image": "img/hobbies/ruth/hiking.jpeg",
        },
        {
            "name": "Concerts",
            "description": "I love listening to live music and have seen Jhene Aiko, Bad Bunny, Karol G, Kaytranada, Andre 3000, Cleo Sol, and more!",
            "image": "img/hobbies/ruth/concert.jpeg",
        },
    ],
    "thrinayani": [
        {
            "name": "Painting and Art",
            "description": "My go-to stress reliever and 'touch some grass' activity — painting and art help me decompress and reset.",
            "image": "img/hobbies/thrinayani/art.jpeg",
        },
        {
            "name": "Cafe Hopping",
            "description": "I love trying new coffee varieties and different cuisines — there's always a new spot to explore!",
            "image": "img/hobbies/thrinayani/cafe.jpeg",
        },
    ],
}
