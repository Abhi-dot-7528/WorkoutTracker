# Workout Tracker


This is a python project to track and store my workout progress into a google sheet with the help of an API. For a beginner it is really important to mark the progress as it boosts up the confidence and daily progress works as a fuel to do better each day.

To make it much easier to do, I created this project as all I have to do, is just type what type of exercise I did today in plain english and it automatically stores it into my google sheet. Plus with the help of the API I can also calculate how much of approximate calories I burnt doing a particular exercise.


## API Reference

#### [Nutritionix API](https://developer.nutritionix.com/)

```http
  POST /v2/natural/exercise
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `x-app-id` | `string` | **Required**. Your Application ID |
| `x-app_key` | `string` | **Required**. Your API key |
| `query` | `string` | **Required**. Your query to be executed. |

#### [Sheety API](https://sheety.co/)

```http
  POST /username/projectName/sheetName
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**. |
| `project_name`      | `string` | **Required**. |
| `sheet_name`      | `string` | **Required**. |
| `json`      | `json` | **Required**. _col_name_: _data_ |

