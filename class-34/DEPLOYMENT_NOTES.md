# Cookie Stand Lab Solution Steps

## Get Running Locally

- Create cookie-stand-api off of Quickstart template
- Clone cookie-stand-api repo
- Poetry install / shell
- > mv things cookie_stands
- Replace thing with CookieStand throughout codebase
- Update Model
  - Including other related modules as needed
  - E.g. Serializer
- Create .env based off .env.sample
- > cp project/.env.sample project/.env
- > python manage.py makemigrations cookie_stands
- > python manage.py migrate
- > python manage.py createsuperuser
- Run dev server locally (no Docker yet)
- Check in browser
  - create a cookie stand in browsable API
- Try api tester
  - > python api_tester get_all
  - Should be able to do CRUD
  - make sure API_HOST, USERNAME, PASSWORD and RESOURCE_URI are correct

## Set Up DB in ElephantSQL

- Create account at ElephantSQL
- Create `cookie-stand-db`
- Gather the info and use it in .env
- Switch engine to postgres
- > python manage.py migrate
- > python manage.py createsuperuser
- Run locally but using ElephantSQL hosted DB
- Test with `api_tester`
  - > python api_tester.py create "Seattle"

## Containerize

- Create heroku app with CLI
- Create `heroku.yml` and update with content
- Using Heroku CLI let it know we're using the container "stack"
- Gather static assets so Admin/API render nicely
  - > python manage.py collectstatic
- ACP to heroku
- Go to Heroku Dashboard Settings
- Update environment variables to match .env
  - Add heroku app's url to ALLOWED_HOSTS
- Open deployed app in browser
- Use `api_tester.py` with deployed URL
