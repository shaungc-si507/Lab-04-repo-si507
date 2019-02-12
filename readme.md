# Part 1

- Fill all empty cell by "NA"
    - "Not Rated" is vaild and don't overwrite that
    - ==> Look all fields, populate "NA"
- Date adhere format (can use regex)
    - if invalid, fill with "NA"
    - TODO: what is the starting 0 requirement about? maybe it's like 03, 04, add the additional zero. But of course like 18, 31, no need to add that zero.
- name output file as `movies_clean.csv`

# Part 2

Transform
    map string (emul) to numbers

Take median
    round to closet int


# Part 3

- 10 Title - movie pairs
  - don't use the original title
  - need to use itertools => use permutation
  - store into a variable

- should be ramdom
- not too long, 6 words || < 45 char


# Ref

- [Medium: Data Cleaning with Python and Pandas: Detecting Missing Values
](https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b): how to use `loc` to do in-place change to dataframe and series in pandas.
- [SO: Pandas convert string to int](https://stackoverflow.com/questions/42719749/pandas-convert-string-to-int)
- [Why apply sometimes isn't faster than for-loop in pandas dataframe?](https://stackoverflow.com/questions/38938318/why-apply-sometimes-isnt-faster-than-for-loop-in-pandas-dataframe). Cell-wise operation in pandas column.
- [SO: Convert categorical data in pandas dataframe](https://stackoverflow.com/questions/32011359/convert-categorical-data-in-pandas-dataframe). Useful to use with Python Enum.
    - [Pandas Official: Categorical Data](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html), creating a Categorical in pandas.
    - [Python Official: Enum & Usage](https://docs.python.org/3/library/enum.html)