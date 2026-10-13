mu <- 60; s <- 4; n <- 100; Xbar <- 58
zCal <- (Xbar - mu) / (s / sqrt(n))
alpha <- 0.01
zTab <- qnorm(1 - alpha / 2)
cat("Z Score:", zCal, "\nCritical Value:", zTab, "\n")
if (abs(zCal) < zTab) { print("Accept H0: MU is equal to 60kg.") } else { print("Accept H1: MU is not equal to 60kg.") }
