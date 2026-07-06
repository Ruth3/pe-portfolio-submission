"""Static strings and configuration values used across the app."""

APP_NAME = "MLH Fellow"
APP_DESCRIPTION = "My Personal Portfolio"

# Each entry drives both the navbar rendering and the route's page title.
# 'key' must match the active_page value passed from the route.
NAV_LINKS = [
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

EDUCATION = {
    "ruth": [
        {
            "degree": "B.A. in Biology & Computer Science",
            "school": "Brandeis University",
            "location": "Waltham, MA",
            "status": "Senior",
        },
    ],
    "thrinayani": [
        {
            "degree": "MS, Computer Science and Software Engineering",
            "school": "University of Washington, Bothell",
            "location": "Bothell, WA",
            "status": "Expected March 2027 · GPA: 3.83/4.0",
        },
    ],
}

EXPERIENCES = {
    "ruth": [
        {
            "role": "Machine Learning Research Intern",
            "company": "MIT FMML",
            "dates": "Current",
            "logo": "img/experience/mit.png",
            "current": True,
            "bullets": [
                "New position, collaborating with researchers at MIT FMML to build and evaluate machine learning models for healthcare and women's health studies.",
            ],
        },
        {
            "role": "Software Engineer Intern — Robotics Simulation",
            "company": "NVIDIA",
            "dates": "",
            "logo": "img/experience/nvidia.png",
            "current": False,
            "bullets": [
                "Integrated a Rapidly-exploring Random Tree (RRT)-based motion planning algorithm into NVIDIA Isaac Sim using Python, interfacing with underlying C++ planning libraries to enable global path planning for a mobile-based robot.",
                "Designed and generated randomized maze-like simulation environments in Python to model real-world navigation constraints and evaluate planner success rates across diverse scenarios.",
            ],
        },
        {
            "role": "Research Intern — ICCAN Team",
            "company": "Memorial Sloan Kettering Cancer Center",
            "dates": "",
            "logo": "img/experience/mskcc.jpg",
            "current": False,
            "bullets": [
                "Developed Python-based data processing pipelines to clean and structure patient monitoring datasets exported from REDCap systems, improving data quality and reducing manual workload.",
                "Evaluated patient-generated health data from a blood pressure telemonitoring study to identify trends supporting data-driven clinical decision-making, presenting findings and reporting statistical changes to the principal investigator.",
            ],
        },
        {
            "role": "Teaching Assistant — ENGR 11A: Intro to Design Methodology",
            "company": "Brandeis University",
            "dates": "",
            "logo": "img/experience/brandeis.png",
            "current": False,
            "bullets": [
                "Guided development of student engineering projects by debugging code and assisting with implementation of web-based systems using Python, Bootstrap, and API integrations.",
                "Troubleshot technical issues across hardware and software workflows, including 3D printing, laser cutting, and CNC machining, ensuring successful project execution.",
            ],
        },
    ],
    "thrinayani": [
        {
            "role": "Software Design Engineer",
            "company": "Schneider Electric – R&D, Industrial Automation",
            "dates": "Feb 2025 – Aug 2025",
            "logo": "img/experience/schneider.png",
            "current": False,
            "bullets": [
                "Reduced PLC license validation time by 30% by engineering a GSE mechanism for Unity M580 industrial controllers using C# and WPF with full unit test coverage, directly supporting factory automation workflows.",
                "Decreased carbon emission reporting latency for manufacturing plants by architecting a real-time edge computing pipeline using Python and FastAPI, improving operational visibility into production metrics.",
                "Accelerated vulnerability inspection workflows by building user management dashboards and RBAC-based access controls using Angular and ASP.NET.",
            ],
        },
        {
            "role": "Graduate Engineer Trainee",
            "company": "Schneider Electric – R&D, Industrial Automation",
            "dates": "Aug 2024 – Feb 2025",
            "logo": "img/experience/schneider.png",
            "current": False,
            "bullets": [
                "Reduced application load times by 20% by refactoring .NET, WPF, and Angular codebases supporting industrial automation software, with maintained unit test coverage across all modules.",
                "Accelerated database query execution by 40% by designing an ORM-based data architecture using SQLite and SQLAlchemy.",
            ],
        },
        {
            "role": "Application Engineer Intern",
            "company": "Schneider Electric – R&D, Industrial Automation",
            "dates": "Jan 2024 – Jul 2024",
            "logo": "img/experience/schneider.png",
            "current": False,
            "bullets": [
                "Shipped production-ready RBAC system using C#, Angular, and .NET with zero vulnerabilities across Sonar and Coverity static analysis; delivered clean, well-tested code reviewed by senior engineers.",
            ],
        },
        {
            "role": "Research Scholar",
            "company": "Amrita Vishwavidyapeetham",
            "dates": "Sep 2023 – Dec 2023",
            "logo": "img/experience/amrita.jpg",
            "current": False,
            "bullets": [
                "Worked under Dr. Rimjhim Padam Singh as a research scholar and published a work on leveraging Spiking Neural Networks for fashion dataset classification — IEEE, 2024.",
            ],
        },
        {
            "role": "Research Scholar",
            "company": "Amrita Vishwavidyapeetham",
            "dates": "Apr 2023 – Jun 2023",
            "logo": "img/experience/amrita.jpg",
            "current": False,
            "bullets": [
                "Worked under Dr. Jyotsna C. as a research scholar and published a work on CNN-based neural networks for age estimation with diverse facial datasets — IEEE, 2024.",
            ],
        },
    ],
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

PROJECTS = {
    "ruth": [
        {
            "name": "Robotics Simulation",
            "description": "Worked with different path planning algorithms to best test how mobile base robots can traverse through maze-like environments!",
            "image": "img/projects/ruth/robotics.jpg",
            "link": "",
        },
        {
            "name": "Drug-Gene Relationship Analyzer",
            "description": "Worked with Hetionet biomedical knowledge graph data to explore how drug compounds connect to genes and diseases, using machine learning to predict their therapeutic potential.",
            "image": "img/projects/ruth/drug.jpg",
            "link": "",
        },
    ],
    "thrinayani": [
        {
            "name": "Fast Marching Method — Ride the Wave",
            "description": "Outperformed OpenCV's GraphCutSeamFinder and DPSeamFinder by implementing an FMM-based seam finder for optimal image seamlines. Solved the Eikonal equation over fused cost fields (color, edge, texture, saliency) for globally optimal seam paths.",
            "image": "img/projects/thrinayani/fmm.png",
            "link": "https://github.com/Thrinayani39e/Fast_Marching_Method_Ride_the_Wave",
        },
        {
            "name": "Distributed Rate Limiter Microservice",
            "description": "Production-ready distributed rate-limiting backend implementing token bucket and sliding window algorithms via Redis. Full audit trail persisted to PostgreSQL, HTTP 429 enforcement with per-client analytics, and deployed via Docker Swarm with GitHub Actions CI/CD.",
            "image": "img/projects/thrinayani/ratelimiter.png",
            "link": "https://github.com/Thrinayani39e/rate-limiter-service",
        },
    ],
}
