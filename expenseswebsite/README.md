# 💰 Finance Dashboard Django Project

Welcome to the Finance Dashboard Django Project! This project aims to provide users with a comprehensive tool for managing finances effectively. From tracking expenses to visualizing financial data, this dashboard has got you covered. 💹

## Project Overview

This Django project offers a finance dashboard where users can efficiently manage their expenses and incomes by category. With a user-friendly interface and robust features, users can easily track their financial activities and make informed decisions. 📊💼

## Languages, Libraries, and Tools

### Languages:
- Python 🐍
- HTML 🌐
- CSS 🎨
- JavaScript 📜

### Libraries and Frameworks:
- Django 🌱
- PostgreSQL (Database) 🗃️
- Chart.js (Data Visualization) 📊

### Tools:
- Git (Version Control) 🛠️
- Heroku (Deployment) 🚀

## Features

The Finance Dashboard Django Project encompasses a wide range of features to empower users in managing their finances effectively. Here's an overview of what you can expect:

- **Django Project Introduction**: Learn about the purpose and scope of the project.
- **Setting up Development Environment**: Configure your development environment for Django.
- **Installing and Setting up a Postgres Database**: Use PostgreSQL for smooth data management.
- **Setting up Static Assets**: Configure HTML, CSS, and JS files for frontend.
- **Setting up Apps, Views, URLs, Templates**: Organize project structure and render pages effectively.
- **Heroku Deployment**: Deploy your application to Heroku for online hosting.
- **Ajax User Registration**: Enhance user registration with Ajax for interactivity.
- **Ajax Validation**: Validate usernames and email addresses in real-time.
- **Password Toggle Feature**: Allow users to toggle password visibility for convenience.
- **User Authentication and Access Control**: Secure user access with login, logout, and access control features.
- **User Preference Management**: Customize user experience with preference management.
- **CRUD Operations for Expenses and Incomes**: Manage expenses and incomes effortlessly.
- **Pagination and Search**: Handle large data sets efficiently with pagination and search functionality.
- **Customizing Django Admin Interface**: Customize admin interface to suit project needs.
- **Password Reset Functionality**: Allow users to securely reset passwords.
- **Email Sending Optimization**: Optimize email sending for faster performance.
- **Data Visualization with Chart.js**: Visualize financial data effectively for analysis.

## Getting Started

### Installation:

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd finance-dashboard-django
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Database Setup:

1. Install PostgreSQL:
    - For Linux:
      ```bash
      sudo apt-get install postgresql
      ```
    - For macOS:
      ```bash
      brew install postgresql
      ```
    - For Windows: Download and install from [PostgreSQL website](https://www.postgresql.org/download/).

2. Create a PostgreSQL database:
    ```bash
    createdb <database-name>
    ```

3. Update database settings in `settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '<database-name>',
            'USER': '<database-user>',
            'PASSWORD': '<database-password>',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    ```

### Running the Project:

1. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

2. Start the development server:
    ```bash
    python manage.py runserver
    ```

3. Open your web browser and navigate to `http://localhost:8000` to view the application.

## Contributing

Contributions to this project are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Created by Lucas Fortunato ✨
   