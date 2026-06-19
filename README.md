# Production Engineering – Week 1 – Portfolio Site

A personal portfolio built with Flask as part of the MLH Fellowship. Week 1 focuses on getting the app running locally; hosting in the cloud comes in later weeks.

---

## Project Structure

```
pe-portfolio-submission/
├── app/
│   ├── __init__.py          # App factory, route definitions, context processor
│   ├── constants.py         # All static strings (page titles, nav links)
│   ├── static/
│   │   ├── img/
│   │   │   ├── favicon.ico
│   │   │   ├── logo.jpg     # Profile picture
│   │   │   └── logo.svg     # Navbar logo
│   │   └── styles/
│   │       └── main.css     # Global styles
│   └── templates/
│       ├── base.html        # Shared layout (head, navbar, content block)
│       └── components/
│           ├── navbar.html  # Navbar — loops over NAV_LINKS from constants
│           ├── home.html    # Home page content
│           ├── about.html   # About page content
│           ├── experience.html
│           ├── projects.html
│           └── hobbies.html
├── example.env              # Template for environment variables
├── requirements.txt         # Python dependencies
└── README.md
```

### How templates are wired together

```
base.html
 ├── includes → components/navbar.html   (rendered on every page)
 └── block content
      └── filled by each page component (home.html, about.html, …)
```

Each page component (`components/*.html`) extends `base.html` and fills the `content` block. Adding a new page means creating a new component, registering a route in `__init__.py`, and adding an entry to `NAV_LINKS` in `constants.py`.

---

## Prerequisites

- Python 3.8+
- pip

---

## Setup

1. **Clone the repo**
   ```bash
   git clone <repo-url>
   cd pe-portfolio-submission
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # macOS / Linux
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp example.env .env
   ```
   The default `.env` sets `URL=localhost:5000`. Edit it if needed.

---

## Running Locally

```bash
export FLASK_APP=app        # Windows: set FLASK_APP=app
export FLASK_ENV=development
flask run
```

The app will be available at `http://localhost:5000`.

| Route         | Page       |
|---------------|------------|
| `/`           | Home       |
| `/about`      | About      |
| `/experience` | Experience |
| `/projects`   | Projects   |
| `/hobbies`    | Hobbies    |

---

## Adding a New Page

1. Add an entry to `NAV_LINKS` in `app/constants.py` (and a `PAGE_TITLES` entry).
2. Create `app/templates/components/<page>.html` extending `base.html`.
3. Add a route in `app/__init__.py`.

---

## Contributing

Pull requests are welcome. For major changes please open an issue first to discuss what you'd like to change.

## Checklist
### GitHub Tasks
- [x] Create Issues for each task below
- [x] Progress on each task in a new branch
- [x] Open a Pull Request when a task is finished to get feedback

### Portfolio Tasks
- [x] Add a photo of yourself to the website
- [x] Add an "About youself" section to the website.
- [x] Add your previous work experiences
- [x] Add your hobbies (including images)
- [x] Add your current/previous education
- [x] Add a map of all the cool locations/countries you visited

### Flask Tasks
- [x] Get your Flask app running locally on your machine using the instructions below.
- [x] Add a template for adding multiple work experiences/education/hobbies using [Jinja](https://jinja.palletsprojects.com/en/3.0.x/api/#basics)
- [x] Create a new page to display hobbies.
- [x] Add a menu bar that dynamically displays other pages in the app



