---
title: "Python Tools for Data Analysis"
collection: teaching
type: "Bootcamp"
permalink: /teaching/001-bigdata-bootcamp-python
venue: "Georgia Tech, School of CSE"
date: 2022-02-26
location: "Atlanta, GA"
toc: true
show: true
---

{% include user_def %}

## 1. Python Installation: Anaconda

{{ hint_info }}
**If you don't feel like using the local environment**, you can try [Google Colab](https://colab.research.google.com/) for a *free* online python environment.
The examples are also available on Colab:  
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1J2rCfbQm5heCt5LN1t8RZHA1O9VaT8b-?usp=sharing)
{{ _hint }}

**Ignore this session if you already have a python environment.**

[Anaconda](https://www.anaconda.com/) is a complete, [open source](https://docs.anaconda.com/anaconda/eula) data science package with a community of over 6 million users.
It is easy to [download](https://www.anaconda.com/download/) and install;
and it supports Linux, macOS, and Windows ([source](https://opensource.com/article/18/4/getting-started-anaconda-python)).

In this tutorial, we'll use [Miniconda](https://docs.conda.io/en/latest/miniconda.html) for minimal installation.
Please refer to [this page](https://conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda) for the difference between Anaconda and Miniconda and which one to choose.

### 1.1. Windows and macOS

1. Download the latest Miniconda installer from the [official website](https://docs.conda.io/en/latest/miniconda.html#windows-installers).
2. Install the package according to the instructions.
3. Start to use *conda* environment with *Anaconda Prompt* or other shells if you enabled this feature during installation.

{{ hint_warning }}
Notice: To use `conda` command in other shells/prompts, you need to add the conda directory to your `PATH` environment variable.
{{ _hint }}

> Please refer to [this page](https://docs.anaconda.com/anaconda/install/windows/) for more information about Anaconda installation on Windows and [this page](https://docs.anaconda.com/anaconda/install/mac-os/) on MacOS.

### 1.2. Linux with terminal 

1. Start the terminal.
2. Switch to `~/Download/` with command `cd ~/Download/`. If the path does not exist, create one using `mkdir ~/Download/`.
3. Download the latest Linux Miniconda distribution using `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`.
4. Once the download is complete, install Miniconda using `bash Miniconda3-latest-Linux-x86_64.sh`.
5. Follow the prompts on the installer screens.
   If you are unsure about any setting, accept the defaults. You can change them later.
6. To make the changes take effect, close and then re-open your terminal window or use the command `source ~/.bashrc`.
7. If you are using *zsh* or other shells, make sure conda is initiated. To do this, switch back to bash and type the command `conda init <shell name>`.

> Please refer to [this page](https://docs.anaconda.com/anaconda/install/linux/)) for more information about Anaconda installation on Linux.

### 1.3. Verify your installation

You can use the command `conda list` to check your conda installation.
If the terminal returns a bunch of python packages, then your installation is successful.

> Please refer to [this page](https://docs.anaconda.com/anaconda/install/verify-install/)) for more information.

### 1.4. Conda environment

With conda, you can easily create, remove, and update environments, each with an independent version of Python interpreter and Python packages.
This is always desirable when you work on different Python projects with different (often conflicting) package dependencies.
In this tutorial, we will use the default *base* environment.
For more information on environment management, please refer to [conda: managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

## 2. Package Installation

If you are using Anaconda or Miniconda, you can use the Anaconda package manager `conda`.
You can also use other managers such as `pip` when the packages are not provided by any conda channels.

To look for a specific package, you can visit [this website](https://anaconda.org/) and type the name of that package in the search box.
For today's instruction, we need to install `numpy`, `matplotlib`,  `scikit-learn` and `pandas`. 

First, switch to your conda environment using `conda activate <env name>` (not necessary if you are using the default *base* environment), then install those packages using the following commands:
```bash
conda install -c conda-forge numpy matplotlib scikit-learn pandas
```
The package manager will automatically install the dependencies.
If you install `scikit-learn` first, which depends on `numpy`, you don't have to install `numpy` manually and the conda package solver will do it for you.

If you prefer a fancier and more powerful python shell, you can choose to install `ipython` and `jupyter notebook`.
```bash
conda install -c conda-forge ipython
conda install jupyter
```
[Jupyter notebook](https://jupyter.org/try) allows you to run your commands using the browser as an interface instead of the terminal.

## 3. Basic Python Concepts

> A more comprehensive tutorial can be found on the [Stanford CS231n website](http://cs231n.github.io/python-numpy-tutorial/#python-basic).

We use **Python 3.9** in this tutorial.

{{ hint_warning }}
Notice that previous Python interpreter versions may behave differently.
Please refer to the [official document](https://docs.python.org/dev/whatsnew/index.html) for more details.
{{ _hint }}

First, in your terminal, type `python` or `ipython` or `jupyter notebook` to start an interactive python shell.
`ipython` or `jupyter notebook` is recommended.

{{ hint_info }}
The tutorial is also on Google Colab: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1J2rCfbQm5heCt5LN1t8RZHA1O9VaT8b-?usp=sharing)
{{ _hint }}

### 3.1. Variable definition, input and output (print)

We do not need to specify the variable type while defining a variable.
The interpreter will automatically infer the data type from the assigned value.
```python
a = 123
b = '123'
c = "1234"
print(a, b, c, type(a), type(b), type(c))
```

A variable can be overwritten by a different type:
```python
a = 123.456
print(type(a))
a = '123'
print(type(a))
```

The `input` method allows you to interactively input information into the program through CLI:
```python
x = input('Input something: ')
print(x, type(x))
```

{{ hint_info }}
Notice that `input` is rarely used.
A more practical input method is [argparse](https://docs.python.org/3/library/argparse.html).
{{ _hint }}

### 3.2. List, tuple, set and dictionary

- **List** is a collection that is *ordered* and *changeable*.
It allows duplicate members.
- **Tuple** is a collection that is _ordered_ but *not changeable*.
It also allows duplicate members.
- **Set** is a collection that is _unordered_ and *unindexed*.
It does not allow duplicate members.
Elements in a set cannot be retrieved by index.
- **Dictionary** is a collection that is _ordered_, *changeable* and *indexed*.
It does not allow duplicate members.  

{{ hint_warning }}
Notice that Dictionary used to be unordered before *Python 3.7*.
{{ _hint }}

```python
_list = [1, 2, 1.2, '1', '2', 1]  # this is a list
_tuple = (1, 2, 1.2, '1', '2', 1)  # this is a tuple
_set = {1, 2, 1.2, '1', '2', 1}  # this is a set
_dict = {  # this is a dict
    1: '111',
    2: '222',
    '1': 567,
    2.2: ['J', 'Q', 'K']
}
print(_list, '\n', _tuple, '\n', _set, '\n', _dict)
```

Access elements

```python
print(_list[0], _list[-2], _list[1: 3])
print(_tuple[1], _tuple[-2])
print(_set[0], _set[-1])
print(_dict[1], _dict['1'], _dict[2.2])
```

Shallow copy

```python
a = _list
a[0] = 888
print(a, '\n', _list)
```

### 3.3. If else

```python
if 888 not in _dict.keys():
    _dict[888] = '???'
elif 999 not in _dict.keys():
    _dict[999] = '!@#$%'
else:
    _dict['qwert'] = 'poiuy'
```

### 3.4. Loops

{{ hint_info }}
**Note:** in Python, the indent is used to define a scope instead of curly brackets `{}`.
Usually, people use 4 whitespaces or one tab character `\t` as one layer of indent.
Be sure to make it consistent throughout the file.
{{ hint }}

- `for` loop:

```python
for x in _list:
    print(x)

for i in range(len(_list)):
    print(_list[i])
```

- `while` loop:

```python
i = 0
while i != len(_list):
    print(_list[i])
    i += 1
```

### 3.5 Function

Define a function:

```python
def my_func(x):
    x += 1
    print('in function: ', x)
    return x
```

Call a function

```python
t = 10
tt = my_func(t)
print(f'out of funciton, t: {t}, tt: {tt}')
```

## 4. Basic Numpy Usage

### 4.1. Array creation

A `numpy` array is a grid of values, all of the same type, and is indexed by a tuple of integers.
The number of dimensions is the *rank* of the array; the *shape* of an array is a tuple of integers giving the size of the array along each dimension.

We can initialize `numpy` arrays from nested Python lists, and access elements using square brackets:

```python
import numpy as np

a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a), a.dtype)
print(a.shape)
print(a[1])

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)
print(b[0, 0], b[0, 1], b[1, 0])
```

Change the type of an array:

```python
print(a.dtype)
a = a.astype(float)
print(a.dtype)
```

Other array creation methods:

```python
a = np.zeros((2,2))   # Create an array of all zeros
print(a)
b = np.ones((1,2))    # Create an array of all ones
print(b)
c = np.full((2,2), 7, dtype=np.float32)  # Create a constant array
print(c)
d = np.eye(3)         # Create a 3x3 identity matrix
print(d)
e = np.random.random((3,3))  # Create an array filled with random values
print(e)
```

### 4.2. Array indexing

Similar to Python lists, `numpy` arrays can be sliced.

```python
# Create a rank 1 array and reshape it to a 3x4 matrix
a = np.arange(12).reshape(3, 4)
b = a[:2, 1:3]
print(a)
print(b)

# Shallow copy
b[0, 0] = 888
print(a)
```

You can mix integer indexing with slice indexing.
However, integer indexing will yield an array of lower rank than the original array:

```python
row_r1 = a[1, :]    # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)
```

You can also access array elements through lists:

```python
x = [0, 1, 2]
y = [3, 1, 0]
print(a[x, y])
```

Or through a boolean array:

```python
b = a > 4
print(b)
print(a[b])
```

### 4.3. Array math

Basic mathematical functions operate element-wise on arrays, and are available both as operator overloads and as functions in the `numpy` module:
```python
x = np.arange(1, 5, dtype=float).reshape(2, 2)
y = np.arange(5, 9, dtype=float).reshape(2, 2)
print(x)
print(y)

# Elementwise sum
print(x + y)
print(np.add(x, y))

# Elementwise difference
print(x - y)
print(np.subtract(x, y))

# Elementwise product
print(x * y)
print(np.multiply(x, y))

# Elementwise division
print(x / y)
print(np.divide(x, y))

# Elementwise square
print(x ** 2)
print(np.power(x, 2))

# Elementwise square root
print(x ** 0.5)
print(np.sqrt(x))
```

Matrix multiplication is realized by `np.dot` or operator `@`:
```python
x = np.arange(1, 5, dtype=float).reshape(2, 2)
y = np.arange(5, 9, dtype=float).reshape(2, 2)
print(x)
print(y)

v = np.array([9, 10], dtype=float)
w = np.array([11, 12], dtype=float)

# Inner product
print(v.dot(w))
print(np.dot(v, w))
print(v @ w)

# Matrix / vector product
print(x.dot(v))
print(np.dot(x, v))
print(x @ v)

# Matrix / matrix product
print(x.dot(y))
print(np.dot(x, y))
print(x @ y)
```

{{ hint_warning }}
**Attention:** `np.dot()` and `@` behaves differently when the matrix rank is larger than 2.
{{ _hint }}

`Numpy` also provides functions for performing computations within an array:
```python
print(np.sum(x))  # Compute sum of all elements; prints "10"
print(x.sum())  # same as above
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"
```

To transpose a matrix, use the `T` attribute of an array object:
```python
print(x.T)
```

If you have a rank >2 matrix, you can use `np.transpose` to specify how to permute the axes:
```python
x = np.arange(24).reshape(2, 3, 4)
print(x.transpose(1, 0, 2).shape)
```

## 5. Using Matplotlib for Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib qt

# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

# Plot the points using matplotlib
plt.plot(x, y)
plt.show()  # You must call plt.show() to make graphics appear.
```

{{ hint_info }}
Note: for jupyter notebook, you can use the command `%matplotlib inline` to make the graphics embedded in the editor or `%matplotlib qt` to make them pop out.
{{ _hint }}


To plot multiple lines at once, and add a title, legend, and axis labels:

```python
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the points using matplotlib
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()
```

You can plot different things in the same figure using the `subplot` function. Here is an example:

```python
# Set up a subplot grid that has height 2 and width 1,
# and set the first such subplot as active.
plt.subplot(2, 1, 1)

# Make the first plot
plt.plot(x, y_sin)
plt.title('Sine')

# Set the second subplot as active, and make the second plot.
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

# Show the figure.
plt.show()
```

## 6. Pandas and Scikit-Learn for Data Science

In this section, we will look at a data science example using pandas as data management tool and scikit-learn (sklearn) as algorithm implementation.
This section is modified from [this tutorial](https://elitedatascience.com/python-machine-learning-tutorial-scikit-learn).

### 6.1. Import packages

```python
import numpy as np
import pandas as pd

# automatically split the data into training and test set
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

# classifiers and regressors
from sklearn.ensemble import RandomForestRegressor
# Construct a Pipeline from the given estimators
from sklearn.pipeline import make_pipeline
# Exhaustive search over specified parameter values for an estimator.
from sklearn.model_selection import GridSearchCV

# Training objective and evaluation metrics
from sklearn.metrics import mean_squared_error, r2_score
# For model persistence
# you can use `from sklearn.externals import joblib` if your sklearn version is earlier than 0.23
import joblib
```

### 6.2. Load data

You can download the [data](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv) by clicking the link or using `wget`: `wget https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv` and move the file to your current folder.
Then, load the `csv` data into memory through `pandas`:

```python
data = pd.read_csv('winequality-red.csv', sep=';')
```

Or, you can directly load the data through URL.

```python
dataset_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url, sep=';')
```

You can also load datasets stored in other formats with `pandas`.
A detailed document is at [pandas: io](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html).

### 6.3. Take a look of the loaded data

The data loaded is stored in the type of `pandas.core.frame.DataFrame`

To give a peak of the data, we can use

```python
print(data)
```

This will return a nice-looking preview of the elements in the DataFrame.

To view the name of the features of a DataFrame, one can use

```python
print(data.keys())
```

To access one column, i.e., all instances of a feature, e.g., `pH`, one can use

```python
# These will return the same result
print(data['pH'])
print(data.pH)
```

To access a row, you need the `DataFrame.iloc` attribute:

```python
print(data.iloc[10])
```

We can also easily print some summary statistics:

```python
print(data.describe())
```

### 6.4. Split data

First, let's separate our target (y) feature from our input (X) features and divide the dataset into training and test sets using the `train_test_split` function:

```python
y = data.quality
X = data.drop('quality', axis=1)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0, stratify=y
)
```

Stratifying your sample by the target variable will ensure your training set looks similar to your test set, making your evaluation metrics more reliable.

### 6.5. Pre-processing

Standardization is the process of subtracting the means from each feature and then dividing by the feature standard deviations. It is a common requirement for machine learning tasks. Many algorithms assume that all features are centered around zero and have approximately the same variance.

```python
scaler = preprocessing.StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# To prove the trainig and testing sets have (nearly) zero mean and one deviation
print(X_train_scaled.mean(axis=0))
print(X_train_scaled.std(axis=0))
print(X_test_scaled.mean(axis=0))
print(X_test_scaled.std(axis=0))
```

### 6.6. Fit the model

If we do not need to fine-tune the hyperparameters, we can define a random forest regression model with the default hyperparameters and fit the model using

```python
regr = RandomForestRegressor()
regr.fit(X_train_scaled, y_train)
```

To examine the performance, we use the test set to calculate the scores

```python
pred = regr.predict(X_test_scaled)

print(r2_score(y_test, pred))
print(mean_squared_error(y_test, pred))
```

### 6.7. Define the cross-validation pipeline

Fine-tuning hyperparameters is an important job in Machine Learning since a set of carefully chosen hyperparameters may greatly improve the performance of the model.

In practice, when we set up the cross-validation pipeline, we won't even need to manually fit the data. Instead, we'll simply declare the class object, like so:

```python
pipeline = make_pipeline(
    preprocessing.StandardScaler(),
    RandomForestRegressor(n_estimators=100)
)
```

To check the hyperparameters, we may use

```python
print pipeline.get_params()
```

or refer to the [official document](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html).

Now, let's declare the hyperparameters we want to tune through cross-validation.

```python
hyperparameters = {
    'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'],
    'randomforestregressor__max_depth': [None, 5, 3, 1]
}
```

Then, we can set a 10-fold cross validation as simple as

```python
clf = GridSearchCV(pipeline, hyperparameters, cv=10)
```

Finally, we can automatically fine-tune the model using

```python
clf.fit(X_train, y_train)
```

After the model fitting, if we want to check the best hyperparameters, we can use

```python
print(clf.best_params_)
```

Same as before, we evaluate the fitted model on test set

```python
pred = clf.predict(X_test)

print(r2_score(y_test, pred))
print(mean_squared_error(y_test, pred))
```

### 6.8. Save and load models

After training, we may want to save the trained model for future use. For this purpose, we can use

```python
joblib.dump(clf, 'rf_regressor.pkl')
```

When you want to load the model again, simply use this function:

```python
clf2 = joblib.load('rf_regressor.pkl')
 
# Predict data set using loaded model
clf2.predict(X_test)
```

---

A more comprehensive example of scikit-learn can be found [here](https://scikit-learn.org/stable/tutorial/statistical_inference/index.html).
