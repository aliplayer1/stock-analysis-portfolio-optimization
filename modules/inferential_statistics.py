import numpy as np
import scipy.stats as stats

class InferentialStatistics:
    def __init__(self, returns_data):
        self.returns_data = returns_data
    
    def confidence_interval(self, confidence=0.95):
        # Calculate confidence interval for mean of returns
        n = len(self.returns_data)
        mean = np.mean(self.returns_data)
        stderr = stats.sem(self.returns_data)
        h = stderr * stats.t.ppf((1 + confidence) / 2, n - 1)
        return mean - h, mean + h
    
    def t_test_mean(self, population_mean=0):
        # Perform t-test to check if the mean of returns is significantly different from population mean
        t_stat, p_value = stats.ttest_1samp(self.returns_data, population_mean)
        return t_stat, p_value
    
    def anova_test(self, *args):
        # Perform ANOVA to compare means across multiple datasets
        return stats.f_oneway(*args)
    
    def correlation_test(self, other_data, method='pearson'):
        # Perform correlation test between two datasets (returns of two stocks)
        if method == 'pearson':
            return stats.pearsonr(self.returns_data, other_data)
        elif method == 'spearman':
            return stats.spearmanr(self.returns_data, other_data)
        else:
            raise ValueError("Method should be 'pearson' or 'spearman'")
    
    def linear_regression(self, independent_data):
        # Perform linear regression between stock returns and an independent variable (e.g., market index)
        slope, intercept, r_value, p_value, std_err = stats.linregress(independent_data, self.returns_data)
        return slope, intercept, r_value, p_value, std_err
