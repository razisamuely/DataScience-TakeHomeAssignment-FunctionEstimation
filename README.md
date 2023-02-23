# DataScience-TakeHomeAssignment-FunctionEstimation
The purpose of this project is to address several questions from the 
DataScience-TakeHomeAssignment-FunctionEstimation 
that I received as part of the data science recruitment process.

For detailed code and functionality pleas see `main.py` and `utils.py`

## Question 

There is an unknown continuous function, denoted by $x → y$, such that x belongs to the interval $[0,1]$ and y belongs to the interval $[0,1]$. 

There is also a function called `check_if_below which`, for each combination of x and y, returns False if the point is above the function and True if it's below the function. 

Your task is to estimate the area under this function. 

For example, if the function is $f(x) = x$, the points (0.1,0.2), (0.1,0.8), and (0.6,0.8) would have a value of 0, while (0.1,0.05), (0.1,0.02), and (0.6,0.1) would have a value of 1.


#### Example for different functions

**Note**: The following functions are of the form $f(x) = x^l$, where $l$ changes between each iteration. 
However, it's possible for the function to be any other continuous function, such as $f(x) = 0.5$ or $f(x) = sin(x)$, etc.



<p align="center">
    <img src="https://raw.githubusercontent.com/razisamuely/DataScience-TakeHomeAssignment-FunctionEstimation/main/data/random_continuse_function_detect_below_abov_points.gif"  width="300" height="230">
</p>


# Solution (1) - Monte Carlo simulation

The maximum area under the unknown function is one, which allows us to use sampling to estimate the proportion of points that evaluate to True.
The following steps can be taken:
Generate n points from a uniform distribution (0,1)
For each point, determine whether it falls above or below the unknown function
Calculate the proportion of points that fall under the function

for `f(x)=x`:

<p align="center">
    <img src="https://raw.githubusercontent.com/razisamuely/DataScience-TakeHomeAssignment-FunctionEstimation/main/data/MonteCarlo_simulation_y_%3D_x.gif"  width="300" height="230">
</p>

for `f(x)=x^2`:


<p align="center">
    <img src="https://raw.githubusercontent.com/razisamuely/DataScience-TakeHomeAssignment-FunctionEstimation/main/data/MonteCarlo_simulation_y_%3D_x_2.gif"  width="300" height="230">
</p>

It appears that we are getting close to the real value using the current method. However, we can improve the accuracy by increasing the number of sampled points or by averaging the results of multiple experiments with the same number of samples.
Increasing the number of samples will provide a more accurate estimate of the proportion of points that fall under the function. The more samples we take, the closer the estimate will be to the true value.
Averaging the results of multiple experiments can also improve the accuracy of the estimate. 
By conducting multiple experiments with the same number of samples and averaging the results, 
we can reduce the impact of any individual experiment that may have deviated from the expected value. 
This can provide a more reliable estimate of the proportion of points that fall under the function.

### Follow-up question:

After presenting the Monte Carlo simulation, a follow-up question was asked: 
"Can we make any statements about the estimated area and the real value"

### Follow-up Answer:
Yes, after presenting the Monte Carlo simulation, we can make statements about the estimated area and the real value.

We can use statistical methods to build a confidence interval for the proportion of points that fall under the function, 
with respect to a chosen error probability $\alpha$. This interval will give us a range of values in which we can be confident the true proportion falls.

For example, if we use a 95% confidence interval, we can say that we are 95% confident that the true proportion of points that 
fall under the function falls within the interval. This provides a measure of the uncertainty in our estimate, and allows us to make statements about the likely range of values for the true area.

It's important to note that the width of the confidence interval will depend on 
the number of samples used in the simulation, as well as the complexity of the 
function being estimated. In general, a larger number of samples will result in a narrower 
confidence interval and a more accurate estimate of the true area.


Solution 2 - Binary search

With stochastic methods, such as the `Monte Carlo simulation` mentioned above, 
the estimated area changes for different iterations with the same predefined parameters. 
This is because the process involves generating random samples to estimate the area.


However, if we want to use determenistic method as `binary search` to find the y values for each x that are close 
enough to the real value, we can do so by defining a function that takes a value of x as input and returns the 
corresponding y value that satisfies the condition (i.e., falls below the unknown function). 

We can start by setting the initial lower and upper bounds of the search interval to 0 and 1, respectively, 
and iteratively narrow down the interval until we reach the desired level of precision.

Here we will define some distance $\epsilon$ for  max distance from true value.

```
def find_y_value(x,func,epsilon,lower_bound = 0, upper_bound =1):
    while True:
        mid_point = (lower_bound + upper_bound) / 2
        if check_if_below(x, mid_point,func = func):
            if upper_bound - mid_point < epsilon:
                return mid_point
            lower_bound = mid_point
        else:
            if mid_point - lower_bound < epsilon:
                return mid_point
            upper_bound = mid_point
```

In this function, we start by setting the initial interval bounds to 0 and 1, 
and then we enter a while loop that iteratively narrows down the interval until 
we reach the desired level of precision (in this case, 0.0001). At each iteration, 
we calculate the midpoint of the current interval and check if the corresponding 
point (x, midpoint) falls below the unknown function. If it does, we update the 
lower bound of the interval to the midpoint; otherwise, we update the upper bound. 
We continue this process until the interval is narrow enough to satisfy the desired level 
of precision, at which point we return the midpoint as the estimated y value for the given x value.
**Note**  that this approach assumes that the function is continuous and that the area under the curve exists. 
If these conditions do not hold, the binary search approach may not be appropriate or may not converge 
to a satisfactory solution.

![image](https://raw.githubusercontent.com/razisamuely/DataScience-TakeHomeAssignment-FunctionEstimation/main/data/binary_search_on_fx_%3D_x.gif)


### Follow-up question:
What is the complexity of the above ?

### Follow-up Answer:
1. Each iteration the search rang reduced by 0.5 (first (0,1) then (0.5,1) or (0,0.5) etc, so after n iteration, the the search range is $0.5^n$
2. Then stop rule is continue search till the search range is smaller then $\epsilon$
3. So $0.5^n >= \epsilon \rightarrow n = log_{0.5}(\epsilon)$

Summary
In this section, we have discussed two techniques for classic function estimation: deterministic and stochastic. 
Deterministic methods involve mathematical equations that directly relate input variables to output variables, 
allowing for precise and exact estimates of a function's behavior. However, deterministic methods may not work 
well for complex functions or data sets with a high degree of variability.
On the other hand, stochastic methods rely on generating random samples of input variables and using them to estimate 
the function's behavior. One popular example of stochastic methods is the Monte Carlo simulation. 
While stochastic methods may not provide exact estimates, they can be useful for complex functions or data sets 
with high variability, as they account for uncertainties in the data.
Function estimation is a crucial part of the data science world, as it is used in a wide range of applications such 
as churn analysis, animal picture recognition, signal behavior, and more. Understanding the main concepts of function 
estimation is essential before diving into advanced techniques. It is also important to note that choosing the right 
method depends on the problem at hand, and one method may not work well for all situations. A data scientist should 
have a good understanding of both deterministic and stochastic methods and when to apply each one to achieve the 
best results.

Code Structure
Please note that the code for this project is not written in classes as is typically done. Instead, the code is organized in a procedural manner for simplicity and ease of understanding.