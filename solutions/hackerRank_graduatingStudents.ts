export function gradingStudents(grades: number[]): number[] {
    const newGrade: number[] = []
    grades.forEach((grade, index) => {
        if (grade >= 38 && (grade % 5) >= 3) {
            while (grade % 5 != 0) {
                grade++;
            }
            newGrade[index] = grade
        } else newGrade[index] = grade
    })
    return newGrade;
}