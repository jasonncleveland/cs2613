    Title: Assignment 3
    Date: 2019-10-18T00:00:00
    Tags: DONE

<!-- more -->

## Part 1: Flatten

The first part of this assignment looked at creating a function to flatten an array with nested arrays. The task was to have any nested arrays flattened into a single array. A majority of the code was taken from the similar excercise in Lab 11. The one change I had to make was checking if an element was an Array and making a recursive call to `flatten` solved the issue with more than one level of nested arrays.

## Part 2: Summarizing JSON Data

Part 2 of this lab involved reading in a JSON file and parsing the data within to extract desired fields. The function `summarize_mail` was created which took in a file name and an unbounded list of arguments specifying which fields to return to summarize the data. This function took advantage of the flatten function from the previous excercise to make working with the data easier. Pulling out the fields involved iterating over the keys of the object and returning them if they were specified. This ran into some issues with nested objects. To solve this I checked the value at the index key and recursively called the function if it was an object.

```javascript
Object.keys(obj).forEach(key => {
	if (typeof obj[key] === "object") {
		// Merge the recursively found keys into this levels keys
		Object.assign(found_keys, search(obj[key]);
	}
});
```

## Part 3: Objects and Constructors

The final part of this lab looked at classes. Specifically the `constructor` and `equals` functions. We started with the constructor that took in a JSON object and stored it. It also extracted the fields 'Subject', 'Date', 'From', and 'To' fields. We then created an `equal` function that compares the current object against another. This needed to be a deep equal to check every field so I took my solution to lab 10 where we created a deep equal check and called it in the equal function. This made this part very simple.

