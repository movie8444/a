isPerfect <- function(n) {
  sum <- 0
  for (i in 1:(n - 1)) {
    if (n %% i == 0) { sum <- sum + i }
  }
  if (n == sum) { return(TRUE) } else { return(FALSE) }
}
num <- as.integer(readline("Enter number: "))
if (isPerfect(num)) { print("Number is perfect") } else { print("Number is not a perfect number") }
