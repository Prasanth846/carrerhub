from dao.database_manager import DatabaseManager
from entity.company import Company
from entity.applicant import Applicant
from entity.jobs import Jobs
from entity.application import Application

from exception.invalid_email_format import InvalidEmailFormat
from exception.salary_negative_exception import SalaryNegativeException
from exception.DeadlineOverException import DeadlineOverException

from datetime import datetime

db = DatabaseManager()

def main_menu():
    while True:
        print("\n📋 CareerHub Main Menu")
        print("1. Add Company")
        print("2. Add Applicant")
        print("3. Post a Job")
        print("4. Apply for a Job")
        print("5. View All Jobs")
        print("6. View Average Salary")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Company Name: ")
            location = input("Location: ")
            company = Company(company_name=name, location=location)
            db.insert_company(company)

        elif choice == '2':
            try:
                first = input("First Name: ")
                last = input("Last Name: ")
                email = input("Email: ")
                phone = input("Phone: ")
                resume = input("Resume Text: ")
                experience = int(input("Years of Experience: "))
                applicant = Applicant(first_name=first, last_name=last, email=email, phone=phone, resume=resume, experience=experience)
                db.insert_applicant(applicant)
            except InvalidEmailFormat as e:
                print("❌", e)
            except Exception as e:
                print("❌ Something went wrong:", e)

        elif choice == '3':
            try:
                company_id = int(input("Company ID: "))
                title = input("Job Title: ")
                description = input("Description: ")
                location = input("Job Location: ")
                salary = float(input("Salary: "))
                job_type = input("Job Type (full time / part time / contract): ")
                deadline_str = input("Application Deadline (YYYY-MM-DD): ")
                deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
                db.insert_job(company_id, title, description, location, salary, job_type, deadline)
            except SalaryNegativeException as e:
                print("❌", e)
            except Exception as e:
                print("❌ Error:", e)

        elif choice == '4':
            try:
                applicant_id = int(input("Applicant ID: "))
                job_id = int(input("Job ID: "))
                cover_letter = input("Cover Letter: ")
                db.insert_job_application(applicant_id, job_id, cover_letter)
            except DeadlineOverException as e:
                print("❌", e)
            except Exception as e:
                print("❌ Error:", e)

        elif choice == '5':
            print("\n📄 Job Listings:")
            jobs = db.get_jobs()
            for job in jobs:
                print(f"{job.job_id} | {job.job_title} | {job.job_location} | ₹{job.salary}")

        elif choice == '6':
            try:
                avg = db.calculate_average_salary()
                print(f"📊 Average Salary: ₹{avg:.2f}")
            except SalaryNegativeException as e:
                print("❌", e)

        elif choice == '7':
            db.close()
            print(" Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
