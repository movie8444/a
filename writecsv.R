student <- data.frame(
  RollNo = c(101, 102, 103, 104, 105),
  Name = c("Akash", "Veer", "Aadarsh", "Ravi", "Vipul"),
  Age = c(18, 19, 20, 18, 21),
  Class = c("FY", "FY", "SY", "SY", "TY"),
  CGPA = c(8.2, 7.8, 9.1, 8.5, 8.9)
)
print(student)
write.csv(student, "student.csv", row.names = FALSE)
