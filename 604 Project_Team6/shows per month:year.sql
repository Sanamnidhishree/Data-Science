-- shows per month

select a.Month, count(*) as shows_per_month
From TED.tedshows as a
group by a.Month
Order by count(*) desc;

-- shows per year

select a.Year, count(*) as shows_per_year
From TED.tedshows as a
group by a.Year
Order by count(*) desc;



