from typing import List, Dict, Tuple, Any

def calculate_active_student_metrics(
    students: List[Dict[str, Any]], 
    target_status: str = 'A'
) -> Tuple[float, List[str]]:
    """Filters students by status, returns their average grade and capitalized names.
    
    Args:
        students: List of student records with name ('n'), grade ('g'), status ('s').
        target_status: The status code to filter by (default 'A').
        
    Returns:
        A tuple of (average_grade, list_of_names).
    """
    if not students:
        return 0.0, []

    matching_students = [s for s in students if s.get('s') == target_status]
    if not matching_students:
        return 0.0, []

    total_grade = sum(s.get('g', 0) for s in matching_students)
    average_grade = round(total_grade / len(matching_students), 2)
    student_names = [s.get('n', '').title() for s in matching_students]

    return average_grade, student_names

if __name__ == "__main__":
    sample_data = [
        {'n': 'alice', 'g': 85, 's': 'A'},
        {'n': 'bob', 'g': 72, 's': 'B'},
        {'n': 'vedanshi', 'g': 92, 's': 'A'}
    ]
    avg, names = calculate_active_student_metrics(sample_data)
    print(f"Refactored Output -> Average: {avg}, Students: {names}")
