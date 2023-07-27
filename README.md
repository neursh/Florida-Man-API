## | The Florida Man API - Knows what a Florida man would do on a specific day. |
### Only one API, this API will return a random event based on the day provided in this format `MMDD`.
```
/florida-man-blessed-you?date=MMDD
```
Example:
```
/florida-man-blessed-you?date=0111
```
P/S: When the month is larger than 10, the format must be switched to `DDMM`.
P/S: When you enter `0000`, the API will return a `301 Moved Permanently` to rick roll.
P/S: There's 1% chance of getting a rick roll redirect even when you typed the right thing.
P/S: 
### Return:
There're two fields:
- `Some florida man did one that day` -> String | will return either `"true"` or `"false"`.
- `This is what he did` -> String | will return a title for an article only when you're typing the right date.
```json
{
  "A florida man did something on that day": "...",
  "This is what he did": "..."
}
```
There're some fields for headers you must follow:
- `User-Agent`: Who need this when everywhere is just bot DDoSing stuff? So if any of the request that has `User-Agent` will return the status code `400 Bad Request Mate`.
- `Is-Birthday`: This serves no purpose at all, you can ignore it because this field is set default to `"false"`. When you set it to `"false"`, the API still returns status `200 OK Bro` but there's no content in body, when you set to `"true"`, the API will return a `410 Gone`, I ain't gonna make you special on your birthday.
- ``
