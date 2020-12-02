# jobs.py
Keeps track of job postings and sends notifications when new ones come out<br />
<br />
I got tired of manually checking job postings, and I wanted to get more
experience with python modules like `requests`, `bs4` and `logging`

## Currently Supported Career Pages
If there is an additional career page that you would like to be added, create a github
issue to request that page
* [Activision](https://careers.activision.com/make-epic-entertainment)
* [Jackbox Games](https://jackbox-games.breezy.hr/)
* [Riot Games (University Programs)](https://www.riotgames.com/en/university-programs)
* [Rockstar Games](https://www.rockstargames.com/careers/openings)
* [Schell Games](https://www.schellgames.com/careers/#apply)
* [Sucker Punch Productions](https://jobs.suckerpunch.com)
* [ZeniMax (Bethesda Game Studios, id Software, etc.)](https://jobs.zenimax.com/jobs)

## Features
- [x] ~~Allow webpage configuration through spreadsheet~~
- [x] ~~Aggregate job postings in Google Sheet~~
- [x] ~~Support identifying job titles based on parented css attributes~~
- [x] ~~Integrate `logging` library~~
- [x] ~~Highlight entry-level positions~~
- [x] ~~Hookup to server for continuous execution~~
- [x] ~~Log updates on sheet~~
- [x] ~~Support dynamically rendered job posting content~~
- [ ] Send Discord notifications for new job postings
- [ ] Send Discord notifications upon errors
- [ ] Track how long a job has been posted
- [ ] Support multi-url configuration for larger companies
- [ ] Support targeted spreadsheet updating instead of complete overwriting
- [ [ Support organic & builtin method of utilizing prod vs dev spreadsheet
- [ ] Include link to *specific* job posting in spreadsheet
- [ ] Support search / filtered career pages (Blizzard, Epic, etc.)
- [ ] Support filters for company-specific webpage characteristics / exclusions

## Setup
To run get the bot running locally, you will need to do the following:
* Create a python virtual environment (`python3 -m venv env`)
* Activate and install necessary packages to that environment
	* `. env/bin/activate`
	* `pip install -r requirements.txt`
* Create a copy of `.env.example` and populate it with correct values
* Acquire the `service_account.json` file (allow you to edit the spreadsheet)
* Install chromedriver (to allow selenium to open Google Chrome)
