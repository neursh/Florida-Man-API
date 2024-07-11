## | The Florida Man API - Knows what a Florida man would do on a specific day. |

https://florida-man-api.neurs.workers.dev

This project uses AI.
### Only one API, this API will return a random event based on the day provided in this default format `md`.
```
/florida-man-blessed-you?date=md
```
Example:
```
/florida-man-blessed-you?date=111
```
P/S: When the month is larger than 10, the format must be switched to `dm`.
<details><summary>Spoilers</summary>
P/S: When you enter `0000`, the API will return a `301 Moved Permanently` to rick roll.
  <details><summary>Spoilers</summary>
  P/S: There's 1% chance of getting a rick roll redirect even when you typed the right thing.
    <details><summary>Spoilers</summary>
    P/S: The AI mentioned above is ChatGPT generating JSON format from the data provided.
      <details><summary>Spoilers</summary>
      P/S: Sorry for the mistake, the default format is `dm`, not `md`. So for the first P/S, you should take another look after knowing this.
        <details><summary>Spoilers</summary>
        P/S: It's my project so the default format is now based on the format that I've mentioned above.
          <details><summary>Spoilers</summary>
          P/S: Sorry for the confusion, the first P/S is.
            <details><summary>Spoilers</summary>
            P/S: Sorry for another confusion, there's no random, each day only has 1 story.
            </details>
          </details>
        </details>
      </details>
    </details>
  </details>
</details>

### Return:
There are two fields:
- `Some florida man did one that day` -> String | will return either `"true"` or `"no idea"`.
- `This is what he did` -> String | will return a title for an article only when you're typing the right date.
```BrainFuck
{
  "A florida man did something on that day": "...",
  "This is what he did": "..."
}
```
There are some fields for headers you must follow:
- `User-Agent`: Who need this when everywhere is just bot DDoSing stuff? So if any of the request that contains anything in `User-Agent` will return the status code `400 Bad Request Mate`.
- `Is-Birthday`: This serves no purpose at all, you can ignore it because this field is set default to `"false"`. When you set it to `"false"`, the API returns status `200 OK Bro` but there's no content in body, when you set to `"true"`, the API will return a `410 Gone`, I ain't gonna make you special on your birthday.
- `Developer-Mode`: This will convert the result in this following pattern: String <- Base64 <- Base32 <- Base16 <- Base8 <- Binary (response has 2 a maximum of characters). Default: `"true"`. If set to `"false"`, the API will thinks that you've got skill issue and will return a `418 I'm a teapot`.
- `EOTC` (End-Of-Thinking-Capacity): The response will be cut in half. Default: `"true"`. If set to `"false"` then the API will send the whole response, other than that, the API just lazy to handle it.

Except for the fact that the API would always return a `303 See Other` when you successfully pulled something out of this, you're ready to go!
