import json
from validation import is_valid_name, is_valid_phone, is_valid_email, is_valid_password, is_valid_date, is_end_date_valid
from validation import replay

USERS_FILE = "users.json"
PROJECTS_FILE = "projects.json"

def load_data(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def register():
    users = load_data(USERS_FILE)
    email = input("\nEnter email: ")
    while not is_valid_email(email):
        print("Invalid email, Please Try Again\n")
        email = input("Enter Email again: ")

    if any(user['email'] == email for user in users):
        print("Email already registered.\n")
        return

    first_name = input("Enter first name: ")
    while not is_valid_name(first_name):
        print("Invalid name, Please Try Again\n")
        first_name = input("Enter first name again: ")

    last_name = input("Enter last name: ")
    while not is_valid_name(last_name):
        print("Invalid name, Please Try Again\n")
        last_name = input("Enter last name again: ")

    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")
    while not is_valid_password(password, confirm_password):
        print("Passwords do not match, Please Try Again\n")
        password = input("Enter password: ")
        confirm_password = input("Confirm password: ")
    
    phone = input("Enter mobile phone: ")
    while not is_valid_phone(phone):
        print("Invalid Egyptian phone number, Please Try Again\n")
        phone = input("Enter mobile phone Again: ")
    users.append({"email": email, "first_name": first_name, "last_name": last_name, "password": password, "phone": phone})
    save_data(USERS_FILE, users)
    print("\n**Registration successful! You can now login.**\n")

def login():
    users = load_data(USERS_FILE)
    email = input("Enter Email: ")
    password = input("Enter password: ")
    for user in users:
        if user['email'] == email and user['password'] == password:
            print("Login successful!\n")
            return email
    print("Invalid credentials.\n")
    return None

def create_project(user_email):
    projects = load_data(PROJECTS_FILE)
    title = input("Enter project title: ")
    details = input("Enter project details: ")
    try:
        target = float(input("Enter total target amount: "))
    except ValueError:
        print("Invalid amount.\n")
        return
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    start_date_obj = is_valid_date(start_date)
    end_date_obj = is_valid_date(end_date)
    if not start_date_obj or not end_date_obj:
        print("Invalid date format.\n")
        return
    if not is_end_date_valid(start_date_obj, end_date_obj):
        print("End date must be after start date.\n")
        return
    project = {"id": len(projects) + 1, "user": user_email, "title": title, "details": details, "target": target, "start_date": start_date, "end_date": end_date}
    projects.append(project)
    save_data(PROJECTS_FILE, projects)
    print("\n**Project created successfully!**\n")
    replay()

def view_projects():
    projects = load_data(PROJECTS_FILE)
    for project in projects:
        print(f"ID: {project['id']} \nTitle: {project['title']}\nTarget: {project['target']} EGP\nStart: {project['start_date']}\nEnd: {project['end_date']}\n")
    replay()

def edit_project(user_email):
    projects = load_data(PROJECTS_FILE)
    project_id = int(input("Enter project ID to edit: "))
    for project in projects:
        if project['id'] == project_id and project['user'] == user_email:
            project['title'] = input("Enter new title: ")
            project['details'] = input("Enter new details: ")
            project['target'] = float(input("Enter new target amount: "))
            save_data(PROJECTS_FILE, projects)
            print("\n**Project updated successfully!**\n")
            return
    print("\n**Project not found or unauthorized.**\n")
    replay()

def delete_project(user_email):
    projects = load_data(PROJECTS_FILE)
    project_id = int(input("Enter project ID to delete: "))
    for project in projects:
        if project['id'] == project_id and project['user'] == user_email:
            projects.remove(project)
            save_data(PROJECTS_FILE, projects)
            print("\n**Project deleted successfully!**\n")
            return
    print("\n**Project not found or unauthorized.**\n")
    replay()

def search_project_by_date():
    projects = load_data(PROJECTS_FILE)
    search_date = input("Enter search date (YYYY-MM-DD): ")
    results = [p for p in projects if p['start_date'] <= search_date <= p['end_date']]
    if results:
        for project in results:
            print(f"ID: {project['id']}, Title: {project['title']}, Start: {project['start_date']}, End: {project['end_date']}")
    else:
        print("\n**No projects found for this date.**\n")
    replay()

def main():
    while True:
        print("\n**Crowdfunding App**\n")
        print("1. Register\n2. Login\n3. Exit\n")
        choice = input("\nChoose an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            user_email = login()
            if user_email:
                while True:
                    print("\n1. Create Project\n2. View Projects\n3. Edit Project\n4. Delete Project\n5. Search Project by Date\n6. Logout")
                    action = input("Choose an option: ")
                    if action == "1":
                        create_project(user_email)
                    elif action == "2":
                        view_projects()
                    elif action == "3":
                        edit_project(user_email)
                    elif action == "4":
                        delete_project(user_email)
                    elif action == "5":
                        search_project_by_date()
                    elif action == "6":
                        break
                    else:
                        print("Invalid choice.\n")
        elif choice == "3":
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
