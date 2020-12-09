# Final Review

## Post Midterm

### Command Line Interface and Data Scraping

Notebooks
* 07-Command-Line-and-Data-collection.ipynb
* lab7
* lab9

Command line concepts
* http://swcarpentry.github.io/shell-novice/
* Download files
* Basic concepts of regular expression
* Search and replace strings
* Chain commands together

Example: data scraping
* Download HTML source of a webpage
* Extract data zip file URLs
* Download data zip files
* Load contents into Python
* Convert to Pandas data frame

GET URL and API concepts:
* GET URL format passes variables to a web page
* APIs are often GET URL formatted
* Common data format is JSON
* Read and parse JSON formatted data

Exercise: Santa Barbara employment numbers
* Data page: https://dev.socrata.com/foundry/data.edd.ca.gov/vduu-fnb7
* Example call: https://data.edd.ca.gov/resource/vduu-fnb7.json?industry_title=Total%20Nonfarm&year=2019
* Read into python

### Portfolio Allocation and Optimization

Notebooks
* 08-Optimizing-Stock-Portfolio-Allocation
* lab5
* lab8
* assignment4

Portfolio allocation concepts
* What is the portfolio allocation problem solving?
* What can you say about the mathematical property of the solution?
* How does constraints change the problem? (e.g. target return)
* An example of optimization

Optimization concepts
* Mathematical formulation of a real problem
* Portfolio problem solves a quadratic objective function (sometimes called quadratic programming)
* Resource allocation problem solves a linear objective function (sometimes called linear programming)
* Constraints define qualification for valid solution
* Objective function evaluates how good solutions are
* Gradient descent iteratively improves a solution until convergence
* E.g. line fits, latent factor representation, machine learning problems, matching, scheduling

## Pre Midterm

### Data and Simulation

Notebooks
* 02-Data-and-Uncertainty
* 03-Distributions-Histograms-and-Bootstrap
* lab1
* lab2
* lab3
* assignment1

Concepts
* Random variable in the computer
* Data as an empirical distribution
* Histogram and ECDF represent information about distribution
* Resampling from data (empirical distribution)
* Pandas

### Visualization

Notebooks
* 04-Exploratory-Data-Analysis-and-Visualization
* lab3
* lab4

Concepts
* Visualization principles
* Kernel smoothing

### Data and Matrices

Notebooks
* 05-Dimension-Reduction-and-Matrix-Factorization
* 06-Movie-Recommendation-System
* lab5
* lab6
* assignment2
* assignment3

Concepts
* Linear combination and redundant information
* Matrix factorizations as different data representations (PCA, ICA, NMF, SVD)

Example: Movie recommender system
* Represent movie ratings product of movie and user attributes in latent factor space
* Fill-in missing ratings to recommend movies
* Choice of loss function (simple linear function, logistic function)
* Calculating matrix factors with gradient descent
* Organizing a system of linear equations into linear algebra operations
