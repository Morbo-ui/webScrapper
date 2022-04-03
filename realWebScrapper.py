from bs4 import BeautifulSoup
import requests


def find_jobs():
    print("Put a job, you\'re looking for")
    name_job = input('>')
    html_text = requests.get(f'https://career.habr.com/vacancies?q={name_job}&l=1&type=all').text
    soup = BeautifulSoup(html_text, 'lxml')

    print('Put a skill that you\'re not familiar with')
    unfamiliar_skill = input('>')
    print(f'Filtering {unfamiliar_skill}')

    jobs = soup.find_all('div', class_='vacancy-card')
    for index, job in enumerate(jobs):
        published_date = job.find('div', class_='vacancy-card__date').text
        if "апреля" in published_date:
            company_name = job.find('a', class_='link-comp link-comp--appearance-dark').text
            skills = job.find('div', class_='vacancy-card__skills').text.replace(" •", ",")
            more_info = job.find('div', class_='vacancy-card__title').a['href']
            if unfamiliar_skill.casefold() not in skills.casefold():
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Required skills: {skills.strip()} \n')
                    f.write(f'More info: https://career.habr.com{more_info}')
                print(f"File saved: {index}")


find_jobs()