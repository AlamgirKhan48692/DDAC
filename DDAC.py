
import pandas as pd

def calculate_demographic_data():
    # Load data
    df = pd.read_csv("adult.data.csv")

    # 1. Race count
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # 4. % with advanced education and >50K
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_edu = df[df['education'].isin(advanced_education)]
    lower_edu = df[~df['education'].isin(advanced_education)]

    higher_edu_rich = round(
        (higher_edu['salary'] == '>50K').sum() / len(higher_edu) * 100, 1)

    lower_edu_rich = round(
        (lower_edu['salary'] == '>50K').sum() / len(lower_edu) * 100, 1)

    # 5. Min work hours
    min_work_hours = df['hours-per-week'].min()

    # 6. % of rich among those who work min hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = round(
        (min_workers['salary'] == '>50K').sum() / len(min_workers) * 100, 1)

    # 7. Country with highest % of >50K
    country_total = df['native-country'].value_counts()
    country_rich = df[df['salary'] == '>50K']['native-country'].value_counts()
    rich_country_pct = (country_rich / country_total * 100).dropna()
    highest_earning_country = rich_country_pct.idxmax()
    highest_earning_country_percentage = round(rich_country_pct.max(), 1)

    # 8. Most popular occupation for those >50K in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_hours': rich_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }