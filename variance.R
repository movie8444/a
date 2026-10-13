student <- read.csv("student.csv")
cat("\nStandard Deviation\nAge =", sd(student$Age), "\nCGPA =", sd(student$CGPA), "\n")
cat("\nVariance\nAge =", var(student$Age), "\nCGPA =", var(student$CGPA), "\n")
cat("\nCovariance (Age and CGPA)\n", cov(student$Age, student$CGPA), "\n")
