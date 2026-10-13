mu <- 3; s <- 0.01; n <- 900; Xbar <- 2.99
zCal <- (Xbar - mu) / (s / sqrt(n))
alpha <- 0.01
zTab <- qnorm(1 - alpha / 2)
cat("Z Score:", zCal, "\nCritical Value:", zTab, "\n")
if (abs(zCal) < zTab) { print("Accept H0: Diameter is 3 cm") } else { print("Accept H1: Diameter is not 3 cm") }
