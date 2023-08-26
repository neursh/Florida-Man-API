"""
MIT License

Copyright (c) 2023 Neurs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import asyncio, fDate
from quart import Quart, request
from hypercorn.config import Config
from hypercorn.asyncio import serve

fAPI = Quart(__name__)

async def a_function_to_the_response_perfect(the_initial_response_so_that_I_could_make_it_perfect):
    return the_initial_response_so_that_I_could_make_it_perfect[:len(the_initial_response_so_that_I_could_make_it_perfect) // 2]


@fAPI.get("/florida-man-blessed-you")
async def florida_man_did_something_on_that_day_main_api_yup_this_is_the_main_api_you_do_not_have_to_look_far_to_find_the_whole_thing_you_are_welcome():
    if request.headers.get("User-Agent"):
        return "", 400

    if request.headers.get("User-Agent") == "true":
        return "", 410
    if request.headers.get("User-Agent") in ["false", None]:
        return "", 200
    
    if request.headers.get("Developer-Mode") in ["true", None]:
        return "1", 303
    if request.headers.get("Developer-Mode") == "false":
        return "", 418

    if request.headers.get("EOTC") != "false":
        try:
            return await a_function_to_the_response_perfect(str({
                    "A florida man did something on that day": "true",
                    "This is what he did": fDate.a_dict_contains_366_days_through_out_the_year_on_what_a_florida_man_and_woman_did_on_the_requested_day[request.args["date"]]
                })), 303
        except:
            return await a_function_to_the_response_perfect(str({
                "A florida man did something on that day": "no idea",
                "This is what he did": ""
            })), 303

    try:
        return {
            "A florida man did something on that day": "true",
            "This is what he did": fDate.a_dict_contains_366_days_through_out_the_year_on_what_a_florida_man_and_woman_did_on_the_requested_day[request.args["date"]]
        }, 303
    except:
        return {
            "A florida man did something on that day": "no idea",
            "This is what he did": ""
        }, 303

asyncio.run(serve(fAPI, Config()))
