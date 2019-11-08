    Title: Assignment 4
    Date: 2019-11-08T00:00:00
    Tags: DONE

<!-- more -->

The goal of this assignment is to create a Python program to query CSV files based on a user provided query. Essentially mimicking an SQL database.

## Reading CSV Files

The first part required to complete this assignment was to read in a CSV file. Python has a built-in library for reading CSV files so this only required reading in the file and then transposing the data to a list. Reading files is a simpe oneline operation, making this part of the assignment easy.

```python
with open(filename, 'r') as csv_file:
	return [row for row in csv.reader(csv_file, delimiter=',')
```

## Parsing Headers

The next requirement was to parse the headers. The first row of a CSV file is normally the headers so that needed to be mapped to the indices to make accessing data easier. This was accomplished using dictionary comprehension.

```python
return { label: i for i, label in enumerate(row) }
```

## Selecting Columns

With the header map now created we can move onto selecting columns. The goal for this section was to create a function that would take in a table and return the table with only the specified columns. This involved more list comprehension and a somewhat janky way of accessing columns. To access the column required calling `row[headers[col]]`. This translates the column name into the row index.

## Transforming Rows into Dictionaries

The previous method of accessing column data was a bit obtuse. The next goal is to improve that. We can improve column access by mapping the columns to a dictionary. Using the headers created in an earlier partwe can use dictionary comprehension to easily create a row dictionary. This should make future data access easier.

## Matching Rows

This section is the most comlex so far. The goal is to create a function that will take in a row and a condition and return whether the row satisfies the condition. The condition is passed in as a 3-tuple that contains the left and right value along with the operator. This was accomplished in a similar fashion to the previous lab on Reverse Polish Notation. I created a helper function with a set of if conditions to return the result of the opertion. One issue encountered was that the value stored was a number represented as a string but the check value was passed as a number. This was remedied by attempting to convert both values to integers and comparing them as strings if the conversion failed. The function also needed to check if the passed operator was a column label and use the column value in the comparison if so. Python makes this easy by using the `in` keyword to check if a string is a key in a dictionary.

## Extending the Query Language

After creating the `check_row` function we wanted to extend the functionality to include *AND* and *OR* operators on conditions. Doing this involves having nested conditions. This was a great opportunity to use recursion. Checking if the operator was *AND* or *OR* and then returning `<left> and <right>` or `<left> or <right>` solves the problem and allows for an indeterminate number of nested conditions.

## Filtering Tables

The final task in this assignment involved the combination of all of the previous parts. The task was to create a function to filter rows in a table based on a condition. This basically required just iterating over the rows and only returning the row if it returned true when calling `check_row`.

Overall, the most complex part of this assignment was creating the `check_row` function. This involved parsing a tuple into its necessary parts and then evaluating the condition. There were a number of edge cases that had to be considered such as converting to integers and then figuring out how to recursively check nested conditions.

