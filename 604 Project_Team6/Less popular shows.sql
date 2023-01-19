-- 100 shows which are less popular that is less views and less likes

select a.Title, b.author, a.Month,a.Year, a.Views, a.Likes from  TED.tedshows as a
left join TED.tedauthor as b
on a.Author_id = b.Author_id
Order by Likes, Views asc
Limit 100;

-- 20 less popular shows between 2020 to 2022.

select a.Title, b.author, a.Month, a.Year, a.Views from  TED.tedshows as a
left join TED.tedauthor as b
on a.Author_id = b.Author_id
where a.Year between '2020' and '2022'
Order by Views asc limit 20;