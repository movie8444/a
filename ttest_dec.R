mu <- 1120; sigma <- 125; n <- 8; Xbar <- 1030
alpha <- 0.05; df <- n - 1
tCal <- (Xbar - mu) / (sigma / sqrt(n - 1))
tTab <- qt(1 - alpha / 2, df)
cat("T Score:", tCal, "\nCritical Value:", tTab, "\n")
if (abs(tCal) < tTab) { print("Accept H0: Equal to 1120") } else { print("Accept H1: Less than 1120") }
