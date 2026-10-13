student <- data.frame(
  RollNo = c(101, 102, 103, 104, 105, 106, 107, 108),
  Name = c("Manish", "Sandesh", "Mathias", "Akash", "Veer", "Aadarsh", "Ravi", "Vipul"),
  Age = c(18, 19, 20, 18, 21, 20, 19, 18),
  Class = c("FY", "FY", "SY", "SY", "TY", "TY", "FY", "SY"),
  CGPA = c(8.2, 7.8, 9.1, 8.5, 7.8, 9.3, 8.2, 8.8)
)
getMode <- function(x) { ux <- unique(x); ux[which.max(tabulate(match(x, ux)))] }
cat("AGE Statistics\nMean:", mean(student$Age), "\nMedian:", median(student$Age), "\nMode:", getMode(student$Age), "\n")
print(quantile(student$Age))
cat("Range:", range(student$Age), "\nIQR:", IQR(student$Age), "\n")
cat("\nCGPA Statistics\nMean:", mean(student$CGPA), "\nMedian:", median(student$CGPA), "\nMode:", getMode(student$CGPA), "\n")
print(quantile(student$CGPA))
cat("Range:", range(student$CGPA), "\nIQR:", IQR(student$CGPA), "\n")
par(mfrow = c(1, 2))
hist(student$Age, main = "Histogram of Age", xlab = "Age")
hist(student$CGPA, main = "Histogram of CGPA", xlab = "CGPA")
