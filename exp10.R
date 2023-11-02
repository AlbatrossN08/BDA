library(datasets)
library(caret)
library(ggplot2)

# Load the mtcars dataset
data <- mtcars

# Split the data into training and testing sets
set.seed(123)
train_index <- sample(seq_len(nrow(data)), nrow(data) * 0.8)
train_data <- data[train_index, ]
test_data <- data[-train_index, ]

# Choose a predictive analytics technique
# Linear regression
model <- lm(mpg ~ disp + hp, data = train_data)

# Evaluate the predictive model on the testing set
predictions <- predict(model, test_data)
rmse <- sqrt(mean((predictions - test_data$mpg)^2))
print(rmse)

# Add a plot of the training data with the regression line
ggplot(train_data, aes(x = disp, y = mpg)) +
  geom_point() +
  stat_smooth(method = "lm", col = "red")

# Save the plot to a file
ggsave("plot.png")

# Deploy the predictive model
save(model, file = "model.rds")
