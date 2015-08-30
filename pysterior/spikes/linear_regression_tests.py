# This is a pilot of encapsulating pymc3 models
import unittest
import numpy as np
from linear_regression import LinearRegression

class LinearRegressionTest(unittest.TestCase):
    def test_multiple_linear_regression(self):
        np.random.seed(123)
        TRUE_ALPHA, TRUE_SIGMA = 1, 1
        TRUE_BETA = [1, 2.5]
        size = 100
        X1 = np.linspace(0, 1, size)
        X2 = np.linspace(0,.2, size)
        y = TRUE_ALPHA + TRUE_BETA[0]*X1 + TRUE_BETA[1]*X2 + np.random.randn(size)*TRUE_SIGMA

        X = np.array(list(zip(X1, X2)))

        lr = LinearRegression()
        lr.fit(X, y, 10000)
        samples = lr.get_samples()
        map_estimate = lr.get_map_estimate()
        expected_map = {'alpha': np.array(1.014043926179071), 'beta': np.array([ 1.46737108,  0.29347422]), 'sigma_log': np.array(0.11928775836956886)}
        self.assertAlmostEqual(float(map_estimate['alpha']), float(expected_map['alpha']), delta=1e-1)
        for true_beta, map_beta in zip(map_estimate['beta'], expected_map['beta']):
            self.assertAlmostEqual(true_beta, map_beta, delta=1e-1)
        test_point = X[7]
        true_y = TRUE_ALPHA + TRUE_BETA[0]*test_point[0] + TRUE_BETA[1]*test_point[1]
        print(true_y)
        predicted_y = lr.predict(test_point)
        print(predicted_y)
        self.assertAlmostEqual(true_y, predicted_y, delta=1e-1)

    def test_simple_linear_regression(self):
        np.random.seed(123)
        TRUE_ALPHA, TRUE_SIGMA = 1, 1
        TRUE_BETA = 2.5
        size = 100
        X = np.linspace(0, 1, size)
        noise = (np.random.randn(size)*TRUE_SIGMA)
        y = (TRUE_ALPHA + TRUE_BETA*X + noise)

        lr = LinearRegression()
        lr.fit(X, y, 2000)
        test_point = X[7]
        true_y = TRUE_ALPHA + TRUE_BETA*test_point
        print(true_y)
        predicted_y = lr.predict(test_point)
        print(predicted_y)
        self.assertAlmostEqual(true_y, predicted_y, delta=1e-1)
        # predicted_line = [lr.predict(x) for x in X]
        # plt.plot(X, y, linewidth=0.0, marker='x', color='g')
        # plt.plot(X, predicted_line)
        # plt.show()


if __name__ == '__main__':
    unittest.main()

