-- Shows with more than 1 author.

select a.Title, b.Num_Authors, a.Month,a.Year
from  TED.tedshows as a
left join TED.tedauthor as b
on a.Author_id = b.Author_id
where b.Num_Authors > 1 
order by Num_Authors desc;

-- Checking any correlation between author occupation and Views.

select a.Title, b.Author, b.Occupation , a.Likes, a.Views
from  TED.tedshows as a
left join TED.tedauthor as b
on a.Author_id = b.Author_id
where NULLIF(b.Occupation,'') is not null
order by Views desc;

-- number of shows per author occupation 

select b.Occupation , count(*) as Shows_per_occupation
from  TED.tedshows as a
left join TED.tedauthor as b
on a.Author_id = b.Author_id
where NULLIF(b.Occupation,'') is not null
group by b.Occupation
having count(*) > 1
Order by count(*) desc;

-- total number of shows per num_authors

select  b.Num_Authors, count(a.Title) as count_of_shows
from  TED.tedshows as a
left join TED.tedauthor as b
on a.Author_id = b.Author_id
group by Num_Authors, a.Year
order by Num_Authors desc;

-- total number of shows per num_authors, years

select  b.Num_Authors, a.Year,count(a.Title) as count_of_shows
from  TED.tedshows as a
left join TED.tedauthor as b
on a.Author_id = b.Author_id
group by Num_Authors, a.Year
order by Num_Authors desc;


-- avg number of Likes per year

select a.Year, avg(a.Likes) as avg_likes from TED.tedshows as a
group by a.Year
order by avg(a.Likes) desc;


-- avg number of Views per year

select a.Year, avg(a.Views) as avg_Views from TED.tedshows as a
group by a.Year
order by avg(a.Views) desc;






