# IT Company Task Manager

This project is a comprehensive task management system designed specifically for IT companies. It provides a platform to efficiently allocate and manage tasks among workers based on their positions and task types.

## Features

- **Worker Management**: Create and manage workers with their respective positions and task types.
- **Task Creation**: Generate tasks for workers, positions, and task types separately.
- **Efficient Allocation**: Allocate tasks to workers based on their positions and expertise, ensuring optimal utilization of resources.
- **Intuitive Interface**: The user interface is designed for ease of use, making task management a breeze.

## Check it out!
[IT Company Task Manager deployed to Render](https://it-company-task-manager-c9zk.onrender.com/)

## How to Use

1. Clone the repository to your local machine.
2. Install the necessary dependencies (if any) mentioned in the project's documentation.
3. Launch the application following the instructions provided in the project's documentation.

## Getting Started
### Installation
To set up and run the IT Company Task Manager project, follow these steps:
1. Clone the Repository:
```bash
git clone https://github.com/Veinmax/IT-company-task-manager.git
```

2. Navigate to the Project Directory:
```bash
cd IT-company-task-manager/
```

3. Create a Virtual Environment:
```bash
python -m venv venv
```

4. Install Dependencies:
```bash
pip install -r requirements.txt
```

5. Configure Environment Variables:
- Create a .env file in the project root.
- Make sure it includes all the variables listed in the .env.sample file.
- Ensure that the variable names and values match those in the sample file.

6. Apply Migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Load Initial Data:
```bash
python manage.py loaddata my_data.json
```
- After loading data from fixture you can use following superuser (or create another one by yourself):
  - Login: `admin.user`
  - Password: `1qazcde3`

8. Run the Server:
```bash
python manage.py runserver
```
