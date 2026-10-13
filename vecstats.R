data <- c(12, 15, 18, 20, 22, 25, 25, 28, 30, 35, 40)
cat("Mean =", mean(data), "\n")
cat("Median =", median(data), "\n")
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}
cat("Mode =", getmode(data), "\n")
cat("Quartiles:\n"); print(quantile(data))
cat("Range =", range(data), "\n")
cat("Inter-Quartile Range (IQR) =", IQR(data), "\n")
hist(data, main = "Histogram of Data", xlab = "Values", ylab = "Frequency")
