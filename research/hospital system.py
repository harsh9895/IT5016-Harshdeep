'''
Author: Harshdeep Banga

'''
class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_admitted = False

    def admit(self):
        self.is_admitted = True
        print(f"{self.name} has been admitted to the hospital.")

    def discharge(self):
        self.is_admitted = False
        print(f"{self.name} has been discharged from the hospital.")


class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def treat(self, patient):
        if patient.is_admitted:
            print(f"Doctor {self.name} is treating {patient.name}.")
        else:
            print(f"{patient.name} is not admitted to the hospital.")


class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []

    def admit_patient(self, patient):
        patient.admit()
        self.patients.append(patient)

    def discharge_patient(self, patient):
        patient.discharge()
        self.patients.remove(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Doctor {doctor.name} has been added to {self.name}.")

    def list_patients(self):
        if not self.patients:
            print("No patients admitted.")
        else:
            print("Admitted Patients:")
            for patient in self.patients:
                print(f"- {patient.name}, Age: {patient.age}")

    def list_doctors(self):
        if not self.doctors:
            print("No doctors available.")
        else:
            print("Available Doctors:")
            for doctor in self.doctors:
                print(f"- Dr. {doctor.name}, Specialty: {doctor.specialty}")


def main():
    my_hospital = Hospital("City Hospital")

    while True:
        print("\n--- Hospital Management System ---")
        print("1. Add Doctor")
        print("2. Admit Patient")
        print("3. Discharge Patient")
        print("4. Treat Patient")
        print("5. List Patients")
        print("6. List Doctors")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter doctor's name: ")
            specialty = input("Enter doctor's specialty: ")
            doctor = Doctor(name, specialty)
            my_hospital.add_doctor(doctor)

        elif choice == '2':
            name = input("Enter patient's name: ")
            age = int(input("Enter patient's age: "))
            patient = Patient(name, age)
            my_hospital.admit_patient(patient)

        elif choice == '3':
            name = input("Enter patient's name to discharge: ")
            patient = next((p for p in my_hospital.patients if p.name == name), None)
            if patient:
                my_hospital.discharge_patient(patient)
            else:
                print("Patient not found.")

        elif choice == '4':
            patient_name = input("Enter patient's name to treat: ")
            doctor_name = input("Enter doctor's name: ")
            patient = next((p for p in my_hospital.patients if p.name == patient_name), None)
            doctor = next((d for d in my_hospital.doctors if d.name == doctor_name), None)
            if patient and doctor:
                doctor.treat(patient)
            else:
                print("Patient or doctor not found.")

        elif choice == '5':
            my_hospital.list_patients()

        elif choice == '6':
            my_hospital.list_doctors()

        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
