isArmstrong <- function(n, p) {
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
if (isArmstrong(num, count)) { cat("Number", num, "is Armstrong\n") } else { cat("Number", num, "is not Armstrong\n") }
