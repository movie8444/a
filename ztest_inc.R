mu <- 1800; sigma <- 100; n <- 50; Xbar <- 1850
zCal <- (Xbar - mu) / (sigma / sqrt(n))
alpha <- 0.05
zTab <- qnorm(1 - alpha)
cat("Z Score:", zCal, "\nCritical Value:", zTab, "\n")
if (abs(zCal) < zTab) { print("Accept H0: Not increased.") } else { print("Accept H1: Increased.") }
