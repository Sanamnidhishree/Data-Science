-- Top 10 ted-talk shows based on views

select a.Title, b.author, a.Month,a.Year, a.Views from  TED.tedshows as a
left join TED.tedauthor as b
on a.Author_id = b.Author_id
Order by Views Desc limit 10;

-- top 20 popular shows between 2020 to 2022 years

select a.Title, b.author, a.Month, a.Year, a.Views from  TED.tedshows as a
left join TED.tedauthor as b
on a.Author_id = b.Author_id
where a.Year between '2020' and '2022'
Order by Views Desc limit 20;


-- Top 10 ted-talk shows based on Likes

select a.Title, b.author, a.Month,a.Year, a.Likes from  TED.tedshows as a
left join TED.tedauthor as b
on a.Author_id = b.Author_id
Order by Likes Desc limit 10;
