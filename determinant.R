n <- as.integer(readline("Enter the order of the square matrix: "))
cat("Enter the elements of the matrix:\n")
mat <- matrix(0, nrow = n, ncol = n)
for (i in 1:n) {
  for (j in 1:n) { mat[i, j] <- as.numeric(readline(paste("Element [", i, ",", j, "]: ", sep = ""))) }
}
cat("\nMatrix:\n"); print(mat)
determinant_value <- det(mat)
cat("\nDeterminant of the matrix =", determinant_value, "\n")
