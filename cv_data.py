"""My CV content, taken from errolito_lopez_resume.pdf. Temporary: it moves into SQLite later."""

CV = {
    "name": "Errolito D. Lopez",
    "title": "Software Engineer",
    "email": "errolitolopez@gmail.com",
    "phone": "+639999138970",
    "summary": (
        "Software Engineer ready for the era of agentic AI. Experienced in building scalable web applications, "
        "strongest in Java and Spring, and now building with LLMs and AI coding agents to ship faster. "
        "Comfortable across the stack and in the cloud, and always exploring new technologies."
    ),
    # (icon, category, skills, on_resume). The print resume is a one-pager, so it only takes some groups.
    "skills": [
        ("bi-cup-hot", "Backend & frameworks", [
            "Java", "Spring", "Microservices", "OAuth2", "Swagger", "Liquibase"], True),
        ("bi-cloud", "Cloud & DevOps", [
            "AWS", "Docker", "Kubernetes", "Jenkins", "GitHub Actions", "SonarQube", "Render"], True),
        ("bi-database", "Data & messaging", ["SQL", "SQLite", "Redis", "Kafka", "RabbitMQ"], True),
        ("bi-activity", "Observability", ["Jaeger", "Prometheus", "Grafana", "Kibana"], False),
        ("bi-tools", "Tooling", ["Maven", "Gradle", "Git", "GitHub", "GitLab"], False),
        ("bi-check2-circle", "Testing", ["JUnit", "Mockito", "Testcontainers"], True),
        ("bi-window", "Frontend (supporting)", ["Angular", "TypeScript"], True),
    ],
    "portfolio_period": "May 2024 – Present",
    "portfolio_intro": (
        "Built Java applications, published libraries and deployed them to the cloud during a career break, "
        "to deepen expertise across the modern Java ecosystem."
    ),
    # on_resume: the one-page resume only lists these.
    "projects": [
        {
            "name": "DB2Spring",
            "links": [("db2spring.site", "https://db2spring.site"),
                      ("GitHub", "https://github.com/errolitolopez/db2spring")],
            "about": "Code generation tool that reads database schemas or SQL statements and produces full-stack "
                     "layers: entities, APIs and service/business logic.",
            "points": [],
            "on_resume": True,
        },
        {
            "name": "My Crud",
            "links": [("mycrud.site", "https://mycrud.site"),
                      ("GitHub", "https://github.com/errolitolopez/my-crud")],
            "about": "A fully integrated system with CI/CD, load balancing, code quality analysis and "
                     "Docker-based builds.",
            "points": [
                "Full observability: Jaeger (tracing), Prometheus (metrics), Grafana (dashboards), Kibana (logs).",
                "Messaging with Kafka (fund transfer with idempotency checks) and RabbitMQ (real-time chat).",
                "APIs secured with Spring Security, OAuth2 and JWT, with role-based access control.",
            ],
            "on_resume": True,
        },
        {
            "name": "Open-source Java libraries",
            "links": [("SmartString", "https://github.com/errolitolopez/smartstring"),
                      ("Common Libraries", "https://github.com/errolitolopez/commons")],
            "about": "SmartString (string case conversion, pluralization) and a set of dependency-free utility "
                     "libraries for everyday backend development.",
            "points": [],
            "on_resume": False,
        },
    ],
    # Recent jobs list their projects. Older ones have only a one-line "summary".
    "experience": [
        {
            "company": "Exist Software Labs, Inc.",
            "period": "Jun 2026 – Present",
            "on_resume": True,
            "projects": [
                {"name": "Energy Billing and Settlement System",
                 "about": "Software for the Philippine energy sector: WESM compliance, billing and settlement "
                          "workflow automation, and energy data management.",
                 "points": []},
            ],
        },
        {
            "company": "Career break",
            "period": "May 2024 – May 2026",
            "on_resume": True,
            "projects": [
                {"name": "Business & upskilling",
                 "about": "Ran a business and upskilled across the modern Java ecosystem, building and deploying "
                          "Java applications and libraries in the cloud.",
                 "points": []},
            ],
        },
        {
            "company": "Flying Future Services, Inc.",
            "period": "May 2021 – Sep 2023",
            "on_resume": True,
            "projects": [
                {"name": "Capital Management System",
                 "about": "Web app that manages customer deposits and withdrawals.",
                 "points": []},
            ],
        },
        {
            "company": "SLI Consulting, Inc.",
            "period": "Jul 2020 – May 2021",
            "on_resume": True,
            "projects": [
                {"name": "Robinson's Bank Motorcycle Inventory Management System",
                 "about": "Tracks motorcycle inventory across stores and warehouses, and sells repossessed "
                          "units through a role-based approval workflow.",
                 "points": []},
            ],
        },
        {
            "company": "White Clock Technologies, Inc.",
            "period": "May 2019 – Jul 2020",
            "on_resume": True,
            "projects": [
                {"name": "UnionBank of the Philippines: Generic Corporate Prepaid Card (Payroll)",
                 "about": "Corporate payroll web app, with REST APIs and KYC integrations.",
                 "points": []},
            ],
        },
        {
            "company": "Ziaplex, Inc.",
            "period": "Jan 2018 – May 2019",
            "on_resume": True,
            "projects": [
                {"name": "DTI Trade Statistics",
                 "about": "Visualizes global trade statistics (exports and imports) by country.",
                 "points": []},
                {"name": "DTI Business Name Registration (BNRS)",
                 "about": "Modernizes business name registration for the Department of Trade and Industry.",
                 "points": []},
            ],
        },
    ],
    "education": [
        {"course": "Bachelor of Science in Information Technology",
         "school": "College of Our Lady of Mercy", "period": "Jun 2013 – Apr 2017"},
    ],
}
