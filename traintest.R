salaryinfo <- data.frame(
  experience = c(1, 2, 3, 4, 5),
  education = c("HSC", "PG", "UG", "SSC", "Phd"),
  industry = c("Health", "Finance", "IT", "Health", "Finance"),
  salary = c(25000, 30000, 35000, 42000, 48000)
)
write.csv(salaryinfo, "salaryinfo.csv", row.names = FALSE)
data <- read.csv("salaryinfo.csv")
data$education <- as.numeric(factor(data$education, levels = c("HSC", "SSC", "PG", "UG", "Phd")))
data$industry <- as.numeric(factor(data$industry, levels = c("IT", "Health", "Finance")))
set.seed(123)
train_index <- sample(nrow(data), size = floor(0.8 * nrow(data)))
test_index <- setdiff(1:nrow(data), train_index)
train_data <- data[train_index, ]; test_data <- data[test_index, ]
model <- lm(salary ~ experience + education + industry, data = train_data)
test_predictions <- predict(model, newdata = test_data)
mse <- mean((test_data$salary - test_predictions)^2)
print(paste("Root Mean Squared Error (RMSE):", sqrt(mse)))
new_observation <- data.frame(experience = 2, education = 4, industry = 1)
cat("Predicted Salary:", predict(model, newdata = new_observation), "\n")
