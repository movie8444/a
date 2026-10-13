mu <- 1800; sigma <- 100; n <- 50; Xbar <- 1850
zCal <- (Xbar - mu) / (sigma / sqrt(n))
alpha <- 0.05
zTab <- qnorm(1 - alpha / 2)
cat("Z Score:", zCal, "\nCritical Value:", zTab, "\n")
if (abs(zCal) < zTab) { print("Accept H0: Not changed.") } else { print("Accept H1: Changed.") }
