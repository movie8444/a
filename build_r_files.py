import os

r_files = {
    "leapyear.R": """year = as.integer(readline("Enter a year to be checked: "))
if(year %% 4 == 0 | year %% 400 == 0){
  cat(year, "is a leap year\\n")
} else {
  cat(year, "is not a leap year\\n")
}""",
    
    "rps.R": """pch <- readline(prompt="Enter (rock, paper or scissor): ")
cat("Player chose: ", pch)
choices <- c("rock", "paper", "scissor")
cch <- sample(choices, 1)
cat("\\nComputer chose: ", cch)
if(pch == "rock" && cch == "scissor" || pch == "scissor" && cch == "paper" || pch == "paper" && cch == "rock"){
  cat("\\nPlayer wins!")
} else if(pch == cch){
  cat("\\nComputer and Player made the same choice. There is a tie.")
} else {
  cat("\\nComputer wins!")
}""",

    "switch.R": """n = as.integer(readline("Enter a number between 1-10: "))
word <- switch(as.character(n),
  "1" = print("One"), "2" = print("Two"), "3" = print("Three"),
  "4" = print("Four"), "5" = print("Five"), "6" = print("Six"),
  "7" = print("Seven"), "8" = print("Eight"), "9" = print("Nine"),
  "10" = print("Ten"), print("Invalid input")
)""",

    "whilesquare.R": """i = 11
while (i <= 20) {
  square = i * i
  cat("\\nSquare of ", i, " is: ", square)
  i = i + 1
}""",

    "forloop.R": """n = as.integer(readline("Enter the range of numbers to be printed: "))
for(i in 1:n) {
  print(i)
}""",

    "factorial.R": """x <- as.integer(readline("Enter a no: "))
while(x <= 0) {
  x <- as.integer(readline("Enter no: "))
}
if(x > 0) {
  fact <- 1
  for(i in 1:x){
    fact <- fact * i
  }
  cat("Factorial: ", fact)
}""",

    "table.R": """n = as.integer(readline("Enter the no whose multiplication table is to be displayed: "))
for(i in 1:10) {
  cat("\\n", n, " x ", i, " = ", n * i)
}""",

    "flower.R": """flist = c("Lily", "Rose", "Jasmine", "Tulip")
print(flist)
fname = readline("Enter flower name: ")
if(fname %in% flist){
  print("Entered flower present in the list")
} else {
  print("Entered flower is not present in the list")
}""",

    "uppercase.R": """string = readline("Enter a string: ")
cat("Upper case: ", toupper(string))
cat("\\nLower case: ", tolower(string))
library(tools)
cat("\\nTitle case: ", toTitleCase(string))""",

    "palindrome.R": """library(stringi)
string = readline("Enter a string: ")
cat("Length of the string is: ", nchar(string))
rev_str = stri_reverse(string)
cat("\\nReversed string: ", rev_str)
if(string == rev_str){
  cat("\\nPalindrome")
} else {
  cat("\\nNot a palindrome")
}""",

    "pythagoras.R": """pytriplet = function(a, b, c){
  if(a^2 + b^2 == c^2){ return (TRUE) } else { return (FALSE) }
}
x = as.integer(readline("Enter number1: "))
y = as.integer(readline("Enter number2: "))
z = as.integer(readline("Enter number3: "))
if(pytriplet(x, y, z)){ print("It is a Pythagorean triplet") } else { print("It is not a Pythagorean triplet") }""",

    "sort.R": """n <- as.integer(readline("Enter size of array: "))
arr <- numeric(n)
for(i in 1:n){ arr[i] <- as.integer(readline("Enter number: ")) }
print(arr)
cat("\\n sorted array elements (ascending) are as follows: ")
print(sort(arr))
cat("\\n sorted array elements (descending) are as follows: ")
print(sort(arr, decreasing=TRUE))""",

    "perfect.R": """isPerfect <- function(n) {
  sum <- 0
  for (i in 1:(n - 1)) {
    if (n %% i == 0) { sum <- sum + i }
  }
  if (n == sum) { return(TRUE) } else { return(FALSE) }
}
num <- as.integer(readline("Enter number: "))
if (isPerfect(num)) { print("Number is perfect") } else { print("Number is not a perfect number") }""",

    "armstrong.R": """isArmstrong <- function(n, p) {
  n1 <- n; sum <- 0
  while (n1 != 0) {
    digit <- n1 %% 10
    sum <- sum + digit^p
    n1 <- as.integer(n1 / 10)
  }
  if (sum == n) { return(TRUE) } else { return(FALSE) }
}
num <- as.integer(readline("Enter number: "))
count <- 0; n1 <- num
while (n1 != 0) { n1 <- as.integer(n1 / 10); count <- count + 1 }
if (isArmstrong(num, count)) { cat("Number", num, "is Armstrong\\n") } else { cat("Number", num, "is not Armstrong\\n") }""",

    "studentdf.R": """rollno <- c(401, 402, 403, 404, 405)
name <- c("Isha", "Dania", "Tanvi", "Salome", "Saihah")
age <- c(19, 18, 19, 20, 19)
class <- c("SY", "SY", "TY", "SY", "TY")
cgpa <- c(8.6, 9.3, 8.8, 7.8, 9.2)
student <- data.frame(rollno, name, age, class, cgpa)
print(student)
print(class(student))
cat("\\nThe structure of the dataframe is as follows:\\n")
str(student)""",

    "matrixcalc.R": """m1 <- matrix(c(2, 3, 4, 1), nrow = 2, byrow = TRUE)
m2 <- matrix(c(3, 2, 2, 1), nrow = 2, byrow = TRUE)
cat("\\n Matrix addition:\\n"); print(m1 + m2)
cat("\\n Matrix transpose:\\n"); print(t(m1))
cat("\\n Matrix inverse:\\n"); print(solve(m1))
cat("\\n Matrix multiplication:\\n"); print(m1 %*% m2)""",

    "determinant.R": """n <- as.integer(readline("Enter the order of the square matrix: "))
cat("Enter the elements of the matrix:\\n")
mat <- matrix(0, nrow = n, ncol = n)
for (i in 1:n) {
  for (j in 1:n) { mat[i, j] <- as.numeric(readline(paste("Element [", i, ",", j, "]: ", sep = ""))) }
}
cat("\\nMatrix:\\n"); print(mat)
determinant_value <- det(mat)
cat("\\nDeterminant of the matrix =", determinant_value, "\\n")""",

    "vecstats.R": """data <- c(12, 15, 18, 20, 22, 25, 25, 28, 30, 35, 40)
cat("Mean =", mean(data), "\\n")
cat("Median =", median(data), "\\n")
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}
cat("Mode =", getmode(data), "\\n")
cat("Quartiles:\\n"); print(quantile(data))
cat("Range =", range(data), "\\n")
cat("Inter-Quartile Range (IQR) =", IQR(data), "\\n")
hist(data, main = "Histogram of Data", xlab = "Values", ylab = "Frequency")""",

    "dfstats.R": """student <- data.frame(
  RollNo = c(101, 102, 103, 104, 105, 106, 107, 108),
  Name = c("Manish", "Sandesh", "Mathias", "Akash", "Veer", "Aadarsh", "Ravi", "Vipul"),
  Age = c(18, 19, 20, 18, 21, 20, 19, 18),
  Class = c("FY", "FY", "SY", "SY", "TY", "TY", "FY", "SY"),
  CGPA = c(8.2, 7.8, 9.1, 8.5, 7.8, 9.3, 8.2, 8.8)
)
getMode <- function(x) { ux <- unique(x); ux[which.max(tabulate(match(x, ux)))] }
cat("AGE Statistics\\nMean:", mean(student$Age), "\\nMedian:", median(student$Age), "\\nMode:", getMode(student$Age), "\\n")
print(quantile(student$Age))
cat("Range:", range(student$Age), "\\nIQR:", IQR(student$Age), "\\n")
cat("\\nCGPA Statistics\\nMean:", mean(student$CGPA), "\\nMedian:", median(student$CGPA), "\\nMode:", getMode(student$CGPA), "\\n")
print(quantile(student$CGPA))
cat("Range:", range(student$CGPA), "\\nIQR:", IQR(student$CGPA), "\\n")
par(mfrow = c(1, 2))
hist(student$Age, main = "Histogram of Age", xlab = "Age")
hist(student$CGPA, main = "Histogram of CGPA", xlab = "CGPA")""",

    "writecsv.R": """student <- data.frame(
  RollNo = c(101, 102, 103, 104, 105),
  Name = c("Akash", "Veer", "Aadarsh", "Ravi", "Vipul"),
  Age = c(18, 19, 20, 18, 21),
  Class = c("FY", "FY", "SY", "SY", "TY"),
  CGPA = c(8.2, 7.8, 9.1, 8.5, 8.9)
)
print(student)
write.csv(student, "student.csv", row.names = FALSE)""",

    "readcsv.R": """student <- read.csv("student.csv")
print(student)
getMode <- function(x) { ux <- unique(x); ux[which.max(tabulate(match(x, ux)))] }
cat("AGE Mean:", mean(student$Age), "\\n")
cat("CGPA Mean:", mean(student$CGPA), "\\n")""",

    "variance.R": """student <- read.csv("student.csv")
cat("\\nStandard Deviation\\nAge =", sd(student$Age), "\\nCGPA =", sd(student$CGPA), "\\n")
cat("\\nVariance\\nAge =", var(student$Age), "\\nCGPA =", var(student$CGPA), "\\n")
cat("\\nCovariance (Age and CGPA)\\n", cov(student$Age, student$CGPA), "\\n")""",

    "skewness.R": """library(moments)
student <- read.csv("student.csv")
cat("Skewness of Age =", skewness(student$Age), "\\n")
cat("Skewness of CGPA =", skewness(student$CGPA), "\\n")
par(mfrow = c(1, 2))
hist(student$Age, main = "Age Distribution", xlab = "Age")
hist(student$CGPA, main = "CGPA Distribution", xlab = "CGPA")""",

    "ztest_dia.R": """mu <- 3; s <- 0.01; n <- 900; Xbar <- 2.99
zCal <- (Xbar - mu) / (s / sqrt(n))
alpha <- 0.01
zTab <- qnorm(1 - alpha / 2)
cat("Z Score:", zCal, "\\nCritical Value:", zTab, "\\n")
if (abs(zCal) < zTab) { print("Accept H0: Diameter is 3 cm") } else { print("Accept H1: Diameter is not 3 cm") }""",

    "ztest_wt.R": """mu <- 60; s <- 4; n <- 100; Xbar <- 58
zCal <- (Xbar - mu) / (s / sqrt(n))
alpha <- 0.01
zTab <- qnorm(1 - alpha / 2)
cat("Z Score:", zCal, "\\nCritical Value:", zTab, "\\n")
if (abs(zCal) < zTab) { print("Accept H0: MU is equal to 60kg.") } else { print("Accept H1: MU is not equal to 60kg.") }""",

    "ztest_dec.R": """mu <- 1800; sigma <- 100; n <- 50; Xbar <- 1780
zCal <- (Xbar - mu) / (sigma / sqrt(n))
alpha <- 0.05
zTab <- qnorm(1 - alpha)
cat("Z Score:", zCal, "\\nCritical Value:", zTab, "\\n")
if (abs(zCal) < zTab) { print("Accept H0: Not decreased.") } else { print("Accept H1: Decreased.") }""",

    "ztest_inc.R": """mu <- 1800; sigma <- 100; n <- 50; Xbar <- 1850
zCal <- (Xbar - mu) / (sigma / sqrt(n))
alpha <- 0.05
zTab <- qnorm(1 - alpha)
cat("Z Score:", zCal, "\\nCritical Value:", zTab, "\\n")
if (abs(zCal) < zTab) { print("Accept H0: Not increased.") } else { print("Accept H1: Increased.") }""",

    "ztest_diff.R": """mu <- 1800; sigma <- 100; n <- 50; Xbar <- 1850
zCal <- (Xbar - mu) / (sigma / sqrt(n))
alpha <- 0.05
zTab <- qnorm(1 - alpha / 2)
cat("Z Score:", zCal, "\\nCritical Value:", zTab, "\\n")
if (abs(zCal) < zTab) { print("Accept H0: Not changed.") } else { print("Accept H1: Changed.") }""",

    "ttest_same.R": """mu <- 1120; sigma <- 125; n <- 8; Xbar <- 1030
tCal <- (Xbar - mu) / (sigma / sqrt(n - 1))
alpha <- 0.05; df <- n - 1
tTab <- qt(1 - alpha / 2, df)
cat("T Score:", tCal, "\\nCritical Value:", tTab, "\\n")
if (abs(tCal) < tTab) { print("Accept H0: Not changed.") } else { print("Accept H1: Changed.") }""",

    "ttest_dec.R": """mu <- 1120; sigma <- 125; n <- 8; Xbar <- 1030
alpha <- 0.05; df <- n - 1
tCal <- (Xbar - mu) / (sigma / sqrt(n - 1))
tTab <- qt(1 - alpha / 2, df)
cat("T Score:", tCal, "\\nCritical Value:", tTab, "\\n")
if (abs(tCal) < tTab) { print("Accept H0: Equal to 1120") } else { print("Accept H1: Less than 1120") }""",

    "ttest_inc.R": """mu <- 1120; sigma <- 125; n <- 8; Xbar <- 1030 
alpha <- 0.05; df <- n - 1
tCal <- (Xbar - mu) / (sigma / sqrt(n - 1))
tTab <- qt(1 - alpha / 2, df)
cat("T Score:", tCal, "\\nCritical Value:", tTab, "\\n")
if (abs(tCal) < tTab) { print("Accept H0: Equal to 1120") } else { print("Accept H1: Less than 1120") }""",

    "chi_mtcars.R": """library(datasets); data("mtcars")
mtcars$mpg_cat <- cut(mtcars$mpg, breaks = c(0, 20, 30, Inf), labels = c("Low", "Medium", "High"), right = FALSE)
contingency_table <- table(mtcars$cyl, mtcars$mpg_cat)
print(contingency_table)
chisq_test_result = chisq.test(contingency_table)
print(chisq_test_result)""",

    "chi_hair.R": """library(datasets); data(HairEyeColor)
contingency_table <- margin.table(HairEyeColor, c("Hair", "Eye"))
print(contingency_table)
chi_square_test <- chisq.test(contingency_table)
print(chi_square_test)""",

    "chi_faith.R": """data("faithful"); head(faithful)
wait_breaks <- c(40, 50, 60, 70, Inf)
erupt_breaks <- c(1.5, 2.0, 2.5, 3.0, Inf)
faithful$wait_cat <- cut(faithful$waiting, breaks = wait_breaks, labels = c("40-50", "50-60", "60-70", "70 above"))
faithful$erupt_cat <- cut(faithful$eruptions, breaks = erupt_breaks, labels = c("1.5-2.0", "2.0-2.5", "2.5-3.0", "3.0 above"))
contingency_table <- table(faithful$wait_cat, faithful$erupt_cat)
print(contingency_table)
chi_square_test <- chisq.test(contingency_table)
print(chi_square_test)""",

    "binomial.R": """size <- 10; prob <- 0.5
cat("Probability of exactly 3 successes:", dbinom(3, size, prob), "\\n")
cat("Cumulative probability of up to 3 successes:", pbinom(3, size, prob), "\\n")
cat("Number of successes corresponding to a cumulative probability of 0.5:", qbinom(0.5, size, prob), "\\n")
cat("5 random binomial variates:", rbinom(5, size, prob), "\\n")""",

    "normal.R": """cat(dnorm(0, mean = 0, sd = 1), "\\n")
cat(pnorm(1, mean = 0, sd = 1), "\\n")
cat(qnorm(0.95, mean = 0, sd = 1), "\\n")
cat(rnorm(5, mean = 0, sd = 1), "\\n")""",

    "reg_simple.R": """library(ggplot2)
x = c(1, 2, 3, 4, 5); y = c(1, 5, 8, 15, 26)
df <- data.frame(x, y)
linear_model <- lm(y ~ x^2, data = df)
summary(linear_model)
plot(x, y)""",

    "reg_faith.R": """library(ggplot2); data("faithful")
linear_model <- lm(waiting ~ eruptions, data = faithful)
summary(linear_model)
plot(faithful$eruptions, faithful$waiting, xlab = "Eruption Duration(mins)", ylab = "Waiting time (mins)", main = "Faithful Geyser: Waiting Time vs. Eruption Duration")
abline(linear_model, col = "red", lwd = 2)""",

    "reg_mtcars.R": """library(ggplot2); data(mtcars)
linear_model <- lm(mpg ~ hp + cyl + disp + wt, data = mtcars)
summary(linear_model)
predicted_mpg <- predict(linear_model)
plot(mtcars$mpg, predicted_mpg, main = "Actual vs Predicted MPG", xlab = "Actual MPG", ylab = "Predicted MPG", pch = 19, col = "blue")
abline(0, 1, col = "red", lwd = 2)""",

    "reg_salary.R": """salaryinfo <- data.frame(
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
abline(0, 1, col = "red", lwd = 2)""",

    "traintest.R": """salaryinfo <- data.frame(
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
cat("Predicted Salary:", predict(model, newdata = new_observation), "\\n")""",

    "reg_wt.R": """model <- lm(mpg ~ wt, data = mtcars)
summary_model <- summary(model)
print(paste("R-Squared: ", summary_model$r.squared))
print(paste("Adjusted R-Squared: ", summary_model$adj.r.squared))
print(paste("Residual Standard Error: ", summary_model$sigma))
new_observation <- data.frame(wt = 3)
print(paste("Predicted MPG: ", predict(model, newdata = new_observation)))"""
}

# Create all files in the current directory
for filename, code in r_files.items():
    with open(filename, "w") as file:
        file.write(code.strip() + "\n")
    print(f"Generated: {filename}")

print("\nSuccess! All 42 files have been created.")
