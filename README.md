# MATH5543 HW2

![Tests](https://github.com/mCodingLLC/SlapThatLikeButton-TestingStarterProject/actions/workflows/tests.yml/badge.svg)

## Homework 2, MATH5543 Course Spring 2022, Oklahoma State University
### Instructor: Dr. Xu Zhang
### Textbook: Randall J. LeVeque. Finite Difference Methods for Ordinary and Partial Differential Equations. SIAM, 2007

To run the project locally:
<!-- Code Blocks -->
```bash
  git clone https://github.com/zomorodiyan/MATH5543
  cd MATH5543
  pip install -r requirements.txt
  pip install -r requirements_dev.txt
  pip install .
  mypy src
  flake8 src
```
### 1.a)
#### fdm2Dmatrix and fdm2Drhs are defined in src/fdm/fd5p.py
### 1.b)
![Alt text](./Plots/1b_contour.png?raw=true "Title")
### 1.c)
![Alt text](./Plots/1c_error.png?raw=true "Title")
#### Comparing the slopes concludes: it is first order


#### project structure template: https://github.com/mCodingLLC/SlapThatLikeButton-TestingStarterProject
