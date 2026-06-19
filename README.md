# Production Engineering – Portfolio Site

A two-person portfolio site built with Flask as part of the MLH Fellowship (Ruth Pérez & Thrinayani Yedhoti). Showcases about, experience, hobbies, and a travel map.

---

## Project Structure

```
pe-portfolio-submission/
├── app/
│   ├── __init__.py              # App factory, route definitions, context processor
│   ├── constants.py             # All static data: NAV_LINKS, PAGE_TITLES, EDUCATION, EXPERIENCES, HOBBIES
│   ├── static/
│   │   ├── img/
│   │   │   ├── favicon.ico
│   │   │   ├── logo.jpg
│   │   │   ├── logo.svg
│   │   │   ├── profiles/        # Headshots (ruth.png, Thrinayani.jpeg)
│   │   │   ├── experience/      # Company logos (mit.png, nvidia.png, schneider.png, etc.)
│   │   │   ├── hobbies/
│   │   │   │   ├── ruth/        # Ruth's hobby images
│   │   │   │   └── thrinayani/  # Thrinayani's hobby images (art.jpeg, cafe.jpeg)
│   │   │   └── travel/          # Travel photos by city (cartagena, lima, san-juan, etc.)
│   │   └── styles/
│   │       └── main.css         # Global styles
│   └── templates/
│       ├── base.html            # Shared layout (head, navbar, content block)
│       └── components/
│           ├── navbar.html      # Navbar — loops over NAV_LINKS from constants
│           ├── about.html       # About page — profiles, bios, travel map
│           ├── experience.html  # Experience page — two sections (Ruth / Thrinayani)
│           ├── hobbies.html     # Hobbies page — two sections (Ruth / Thrinayani)
│           └── projects.html    # Projects page
├── example.env                  # Template for environment variables
├── requirements.txt             # Python dependencies
└── README.md
```

### How templates are wired together

```
base.html
 ├── includes → components/navbar.html   (rendered on every page)
 └── block content
      └── filled by each page component (about.html, experience.html, …)
```

Each page component (`components/*.html`) extends `base.html` and fills the `content` block. Data (experiences, hobbies, education) lives in `constants.py` and is passed to templates via routes in `__init__.py`.

### Data structure in `constants.py`

`EDUCATION`, `EXPERIENCES`, and `HOBBIES` are all dicts keyed by person:

```python
EXPERIENCES = {
    "ruth": [ { "role": ..., "company": ..., "dates": ..., "logo": ..., "bullets": [...] }, ... ],
    "thrinayani": [ ... ],
}
```

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

| Route         | Page                        |
|---------------|-----------------------------|
| `/`           | Redirects to `/about`       |
| `/about`      | About — profiles & map      |
| `/experience` | Experience (Ruth & Thrinayani) |
| `/hobbies`    | Hobbies (Ruth & Thrinayani) |
| `/projects`   | Projects                    |

---

## Adding Content

### New hobby or experience entry
Edit the relevant list in `app/constants.py` under the `ruth` or `thrinayani` key. Drop the image into the matching folder under `app/static/img/`.

### New page
1. Add an entry to `NAV_LINKS` and `PAGE_TITLES` in `app/constants.py`.
2. Create `app/templates/components/<page>.html` extending `base.html`.
3. Add a route in `app/__init__.py`.

---

## Checklist
### GitHub Tasks
- [x] Create Issues for each task below
- [x] Progress on each task in a new branch
- [x] Open a Pull Request when a task is finished to get feedback

### Portfolio Tasks
- [x] Add a photo of yourself to the website
- [x] Add an "About yourself" section to the website
- [x] Add your previous work experiences
- [x] Add your hobbies (including images)
- [x] Add your current/previous education
- [x] Add a map of all the cool locations/countries you visited

### Flask Tasks
- [x] Get your Flask app running locally on your machine using the instructions below
- [x] Add a template for adding multiple work experiences/education/hobbies using [Jinja](https://jinja.palletsprojects.com/en/3.0.x/api/#basics)
- [x] Create a new page to display hobbies
- [x] Add a menu bar that dynamically displays other pages in the app
