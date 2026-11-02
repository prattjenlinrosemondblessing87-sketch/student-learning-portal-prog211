class Course:
    def __init__(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits

    def get_course_details(self):
        return (self.course_code, self.course_name, self.credits)


class Student:
    total_students_enrolled = 0

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = {}
        Student.total_students_enrolled += 1

    def update_record(self, new_name):
        old_name = self.name
        self.name = new_name
        print(f"   [Update] Student ID {self.student_id} changed name from '{old_name}' to '{new_name}'.")

    def enroll_in_course(self, course_object):
        self.enrolled_courses[course_object.course_code] = course_object
        print(f"   [Success] {self.name} successfully enrolled in {course_object.course_name}.")

    def display_info(self):
        print(f"\n--- Student Profile (ID: {self.student_id}) ---")
        print(f"Name: {self.name}")
        print("Enrolled Courses:")
        if not self.enrolled_courses:
            print("  No courses enrolled yet.")
        for course in self.enrolled_courses.values():
            code, title, units = course.get_course_details()
            print(f"  - {code}: {title} ({units} Credits)")

    @classmethod
    def get_global_enrollment_count(cls):
        return cls.total_students_enrolled

    @staticmethod
    def validate_student_id(student_id):
        return student_id.startswith("LU-SL-")


student_directory = {}

def add_student_record(student_id, name):
    if not Student.validate_student_id(student_id):
        print(f"   [Error] Rejecting ID '{student_id}'. Must start with 'LU-SL-'.")
        return

    if student_id in student_directory:
        print(f"   [Error] Student ID {student_id} already exists.")
    else:
        new_student = Student(student_id, name)
        student_directory[student_id] = new_student
        print(f"System: Added student {name} to the registry.")

def display_all_records():
    print("\n=============================================")
    print("      ONLINE LEARNING PORTAL REGISTRY        ")
    print("=============================================")
    for student_id, student_obj in student_directory.items():
        student_obj.display_info()
    print("=============================================")


if __name__ == "__main__":
    print("Initializing Student Learning Portal...\n")

    oop1 = Course("PROG211", "Object-Oriented Programming 1", 4)
    dsa = Course("COMP203", "Data Structures & Algorithms", 3)

    print("Testing Security ID Validation (Static Method):")
    add_student_record("BAD-ID-123", "Invalid User Example")
    add_student_record("LU-SL-001", "Alex Demo")
    add_student_record("LU-SL-002", "Sam Sample")

    print("\nUpdating an Existing Student Record:")
    student_directory["LU-SL-001"].update_record("Alex Demo-Brown")

    print("\nProcessing Course Enrolments...")
    student_directory["LU-SL-001"].enroll_in_course(oop1)
    student_directory["LU-SL-001"].enroll_in_course(dsa)
    student_directory["LU-SL-002"].enroll_in_course(oop1)

    display_all_records()

    total = Student.get_global_enrollment_count()
    print(f"DPG Global Metric - Total System Users: {total}\n")