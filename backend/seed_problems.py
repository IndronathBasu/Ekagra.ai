"""
Seed script to add sample problems and test cases to the database.
Run this to populate your database with example problems for testing.
"""
import sys
from pathlib import Path

# Add backend to path
sys.path.append(str(Path(__file__).parent))

from app.core.database import SessionLocal
from app.models.problem import Problem
from app.models.test_case import TestCase

def seed_problems():
    """Add sample problems to the database."""
    db = SessionLocal()
    
    try:
        # Check if problems already exist
        existing = db.query(Problem).count()
        if existing > 0:
            print(f"[WARNING] Database already has {existing} problems.")
            response = input("Do you want to add more? (y/n): ")
            if response.lower() != 'y':
                print("Skipping seed.")
                return
        
        print("[INFO] Seeding problems and test cases...")
        
        # Problem 1: Hello World (Easy)
        problem1 = Problem(
            domain="Programming",
            subject="Python",
            topic="Basics",
            cluster="Print Statements",
            question_type="coding",
            cognitive_dimension="application",
            difficulty_band=1,
            super_band=1,
            concepts=["stdout", "print"],
            skills_tested=["print"],
            problem_statement="""Write a Python program that prints 'Hello, World!' to the console.

**Requirements:**
- Use the print() function
- Output exactly: Hello, World!

**Example:**
When you run your program, it should output:
```
Hello, World!
```""",
            example_input="",
            example_output="Hello, World!",
            estimated_time_seconds=60,
            mastery_weight=1.0,
            metadata_={}
        )
        db.add(problem1)
        db.flush()  # Get the ID
        
        # Test cases for Problem 1
        test_case_1_1 = TestCase(
            problem_id=problem1.id,
            input_data="",
            expected_output="Hello, World!",
            is_hidden=False
        )
        db.add(test_case_1_1)
        
        # Problem 2: Sum Two Numbers (Easy)
        problem2 = Problem(
            domain="Programming",
            subject="Python",
            topic="Basics",
            cluster="Arithmetic Operations",
            question_type="coding",
            cognitive_dimension="application",
            difficulty_band=1,
            super_band=1,
            concepts=["arithmetic", "addition", "input"],
            skills_tested=["arithmetic", "input"],
            problem_statement="""Write a Python program that reads two integers from input and prints their sum.

**Requirements:**
- Read two integers from standard input
- Calculate and print their sum

**Example Input:**
```
5
3
```

**Example Output:**
```
8
```""",
            example_input="5\n3",
            example_output="8",
            estimated_time_seconds=120,
            mastery_weight=1.5,
            metadata_={}
        )
        db.add(problem2)
        db.flush()
        
        # Test cases for Problem 2
        test_case_2_1 = TestCase(
            problem_id=problem2.id,
            input_data="5\n3",
            expected_output="8",
            is_hidden=False
        )
        test_case_2_2 = TestCase(
            problem_id=problem2.id,
            input_data="10\n20",
            expected_output="30",
            is_hidden=True
        )
        test_case_2_3 = TestCase(
            problem_id=problem2.id,
            input_data="-5\n5",
            expected_output="0",
            is_hidden=True
        )
        db.add_all([test_case_2_1, test_case_2_2, test_case_2_3])
        
        # Problem 3: Check Even or Odd (Easy)
        problem3 = Problem(
            domain="Programming",
            subject="Python",
            topic="Conditionals",
            cluster="If-Else Statements",
            question_type="coding",
            cognitive_dimension="application",
            difficulty_band=1,
            super_band=1,
            concepts=["conditionals", "modulo", "if-else"],
            skills_tested=["conditionals", "modulo"],
            problem_statement="""Write a Python program that reads an integer and prints "Even" if it's even, or "Odd" if it's odd.

**Requirements:**
- Read an integer from input
- Use modulo operator (%) to check if number is even
- Print "Even" or "Odd"

**Example Input 1:**
```
4
```

**Example Output 1:**
```
Even
```

**Example Input 2:**
```
7
```

**Example Output 2:**
```
Odd
```""",
            example_input="4",
            example_output="Even",
            estimated_time_seconds=120,
            mastery_weight=2.0,
            metadata_={}
        )
        db.add(problem3)
        db.flush()
        
        # Test cases for Problem 3
        test_case_3_1 = TestCase(
            problem_id=problem3.id,
            input_data="4",
            expected_output="Even",
            is_hidden=False
        )
        test_case_3_2 = TestCase(
            problem_id=problem3.id,
            input_data="7",
            expected_output="Odd",
            is_hidden=False
        )
        test_case_3_3 = TestCase(
            problem_id=problem3.id,
            input_data="0",
            expected_output="Even",
            is_hidden=True
        )
        test_case_3_4 = TestCase(
            problem_id=problem3.id,
            input_data="15",
            expected_output="Odd",
            is_hidden=True
        )
        db.add_all([test_case_3_1, test_case_3_2, test_case_3_3, test_case_3_4])
        
        # Problem 4: Find Maximum (Medium)
        problem4 = Problem(
            domain="Programming",
            subject="Python",
            topic="Arrays",
            cluster="Finding Elements",
            question_type="coding",
            cognitive_dimension="analysis",
            difficulty_band=2,
            super_band=2,
            concepts=["arrays", "loops", "comparison"],
            skills_tested=["loops", "arrays", "comparison"],
            problem_statement="""Write a Python program that reads a list of integers and finds the maximum value.

**Requirements:**
- Read the number of elements first
- Then read that many integers
- Find and print the maximum value

**Example Input:**
```
5
3 7 2 9 1
```

**Example Output:**
```
9
```""",
            example_input="5\n3 7 2 9 1",
            example_output="9",
            estimated_time_seconds=180,
            mastery_weight=2.5,
            metadata_={}
        )
        db.add(problem4)
        db.flush()
        
        # Test cases for Problem 4
        test_case_4_1 = TestCase(
            problem_id=problem4.id,
            input_data="5\n3 7 2 9 1",
            expected_output="9",
            is_hidden=False
        )
        test_case_4_2 = TestCase(
            problem_id=problem4.id,
            input_data="3\n-5 -2 -10",
            expected_output="-2",
            is_hidden=True
        )
        test_case_4_3 = TestCase(
            problem_id=problem4.id,
            input_data="1\n42",
            expected_output="42",
            is_hidden=True
        )
        db.add_all([test_case_4_1, test_case_4_2, test_case_4_3])
        
        # Problem 5: Factorial (Medium)
        problem5 = Problem(
            domain="Programming",
            subject="Python",
            topic="Recursion",
            cluster="Mathematical Functions",
            question_type="coding",
            cognitive_dimension="synthesis",
            difficulty_band=2,
            super_band=2,
            concepts=["recursion", "factorial", "loops"],
            skills_tested=["recursion", "loops"],
            problem_statement="""Write a Python program that calculates the factorial of a number.

**Requirements:**
- Read an integer n (0 <= n <= 10)
- Calculate n! (factorial of n)
- Print the result

**Note:** 
- 0! = 1
- n! = n × (n-1) × (n-2) × ... × 1

**Example Input:**
```
5
```

**Example Output:**
```
120
```""",
            example_input="5",
            example_output="120",
            estimated_time_seconds=240,
            mastery_weight=3.0,
            metadata_={}
        )
        db.add(problem5)
        db.flush()
        
        # Test cases for Problem 5
        test_case_5_1 = TestCase(
            problem_id=problem5.id,
            input_data="5",
            expected_output="120",
            is_hidden=False
        )
        test_case_5_2 = TestCase(
            problem_id=problem5.id,
            input_data="0",
            expected_output="1",
            is_hidden=False
        )
        test_case_5_3 = TestCase(
            problem_id=problem5.id,
            input_data="3",
            expected_output="6",
            is_hidden=True
        )
        test_case_5_4 = TestCase(
            problem_id=problem5.id,
            input_data="7",
            expected_output="5040",
            is_hidden=True
        )
        db.add_all([test_case_5_1, test_case_5_2, test_case_5_3, test_case_5_4])
        
        # Commit all changes
        db.commit()
        
        print(f"[SUCCESS] Successfully seeded 5 problems with test cases!")
        print("\nProblems added:")
        print("  1. Hello World (Easy)")
        print("  2. Sum Two Numbers (Easy)")
        print("  3. Check Even or Odd (Easy)")
        print("  4. Find Maximum (Medium)")
        print("  5. Factorial (Medium)")
        
    except Exception as e:
        db.rollback()
        print(f"[ERROR] Error seeding problems: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    seed_problems()

