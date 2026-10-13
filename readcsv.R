student <- read.csv("student.csv")
print(student)
getMode <- function(x) { ux <- unique(x); ux[which.max(tabulate(match(x, ux)))] }
cat("AGE Mean:", mean(student$Age), "\n")
cat("CGPA Mean:", mean(student$CGPA), "\n")
