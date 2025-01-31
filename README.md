# economic_survey_analyzer

The Annual [Economic Survey](https://www.indiabudget.gov.in/economicsurvey/) is a great Document that tells about the progress and trajectory of what our government thinks, it is a big document but it can be very confusing to understand. This project is an attempt to summarise each section.

I am using gemini1.5 flash as it has a generous free tier of free API calls

## setup
- clone this repo
- run `python3.11 -m venv env`
- activate the virtual environment with `source env/bin/activate`
- `pip install -r requirements.txt`
- `cp .env.template .env`
- put gemini API key in .env
- RUN [GET_SURVERY_PDFS](./notebooks/get_all_survery_pdfs.ipynb)
- RUN [GET_ALL_SURVERY_SUMMARY](./notebooks/get_all_survery_summary.ipynb)
- RUN [CONVERTING_TO_HTML](./notebooks/convert_to_html.py)


