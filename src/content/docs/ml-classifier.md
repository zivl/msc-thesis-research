---
title: "5. Machine-Learning Based Classifier – Our Proposal and Motivation"
---

While researching for a better solution to Android’s user-consent permission system, we came up with the idea of implementing a machine-learning based classifier for app trustworthiness. Having trained such classifier let us test any app against the classifier’s model and have a wiser decision whether to install an app or not, according to the classification result.

In our solution we set the following system requirements in terms of its design and implementation:

1.  Scalability – we would like to be able to add as many features as needed without affecting the viability of the solution. This gives us reliable results as all the features of a certain app are (or can be) modeled.

2.  Consistency – we would like to get the exact same results for a given input and a given dataset.

3.  Flexibility – we would like to be able to intervene or bias the classifier in order to adapt it to certain environment. In learning techniques, it is sometimes required to have the ability to insert variables to modify the algorithm or using hooks to adapt the algorithm to specific requirements and/or changing environments as well.

4.  Efficiency – we would like to be able to get an accurate prediction without paying for it in processing time and complexity. In our solution, classification process takes up to 2ms.

5.  Platform Independent – we would like to be able to deploy this solution on any machine runs any operating system. All code in our solution is written with Java – hence this solution can be deployed on any machine runs Java Virtual-Machine.

6.  Portability – we would like to be able to provide our solution on mobile devices as well as being able to provide it as a service. In our solution, we build a core framework to be able to test and classify apps in such way that it is extensible and pluggable to any external usage, e.g. build graphical-user-interface on top of it or deploy it in the cloud to provide app classification as a service.

##  5.1. A Prediction Model Using Linear and Logistic Regression

Regression or Regression Analysis is a technique used for the modeling and analysis of numerical data by exploiting the relationship between two or more variables so that we can gain information about one of them through knowing values of the other \[42\]. Regression is mainly used for prediction, estimation, and hypothesis testing and modeling causal relationships. A few basic terms and legend in the Regression field:

$$
Y = X_{1} + X_{2} + \ldots + X_{n}
$$

Linear regression is an approach to model the relationship between a scalar dependent variable *Y* and one or more independent (explanatory) variables denoted *X*. In linear regression, data are modeled using *Linear Predictor Functions*, and unknown model parameters are estimated from the data. *Linear Predictor Function* is a linear function of a set of coefficients and independent variables, whose value is used to predict the outcome of a dependent variable.

The basic form of a linear predictor function $f(i)$ is:

$$
f(i) = \beta_{0} + \beta_{1}x_{i1} + \beta_{2}x_{i2} + \ldots + \beta_{p}x_{ip}
$$

Where:

- *i* is the data point

- *p* is consisting of *p* independent variables

- $\beta_{0},\ldots{,\beta}_{p}$ are the coefficients (regression coefficients, weights) indicating the relative effect of a particular independent variable on the outcome.

Given a data set (also known as “corpus”) $\left\{ y_{i},x_{i1},\ldots,x_{ip} \right\}_{i = 1}^{n}$ of *n* observations, a linear regression model assumes that the relationship between the dependent variable $y_{i}$ and the p-vector of regressors $x_{i}$ is linear.

The regression method we are using as part of the linear regression analysis is Logistic Regression. Logistic regression is a type of regression analysis used for predicting the outcome of a categorical (a variable that can take on a limited number of categories) dependent variable based on one or more predictor variables \[42\]. The probabilities describing the possible outcome of a single trial are modeled, as a function of independent variables, using a logistic function. Logistic regression can be binomial or multinomial.

Binary logistic regression deals with situations in which the observed outcome for a dependent variable can have only two possible types which are 1 for *success* or *case* and 0 for *failure* or *non-case* (for example, we are defining apps as *safe* or *malicious*). Multinomial logistic regression deals with situations where the outcome can have three or more possible types (e.g., "better" vs. "no change" vs. "worse"). Logistic regression is especially used for predicting binary outcomes of the dependent variable by treating the dependent variable as the outcome of a Bernoulli trial.

The natural logarithm of the odds of the dependent variable being a success (a case), also known as “logit“, is then fit to the predictors using linear regression analysis. The predicted value of the logit is converted back into predicted odds via the inverse of the natural logarithm, namely the exponential function. Therefore, although the observed dependent variable *Y* in logistic regression is a zero-or-one variable, the logistic regression estimates the odds, as a continuous variable, that the dependent variable is a success (a case).

The basic form of a logistic function $l(t)$, is as follows:

$$
l(t) = \frac{e^{t}}{e^{t} + 1}
$$

*t* is the linear function (from above) of a linear combination of independent variables *X*.

The logistic function $\pi(X)$, interpreted as the probability of the dependent variable equaling a "success" or "case" rather than a failure or non-case, can be also written as:

$$
\pi(X) = \frac{e^{(\beta_{0} + \beta_{1}x_{i1} + \ldots + \beta_{p}x_{ip})}}{e^{(\beta_{0} + \beta_{1}x_{i1} + \ldots + \beta_{p}x_{ip})} + 1}
$$

and the inverse of the logistic function (logit) $g(x)$:

$$
g(x) = ln\frac{\pi(x)}{1 - \pi(x)}
$$

##  5.2. Logistic Regression Use in Other Fields

Logistic Regression is used extensively in numerous disciplines, including the medical and social science fields. For example, the Trauma and Injury Severity Score (TRISS), which is widely used to predict mortality in injured patients, was originally developed by Boyd et al. using logistic regression \[24\]. Logistic regression might be used to predict whether a patient has a given disease, based on observed patient characteristics (age, gender, body mass index, results of various blood tests, and so on).

Another example might be to predict whether an American voter will vote Democratic or Republican, based on age, income, gender, race, state of residence, votes in previous elections, etc \[44\]. The technique can also be used in engineering, especially for predicting the probability of failure of a given process, system or product \[26\]. 

Logistic regression is also used in marketing applications such as prediction of a customer's propensity to purchase a product or cease a subscription \[43\]. In economics it can be used to predict the likelihood of a person's choosing to be in the labor force, and a business application would be to predict the likelihood of a homeowner defaulting on a mortgage.

## 5.3. Why Our Problem Fit the Linear Regression?

The goal of our system is prediction. Linear regression is used to fit a predictive model to an observed data set of *Y* and *X* values. The dependent variable *Y* is actually the prediction result of our classifier. The *X* variable represents a vector of predictors, i.e. the required permissions of a certain app. After developing such model it can be used to predict the risk value (*Y*), for a newly observed vector of permissions (*X).* Such a predictor is the exact functionality we wish to have achieve using our model.
