# jobs.py
Keeps track of job postings and sends notifications when new ones come out<br />
<br />
I got tired of manually checking job postings, and I wanted to get more
experience with python modules like `requests`, `bs4` and `logging`

## Functionality
- [x] Allow webpage configuration through spreadsheet
- [x] Aggregate job postings in Google Sheet
- [x] Support identifying job titles based on parented css attributes
- [x] Integrate `logging` library
- [ ] Improve identification of entry-level positions (Potentially add highlight?)
- [ ] Hookup to server for continuous execution
- [ ] Support dynamically rendered job posting content
- [ ] Support multi-url configuration for larger companies
- [ ] Support targeted spreadsheet updating instead of complete overwriting
- [ ] Track how long a job has been posted
- [ ] Send Discord notifications for new job postings
- [ ] Send Discord notifications upon errors
- [ ] Include link to *specific* job posting in spreadsheet
- [ ] Support search / filtered career pages (Blizzard, Epic, etc.)

## Supported Career Pages
* [Jackbox Games](https://jackbox-games.breezy.hr/)
* [Riot Games (University Programs)](https://www.riotgames.com/en/university-programs)
* [Sucker Punch Productions](https://jobs.suckerpunch.com)
