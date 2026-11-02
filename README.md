# Student Learning Portal

A Python program that uses Object-Oriented Programming (OOP) to register students, update their records, and enrol them in courses. It was built for PROG211 Object-Oriented Programming 1 at Limkokwing University of Creative Technology, Sierra Leone.

## Author
- Name: Jenlin Blessing Pratt
- Module: PROG211 Object-Oriented Programming 1
- Lecturer: Amandus Benjamin Coker
- Institution: Limkokwing University of Creative Technology, Sierra Leone

## Problem Solved (Education)
Schools and universities need a simple way to keep accurate student records and track course enrolments. This portal registers students with unique IDs, rejects invalid or duplicate IDs, updates records, enrols students in courses, and displays a full registry.

## Features
- Two classes: Course and Student
- One data structure: a dictionary (student_directory) that stores students by ID
- Instance methods: update_record(), enroll_in_course(), display_info()
- Class method: get_global_enrollment_count()
- Static method: validate_student_id()
- A tuple returned by get_course_details()

## How to Run
1. Install Python 3 from https://www.python.org
2. Download learning_portal.py from this repository
3. Open a terminal in the same folder and run:

   python learning_portal.py

## Example Usage (Sample Output)

Initializing Student Learning Portal...

Testing Security ID Validation (Static Method):
   [Error] Rejecting ID 'BAD-ID-123'. Must start with 'LU-SL-'.
System: Added student Alex Demo to the registry.
System: Added student Sam Sample to the registry.

Updating an Existing Student Record:
   [Update] Student ID LU-SL-001 changed name from 'Alex Demo' to 'Alex Demo-Brown'.

Processing Course Enrolments...
   [Success] Alex Demo-Brown successfully enrolled in Object-Oriented Programming 1.
   [Success] Alex Demo-Brown successfully enrolled in Data Structures & Algorithms.
   [Success] Sam Sample successfully enrolled in Object-Oriented Programming 1.

(The registry is then displayed, ending with: DPG Global Metric - Total System Users: 2)

## How This Project Meets Digital Public Goods (DPG) Standards
- Open-source: the code is public on GitHub under the MIT Licence.
- Inclusive and accessible: plain text output with clear labels; runs on any computer with Python.
- Privacy-respecting: only fictional names and IDs are used; no sensitive personal data is stored.
- Modular and reusable: classes and functions are separate and easy to extend.
- Relevant to the SDGs: supports SDG 4, Quality Education.
- Open licence: MIT Licence (see LICENSE).
- Clear ownership: author and institution are named above.
- Platform independent: standard Python only, no paid tools or extra libraries.
- Documentation: this README and clearly named code.
- Do no harm: no personal data is stored, and invalid IDs are rejected.

## Licence
Released under the MIT Licence. See the LICENSE file.
