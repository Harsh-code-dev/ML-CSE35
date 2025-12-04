

def mean(values):
    return sum(values) / len(values)

def covariance(x, y):
    xm = mean(x)
    ym = mean(y)
    cov = 0
    for i in range(len(x)):
        cov += (x[i] - xm) * (y[i] - ym)
    return cov

def variance(values):
    m = mean(values)
    var = 0
    for val in values:
        var += (val - m) ** 2
    return var

def train_linear_regression(x, y):
    m = covariance(x, y) / variance(x)
    b = mean(y) - m * mean(x)
    return m, b

def predict(x, m, b):
    return m * x + b



X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

m, b = train_linear_regression(X, Y)

print("Slope (m):", m)
print("Intercept (b):", b)


print("Prediction for x=6:", predict(6, m, b))
