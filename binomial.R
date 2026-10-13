size <- 10; prob <- 0.5
cat("Probability of exactly 3 successes:", dbinom(3, size, prob), "\n")
cat("Cumulative probability of up to 3 successes:", pbinom(3, size, prob), "\n")
cat("Number of successes corresponding to a cumulative probability of 0.5:", qbinom(0.5, size, prob), "\n")
cat("5 random binomial variates:", rbinom(5, size, prob), "\n")
