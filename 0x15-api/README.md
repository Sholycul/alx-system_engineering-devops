#PROJECT: 0x15-api

This project contains a series of Python scripts that interact with a REST API to gather, display, and export TODO list information for employees. Each script performs a specific task, from gathering data to exporting it in various formats.

## Table of Contents
1. [Tasks](#tasks)
   - [0. Gather data from an API](#0-gather-data-from-an-api)
   - [1. Export to CSV](#1-export-to-csv)
   - [2. Export to JSON](#2-export-to-json)
   - [3. Dictionary of list of dictionaries](#3-dictionary-of-list-of-dictionaries)
2. [Usage](#usage)

## Tasks

### 0. Gather data from an API

This script retrieves information about an employee's TODO list progress using a REST API.

#### Requirements:
- The script uses the `requests` module to make HTTP requests.
- It accepts an integer as a parameter (the employee ID).
- It displays the employee's TODO list progress in the following format:
  ```
  Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
       TASK_TITLE
       ...
  ```

#### Example Usage:
```bash
$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     ...
```

### 1. Export to CSV

This script extends task #0 to export the TODO list data to a CSV file.

#### Requirements:
- Exports all tasks owned by the employee.
- The CSV file format: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`.
- The file name is `USER_ID.csv`.

#### Example Usage:
```bash
$ python3 1-export_to_CSV.py 2
$ cat 2.csv
"2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
"2","Antonette","True","distinctio vitae autem nihil ut molestias quo"
...
```

### 2. Export to JSON

This script extends task #0 to export the TODO list data to a JSON file.

#### Requirements:
- Exports all tasks owned by the employee.
- The JSON file format: 
  ```json
  {
    "USER_ID": [
      {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
      ...
    ]
  }
  ```
- The file name is `USER_ID.json`.

#### Example Usage:
```bash
$ python3 2-export_to_JSON.py 2
$ cat 2.json
{
  "2": [
    {"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false, "username": "Antonette"},
    {"task": "distinctio vitae autem nihil ut molestias quo", "completed": true, "username": "Antonette"},
    ...
  ]
}
```

### 3. Dictionary of list of dictionaries

This script extends task #0 to export data of all employees to a single JSON file.

#### Requirements:
- Exports all tasks for all employees.
- The JSON file format:
  ```json
  {
    "USER_ID": [
      {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
      ...
    ],
    ...
  }
  ```
- The file name is `todo_all_employees.json`.

#### Example Usage:
```bash
$ python3 3-dictionary_of_list_of_dictionaries.py
$ cat todo_all_employees.json
{
  "1": [
    {"username": "Bret", "task": "delectus aut autem", "completed": false},
    ...
  ],
  ...
}
```

## Usage

To use any of these scripts, simply run them with the appropriate parameters. For example, to gather data for an employee with ID 2, you would run:

```bash
$ python3 0-gather_data_from_an_API.py 2
```

Ensure you have the `requests` module installed. You can install it using pip:

```bash
$ pip install requests
```
