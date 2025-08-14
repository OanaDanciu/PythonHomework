A Python-based microservice for executing mathematical operations (power, fibonacci, factorial,
sum_digits) via both a REST API and CLI interface. Designed with production-readiness in mind, the 
service follows a modular MVCS architecture, uses FastAPI for API handling and Click for CLI commands,
and supports advanced features like SQLite persistence, multithreaded execution, @lru_cache optimization,
centralized logging, input validation with Pydantic, flake8 linting, and full Docker containerization 
via Rancher Desktop. Easily extensible and ideal for scalable, testable, and portable deployments.