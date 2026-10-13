salaryinfo <- data.frame(
  experience = c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
  education = c(12, 14, 14, 16, 16, 18, 18, 20, 20, 22),
  industry = c(1, 1, 2, 2, 1, 3, 2, 3, 3, 2),
  salary = c(25000, 30000, 35000, 42000, 48000, 55000, 62000, 70000, 78000, 85000)
)
write.csv(salaryinfo, "salaryinfo.csv", row.names = FALSE)
data <- read.csv("salaryinfo.csv")
linear_model <- lm(salary ~ experience + education + industry, data = data)
summary(linear_model)
new_data <- data.frame(experience = 6, education = 18, industry = 2)
predicted_salary <- predict(linear_model)
plot(data$salary, predicted_salary, main = "Actual vs Predicted Salary", xlab = "Actual Salary", ylab = "Predicted Salary", pch = 19, col = "blue")
abline(0, 1, col = "red", lwd = 2)
