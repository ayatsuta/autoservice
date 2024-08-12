# autoservice

AutoService is a web-based application designed to manage vehicle workshops. 
The platform allows users to manage vehicles, assign managers, and track workshop activities.

## Features

- **Vehicle Management**: Create, update, and delete vehicle records.
- **Manager Assignment**: Assign managers to specific vehicles.
- **User Authentication**: Secure login and user management.

## Project Structure

- **autoservice/**: Main project folder containing settings and configurations.
- **workshop/**: Django app responsible for managing vehicles and workshop-related features.
- **static/**: Directory for static files (CSS, JavaScript, images).
- **templates/**: Directory for HTML templates.
- **db.sqlite3**: SQLite database file.
- **manage.py**: Django management script.
- **.env**: Environment variables for the project.
- **.gitignore**: Specifies files and directories that Git should ignore.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtual environment

### Setup

1. **Clone the repository:**
    ```bash
    git clone <https://github.com/ayatsuta/autoservice>
    cd autoservice
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
   - Create a `.env` file in the root directory with the following content:
     ```plaintext
     SECRET_KEY=your-secret-key
     DEBUG=True
     DATABASE_URL=sqlite:///db.sqlite3
     ```

5. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the web application at `http://127.0.0.1:8000/`.
- Log in with the superuser credentials.
- Start managing vehicles and assigning managers!

## Testing

To run the tests, use the following command:

```bash
python manage.py test
