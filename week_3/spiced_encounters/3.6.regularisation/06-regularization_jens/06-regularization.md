# Regularization

29/03/2022

### Generalization gap

​	Difference between training and validation (test) score.  
​	Irreducible error - this can not be reduced (inherent property of data)

<img src="./error.png" alt="fitting error" style="zoom:50%;" />

#### 	Overfitting

​		Model learns training data not feature information.    
​		Score of training data is great, test score is very weak

​		**Why? ** 
​		Model too complicated    
​		Training data set too small   
​		Training data contains noise (garbage in - garbage out)  
​		Model has high variance   

​		**How to prevent**	   
​		Cross-validation   
​		Remove redundant features   
​		Regularization   
​		Early stopping, ensembling

#### 	Underfitting		

​		Model only learns main trend, does not use all feature information   
​		Training and test score are low

​		**Why?**   
​		Model is too simple   
​		Training data is too small    
​		Training data contains noise (garbage in - garbage out)    
​		Model has high bias   
​		

<img src="./bias-variance.png" alt="bias vs. variance" style="zoom: 50%;" />	

#### Norm

​	**$l1$ norm**    
​		Manhatten or taxi cab norm   
​		$||\mathbf{x}||_1 := \sum_{i=1}^n |x_i|$

​	**$l2$ norm**
​		Euclidean norm    
​		$||\mathbf{x}||_2 := \sqrt{x_1^2 + x_2^2 + ... + x_n^2}$

### Regularization

​	OLS: $\text{loss} = \sum_{i=1}^n (y_i - \hat{y}_i)^2 = \sum_{i=1}^n (y_i - \sum_{j=1}^p x_{ij}\theta_j)^2$   

​	**Lasso** (Least Absolute Shrinkage and Selection Operator)   
```{python}
sklearn.linear_model.Lasso
```

​		$\text{loss} = \sum_{i=1}^n (y_i - \hat{y}_i)^2 + \alpha \sum_{j=1}^p|\theta_j|$   
​		Can set weights to zero and is applied for feature selection   

​	**Ridge** 

```{python}
sklearn.linear_model.Ridge
```

​		$\text{loss} = \sum_{i=1}^n (y_i - \hat{y}_i)^2 + \alpha \sum_{j=1}^p\theta_j^2$   
​		Minimizes weights, can be applied to counteract multicollinearity
​		More stable

​	**ElasticNet**

```{python}
sklearn.linear_model.ElasticNet
```

​		$\text{loss} = ||y_i - \hat{y}_i||_2^2 + \alpha \cdot ratio \cdot ||\mathbf{\theta}||_1 + \alpha \cdot (1-ratio)\cdot ||\mathbf{\theta}||_2^2$   
​		Best of both worlds

### Further reading

*   [StatQuest on Lasso](https://www.youtube.com/watch?v=NGf0voTMlcs)
*   [StatQuest on Ridge](https://www.youtube.com/watch?v=Q81RR3yKn30)
*   [StatQuest on ElasticNet](https://www.youtube.com/watch?v=1dKRdX9bfIo)
